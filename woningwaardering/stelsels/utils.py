import asyncio
import warnings
from datetime import date
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from functools import wraps
from importlib.resources import files
from typing import Any, Callable, Counter, List, Tuple

import pandas as pd
import requests
from loguru import logger
from pydantic import BaseModel

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenEnergieprestatie,
    EenhedenRuimte,
    EenhedenWoonplaats,
    Referentiedata,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Ruimtedetailsoort,
    Ruimtesoort,
    RuimtesoortReferentiedata,
)
from woningwaardering.vera.referentiedata.eenheidmonument import (
    Eenheidmonument,
    EenheidmonumentReferentiedata,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelsel import (
    Woningwaarderingstelsel,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element

_STELSELGROEPEN_MET_SUBTOTAAL_AANTAL = frozenset(
    {
        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
        Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,
    }
)

KADASTER_SPARQL_ENDPOINT = "https://data.kkg.kadaster.nl/service/sparql"

# Kolombreedtes voor tabeloutput (zie docs/voor-ontwikkelaars/testing.md)
W_NAAM = 60
W_GETAL = 10  # rechts uitgelijnd, bijv. "205000.00"
W_EENHEID = 3  # links uitgelijnd na het getal, bijv. "EUR" / "m²" / "st"
W_PUNTEN = 9  # "XXX.00 pt" (drie cijfers voor de komma)
W_OPSLAG = 7
_GAP = "  "
_INDENT = "  "
_BULLET = "- "
# Inschuif aan het begin van elke tabelregel (naamkolom).
_TABEL_RIJ_INSCHUIF = "  "
# Spatie tussen getal- en eenheidskolom.
_GETAL_EENHEID_GAP = " "


class WoningwaarderingTabel:
    """Tekstuele weergave van een woningwaarderingresultaat (samenvatting + detailsecties)."""

    def __init__(self, lines: list[str]) -> None:
        self._lines = lines

    def get_string(self) -> str:
        return "\n".join(self._lines)

    def __str__(self) -> str:
        return self.get_string()


def _tabel_fmt_num(waarde: float | Decimal | None) -> str:
    if waarde is None:
        return ""
    return (
        f"{Decimal(str(waarde)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP):.2f}"
    )


_MEETEENHEID_AFKORTING: dict[str, str] = {
    "M2": "m²",
    "MIL": "mm",
    "EUR": "EUR",
    "STU": "st",
    "MTR": "m",
    "M3": "m³",
    "CM": "cm",
    "KGR": "kg",
    "GRM": "g",
    "LTR": "l",
    "MIN": "min",
    "UUR": "uur",
}


def _meeteenheid_afkorting(meeteenheid: Referentiedata | None) -> str:
    if meeteenheid is None:
        return ""
    if meeteenheid.code:
        return _MEETEENHEID_AFKORTING.get(meeteenheid.code, meeteenheid.code)
    return meeteenheid.naam or ""


def _format_aantal_delen(
    aantal: float | Decimal | int | None,
    meeteenheid: Referentiedata | None,
) -> tuple[str, str]:
    """Splits aantal in getal- en eenheidstekst voor aparte tabelkolommen."""
    if aantal is None:
        return "", ""
    return _tabel_fmt_num(aantal), _meeteenheid_afkorting(meeteenheid)


# Vaste eindpositie (karakterindex) van elke waardekolom, inclusief de rij-inschuif.
# De naamkolom staat links; getal/punten/opslag worden rechts uitgelijnd, eenheid
# links in een vaste kolom na het getal — zodat cijfers verticaal uitlijnen.
_GETAL_KOLOM_EINDE = len(_TABEL_RIJ_INSCHUIF) + W_NAAM + len(_GAP) + W_GETAL
_EENHEID_KOLOM_EINDE = _GETAL_KOLOM_EINDE + len(_GETAL_EENHEID_GAP) + W_EENHEID
_PUNTEN_KOLOM_EINDE = _EENHEID_KOLOM_EINDE + len(_GAP) + W_PUNTEN
_OPSLAG_KOLOM_EINDE = _PUNTEN_KOLOM_EINDE + len(_GAP) + W_OPSLAG


def _plaats_rechts(regel: str, tekst: str, kolom_einde: int) -> str:
    """Plak ``tekst`` rechts uitgelijnd achter ``regel`` zodat het op ``kolom_einde`` eindigt.

    Wanneer ``regel`` al te lang is, schuift ``tekst`` naar rechts met minimaal één spatie.
    """
    if not tekst:
        return regel
    padding = max(1, kolom_einde - len(regel) - len(tekst))
    return f"{regel}{' ' * padding}{tekst}"


def _plaats_eenheid(regel: str, eenheid: str) -> str:
    """Plak ``eenheid`` links uitgelijnd in de eenheidskolom (direct na het getal)."""
    if not eenheid:
        return regel
    if len(regel) < _GETAL_KOLOM_EINDE:
        regel = f"{regel}{' ' * (_GETAL_KOLOM_EINDE - len(regel))}"
    regel = f"{regel}{_GETAL_EENHEID_GAP}{eenheid}"
    if len(regel) < _EENHEID_KOLOM_EINDE:
        regel = f"{regel}{' ' * (_EENHEID_KOLOM_EINDE - len(regel))}"
    return regel


def _tabel_regel(
    naam: str,
    *,
    aantal: str = "",
    eenheid: str = "",
    punten: str = "",
    opslag: str = "",
) -> str:
    """Formatteer één tabelregel met de gedeelde kolomopmaak.

    Wordt gebruikt voor de regels in de samenvatting, de detailregels in een
    stelselgroep en de totaalregels: de naam staat links; getal, punten en opslag
    lijnen rechts uit op vaste kolomeinden; de eenheid staat in een vaste kolom
    direct na het getal.
    """
    regel = _TABEL_RIJ_INSCHUIF + naam
    regel = _plaats_rechts(regel, aantal, _GETAL_KOLOM_EINDE)
    regel = _plaats_eenheid(regel, eenheid)
    regel = _plaats_rechts(regel, punten, _PUNTEN_KOLOM_EINDE)
    regel = _plaats_rechts(regel, opslag, _OPSLAG_KOLOM_EINDE)
    return regel.rstrip()


def _tabel_scheiding(*, toon_aantal: bool) -> str:
    """Scheidingsregel boven een totaalregel (onder de getal- en puntenkolom)."""
    return _tabel_regel(
        "",
        aantal="-" * W_GETAL if toon_aantal else "",
        punten="-" * W_PUNTEN,
    )


def _format_punten_cel(waarde: str) -> str:
    if not waarde:
        return ""
    return f"{waarde} pt"


def _waardering_opslag(waardering: WoningwaarderingResultatenWoningwaardering) -> str:
    if waardering.opslagpercentage is None:
        return ""
    return f"{waardering.opslagpercentage:.0%}"


def _groep_toon_opslag_kolom(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> bool:
    if groep.opslagpercentage is not None and groep.opslagpercentage > 0:
        return True
    for waardering in groep.woningwaarderingen or []:
        if waardering.opslagpercentage is not None and waardering.opslagpercentage > 0:
            return True
    return False


def _waardering_meeteenheid(
    waardering: WoningwaarderingResultatenWoningwaardering,
) -> Referentiedata | None:
    if waardering.criterium is None:
        return None
    return waardering.criterium.meeteenheid


def _waardering_punten(
    waardering: WoningwaarderingResultatenWoningwaardering,
) -> str:
    if waardering.punten is None:
        return ""
    return _format_punten_cel(_tabel_fmt_num(waardering.punten))


def _onderliggende_waarderingen(
    parent: WoningwaarderingResultatenWoningwaardering,
    waarderingen: list[WoningwaarderingResultatenWoningwaardering],
) -> list[WoningwaarderingResultatenWoningwaardering]:
    if parent.criterium is None or parent.criterium.id is None:
        return []
    parent_id = parent.criterium.id
    return [
        w
        for w in waarderingen
        if w.criterium is not None
        and w.criterium.bovenliggende_criterium is not None
        and w.criterium.bovenliggende_criterium.id == parent_id
    ]


def _render_waardering_pre_order(
    waardering: WoningwaarderingResultatenWoningwaardering,
    waarderingen: list[WoningwaarderingResultatenWoningwaardering],
    regels: list[str],
    *,
    toon_opslag_kolom: bool,
    indent: int = 0,
) -> None:
    if waardering.criterium is None:
        return

    prefix = (_INDENT * indent + _BULLET) if indent > 0 else ""
    getal, eenheid = _format_aantal_delen(
        waardering.aantal, _waardering_meeteenheid(waardering)
    )
    regels.append(
        _tabel_regel(
            prefix + (waardering.criterium.naam or ""),
            aantal=getal,
            eenheid=eenheid,
            punten=_waardering_punten(waardering),
            opslag=_waardering_opslag(waardering) if toon_opslag_kolom else "",
        )
    )

    for kind in _onderliggende_waarderingen(waardering, waarderingen):
        _render_waardering_pre_order(
            kind,
            waarderingen,
            regels,
            toon_opslag_kolom=toon_opslag_kolom,
            indent=indent + 1,
        )


def _gedeeld_met_deler(criterium_id: str | None) -> Decimal:
    """Bepaal waarmee een bruto ``aantal`` gedeeld moet worden (gedeeld-met-deler).

    Output slaat vaak het ongedeelde getal op (bijv. 10 m²) terwijl de
    gedeeld-met-lagen in de hiërarchie staan. De deler haal je uit de
    criterium-id: een pad-id met ``__``-segmenten. Elk segment
    ``gedeeld_met_{n}_…`` (adressen of onzelfstandige woonruimten) levert
    factor ``n``; meerdere lagen worden vermenigvuldigd (bijv. 4 × 10).
    Zonder ``gedeeld_met``-segment is de deler 1 (privé).
    """
    if criterium_id is None:
        return Decimal("1")
    product = Decimal("1")
    for part in criterium_id.split("__"):
        if part.startswith("gedeeld_met_"):
            getal = part[len("gedeeld_met_") :].split("_", 1)[0]
            try:
                product *= Decimal(getal)
            except InvalidOperation:
                continue
    return product


def _waardering_voor_criterium_id(
    criterium_id: str | None,
    waarderingen: list[WoningwaarderingResultatenWoningwaardering],
) -> WoningwaarderingResultatenWoningwaardering | None:
    if criterium_id is None:
        return None
    return next(
        (
            w
            for w in waarderingen
            if w.criterium is not None and w.criterium.id == criterium_id
        ),
        None,
    )


def _effectieve_aantal_bijdrage(
    waardering: WoningwaarderingResultatenWoningwaardering,
    waarderingen: list[WoningwaarderingResultatenWoningwaardering],
) -> Decimal | None:
    if waardering.aantal is None or waardering.criterium is None:
        return None

    bovenliggend = waardering.criterium.bovenliggende_criterium
    if bovenliggend is not None and bovenliggend.id is not None:
        parent = _waardering_voor_criterium_id(bovenliggend.id, waarderingen)
        if parent is not None and parent.aantal is not None:
            return None
        deler = _gedeeld_met_deler(waardering.criterium.id)
        return rond_af(Decimal(str(waardering.aantal)) / deler, decimalen=2)

    criterium_id = waardering.criterium.id or ""
    if criterium_id in criteriumsleutel_ids(waarderingen):
        if waardering.punten is not None:
            return rond_af(Decimal(str(waardering.aantal)), decimalen=2)
        return None

    return rond_af(Decimal(str(waardering.aantal)), decimalen=2)


def som_effectieve_aantal_waarderingen(
    waarderingen: list[WoningwaarderingResultatenWoningwaardering] | None,
) -> Decimal:
    """Som van effectieve hoeveelheden (o.a. gedeelde m² / gedeeld_met), zonder dubbele kop+kind."""
    bijdragen = [
        b
        for w in waarderingen or []
        if (b := _effectieve_aantal_bijdrage(w, waarderingen or [])) is not None
    ]
    if not bijdragen:
        return Decimal("0")
    return rond_af(sum(bijdragen), decimalen=2)


def groep_toont_subtotaal_aantal(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> bool:
    """Of de stelselgroep-`Totaal`-regel in tabellen een hoeveelheid mag tonen."""
    criterium_groep = groep.criterium_groep
    if (
        criterium_groep is None
        or criterium_groep.stelsel is None
        or criterium_groep.stelselgroep is None
    ):
        return False
    if criterium_groep.stelsel != Woningwaarderingstelsel.zelfstandige_woonruimten:
        return False
    return criterium_groep.stelselgroep in _STELSELGROEPEN_MET_SUBTOTAAL_AANTAL


def _groep_subtotaal_aantal_delen(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> tuple[str, str]:
    if not groep_toont_subtotaal_aantal(groep):
        return "", ""

    waarderingen = groep.woningwaarderingen or []
    met_aantal = [
        w
        for w in waarderingen
        if w.aantal is not None
        and w.criterium is not None
        and w.criterium.meeteenheid is not None
    ]
    if not met_aantal:
        return "", ""

    totaal = som_effectieve_aantal_waarderingen(waarderingen)
    if totaal == Decimal("0"):
        return "", ""

    meeteenheid_codes = [
        w.criterium.meeteenheid.code or ""
        for w in met_aantal
        if w.criterium is not None and w.criterium.meeteenheid is not None
    ]
    if len(set(meeteenheid_codes)) > 1:
        return "", ""

    meeteenheid = next(
        (
            w.criterium.meeteenheid
            for w in met_aantal
            if w.criterium is not None and w.criterium.meeteenheid is not None
        ),
        None,
    )
    return _format_aantal_delen(float(totaal), meeteenheid)


def _render_detail_groep(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> list[str]:
    waarderingen = groep.woningwaarderingen or []
    if not waarderingen:
        return []

    stelselgroep_naam = (
        groep.criterium_groep
        and groep.criterium_groep.stelselgroep
        and groep.criterium_groep.stelselgroep.naam
        or ""
    )
    toon_opslag_kolom = _groep_toon_opslag_kolom(groep)

    regels: list[str] = [stelselgroep_naam.upper()]

    tops = [
        w
        for w in waarderingen
        if w.criterium is not None and w.criterium.bovenliggende_criterium is None
    ]
    for waardering in tops:
        _render_waardering_pre_order(
            waardering,
            waarderingen,
            regels,
            toon_opslag_kolom=toon_opslag_kolom,
        )

    subtotaal_aantal, subtotaal_eenheid = _groep_subtotaal_aantal_delen(groep)
    groep_punten = _tabel_fmt_num(groep.punten) if groep.punten is not None else ""
    groep_opslag = (
        f"{groep.opslagpercentage:.0%}"
        if toon_opslag_kolom and groep.opslagpercentage is not None
        else ""
    )

    regels.append(_tabel_scheiding(toon_aantal=bool(subtotaal_aantal)))
    regels.append(
        _tabel_regel(
            "Totaal",
            aantal=subtotaal_aantal,
            eenheid=subtotaal_eenheid,
            punten=_format_punten_cel(groep_punten),
            opslag=groep_opslag,
        )
    )
    return regels


def _render_samenvatting(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> list[str]:
    lines: list[str] = []
    for groep in resultaat.groepen or []:
        stelselgroep_naam = (
            groep.criterium_groep
            and groep.criterium_groep.stelselgroep
            and groep.criterium_groep.stelselgroep.naam
            or ""
        )
        punten = groep.punten
        waarde = ""
        if punten is not None and punten != 0:
            waarde = _format_punten_cel(_tabel_fmt_num(punten))
        toon_opslag_kolom = _groep_toon_opslag_kolom(groep)
        opslag = (
            f"{groep.opslagpercentage:.0%}"
            if toon_opslag_kolom and groep.opslagpercentage is not None
            else ""
        )
        lines.append(_tabel_regel(stelselgroep_naam, punten=waarde, opslag=opslag))

    lines.append(_tabel_scheiding(toon_aantal=False))

    if resultaat.punten is not None:
        lines.append(
            _tabel_regel(
                "TOTAAL", punten=_format_punten_cel(_tabel_fmt_num(resultaat.punten))
            )
        )

    opslag_percentage = ""
    opslag_bedrag = ""
    if resultaat.opslagpercentage is not None and resultaat.opslagpercentage > 0:
        opslag_percentage = f"{resultaat.opslagpercentage:.0%}"
    if resultaat.huurprijsopslag is not None and resultaat.huurprijsopslag > 0:
        opslag_bedrag = _tabel_fmt_num(resultaat.huurprijsopslag)
    if opslag_percentage or opslag_bedrag:
        lines.append(
            _tabel_regel(
                "Opslag",
                aantal=opslag_bedrag,
                eenheid="EUR" if opslag_bedrag else "",
                opslag=opslag_percentage,
            )
        )

    if resultaat.maximale_huur is not None:
        lines.append(
            _tabel_regel(
                "Maximaal redelijke huur",
                aantal=_tabel_fmt_num(resultaat.maximale_huur),
                eenheid="EUR",
            )
        )

    if (
        resultaat.opslagpercentage is not None
        and resultaat.opslagpercentage > 0
        and resultaat.maximale_huur_inclusief_opslag is not None
    ):
        lines.append(
            _tabel_regel(
                "Maximaal redelijke huur inclusief opslag",
                aantal=_tabel_fmt_num(resultaat.maximale_huur_inclusief_opslag),
                eenheid="EUR",
            )
        )

    return lines


def naar_tabel(
    woningwaardering_resultaat: (
        WoningwaarderingResultatenWoningwaarderingResultaat
        | WoningwaarderingResultatenWoningwaarderingGroep
    ),
    *,
    eenheid_id: str | None = None,
) -> WoningwaarderingTabel:
    """
    Genereer een tabel met de details van een woningwaarderingresultaat.

    Args:
        woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | WoningwaarderingResultatenWoningwaarderingGroep): Het object om de gegevens uit te halen.
        eenheid_id (str | None): Optioneel eenheid-id voor de samenvattingskop.

    Returns:
        WoningwaarderingTabel: Samenvatting (volledig resultaat) en detailsecties.
    """
    if isinstance(
        woningwaardering_resultaat, WoningwaarderingResultatenWoningwaarderingGroep
    ):
        groepen = [woningwaardering_resultaat]
        toon_samenvatting = False
        volledig_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None
    else:
        volledig_resultaat = woningwaardering_resultaat
        groepen = volledig_resultaat.groepen or []
        toon_samenvatting = True

    detail_secties = [_render_detail_groep(groep) for groep in groepen]
    heeft_detail_secties = any(detail_secties)

    lines: list[str] = []
    if toon_samenvatting and volledig_resultaat is not None:
        titel = "SAMENVATTING"
        if eenheid_id:
            titel = f"{titel} {eenheid_id}"
        lines.append(titel)
        lines.extend(_render_samenvatting(volledig_resultaat))
        if heeft_detail_secties:
            lines.append("")

    eerste_detail = True
    for detail in detail_secties:
        if not detail:
            continue
        if not eerste_detail:
            lines.append("")
        eerste_detail = False
        lines.extend(detail)

    return WoningwaarderingTabel(lines)


def energieprestatie_met_geldig_label(
    peildatum: date, eenheid: EenhedenEenheid
) -> EenhedenEnergieprestatie | None:
    """
    Returnt de eerste geldige energieprestatie met een energielabel van een eenheid.

    Args:
        peildatum (date): De peildatum waarop de energieprestatie geldig moet zijn.
        eenheid (EenhedenEenheid): De eenheid met mogelijke energieprestaties.

    Returns:
        EenhedenEnergieprestatie | None: De eerst geldige energieprestatie en None wanneer er geen geldige energieprestatie met label is gevonden.
    """
    aantal_energieprestaties = len(eenheid.energieprestaties or [])
    if aantal_energieprestaties == 0:
        warnings.warn(
            f"Eenheid ({eenheid.id}): 'energieprestaties' is None", UserWarning
        )
        return None

    vereiste_attributen: List[
        Tuple[str, Callable[[EenhedenEnergieprestatie], bool]]
    ] = [
        ("soort", lambda ep: ep.soort is not None),
        ("status", lambda ep: ep.status is not None),
        ("begindatum", lambda ep: ep.begindatum is not None),
        ("einddatum", lambda ep: ep.einddatum is not None),
        ("label", lambda ep: ep.label is not None),
    ]

    for idx, energieprestatie in enumerate(eenheid.energieprestaties or []):
        logger.debug(
            f"Eenheid ({eenheid.id}): energieprestatie {idx + 1} van {aantal_energieprestaties} wordt gevalideerd."
        )
        ontbrekende_attributen = [
            naam for naam, check in vereiste_attributen if not check(energieprestatie)
        ]
        if ontbrekende_attributen:
            logger.debug(
                f"Eenheid ({eenheid.id}) mist energieprestatie attributen: {', '.join(ontbrekende_attributen)}."
            )
            continue

        if energieprestatie.soort not in (
            Energieprestatiesoort.energie_index,
            Energieprestatiesoort.energielabel_conform_nta8800,
            Energieprestatiesoort.primair_energieverbruik_woningbouw,
            Energieprestatiesoort.voorlopig_energielabel,
        ):
            logger.debug(
                f"Eenheid ({eenheid.id}): ongeldige energieprestatiesoort '{energieprestatie.soort}'."
            )
            continue

        # 2.4.3 Geldigheid energieprestatie op peildatum (beleidsboek).
        # Wij berekenen de 10-jaarsgeldigheid niet zelf; wij gaan uit van de geldigheid van het energielabel.
        # In EP-online is dat de 'Geldig tot'-datum; in VERA is dat einddatum. Peildatum moet vóór einddatum liggen.
        begindatum = energieprestatie.begindatum
        einddatum = energieprestatie.einddatum
        if begindatum is None or einddatum is None:
            continue
        if not (begindatum <= peildatum < einddatum):
            logger.debug(
                f"Eenheid ({eenheid.id}): peildatum {peildatum} valt buiten geldigheidsperiode van de energieprestatie."
            )
            continue

        if energieprestatie.status != Energieprestatiestatus.definitief:
            logger.debug(
                f"Eenheid ({eenheid.id}): energieprestatie status is niet definitief."
            )
            continue

        logger.info(f"Eenheid ({eenheid.id}): geldige energieprestatie gevonden.")
        logger.debug(
            f"Energieprestatie: id={energieprestatie.id} soort={energieprestatie.soort.naam if energieprestatie.soort else None}"
            f" status={energieprestatie.status.naam if energieprestatie.status else None}"
            f" label={energieprestatie.label.naam if energieprestatie.label else None}"
            f" waarde={energieprestatie.waarde} begindatum={energieprestatie.begindatum}"
            f" einddatum={energieprestatie.einddatum}"
        )
        return energieprestatie

    logger.info(f"Eenheid ({eenheid.id}): geen geldige energieprestatie gevonden.")
    return None


def rond_af(
    getal: float | None | Decimal, decimalen: int, rounding: str | None = ROUND_HALF_UP
) -> Decimal:
    """
    Rondt een getal af op een bepaald aantal decimalen volgens de standaard afrondingsregels (arithmetic).

    Args:
        getal (float | None | Decimal): Het getal om af te ronden.
        decimalen (int): Het aantal decimalen na de komma om op af te ronden.
        rounding (str | None, optional): Het type afrondingsregel. Default is ROUND_HALF_UP.

    Returns:
        Decimal: Het afgeronde getal.

    Raises:
        ValueError: als de input None is.
    """
    if getal is None:
        raise ValueError("Kan None niet afronden")
    return Decimal(str(getal)).quantize(Decimal(f"1e{-decimalen}"), rounding=rounding)


def rond_af_op_kwart(getal: float | None | Decimal) -> Decimal:
    """
    Rond een getal af op een kwart.

    Args:
        getal (float | None | Decimal): Het getal om af te ronden.

    Returns:
        Decimal: Het afgeronde getal.

    Raises:
        ValueError: als de input None is.
    """
    if getal is None:
        raise ValueError("Kan None niet afronden")
    kwart = Decimal("0.25")
    return (Decimal(getal) / kwart).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    ) * kwart


def parent_ids_met_onderliggende_punten(
    waarderingen: list[WoningwaarderingResultatenWoningwaardering] | None,
) -> set[str]:
    ids: set[str] = set()
    for waardering in waarderingen or []:
        if waardering.punten is None or waardering.criterium is None:
            continue
        bovenliggend = waardering.criterium.bovenliggende_criterium
        if bovenliggend is not None and bovenliggend.id is not None:
            ids.add(bovenliggend.id)
    return ids


def parent_ids_met_onderliggende_aantal(
    waarderingen: list[WoningwaarderingResultatenWoningwaardering] | None,
) -> set[str]:
    ids: set[str] = set()
    for waardering in waarderingen or []:
        if waardering.aantal is None or waardering.criterium is None:
            continue
        bovenliggend = waardering.criterium.bovenliggende_criterium
        if bovenliggend is not None and bovenliggend.id is not None:
            ids.add(bovenliggend.id)
    return ids


def criteriumsleutel_ids(
    waarderingen: list[WoningwaarderingResultatenWoningwaardering] | None,
) -> set[str]:
    """Ids die als bovenliggende criteriumsleutel in de waarderingen-graaf voorkomen."""
    return parent_ids_met_onderliggende_punten(
        waarderingen
    ) | parent_ids_met_onderliggende_aantal(waarderingen)


def som_punten_waarderingen(
    waarderingen: list[WoningwaarderingResultatenWoningwaardering] | None,
) -> float:
    """Som van punten op alle waarderingen in een groep (afgerond op kwart).

    Returnwaarde is bedoeld voor VERA-velden (``punten``).
    """
    if not waarderingen:
        return 0.0
    totaal = sum(Decimal(str(w.punten)) for w in waarderingen if w.punten is not None)
    return float(rond_af_op_kwart(totaal))


def update_eenheid_monumenten(eenheid: EenhedenEenheid) -> EenhedenEenheid:
    """
    Voegt monumentale statussen toe aan een eenheid d.m.v. aanroepen API's.

    Args:
        eenheid (EenhedenEenheid): De eenheid waarvoor de monumentale status wordt opgehaald

    Returns:
        EenhedenEenheid: De met monumentale statussen bijgewerkte eenheid
    """
    try:
        from monumenten import MonumentenClient

        has_monumenten = True
    except ImportError:
        has_monumenten = False
        warnings.warn(
            "Package 'monumenten' is niet geïnstalleerd. Monumentale status wordt niet automatisch bijgewerkt. "
            "Installeer met: pip install woningwaardering[monumenten]",
            UserWarning,
        )
        return eenheid

    if not has_monumenten:
        return eenheid

    eenheid.monumenten = eenheid.monumenten or []
    try:
        if (
            eenheid.adresseerbaar_object_basisregistratie is None
            or eenheid.adresseerbaar_object_basisregistratie.bag_identificatie is None
        ):
            logger.warning(f"Eenheid ({eenheid.id}): Geen bag_identificatie gevonden")
            return eenheid

        logger.debug(
            f"Eenheid ({eenheid.id}): Monumentale statussen worden opgehaald voor eenheid met bag_identificatie {eenheid.adresseerbaar_object_basisregistratie.bag_identificatie}"
        )
        bag_verblijfsobject_ids = [
            eenheid.adresseerbaar_object_basisregistratie.bag_identificatie
        ]

        async def _get_monuments() -> Any:
            async with MonumentenClient() as client:
                return await client.process_from_list(
                    bag_verblijfsobject_ids,
                    to_vera=True,
                )

        # Voer de async context manager uit in een synchrone context
        monumenten = asyncio.run(_get_monuments()).get(
            eenheid.adresseerbaar_object_basisregistratie.bag_identificatie, []
        )

        if monumenten:
            logger.info(
                f"Eenheid ({eenheid.id}): Monumentale statussen gevonden: {', '.join(monument['naam'] for monument in monumenten)}"
            )
            eenheid.monumenten = [
                EenheidmonumentReferentiedata(
                    code=monument["code"], naam=monument["naam"]
                )
                for monument in monumenten
                if monument["code"] != Eenheidmonument.rijksmonument.code
                or "RCE" in (monument.get("bron") or [])
            ]
        else:
            logger.debug(f"Eenheid ({eenheid.id}): Geen monumentale statussen gevonden")
    except Exception as e:
        warnings.warn(
            f"Monumentale statussen konden niet worden opgehaald m.b.v. API: {e}",
            UserWarning,
        )
    return eenheid


def normaliseer_ruimte_namen(eenheid: EenhedenEenheid) -> None:
    for ruimte in eenheid.ruimten or []:
        if not ruimte.naam:
            ruimte.naam = getattr(ruimte.detail_soort, "naam", ruimte.id)

    naam_counter = Counter(
        ruimte.naam for ruimte in eenheid.ruimten or [] if ruimte.naam
    )
    nummering_counter: Counter[str] = Counter()

    for ruimte in eenheid.ruimten or []:
        if ruimte.naam is not None and naam_counter[ruimte.naam] > 1:
            nummering_counter[ruimte.naam] += 1
            ruimte.naam = f"{ruimte.naam} {nummering_counter[ruimte.naam]}"


def waarschuw_dubbele_ids(instance: BaseModel) -> None:
    """
    Waarschuw bij dubbele, niet-lege id's binnen dezelfde lijst in dit Pydantic object.
    """
    for veld, veld_info in type(instance).model_fields.items():
        # Deprecated velden overslaan: getattr triggert anders een DeprecationWarning.
        if veld_info.deprecated:
            continue
        waarde = getattr(instance, veld, None)
        if isinstance(waarde, BaseModel):
            waarschuw_dubbele_ids(waarde)
        elif isinstance(waarde, list):
            items = [item for item in waarde if isinstance(item, BaseModel)]
            id_counter = Counter(
                id_waarde
                for item in items
                if (id_waarde := getattr(item, "id", None)) is not None
            )
            for id_waarde, aantal in id_counter.items():
                if aantal > 1:
                    warnings.warn(
                        f"Id '{id_waarde}' komt {aantal} keer voor in "
                        f"'{type(instance).__name__}.{veld}'.",
                        UserWarning,
                    )
            for item in items:
                waarschuw_dubbele_ids(item)


def _classificeer_ruimte_dec(
    func: Callable[[EenhedenRuimte], Ruimtesoort | None],
) -> Callable[[EenhedenRuimte], Ruimtesoort | None]:
    """Logt de classificatie van de ruimte volgens het Woningwaarderingstelsel"""

    @wraps(func)
    def wrapper(ruimte: EenhedenRuimte) -> Ruimtesoort | None:
        ruimtesoort = func(ruimte)
        if ruimtesoort is not None:
            logger.debug(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) is geclassificeerd als een {ruimtesoort}"
            )
        else:
            logger.debug(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) kan niet worden geclassificeerd als een ruimtesoort."
            )
        return ruimtesoort

    return wrapper


# @_classificeer_ruimte_dec
def classificeer_ruimte(ruimte: EenhedenRuimte) -> RuimtesoortReferentiedata | None:
    """
    Classificeert de ruimte volgens het Woningwaarderingstelsel

    Args:
        ruimte (EenhedenRuimte): De ruimte die geclassificeerd moet worden.

    Returns:
        RuimtesoortReferentiedata | None: De classificatie van de ruimte volgens het Woningwaarderingstelsel.
            Geeft `None` terug als de ruimte niet kan worden gewaardeerd.
    """

    if ruimte.oppervlakte is None:
        warning_msg = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte"
        warnings.warn(warning_msg, UserWarning)
        return None

    if ruimte.soort is None:
        warning_msg = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen soort"
        warnings.warn(warning_msg, UserWarning)
        return None

    if ruimte.detail_soort is None:
        warning_msg = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort"
        warnings.warn(warning_msg, UserWarning)
        return None

    if ruimte.soort == Ruimtesoort.verkeersruimte:
        return Ruimtesoort.verkeersruimte

    if (
        ruimte.detail_soort
        in [  # deze ruimten zijn sowieso buitenruimten
            Ruimtedetailsoort.atrium_en_of_patio,
            Ruimtedetailsoort.achtertuin,
            Ruimtedetailsoort.balkon,
            Ruimtedetailsoort.zijtuin,
            Ruimtedetailsoort.voortuin,
            Ruimtedetailsoort.dakterras,
            Ruimtedetailsoort.terras,
            Ruimtedetailsoort.tuin,
            Ruimtedetailsoort.tuin_rondom,
            Ruimtedetailsoort.loggia,
            Ruimtedetailsoort.overige_buitenruimte,
        ]
        or (  # privé parkeerplaatsen buiten zijn privé buitenruimten
            ruimte.detail_soort
            in [
                Ruimtedetailsoort.carport,
            ]
            and not gedeeld_met_adressen(ruimte)
        )
        or (
            ruimte.detail_soort == Ruimtedetailsoort.parkeerplaats
            and ruimte.soort == Ruimtesoort.buitenruimte
            and not gedeeld_met_adressen(ruimte)
        )
    ):
        return Ruimtesoort.buitenruimte

    # Keuken, badkamer en doucheruimte worden altijd gewaardeerd als vertrek
    if ruimte.detail_soort in [
        Ruimtedetailsoort.keuken,
        Ruimtedetailsoort.badkamer,
        Ruimtedetailsoort.badkamer_met_toilet,
        Ruimtedetailsoort.doucheruimte,
    ]:
        return Ruimtesoort.vertrek

    if ruimte.detail_soort in [
        Ruimtedetailsoort.woonkamer,
        Ruimtedetailsoort.woon_en_of_slaapkamer,
        Ruimtedetailsoort.woonkamer_en_of_keuken,
        Ruimtedetailsoort.woon_en_of_slaapkamer_en_of_keuken,
        Ruimtedetailsoort.slaapkamer,
        Ruimtedetailsoort.overig_vertrek,
        Ruimtedetailsoort.bijkeuken,
        Ruimtedetailsoort.berging,
        Ruimtedetailsoort.bergruimte,
        Ruimtedetailsoort.wasruimte,
        Ruimtedetailsoort.kelder,
        Ruimtedetailsoort.serre,
        Ruimtedetailsoort.schuur,
        Ruimtedetailsoort.tussenkamer,
        Ruimtedetailsoort.containerruimte,
        Ruimtedetailsoort.recreatieruimte,
        Ruimtedetailsoort.overige_ruimte,
    ]:
        if (
            ruimte.detail_soort == Ruimtedetailsoort.berging
            and ruimte.soort == Ruimtesoort.overige_ruimten
        ):
            aantal_adressen = ruimte.gedeeld_met_aantal_adressen or 1
            if (
                Decimal(str(ruimte.oppervlakte)) / Decimal(str(aantal_adressen))
            ) >= Decimal("2"):
                return Ruimtesoort.overige_ruimten
            else:
                return None

        if ruimte.soort == Ruimtesoort.vertrek:
            if ruimte.oppervlakte >= 4:
                return Ruimtesoort.vertrek
            if ruimte.oppervlakte >= 2:
                return Ruimtesoort.overige_ruimten

        if ruimte.soort == Ruimtesoort.overige_ruimten:
            if ruimte.oppervlakte >= 2:
                return Ruimtesoort.overige_ruimten

    if ruimte.detail_soort == Ruimtedetailsoort.toiletruimte:
        # mag alleen als overige ruimte gewaardeerd worden
        if ruimte.oppervlakte >= 2:
            return Ruimtesoort.overige_ruimten

    if (
        ruimte.detail_soort in [Ruimtedetailsoort.garage]
        and not gedeeld_met_adressen(
            ruimte
        )  # garages moeten privé zijn om gecategoriseerd te worden als overige ruimte
        or (
            ruimte.detail_soort == Ruimtedetailsoort.parkeerplaats
            and ruimte.soort == Ruimtesoort.overige_ruimten
            and not gedeeld_met_adressen(ruimte)
        )
    ):
        if ruimte.oppervlakte >= 2.0:
            return Ruimtesoort.overige_ruimten

    if (
        ruimte.detail_soort == Ruimtedetailsoort.zolder
        or ruimte.detail_soort == Ruimtedetailsoort.zoldervertrek
    ):
        if ruimte.soort == Ruimtesoort.vertrek:
            if (
                heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.trap)
                and ruimte.oppervlakte >= 4
            ):
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een vaste trap: Ruimte wordt gewaardeerd als {Ruimtesoort.vertrek.naam}."
                )
                return Ruimtesoort.vertrek

            else:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen vaste trap gevonden: Ruimte wordt niet gewaardeerd als {ruimte.soort.naam}."
                )

        if ruimte.soort == Ruimtesoort.overige_ruimten:
            if (
                heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.trap)
                or heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.vlizotrap
                )
            ) and ruimte.oppervlakte >= 2:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een trap: Ruimte wordt gewaardeerd als {Ruimtesoort.overige_ruimten.naam}."
                )
                return Ruimtesoort.overige_ruimten

            else:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen trap: Ruimte wordt niet gewaardeerd als {Ruimtesoort.overige_ruimten.naam}."
                )

    return None


def voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte: EenhedenRuimte) -> str:
    """
    Deze functie voegt de oppervlakte van kasten toe aan een ruimte en retourneert de naam van de ruimte inclusief het aantal kasten.

    Args:
        ruimte (EenhedenRuimte): De ruimte waar kasten aan toegevoegd moeten worden.

    Returns:
        str: De naam van de ruimte inclusief het aantal toegevoegde kasten.
    """

    criterium_naam = ruimte.naam or "Naamloze ruimte"

    if ruimte.detail_soort is None or ruimte.detail_soort is None:
        message = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort"
        warnings.warn(message, UserWarning)
        return criterium_naam

    if ruimte.oppervlakte is None:
        message = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte"
        warnings.warn(message, UserWarning)
        return criterium_naam

    # Van vaste kasten wordt de netto oppervlakte bepaald
    # en bij de oppervlakte van de betreffende ruimte opgeteld.
    # Een kast waarvan de deur uitkomt op een
    # verkeersruimte, wordt niet gewaardeerd
    if ruimte.detail_soort not in [
        Ruimtedetailsoort.hal,
        Ruimtedetailsoort.overloop,
        Ruimtedetailsoort.entree,
        Ruimtedetailsoort.gang,
    ]:
        ruimte_kasten = [
            verbonden_ruimte
            for verbonden_ruimte in ruimte.verbonden_ruimten or []
            if verbonden_ruimte.detail_soort is not None
            and verbonden_ruimte.detail_soort == Ruimtedetailsoort.kast
        ]

        aantal_ruimte_kasten = len(ruimte_kasten)

        if aantal_ruimte_kasten > 0:
            ruimte.oppervlakte += sum(
                [
                    ruimte_kast.oppervlakte
                    for ruimte_kast in ruimte_kasten
                    if ruimte_kast.oppervlakte is not None
                ]
            )

            if ruimte.inhoud is not None:
                ruimte.inhoud += sum(
                    [
                        ruimte_kast.inhoud
                        for ruimte_kast in ruimte_kasten
                        if ruimte_kast.inhoud is not None
                    ]
                )

            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): de netto oppervlakte van {aantal_ruimte_kasten} verbonden {'kast' if aantal_ruimte_kasten == 1 else 'kasten'} is erbij opgeteld."
            )

            criterium_naam = f"{ruimte.naam} (+{aantal_ruimte_kasten} {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'})"
    return criterium_naam


def gedeeld_met_adressen(ruimte: EenhedenRuimte) -> bool:
    """Geeft True terug als de ruimte gedeeld is met andere adressen"""
    return (
        ruimte.gedeeld_met_aantal_adressen is not None
        and ruimte.gedeeld_met_aantal_adressen >= 2
    )


def gedeeld_met_onzelfstandige_woonruimten(
    ruimte: EenhedenRuimte,
) -> bool:
    """Geeft True terug als de ruimte gedeeld is met andere onzelfstandige woonruimten"""
    return (
        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
        and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 2
    )


WOONPLAATS_QUERY_TEMPLATE = """
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
prefix sor: <https://data.kkg.kadaster.nl/sor/model/def/>
prefix nen3610: <http://modellen.geostandaarden.nl/def/nen3610#>
prefix skos: <http://www.w3.org/2004/02/skos/core#>

select DISTINCT ?identificatie ?naam
where {{
  values ?postcode {{ "{postcode}" }}
  values ?huisnummer {{ {huisnummer} }}
  values ?huisnummertoevoeging {{ "{huisnummertoevoeging}" }}
  values ?huisletter {{ "{huisletter}" }}

  ?adres a imxgeo:Adres;
         imxgeo:postcode ?postcode;
         imxgeo:huisnummer ?adresHuisnummer;
         imxgeo:plaatsnaam ?naam;
         imxgeo:isAdresVanGebouw/imxgeo:bevindtZichOpPerceel/imxgeo:ligtInRegistratieveRuimte ?registratieveRuimte.
  ?registratieveRuimte a imxgeo:Woonplaats;
         imxgeo:status "Woonplaats aangewezen";
         nen3610:identificatie ?identificatie
  optional
  {{
    ?adres imxgeo:huisnummer ?adresHuisnummer.
  }}
  optional
  {{
    ?adres imxgeo:huisnummertoevoeging ?adresHuisnummertoevoeging.
  }}
  optional
  {{
    ?adres imxgeo:huisletter ?adresHuisletter.
  }}
  FILTER(
    (!BOUND(?adresHuisnummer) && ?huisnummer = "") ||
    (?adresHuisnummer = ?huisnummer)
  )
  FILTER(
    (!BOUND(?adresHuisletter) && ?huisletter = "") ||
    (lcase(?adresHuisletter) = lcase(?huisletter))
  )
  FILTER(
    (!BOUND(?adresHuisnummertoevoeging) && ?huisnummertoevoeging = "") ||
    (lcase(?adresHuisnummertoevoeging) = lcase(?huisnummertoevoeging))
  )
}}
"""


def _normaliseer_woonplaatsnaam(naam: str) -> str:
    return naam.strip().casefold()


def _formatteer_adresomschrijving(adres: EenhedenEenheidadres) -> str:
    return " ".join(
        filter(
            None,
            [
                adres.postcode,
                adres.huisnummer,
                adres.huisletter,
                adres.huisnummer_toevoeging,
            ],
        )
    )


def _woonplaatsnamen_komen_overeen(naam1: str, naam2: str) -> bool:
    return _normaliseer_woonplaatsnaam(naam1) == _normaliseer_woonplaatsnaam(naam2)


def get_woonplaats(adres: EenhedenEenheidadres) -> EenhedenWoonplaats | None:
    """
    Haalt de woonplaats op voor een gegeven adres.

    Als de BAG-woonplaatscode is opgegeven, wordt die gebruikt. Anders wordt de
    woonplaats bij het Kadaster opgehaald op basis van postcode, huisnummer,
    huisletter en huisnummertoevoeging. Is alleen een woonplaatsnaam opgegeven en
    die wijkt af van het Kadaster, dan wordt None teruggegeven met een waarschuwing.

    Args:
        adres (EenhedenEenheidadres): Adres met woonplaats met woonplaatscode of postcode, huisnummer en optioneel huisletter en huisnummertoevoeging.

    Returns:
        EenhedenWoonplaats | None: de woonplaats,
                               of None als de gegevens niet gevonden kunnen worden.
    """
    if adres.woonplaats is not None and adres.woonplaats.code is not None:
        return adres.woonplaats

    if not adres.postcode or not adres.huisnummer:
        return None

    logger.info("Woonplaats wordt opgehaald via het Kadaster")

    if not adres.huisnummer.isnumeric():
        warnings.warn(
            f'Huisnummer "{adres.huisnummer}" moet numeriek zijn. Maak gebruik van de attributen huisnummer, huisnummerToevoeging en huisletter voor de nummeraanduiding.'
        )

    query = WOONPLAATS_QUERY_TEMPLATE.format(
        postcode=adres.postcode.replace(" ", ""),
        huisnummer=int(adres.huisnummer),
        huisletter=adres.huisletter or "",
        huisnummertoevoeging=adres.huisnummer_toevoeging or "",
    )
    request_data = {"query": query, "format": "json"}

    try:
        response = requests.post(KADASTER_SPARQL_ENDPOINT, data=request_data, timeout=5)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and len(result) == 1:
            woonplaats_kadaster = EenhedenWoonplaats(
                code=result[0]["identificatie"], naam=result[0]["naam"]
            )
            if (
                adres.woonplaats
                and adres.woonplaats.naam
                and woonplaats_kadaster.naam
                and not _woonplaatsnamen_komen_overeen(
                    adres.woonplaats.naam, woonplaats_kadaster.naam
                )
            ):
                warnings.warn(
                    f"Woonplaats {woonplaats_kadaster.naam} is gevonden voor adres "
                    f"{_formatteer_adresomschrijving(adres)}, terwijl woonplaats "
                    f"{adres.woonplaats.naam} is opgegeven. Kan geen woonplaats "
                    f"bepalen voor de waardering.",
                    UserWarning,
                )
                return None
            return woonplaats_kadaster
        return None
    except requests.RequestException as e:
        warnings.warn(f"Fout bij het ophalen van woonplaatsdata: {e}", UserWarning)
        return None


def get_corop_voor_woonplaats(woonplaats_code: str) -> dict[str, str] | None:
    """
    Haalt het COROP-gebied op voor een gegeven woonplaatscode.

    Args:
        woonplaats_code (str): De code van de woonplaats.

    Returns:
        dict[str, str] | None: Een dictionary met 'code' en 'naam' van het COROP-gebied,
                               of None als de gegevens niet gevonden kunnen worden.
    """
    data = pd.read_csv(
        str(files("woningwaardering").joinpath("data/corop/corop.generated.csv")),
        dtype={"Woonplaatscode": str, "Gemeentecode": str, "COROP-gebiedcode": str},
    )

    woonplaats_dataframe = data[data["Woonplaatscode"] == woonplaats_code.lstrip("WP")]

    if woonplaats_dataframe.empty:
        return None

    resultaat = woonplaats_dataframe.iloc[0]

    return {"code": resultaat["COROP-gebiedcode"], "naam": resultaat["COROP-gebied"]}
