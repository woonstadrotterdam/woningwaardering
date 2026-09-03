from decimal import ROUND_HALF_UP, Decimal

from woningwaardering.stelsels.utils import som_effectieve_aantal_waarderingen
from woningwaardering.vera.bvg.generated import (
    Referentiedata,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelsel import (
    Woningwaarderingstelsel,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)

_STELSELGROEPEN_MET_SUBTOTAAL_AANTAL = frozenset(
    {
        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
        Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,
    }
)

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


class WoningwaarderingRapport:
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

    Wordt gebruikt voor de regels in de samenvatting, de waarderingen in een
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
                "Totaal afgerond op hele punten",
                punten=_format_punten_cel(_tabel_fmt_num(resultaat.punten)),
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


def naar_rapport(
    woningwaardering_resultaat: (
        WoningwaarderingResultatenWoningwaarderingResultaat
        | WoningwaarderingResultatenWoningwaarderingGroep
    ),
    *,
    eenheid_id: str | None = None,
) -> WoningwaarderingRapport:
    """
    Genereer een rapport met de details van een woningwaarderingresultaat.

    Args:
        woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | WoningwaarderingResultatenWoningwaarderingGroep): Het object om de gegevens uit te halen.
        eenheid_id (str | None): Optioneel eenheid-id voor de samenvattingskop.

    Returns:
        WoningwaarderingRapport: Samenvatting (volledig resultaat) en detailsecties.
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

    return WoningwaarderingRapport(lines)
