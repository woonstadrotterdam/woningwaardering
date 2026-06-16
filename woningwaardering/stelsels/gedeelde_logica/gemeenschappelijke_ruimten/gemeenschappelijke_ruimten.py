"""Gedeelde waardering voor gemeenschappelijke ruimten (Strategie B).

De module centraliseert GEM (zelfstandig) en GBA (onzelfstandig): groepering op
``(aantal_onzelfstandige_woonruimten, aantal_adressen)``, geneste
``gedeeld_met``-aggregaten en tot vijf secties met privé-stelselgroepnamen.
Lege secties worden niet geëmit.

Example:
    Output van GBA-voorbeeld ``voorbeeld_beleidsboek``::

        gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen
          └─ gedeeld_met_2_onzelfstandige_woonruimten
               └─ gedeeld_met_2_adressen
                    ├─ Oppervlakte van vertrekken (punten op sectie)
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
from collections.abc import Callable, Iterable
from decimal import Decimal
from typing import NamedTuple

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.criterium_id import (
    CriteriumId,
    GedeeldMetSoort,
    weergavenaam_voor,
)
from woningwaardering.stelsels.gedeelde_logica.keuken.keuken import waardeer_keuken
from woningwaardering.stelsels.gedeelde_logica.oppervlakte_van_overige_ruimten.oppervlakte_van_overige_ruimten import (
    bereken_oppervlakte_punten,
    bereken_zolder_correctie,
    is_zolder_zonder_vaste_trap,
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.gedeelde_logica.oppervlakte_van_vertrekken.oppervlakte_van_vertrekken import (
    waardeer_oppervlakte_van_vertrek,
)
from woningwaardering.stelsels.gedeelde_logica.verkoeling_en_verwarming.verkoeling_en_verwarming import (
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselgroepReferentiedata,
    WoningwaarderingstelselReferentiedata,
)


class _Deelgroep(NamedTuple):
    aantal_onz: int
    aantal_adressen: int

    @property
    def factor(self) -> Decimal:
        return Decimal(str(self.aantal_onz)) * Decimal(str(self.aantal_adressen))


SanitairVoorRuimten = Callable[
    [list[EenhedenRuimte]],
    Iterable[tuple[EenhedenRuimte, list[WoningwaarderingResultatenWoningwaardering]]],
]

VerkoelingEnVerwarmingResultaat = tuple[
    EenhedenRuimte, WoningwaarderingResultatenWoningwaardering
]


def waardeer_gemeenschappelijke_ruimten(
    *,
    stelselgroep: WoningwaarderingstelselgroepReferentiedata,
    stelsel: WoningwaarderingstelselReferentiedata,
    ruimten: list[EenhedenRuimte],
    sanitair_voor_ruimten: SanitairVoorRuimten,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    """Waardeert gemeenschappelijke ruimten volgens Strategie B.

    Groepeert ruimten op ``(aantal_onzelfstandige_woonruimten, aantal_adressen)``
    en bouwt per deelgroep tot vijf secties onder het ``gedeeld_met_n_adressen``-
    aggregaat. Lege secties worden niet geëmit.

    Args:
        stelselgroep (WoningwaarderingstelselgroepReferentiedata): GEM- of GBA-stelselgroep.
        stelsel (WoningwaarderingstelselReferentiedata): Zelfstandig of onzelfstandig stelsel.
        ruimten (list[EenhedenRuimte]): Gedeelde ruimten (reeds gefilterd door de caller).
        sanitair_voor_ruimten (SanitairVoorRuimten): Sanitair-waardering per deelgroep (batch voor onz).

    Returns:
        list[WoningwaarderingResultatenWoningwaardering]: Alle waarderingen inclusief gedeeld-met-koppen en secties.

    Example:
        Zie ``tests/data/onzelfstandige_woonruimten/stelselgroepen/
        gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen/output/
        voorbeeld_beleidsboek.json``.
    """
    deelgroepen = _groepeer_deelgroepen(ruimten)
    waarderingen: list[WoningwaarderingResultatenWoningwaardering] = []
    stelselgroep_id = CriteriumId.voor_stelselgroep(stelselgroep)
    # Maximering (bijv. max 4 pt verwarmde overige ruimten) telt over alle gedeelde
    # ruimten; niet per deelgroep apart.
    verkoeling_resultaten: list[VerkoelingEnVerwarmingResultaat] = list(
        waardeer_verkoeling_en_verwarming(ruimten)
    )
    geëmitte_onz_koppen: set[str] = set()

    for deelgroep, groep_ruimten in sorted(
        deelgroepen.items(),
        key=lambda item: (item[0].aantal_onz, item[0].aantal_adressen),
    ):
        onz_id = (
            stelselgroep_id.gedeeld_met_criterium(
                deelgroep.aantal_onz, GedeeldMetSoort.onzelfstandige_woonruimten
            )
            if deelgroep.aantal_onz > 1
            else None
        )
        if deelgroep.aantal_adressen > 1:
            if onz_id is not None:
                adressen_id = onz_id.gedeeld_met_criterium(
                    deelgroep.aantal_adressen, GedeeldMetSoort.adressen
                )
            else:
                adressen_id = stelselgroep_id.gedeeld_met_criterium(
                    deelgroep.aantal_adressen, GedeeldMetSoort.adressen
                )
        else:
            adressen_id = None

        if adressen_id is None:
            continue

        sectie_waarderingen: list[WoningwaarderingResultatenWoningwaardering] = []
        sectie_waarderingen.extend(
            _bouw_oppervlakte_van_vertrekken_sectie(
                groep_ruimten, adressen_id, deelgroep.factor
            )
        )
        sectie_waarderingen.extend(
            _bouw_oppervlakte_van_overige_ruimten_sectie(
                groep_ruimten, adressen_id, deelgroep.factor
            )
        )
        groep_ruimte_ids = {
            ruimte.id for ruimte in groep_ruimten if ruimte.id is not None
        }
        sectie_waarderingen.extend(
            _bouw_verkoeling_en_verwarming_sectie(
                [
                    (ruimte, bron)
                    for ruimte, bron in verkoeling_resultaten
                    if ruimte.id in groep_ruimte_ids
                ],
                adressen_id,
                deelgroep.factor,
            )
        )
        sectie_waarderingen.extend(
            _bouw_keuken_sectie(groep_ruimten, stelsel, adressen_id, deelgroep.factor)
        )
        sectie_waarderingen.extend(
            _bouw_sanitair_sectie(
                groep_ruimten,
                sanitair_voor_ruimten,
                adressen_id,
                deelgroep.factor,
            )
        )

        if not sectie_waarderingen:
            continue

        if onz_id is not None and str(onz_id) not in geëmitte_onz_koppen:
            waarderingen.append(
                _maak_kop(
                    onz_id,
                    utils.naam_gedeeld_met_groep(
                        deelgroep.aantal_onz,
                        soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                    ),
                )
            )
            geëmitte_onz_koppen.add(str(onz_id))

        waarderingen.append(
            _maak_kop(
                adressen_id,
                utils.naam_gedeeld_met_groep(
                    deelgroep.aantal_adressen,
                    soort=GedeeldMetSoort.adressen,
                ),
                bovenliggend=onz_id,
            )
        )
        waarderingen.extend(sectie_waarderingen)

    return waarderingen


def _groepeer_deelgroepen(
    ruimten: list[EenhedenRuimte],
) -> dict[_Deelgroep, list[EenhedenRuimte]]:
    deelgroepen: dict[_Deelgroep, list[EenhedenRuimte]] = defaultdict(list)
    for ruimte in ruimten:
        aantal_adressen = ruimte.gedeeld_met_aantal_eenheden or 1
        if aantal_adressen <= 1:
            continue
        aantal_onz = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
        deelgroepen[_Deelgroep(aantal_onz, aantal_adressen)].append(ruimte)
    return deelgroepen


def _maak_kop(
    criterium_id: CriteriumId,
    naam: str,
    *,
    bovenliggend: CriteriumId | None = None,
) -> WoningwaarderingResultatenWoningwaardering:
    criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
        id=str(criterium_id),
        naam=naam,
    )
    if bovenliggend is not None:
        criterium.bovenliggende_criterium = bovenliggend.naar_criterium_sleutels()
    return WoningwaarderingResultatenWoningwaardering(criterium=criterium)


def _suffix_na_stelselgroep(bron_id: str | None, stelselgroep_name: str) -> str | None:
    if not bron_id:
        return None
    prefix = f"{stelselgroep_name}__"
    if not bron_id.startswith(prefix):
        return None
    return bron_id[len(prefix) :]


def _herschrijf_onder_sectie(
    bron: WoningwaarderingResultatenWoningwaardering,
    *,
    sectie_id: CriteriumId,
    factor: Decimal,
    private_stelselgroep_name: str,
    bovenliggende_override: CriteriumId | None = None,
    met_ruimte_laag: bool = False,
    ruimte_id: str | None = None,
) -> WoningwaarderingResultatenWoningwaardering | None:
    if bron.criterium is None:
        return None

    suffix = _suffix_na_stelselgroep(bron.criterium.id, private_stelselgroep_name)
    if suffix is None:
        return None

    if met_ruimte_laag and ruimte_id is not None:
        if suffix.startswith(f"{ruimte_id}__"):
            installatie_suffix = suffix[len(ruimte_id) + 2 :]
            parent = bovenliggende_override or sectie_id.met_onderliggend(ruimte_id)
            nieuw_id = parent.met_onderliggend(installatie_suffix)
        else:
            parent = bovenliggende_override or sectie_id
            nieuw_id = parent.met_onderliggend(suffix)
    else:
        parent = bovenliggende_override or sectie_id
        nieuw_id = parent.met_onderliggend(suffix)

    criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
        id=str(nieuw_id),
        naam=bron.criterium.naam,
        meeteenheid=bron.criterium.meeteenheid,
        bovenliggende_criterium=parent.naar_criterium_sleutels(),
    )
    nieuw = WoningwaarderingResultatenWoningwaardering(
        criterium=criterium,
        aantal=bron.aantal,
        punten=None,
    )

    if bron.punten is not None:
        nieuw.punten = float(
            utils.rond_af(Decimal(str(bron.punten)) / factor, decimalen=2)
        )

    return nieuw


def _maak_ruimte_criterium(
    sectie_id: CriteriumId,
    ruimte: EenhedenRuimte,
) -> WoningwaarderingResultatenWoningwaardering:
    ruimte_id = CriteriumId(
        path=str(sectie_id.met_onderliggend(ruimte.id)),
        bovenliggend=sectie_id,
    )
    return WoningwaarderingResultatenWoningwaardering(
        criterium=ruimte_id.met_criterium(utils.ruimte_weergavenaam(ruimte)),
        punten=None,
    )


def _sectie_id(adressen_id: CriteriumId, sectie_name: str) -> CriteriumId:
    return adressen_id.met_onderliggend(sectie_name)


def _bouw_oppervlakte_van_vertrekken_sectie(
    ruimten: list[EenhedenRuimte],
    adressen_id: CriteriumId,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    vertrekken = [
        ruimte
        for ruimte in ruimten
        if utils.classificeer_ruimte(ruimte) == Ruimtesoort.vertrek
    ]
    if not vertrekken:
        return []

    sectie = _sectie_id(
        adressen_id, Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.name
    )
    totaal_oppervlakte = sum(
        (
            utils.rond_af(ruimte.oppervlakte, decimalen=2)
            for ruimte in vertrekken
            if ruimte.oppervlakte is not None
        ),
        start=Decimal("0"),
    )
    sectie_punten = (
        bereken_oppervlakte_punten(totaal_oppervlakte, Decimal("1.0")) / factor
    )

    details: list[WoningwaarderingResultatenWoningwaardering] = []
    for ruimte in vertrekken:
        if ruimte.soort is None:
            warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
            continue
        oppervlakte_resultaat = next(waardeer_oppervlakte_van_vertrek(ruimte), None)
        if oppervlakte_resultaat is None or oppervlakte_resultaat.criterium is None:
            continue
        detail = _herschrijf_onder_sectie(
            oppervlakte_resultaat,
            sectie_id=sectie,
            factor=factor,
            private_stelselgroep_name=Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.name,
        )
        if detail is not None:
            detail.punten = None
            details.append(detail)

    if not details:
        return []

    sectie_waardering = WoningwaarderingResultatenWoningwaardering(
        criterium=sectie.met_criterium(
            Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam
        ),
        punten=float(sectie_punten),
    )
    return [sectie_waardering, *details]


def _bouw_oppervlakte_van_overige_ruimten_sectie(
    ruimten: list[EenhedenRuimte],
    adressen_id: CriteriumId,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    overige = [
        ruimte
        for ruimte in ruimten
        if utils.classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
    ]
    if not overige:
        return []

    sectie = _sectie_id(
        adressen_id, Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.name
    )
    totaal_oppervlakte = sum(
        (
            utils.rond_af(ruimte.oppervlakte, decimalen=2)
            for ruimte in overige
            if ruimte.oppervlakte is not None
        ),
        start=Decimal("0"),
    )
    sectie_punten = (
        bereken_oppervlakte_punten(totaal_oppervlakte, Decimal("0.75")) / factor
    )

    details: list[WoningwaarderingResultatenWoningwaardering] = []
    for ruimte in overige:
        if ruimte.soort is None:
            warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
            continue
        oppervlakte_resultaat = next(
            waardeer_oppervlakte_van_overige_ruimte(ruimte), None
        )
        if oppervlakte_resultaat is None or oppervlakte_resultaat.criterium is None:
            continue
        detail = _herschrijf_onder_sectie(
            oppervlakte_resultaat,
            sectie_id=sectie,
            factor=factor,
            private_stelselgroep_name=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.name,
        )
        if detail is not None:
            detail.punten = None
            details.append(detail)

    correcties: list[WoningwaarderingResultatenWoningwaardering] = []
    for ruimte in overige:
        if not is_zolder_zonder_vaste_trap(ruimte):
            continue
        zolder_oppervlakte = utils.rond_af(ruimte.oppervlakte, decimalen=2)
        correctie_punten = (
            bereken_zolder_correctie(totaal_oppervlakte, zolder_oppervlakte) / factor
        )
        correctie_id = sectie.met_onderliggend(ruimte.id).met_onderliggend(
            "correctie_zolder_zonder_vaste_trap"
        )
        correctie = WoningwaarderingResultatenWoningwaardering(
            criterium=correctie_id.met_criterium("Correctie: zolder zonder vaste trap"),
            punten=float(correctie_punten),
        )
        if correctie.criterium is not None:
            correctie.criterium.bovenliggende_criterium = (
                sectie.naar_criterium_sleutels()
            )
        correcties.append(correctie)

    if not details and not correcties:
        return []

    sectie_naam = Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam
    if correcties:
        sectie_kop = WoningwaarderingResultatenWoningwaardering(
            criterium=sectie.met_criterium(sectie_naam),
        )
        subtotaal_id = sectie.met_onderliggend("subtotaal")
        subtotaal = WoningwaarderingResultatenWoningwaardering(
            criterium=subtotaal_id.met_criterium(
                "Subtotaal",
                meeteenheid=Meeteenheid.vierkante_meter_m2,
            ),
            aantal=float(utils.rond_af(totaal_oppervlakte, decimalen=2)),
            punten=float(sectie_punten),
        )
        sectie_prefix = f"{sectie}__"
        for detail in details:
            if detail.criterium is None or not detail.criterium.id:
                continue
            ruimte_suffix = detail.criterium.id.removeprefix(sectie_prefix)
            detail.criterium.id = str(subtotaal_id.met_onderliggend(ruimte_suffix))
            detail.criterium.bovenliggende_criterium = (
                WoningwaarderingCriteriumSleutels(id=str(subtotaal_id))
            )
        return [sectie_kop, subtotaal, *details, *correcties]

    return [
        WoningwaarderingResultatenWoningwaardering(
            criterium=sectie.met_criterium(sectie_naam),
            punten=float(sectie_punten),
        ),
        *details,
    ]


def _bouw_verkoeling_en_verwarming_sectie(
    verkoeling_resultaten: list[VerkoelingEnVerwarmingResultaat],
    adressen_id: CriteriumId,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    sectie = _sectie_id(
        adressen_id, Woningwaarderingstelselgroep.verkoeling_en_verwarming.name
    )
    details: list[WoningwaarderingResultatenWoningwaardering] = []
    groeperingen: dict[str, WoningwaarderingResultatenWoningwaardering] = {}
    private_naam = Woningwaarderingstelselgroep.verkoeling_en_verwarming.name

    for _ruimte, bron in verkoeling_resultaten:
        if bron.criterium is None or bron.criterium.id is None:
            continue
        suffix = _suffix_na_stelselgroep(bron.criterium.id, private_naam)
        if suffix is None or "__" not in suffix:
            continue

        groepering_deel, detail_deel = suffix.split("__", 1)
        groepering_id = sectie.met_onderliggend(groepering_deel)
        if str(groepering_id) not in groeperingen:
            groeperingen[str(groepering_id)] = (
                WoningwaarderingResultatenWoningwaardering(
                    criterium=groepering_id.met_criterium(
                        weergavenaam_voor(groepering_deel)
                    ),
                )
            )

        detail_id = groepering_id.met_onderliggend(detail_deel)
        detail = WoningwaarderingResultatenWoningwaardering(
            criterium=detail_id.met_criterium(
                bron.criterium.naam,
                meeteenheid=bron.criterium.meeteenheid,
            ),
            aantal=bron.aantal,
        )
        if bron.punten is not None:
            detail.punten = float(
                utils.rond_af(Decimal(str(bron.punten)) / factor, decimalen=2)
            )
        details.append(detail)

    if not details:
        return []

    sectie_waardering = WoningwaarderingResultatenWoningwaardering(
        criterium=sectie.met_criterium(
            Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam
        ),
    )
    return [sectie_waardering, *groeperingen.values(), *details]


def _bouw_keuken_sectie(
    ruimten: list[EenhedenRuimte],
    stelsel: WoningwaarderingstelselReferentiedata,
    adressen_id: CriteriumId,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    sectie = _sectie_id(adressen_id, Woningwaarderingstelselgroep.keuken.name)
    ruimte_criteria: dict[str, WoningwaarderingResultatenWoningwaardering] = {}
    details: list[WoningwaarderingResultatenWoningwaardering] = []

    for ruimte in ruimten:
        if ruimte.id is None or ruimte.detail_soort is None:
            continue
        ruimte_details: list[WoningwaarderingResultatenWoningwaardering] = []
        ruimte_criterium_id = CriteriumId(
            path=str(sectie.met_onderliggend(ruimte.id)),
            bovenliggend=sectie,
        )
        for bron in waardeer_keuken(ruimte, stelsel):
            if bron.criterium is None or not bron.punten:
                continue
            detail = _herschrijf_onder_sectie(
                bron,
                sectie_id=sectie,
                factor=factor,
                private_stelselgroep_name=Woningwaarderingstelselgroep.keuken.name,
                bovenliggende_override=ruimte_criterium_id,
                met_ruimte_laag=True,
                ruimte_id=ruimte.id,
            )
            if detail is not None:
                ruimte_details.append(detail)
        if ruimte_details:
            ruimte_criteria[ruimte.id] = _maak_ruimte_criterium(sectie, ruimte)
            details.extend(ruimte_details)

    if not details:
        return []

    sectie_waardering = WoningwaarderingResultatenWoningwaardering(
        criterium=sectie.met_criterium(Woningwaarderingstelselgroep.keuken.naam),
    )
    return [
        sectie_waardering,
        *[ruimte_criteria[ruimte_id] for ruimte_id in sorted(ruimte_criteria)],
        *details,
    ]


def _bouw_sanitair_sectie(
    ruimten: list[EenhedenRuimte],
    sanitair_voor_ruimten: SanitairVoorRuimten,
    adressen_id: CriteriumId,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    sectie = _sectie_id(adressen_id, Woningwaarderingstelselgroep.sanitair.name)
    ruimte_criteria: dict[str, WoningwaarderingResultatenWoningwaardering] = {}
    details: list[WoningwaarderingResultatenWoningwaardering] = []

    for ruimte, bronnen in sanitair_voor_ruimten(ruimten):
        if ruimte.id is None:
            continue
        ruimte_details: list[WoningwaarderingResultatenWoningwaardering] = []
        ruimte_criterium_id = CriteriumId(
            path=str(sectie.met_onderliggend(ruimte.id)),
            bovenliggend=sectie,
        )
        for bron in bronnen:
            if bron.criterium is None or not bron.punten:
                continue
            detail = _herschrijf_onder_sectie(
                bron,
                sectie_id=sectie,
                factor=factor,
                private_stelselgroep_name=Woningwaarderingstelselgroep.sanitair.name,
                bovenliggende_override=ruimte_criterium_id,
                met_ruimte_laag=True,
                ruimte_id=ruimte.id,
            )
            if detail is not None:
                ruimte_details.append(detail)
        if ruimte_details:
            ruimte_criteria[ruimte.id] = _maak_ruimte_criterium(sectie, ruimte)
            details.extend(ruimte_details)

    if not details:
        return []

    sectie_waardering = WoningwaarderingResultatenWoningwaardering(
        criterium=sectie.met_criterium(Woningwaarderingstelselgroep.sanitair.naam),
    )
    return [
        sectie_waardering,
        *[ruimte_criteria[ruimte_id] for ruimte_id in sorted(ruimte_criteria)],
        *details,
    ]
