"""Gedeelde waardering voor gemeenschappelijke ruimten (Strategie B).

De module centraliseert GEM (zelfstandig) en GBA (onzelfstandig): groepering op
``(aantal_onzelfstandige_woonruimten, aantal_adressen)``, geneste
gedeeld-met-criteria en tot vijf geneste stelselgroepen.
Lege geneste stelselgroepen worden overgeslagen.

Example:
    Output van GBA-voorbeeld ``voorbeeld_beleidsboek``::

        gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen
          └─ gedeeld_met_2_onzelfstandige_woonruimten
               └─ gedeeld_met_2_adressen
                    ├─ Oppervlakte van vertrekken (punten op geneste stelselgroep)
                    ├─ Oppervlakte van overige ruimten
                    ├─ Keuken → ruimte-laag → Lengte aanrecht
                    └─ Sanitair → ruimte-laag → Douche

    Zie ``tests/data/onzelfstandige_woonruimten/stelselgroepen/
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen/output/
    voorbeeld_beleidsboek.json``.
"""

from __future__ import annotations

import warnings
from collections import defaultdict
from collections.abc import Callable, Iterator
from decimal import Decimal
from typing import NamedTuple

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.criterium_id import GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica.keuken.keuken import bouw_keuken
from woningwaardering.stelsels.gedeelde_logica.oppervlakte_van_overige_ruimten.oppervlakte_van_overige_ruimten import (
    bereken_oppervlakte_punten,
    bereken_zolder_correctie,
    is_zolder_zonder_vaste_trap,
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.gedeelde_logica.oppervlakte_van_vertrekken.oppervlakte_van_vertrekken import (
    waardeer_oppervlakte_van_vertrek,
)
from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    SanitairVoorRuimten,
    bouw_sanitair,
)
from woningwaardering.stelsels.gedeelde_logica.verkoeling_en_verwarming.verkoeling_en_verwarming import (
    VerkoelingEnVerwarmingResultaat,
    bouw_verkoeling_en_verwarming,
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.woningwaardering_groep import (
    Waardering,
    WoningwaarderingGroep,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    Referentiedata,
    WoningwaarderingResultatenWoningwaardering,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselReferentiedata,
)
from woningwaardering.vera.referentiedata.ruimtesoort import RuimtesoortReferentiedata


class _Deelgroep(NamedTuple):
    aantal_onz: int
    aantal_adressen: int

    @property
    def factor(self) -> Decimal:
        return Decimal(str(self.aantal_onz)) * Decimal(str(self.aantal_adressen))


class _OppervlakteDetail(NamedTuple):
    ruimte_id: str
    naam: str
    meeteenheid: Referentiedata | None
    aantal: float | None


def waardeer_gemeenschappelijke_ruimten(
    *,
    groep: WoningwaarderingGroep,
    ruimten: list[EenhedenRuimte],
    sanitair_voor_ruimten: SanitairVoorRuimten,
) -> None:
    """Waardeert gemeenschappelijke ruimten volgens Strategie B.

    GEM en GBA delen dezelfde keten: groepeer op (onz, adressen), nest onder
    gedeeld-met-criteria, en voeg per deelgroep geneste stelselgroepen toe.
    Lege geneste stelselgroepen worden overgeslagen.

    Args:
        groep (WoningwaarderingGroep): Doelgroep; ``woningwaarderingen`` wordt
            aangevuld.
        ruimten (list[EenhedenRuimte]): Gedeelde ruimten (reeds gefilterd door de caller).
        sanitair_voor_ruimten (SanitairVoorRuimten): Sanitair-waardering per deelgroep (batch voor onz).

    Example:
        Zie ``tests/data/onzelfstandige_woonruimten/stelselgroepen/
        gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen/output/
        voorbeeld_beleidsboek.json``.

    Raises:
        ValueError: Als ``groep.criterium_groep`` ontbreekt.
        TypeError: Als ``stelsel`` geen ``WoningwaarderingstelselReferentiedata`` is.
    """
    if groep.criterium_groep is None:
        raise ValueError("criterium_groep is verplicht op WoningwaarderingGroep")
    stelsel_raw = groep.criterium_groep.stelsel
    if not isinstance(stelsel_raw, WoningwaarderingstelselReferentiedata):
        raise TypeError("stelsel moet WoningwaarderingstelselReferentiedata zijn")
    stelsel = stelsel_raw
    deelgroepen = _groepeer_deelgroepen(ruimten)
    # Maximering (bijv. max 4 pt verwarmde overige ruimten) telt over alle gedeelde
    # ruimten; niet per deelgroep apart.
    # Maximering loopt over alle ruimten; per deelgroep filteren we de bronresultaten.
    verkoeling_resultaten: list[VerkoelingEnVerwarmingResultaat] = list(
        waardeer_verkoeling_en_verwarming(ruimten)
    )
    # Eén gedeeld-met-onz-laag per aantal onzelfstandige woonruimten (hergebruik tussen deelgroepen).
    gedeeld_met_onz_handles: dict[int, Waardering] = {}

    for deelgroep, groep_ruimten in sorted(
        deelgroepen.items(),
        key=lambda item: (item[0].aantal_onz, item[0].aantal_adressen),
    ):
        if deelgroep.aantal_adressen <= 1:
            continue

        if deelgroep.aantal_onz > 1:
            onz_handle = gedeeld_met_onz_handles.get(deelgroep.aantal_onz)
            if onz_handle is None:
                onz_handle = groep.met_gedeeld_met_criterium(
                    deelgroep.aantal_onz,
                    GedeeldMetSoort.onzelfstandige_woonruimten,
                    naam=utils.naam_gedeeld_met_groep(
                        deelgroep.aantal_onz,
                        soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                    ),
                )
                gedeeld_met_onz_handles[deelgroep.aantal_onz] = onz_handle
            bovenliggende: Waardering | WoningwaarderingGroep = onz_handle
        else:
            bovenliggende = groep

        gedeeld_met_adressen = bovenliggende.met_gedeeld_met_criterium(
            deelgroep.aantal_adressen,
            GedeeldMetSoort.adressen,
            naam=utils.naam_gedeeld_met_groep(
                deelgroep.aantal_adressen,
                soort=GedeeldMetSoort.adressen,
            ),
        )

        _bouw_oppervlakte_van_vertrekken(
            groep_ruimten, gedeeld_met_adressen, deelgroep.factor
        )
        _bouw_oppervlakte_van_overige_ruimten(
            groep_ruimten, gedeeld_met_adressen, deelgroep.factor
        )
        groep_ruimte_ids = {
            ruimte.id for ruimte in groep_ruimten if ruimte.id is not None
        }
        verkoeling_geneste = gedeeld_met_adressen.met_onderliggend(
            Woningwaarderingstelselgroep.verkoeling_en_verwarming.name,
            naam=Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam,
        )
        bouw_verkoeling_en_verwarming(
            [
                (ruimte, bron)
                for ruimte, bron in verkoeling_resultaten
                if ruimte.id in groep_ruimte_ids
            ],
            verkoeling_geneste,
            deelgroep.factor,
        )
        keuken_geneste = gedeeld_met_adressen.met_onderliggend(
            Woningwaarderingstelselgroep.keuken.name,
            naam=Woningwaarderingstelselgroep.keuken.naam,
        )
        bouw_keuken(groep_ruimten, stelsel, keuken_geneste, deelgroep.factor)
        sanitair_geneste = gedeeld_met_adressen.met_onderliggend(
            Woningwaarderingstelselgroep.sanitair.name,
            naam=Woningwaarderingstelselgroep.sanitair.naam,
        )
        bouw_sanitair(
            groep_ruimten, sanitair_voor_ruimten, sanitair_geneste, deelgroep.factor
        )


def _groepeer_deelgroepen(
    ruimten: list[EenhedenRuimte],
) -> dict[_Deelgroep, list[EenhedenRuimte]]:
    """Groepeert ruimten op (aantal_onz, aantal_adressen).

    Alleen ruimten met ``gedeeld_met_aantal_eenheden > 1`` komen in aanmerking;
    per unieke combinatie ontstaat één deelgroep met dezelfde factor.

    Args:
        ruimten (list[EenhedenRuimte]): Gedeelde ruimten van de caller.

    Returns:
        dict[_Deelgroep, list[EenhedenRuimte]]: Deelgroep naar ruimten.

    Example:
        Twee ruimten met (2 onz, 4 adressen) → één deelgroep, factor ``8``.
    """
    deelgroepen: dict[_Deelgroep, list[EenhedenRuimte]] = defaultdict(list)
    for ruimte in ruimten:
        aantal_adressen = ruimte.gedeeld_met_aantal_eenheden or 1
        if aantal_adressen <= 1:
            continue
        aantal_onz = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
        deelgroepen[_Deelgroep(aantal_onz, aantal_adressen)].append(ruimte)
    return deelgroepen


def _verzamel_oppervlakte_details(
    ruimten: list[EenhedenRuimte],
    *,
    ruimtesoort: RuimtesoortReferentiedata,
    stelselgroep_naam_key: str,
    waardeer_ruimte: Callable[
        [EenhedenRuimte], Iterator[WoningwaarderingResultatenWoningwaardering]
    ],
) -> list[_OppervlakteDetail]:
    """Verzamelt oppervlakte-detailregels voordat een geneste stelselgroep wordt opgebouwd.

    Roept per ruimte eerst de bron-``waardeer_*`` aan zodat waarschuwingen behouden
    blijven. Het totaal voor puntenberekening komt uit de som van detail-``aantal``,
    niet uit alle ruimten met oppervlakte — zo sluit subtotaal en details op elkaar aan
    wanneer sommige ruimten geen detail opleveren.

    Args:
        ruimten (list[EenhedenRuimte]): Ruimten in de deelgroep (reeds gefilterd op soort).
        ruimtesoort (RuimtesoortReferentiedata): Vertrek of overige ruimten.
        stelselgroep_naam_key (str): Sleutel van de bron-stelselgroep in het criteriumid.
        waardeer_ruimte (Callable[[EenhedenRuimte], Iterator[WoningwaarderingResultatenWoningwaardering]]): Bron-waardering per ruimte (bijv. ``waardeer_oppervlakte_van_vertrek``).

    Returns:
        list[_OppervlakteDetail]: Detailregels voor de keten.
    """
    details: list[_OppervlakteDetail] = []
    for ruimte in ruimten:
        if utils.classificeer_ruimte(ruimte) != ruimtesoort:
            continue
        if ruimte.soort is None:
            warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
            continue
        # waardeer_* draaien voor warnings; alleen geslaagde details tellen mee voor totaal.
        bron = next(iter(waardeer_ruimte(ruimte)), None)
        if bron is None or bron.criterium is None or bron.criterium.naam is None:
            continue
        # bijv. ``oppervlakte_van_vertrekken__Space_1``
        # ruimte_id = ``Space_1``
        ruimte_id = utils.criteriumid_onder_stelselgroep(
            bron.criterium.id, stelselgroep_naam_key
        )
        if ruimte_id is None:
            continue
        details.append(
            _OppervlakteDetail(
                ruimte_id=ruimte_id,
                naam=bron.criterium.naam,
                meeteenheid=bron.criterium.meeteenheid,
                aantal=bron.aantal,
            )
        )
    return details


def _bouw_oppervlakte_van_vertrekken(
    ruimten: list[EenhedenRuimte],
    gedeeld_met_adressen: Waardering,
    factor: Decimal,
) -> None:
    """Nest oppervlakte van vertrekken onder het gedeeld-met-adressen-criterium.

    Berekent gedeelde punten (factor = onz × adressen) op de geneste stelselgroep;
    detailregels tonen alleen oppervlakte zonder eigen punten. Bij geen geldige
    details wordt niets uitgegeven (lege geneste stelselgroep overslaan).

    Args:
        ruimten (list[EenhedenRuimte]): Ruimten in de deelgroep.
        gedeeld_met_adressen (Waardering): Keten-handle onder gedeeld-met adressen.
        factor (Decimal): Deler voor punten (onz × adressen).

    Returns:
        None: Mutatie via ``met_onderliggend`` op de keten-handle.

    Example:
        Zie ``tests/data/onzelfstandige_woonruimten/stelselgroepen/
        gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen/output/
        voorbeeld_beleidsboek.json`` onder ``...__oppervlakte_van_vertrekken``.
    """
    vertrekken = [
        ruimte
        for ruimte in ruimten
        if utils.classificeer_ruimte(ruimte) == Ruimtesoort.vertrek
    ]
    if not vertrekken:
        return

    naam_key = Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.name
    details = _verzamel_oppervlakte_details(
        vertrekken,
        ruimtesoort=Ruimtesoort.vertrek,
        stelselgroep_naam_key=naam_key,
        waardeer_ruimte=waardeer_oppervlakte_van_vertrek,
    )
    if not details:
        return

    totaal_oppervlakte = sum(
        (
            Decimal(str(detail.aantal))
            for detail in details
            if detail.aantal is not None
        ),
        start=Decimal("0"),
    )
    punten = bereken_oppervlakte_punten(totaal_oppervlakte, Decimal("1.0")) / factor
    geneste = gedeeld_met_adressen.met_onderliggend(
        naam_key,
        naam=Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam,
        punten=float(punten),
    )
    for ruimte_id, naam, meeteenheid, aantal in details:
        geneste.met_onderliggend(
            ruimte_id,
            naam=naam,
            meeteenheid=meeteenheid,
            aantal=aantal,
        )


def _bouw_oppervlakte_van_overige_ruimten(
    ruimten: list[EenhedenRuimte],
    gedeeld_met_adressen: Waardering,
    factor: Decimal,
) -> None:
    """Nest oppervlakte van overige ruimten onder gedeeld-met, met optionele zoldercorrectie.

    Zelfde patroon als vertrekken, met factor 0,75. Bij zolder zonder vaste trap:
    structurele geneste stelselgroep → subtotaal → details → correcties (beleidsboek-pad).
    Zonder zoldercorrectie: punten direct op de geneste stelselgroep.

    Args:
        ruimten (list[EenhedenRuimte]): Ruimten in de deelgroep.
        gedeeld_met_adressen (Waardering): Keten-handle onder gedeeld-met adressen.
        factor (Decimal): Deler voor punten (onz × adressen).

    Returns:
        None: Mutatie via ``met_onderliggend`` op de keten-handle.

    Example:
        Met zoldercorrectie: ``tests/data/zelfstandige_woonruimten/stelselgroepen/
        gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen/output/
        zolder_zonder_vaste_trap.json``.
    """
    overige = [
        ruimte
        for ruimte in ruimten
        if utils.classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
    ]
    if not overige:
        return

    naam_key = Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.name
    naam = Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam
    heeft_correcties = any(is_zolder_zonder_vaste_trap(ruimte) for ruimte in overige)

    # Zolderpad: geneste (structureel) → subtotaal → details → correcties.
    if heeft_correcties:
        details = _verzamel_oppervlakte_details(
            overige,
            ruimtesoort=Ruimtesoort.overige_ruimten,
            stelselgroep_naam_key=naam_key,
            waardeer_ruimte=waardeer_oppervlakte_van_overige_ruimte,
        )
        if not details and not any(
            is_zolder_zonder_vaste_trap(ruimte) for ruimte in overige
        ):
            return

        totaal_oppervlakte = sum(
            (
                Decimal(str(detail.aantal))
                for detail in details
                if detail.aantal is not None
            ),
            start=Decimal("0"),
        )
        punten = (
            bereken_oppervlakte_punten(totaal_oppervlakte, Decimal("0.75")) / factor
        )

        geneste = gedeeld_met_adressen.met_onderliggend(naam_key, naam=naam)
        bovenliggend_voor_details = geneste.met_onderliggend(
            "subtotaal",
            naam="Subtotaal",
            aantal=float(utils.rond_af(totaal_oppervlakte, decimalen=2)),
            punten=float(punten),
            meeteenheid=Meeteenheid.vierkante_meter_m2,
        )
        for ruimte_id, detail_naam, meeteenheid, aantal in details:
            bovenliggend_voor_details.met_onderliggend(
                ruimte_id,
                naam=detail_naam,
                meeteenheid=meeteenheid,
                aantal=aantal,
            )

        for ruimte in overige:
            if not is_zolder_zonder_vaste_trap(ruimte):
                continue
            zolder_oppervlakte = utils.rond_af(ruimte.oppervlakte, decimalen=2)
            correctie_punten = (
                bereken_zolder_correctie(totaal_oppervlakte, zolder_oppervlakte)
                / factor
            )
            geneste.met_onderliggend(
                f"{ruimte.id}__correctie_zolder_zonder_vaste_trap",
                naam="Correctie: zolder zonder vaste trap",
                punten=float(correctie_punten),
            )
        return

    details = _verzamel_oppervlakte_details(
        overige,
        ruimtesoort=Ruimtesoort.overige_ruimten,
        stelselgroep_naam_key=naam_key,
        waardeer_ruimte=waardeer_oppervlakte_van_overige_ruimte,
    )
    if not details:
        return

    totaal_oppervlakte = sum(
        (
            Decimal(str(detail.aantal))
            for detail in details
            if detail.aantal is not None
        ),
        start=Decimal("0"),
    )
    punten = bereken_oppervlakte_punten(totaal_oppervlakte, Decimal("0.75")) / factor
    geneste = gedeeld_met_adressen.met_onderliggend(
        naam_key,
        naam=naam,
        punten=float(punten),
    )
    for ruimte_id, detail_naam, meeteenheid, aantal in details:
        geneste.met_onderliggend(
            ruimte_id,
            naam=detail_naam,
            meeteenheid=meeteenheid,
            aantal=aantal,
        )
