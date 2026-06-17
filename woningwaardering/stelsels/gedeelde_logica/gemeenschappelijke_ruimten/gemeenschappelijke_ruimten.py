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

    GEM en GBA delen dezelfde keten: groepeer op (onz, adressen), nest onder
    gedeeld-met-criteria, en voeg per deelgroep geneste stelselgroepen toe.
    Lege geneste stelselgroepen worden overgeslagen.

    Args:
        stelselgroep (WoningwaarderingstelselgroepReferentiedata): GEM- of GBA-stelselgroep.
        stelsel (WoningwaarderingstelselReferentiedata): Zelfstandig of onzelfstandig stelsel.
        ruimten (list[EenhedenRuimte]): Gedeelde ruimten (reeds gefilterd door de caller).
        sanitair_voor_ruimten (SanitairVoorRuimten): Sanitair-waardering per deelgroep (batch voor onz).

    Returns:
        list[WoningwaarderingResultatenWoningwaardering]: Alle waarderingen inclusief gedeeld-met-criteria en geneste stelselgroepen.

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
    toegevoegde_onz_gedeeld_met_criterium_ids: set[str] = set()

    for deelgroep, groep_ruimten in sorted(
        deelgroepen.items(),
        key=lambda item: (item[0].aantal_onz, item[0].aantal_adressen),
    ):
        gedeeld_met_onz_criterium_id = (
            stelselgroep_id.gedeeld_met_criterium(
                deelgroep.aantal_onz, GedeeldMetSoort.onzelfstandige_woonruimten
            )
            if deelgroep.aantal_onz > 1
            else None
        )
        if deelgroep.aantal_adressen > 1:
            if gedeeld_met_onz_criterium_id is not None:
                gedeeld_met_adressen_criterium_id = (
                    gedeeld_met_onz_criterium_id.gedeeld_met_criterium(
                        deelgroep.aantal_adressen, GedeeldMetSoort.adressen
                    )
                )
            else:
                gedeeld_met_adressen_criterium_id = (
                    stelselgroep_id.gedeeld_met_criterium(
                        deelgroep.aantal_adressen, GedeeldMetSoort.adressen
                    )
                )
        else:
            gedeeld_met_adressen_criterium_id = None

        if gedeeld_met_adressen_criterium_id is None:
            continue

        geneste_stelselgroep_waarderingen: list[
            WoningwaarderingResultatenWoningwaardering
        ] = []
        geneste_stelselgroep_waarderingen.extend(
            _bouw_geneste_stelselgroep_oppervlakte_van_vertrekken(
                groep_ruimten, gedeeld_met_adressen_criterium_id, deelgroep.factor
            )
        )
        geneste_stelselgroep_waarderingen.extend(
            _bouw_geneste_stelselgroep_oppervlakte_van_overige_ruimten(
                groep_ruimten, gedeeld_met_adressen_criterium_id, deelgroep.factor
            )
        )
        groep_ruimte_ids = {
            ruimte.id for ruimte in groep_ruimten if ruimte.id is not None
        }
        geneste_stelselgroep_waarderingen.extend(
            _bouw_geneste_stelselgroep_verkoeling_en_verwarming(
                [
                    (ruimte, bron)
                    for ruimte, bron in verkoeling_resultaten
                    if ruimte.id in groep_ruimte_ids
                ],
                gedeeld_met_adressen_criterium_id,
                deelgroep.factor,
            )
        )
        geneste_stelselgroep_waarderingen.extend(
            _bouw_geneste_stelselgroep_keuken(
                groep_ruimten,
                stelsel,
                gedeeld_met_adressen_criterium_id,
                deelgroep.factor,
            )
        )
        geneste_stelselgroep_waarderingen.extend(
            _bouw_geneste_stelselgroep_sanitair(
                groep_ruimten,
                sanitair_voor_ruimten,
                gedeeld_met_adressen_criterium_id,
                deelgroep.factor,
            )
        )

        if not geneste_stelselgroep_waarderingen:
            continue

        if (
            gedeeld_met_onz_criterium_id is not None
            and str(gedeeld_met_onz_criterium_id)
            not in toegevoegde_onz_gedeeld_met_criterium_ids
        ):
            waarderingen.append(
                _maak_gedeeld_met_criterium(
                    gedeeld_met_onz_criterium_id,
                    utils.naam_gedeeld_met_groep(
                        deelgroep.aantal_onz,
                        soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                    ),
                )
            )
            toegevoegde_onz_gedeeld_met_criterium_ids.add(
                str(gedeeld_met_onz_criterium_id)
            )

        waarderingen.append(
            _maak_gedeeld_met_criterium(
                gedeeld_met_adressen_criterium_id,
                utils.naam_gedeeld_met_groep(
                    deelgroep.aantal_adressen,
                    soort=GedeeldMetSoort.adressen,
                ),
                bovenliggend=gedeeld_met_onz_criterium_id,
            )
        )
        waarderingen.extend(geneste_stelselgroep_waarderingen)

    return waarderingen


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


def _maak_gedeeld_met_criterium(
    criterium_id: CriteriumId,
    naam: str,
    *,
    bovenliggend: CriteriumId | None = None,
) -> WoningwaarderingResultatenWoningwaardering:
    """Maakt een structuurwaardering voor een gedeeld-met-criterium (zonder punten).

    Gedeeld-met-niveaus zijn structuurniveaus in de output (zonder punten); punten zitten op
    geneste stelselgroepen of lager.

    Args:
        criterium_id (CriteriumId): Id van het gedeeld-met-criterium.
        naam (str): Weergavenaam in output.
        bovenliggend (CriteriumId | None): Optioneel bovenliggend gedeeld-met-criterium.

    Returns:
        WoningwaarderingResultatenWoningwaardering: Waardering met alleen ``criterium``.

    Example:
        ``_maak_gedeeld_met_criterium(adressen_id, "Gedeeld met 2 adressen", bovenliggend=onz_id)``
    """
    criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
        id=str(criterium_id),
        naam=naam,
    )
    if bovenliggend is not None:
        criterium.bovenliggende_criterium = bovenliggend.naar_criterium_sleutels()
    return WoningwaarderingResultatenWoningwaardering(criterium=criterium)


def _suffix_na_stelselgroep(bron_id: str | None, stelselgroep_name: str) -> str | None:
    """Haalt het restdeel van een bron-criteriumid op na ``{stelselgroep}__``.

    Bron-waarderingen uit stelselgroep-modules beginnen met ``{stelselgroep}__``;
    bij herschrijven onder een geneste stelselgroep is alleen dat restdeel nodig.

    Args:
        bron_id (str | None): Bron-criteriumid.
        stelselgroep_name (str): Naam van de stelselgroep in het criteriumid.

    Returns:
        str | None: Rest van het id na ``{stelselgroep}__``, of ``None`` bij geen match.

    Example:
        >>> _suffix_na_stelselgroep("keuken__Space_1__lengte_aanrecht", "keuken")
        'Space_1__lengte_aanrecht'
    """
    if not bron_id:
        return None
    prefix = f"{stelselgroep_name}__"
    if not bron_id.startswith(prefix):
        return None
    return bron_id[len(prefix) :]


def _herschrijf_onder_geneste_stelselgroep(
    bron: WoningwaarderingResultatenWoningwaardering,
    *,
    geneste_stelselgroep_id: CriteriumId,
    factor: Decimal,
    geneste_stelselgroep_naam: str,
    bovenliggende_override: CriteriumId | None = None,
    met_ruimte_laag: bool = False,
    ruimte_id: str | None = None,
) -> WoningwaarderingResultatenWoningwaardering | None:
    """Herschrijft een bron-waardering naar het pad onder een geneste stelselgroep.

    Hergebruikt bestaande stelselgroep-logica (keuken, sanitair, …) en past
    ids, bovenliggend en punten (gedeeld door ``factor``) aan voor gedeeld-met.

    Args:
        bron (WoningwaarderingResultatenWoningwaardering): Bron-waardering uit een stelselgroep-module.
        geneste_stelselgroep_id (CriteriumId): Doel-criteriumid van de geneste stelselgroep.
        factor (Decimal): Deler voor punten (onz × adressen).
        geneste_stelselgroep_naam (str): Stelselgroepnaam in het bron-id.
        bovenliggende_override (CriteriumId | None): Optioneel ruimtecriterium als bovenliggend.
        met_ruimte_laag (bool): Of keuken/sanitair een ruimte-laag heeft.
        ruimte_id (str | None): Ruimte-id bij ``met_ruimte_laag``.

    Returns:
        WoningwaarderingResultatenWoningwaardering | None: Nieuwe waardering, of ``None`` bij onherkenbaar bron-id.

    Example:
        Privé ``keuken__Space_1__lengte_aanrecht`` →
        ``...__gedeeld_met_2_adressen__keuken__Space_1__lengte_aanrecht``.
    """
    if bron.criterium is None:
        return None

    suffix = _suffix_na_stelselgroep(bron.criterium.id, geneste_stelselgroep_naam)
    if suffix is None:
        return None

    if met_ruimte_laag and ruimte_id is not None:
        if suffix.startswith(f"{ruimte_id}__"):
            installatie_suffix = suffix[len(ruimte_id) + 2 :]
            bovenliggend_criterium_id = (
                bovenliggende_override
                or geneste_stelselgroep_id.met_onderliggend(ruimte_id)
            )
            nieuw_id = bovenliggend_criterium_id.met_onderliggend(installatie_suffix)
        else:
            bovenliggend_criterium_id = (
                bovenliggende_override or geneste_stelselgroep_id
            )
            nieuw_id = bovenliggend_criterium_id.met_onderliggend(suffix)
    else:
        bovenliggend_criterium_id = bovenliggende_override or geneste_stelselgroep_id
        nieuw_id = bovenliggend_criterium_id.met_onderliggend(suffix)

    criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
        id=str(nieuw_id),
        naam=bron.criterium.naam,
        meeteenheid=bron.criterium.meeteenheid,
        bovenliggende_criterium=bovenliggend_criterium_id.naar_criterium_sleutels(),
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
    geneste_stelselgroep_id: CriteriumId,
    ruimte: EenhedenRuimte,
) -> WoningwaarderingResultatenWoningwaardering:
    """Maakt een ruimtecriterium onder een geneste stelselgroep (zonder punten).

    Keuken en sanitair hebben een extra laag per ruimte; dit criterium groepeert
    installatiedetails onder de juiste ruimte in de output.

    Args:
        geneste_stelselgroep_id (CriteriumId): Id van de geneste stelselgroep.
        ruimte (EenhedenRuimte): Ruimte waarvoor het criterium wordt gemaakt.

    Returns:
        WoningwaarderingResultatenWoningwaardering: Structuurwaardering voor de ruimte.

    Example:
        Geneste stelselgroep ``...__keuken`` + ruimte ``Space_1`` →
        ``...__keuken__Space_1`` met weergavenaam van de ruimte.
    """
    ruimte_id = CriteriumId(
        path=str(geneste_stelselgroep_id.met_onderliggend(ruimte.id)),
        bovenliggend=geneste_stelselgroep_id,
    )
    return WoningwaarderingResultatenWoningwaardering(
        criterium=ruimte_id.met_criterium(utils.ruimte_weergavenaam(ruimte)),
        punten=None,
    )


def _geneste_stelselgroep_id(
    gedeeld_met_adressen_criterium_id: CriteriumId, geneste_stelselgroep_naam: str
) -> CriteriumId:
    """Bouwt het criteriumid van een geneste stelselgroep onder gedeeld-met.

    Vijf vaste stelselgroepnamen (oppervlakte, keuken, …) worden als
    ``criteriumid_toevoeging`` onder het adressen-gedeeld-met-criterium gehangen.

    Args:
        gedeeld_met_adressen_criterium_id (CriteriumId): Gedeeld-met-criterium voor adressen.
        geneste_stelselgroep_naam (str): VERA-stelselgroepnaam als ``criteriumid_toevoeging``.

    Returns:
        CriteriumId: Id van de geneste stelselgroep.

    Example:
        ``...__gedeeld_met_2_adressen__keuken``
    """
    return gedeeld_met_adressen_criterium_id.met_onderliggend(geneste_stelselgroep_naam)


def _bouw_geneste_stelselgroep_oppervlakte_van_vertrekken(
    ruimten: list[EenhedenRuimte],
    gedeeld_met_adressen_criterium_id: CriteriumId,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    """Bouwt output voor oppervlakte van vertrekken onder gedeeld-met.

    Telt vertrekken in de deelgroep, berekent gedeelde punten (factor = onz × adressen),
    en voegt detailregels zonder eigen punten toe.

    Args:
        ruimten (list[EenhedenRuimte]): Ruimten in de deelgroep.
        gedeeld_met_adressen_criterium_id (CriteriumId): Gedeeld-met-criterium voor adressen.
        factor (Decimal): Deler voor punten (onz × adressen).

    Returns:
        list[WoningwaarderingResultatenWoningwaardering]: Lege lijst of geneste stelselgroep + details.

    Example:
        Zie ``voorbeeld_beleidsboek.json`` onder ``...__oppervlakte_van_vertrekken``.
    """
    vertrekken = [
        ruimte
        for ruimte in ruimten
        if utils.classificeer_ruimte(ruimte) == Ruimtesoort.vertrek
    ]
    if not vertrekken:
        return []

    geneste_stelselgroep_id = _geneste_stelselgroep_id(
        gedeeld_met_adressen_criterium_id,
        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.name,
    )
    totaal_oppervlakte = sum(
        (
            utils.rond_af(ruimte.oppervlakte, decimalen=2)
            for ruimte in vertrekken
            if ruimte.oppervlakte is not None
        ),
        start=Decimal("0"),
    )
    geneste_stelselgroep_punten = (
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
        detail = _herschrijf_onder_geneste_stelselgroep(
            oppervlakte_resultaat,
            geneste_stelselgroep_id=geneste_stelselgroep_id,
            factor=factor,
            geneste_stelselgroep_naam=Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.name,
        )
        if detail is not None:
            detail.punten = None
            details.append(detail)

    if not details:
        return []

    geneste_stelselgroep_waardering = WoningwaarderingResultatenWoningwaardering(
        criterium=geneste_stelselgroep_id.met_criterium(
            Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam
        ),
        punten=float(geneste_stelselgroep_punten),
    )
    return [geneste_stelselgroep_waardering, *details]


def _bouw_geneste_stelselgroep_oppervlakte_van_overige_ruimten(
    ruimten: list[EenhedenRuimte],
    gedeeld_met_adressen_criterium_id: CriteriumId,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    """Bouwt output voor oppervlakte van overige ruimten inclusief zoldercorrectie.

    Zelfde patroon als vertrekken, met factor 0,75 en optioneel subtotaal +
    correctie bij zolders zonder vaste trap.

    Args:
        ruimten (list[EenhedenRuimte]): Ruimten in de deelgroep.
        gedeeld_met_adressen_criterium_id (CriteriumId): Gedeeld-met-criterium voor adressen.
        factor (Decimal): Deler voor punten (onz × adressen).

    Returns:
        list[WoningwaarderingResultatenWoningwaardering]: Lege lijst of waarderingen met optionele correctie.

    Example:
        Met zoldercorrectie: geneste stelselgroep → subtotaal → details → correctie.
    """
    overige = [
        ruimte
        for ruimte in ruimten
        if utils.classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
    ]
    if not overige:
        return []

    geneste_stelselgroep_id = _geneste_stelselgroep_id(
        gedeeld_met_adressen_criterium_id,
        Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.name,
    )
    totaal_oppervlakte = sum(
        (
            utils.rond_af(ruimte.oppervlakte, decimalen=2)
            for ruimte in overige
            if ruimte.oppervlakte is not None
        ),
        start=Decimal("0"),
    )
    geneste_stelselgroep_punten = (
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
        detail = _herschrijf_onder_geneste_stelselgroep(
            oppervlakte_resultaat,
            geneste_stelselgroep_id=geneste_stelselgroep_id,
            factor=factor,
            geneste_stelselgroep_naam=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.name,
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
        correctie_id = geneste_stelselgroep_id.met_onderliggend(
            ruimte.id
        ).met_onderliggend("correctie_zolder_zonder_vaste_trap")
        correctie = WoningwaarderingResultatenWoningwaardering(
            criterium=correctie_id.met_criterium("Correctie: zolder zonder vaste trap"),
            punten=float(correctie_punten),
        )
        if correctie.criterium is not None:
            correctie.criterium.bovenliggende_criterium = (
                geneste_stelselgroep_id.naar_criterium_sleutels()
            )
        correcties.append(correctie)

    if not details and not correcties:
        return []

    geneste_stelselgroep_naam = (
        Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam
    )
    if correcties:
        geneste_stelselgroep_criterium = WoningwaarderingResultatenWoningwaardering(
            criterium=geneste_stelselgroep_id.met_criterium(geneste_stelselgroep_naam),
        )
        subtotaal_id = geneste_stelselgroep_id.met_onderliggend("subtotaal")
        subtotaal = WoningwaarderingResultatenWoningwaardering(
            criterium=subtotaal_id.met_criterium(
                "Subtotaal",
                meeteenheid=Meeteenheid.vierkante_meter_m2,
            ),
            aantal=float(utils.rond_af(totaal_oppervlakte, decimalen=2)),
            punten=float(geneste_stelselgroep_punten),
        )
        geneste_stelselgroep_prefix = f"{geneste_stelselgroep_id}__"
        for detail in details:
            if detail.criterium is None or not detail.criterium.id:
                continue
            ruimte_suffix = detail.criterium.id.removeprefix(
                geneste_stelselgroep_prefix
            )
            detail.criterium.id = str(subtotaal_id.met_onderliggend(ruimte_suffix))
            detail.criterium.bovenliggende_criterium = (
                WoningwaarderingCriteriumSleutels(id=str(subtotaal_id))
            )
        return [geneste_stelselgroep_criterium, subtotaal, *details, *correcties]

    return [
        WoningwaarderingResultatenWoningwaardering(
            criterium=geneste_stelselgroep_id.met_criterium(geneste_stelselgroep_naam),
            punten=float(geneste_stelselgroep_punten),
        ),
        *details,
    ]


def _bouw_geneste_stelselgroep_verkoeling_en_verwarming(
    verkoeling_resultaten: list[VerkoelingEnVerwarmingResultaat],
    gedeeld_met_adressen_criterium_id: CriteriumId,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    """Nest verkoeling/verwarming onder gedeeld-met met groeperingscriteria.

    Maximering loopt over alle ruimten; deze functie filtert per deelgroep en
    maakt groeperingscriteria (bijv. ``verwarmde_vertrekken``) plus details.

    Args:
        verkoeling_resultaten (list[VerkoelingEnVerwarmingResultaat]): Bron per ruimte.
        gedeeld_met_adressen_criterium_id (CriteriumId): Gedeeld-met-criterium voor adressen.
        factor (Decimal): Deler voor punten (onz × adressen).

    Returns:
        list[WoningwaarderingResultatenWoningwaardering]: Lege lijst of geneste stelselgroep + groeperingen + details.

    Example:
        ``...__verkoeling_en_verwarming__verwarmde_vertrekken__...`` onder adressen-id.
    """
    geneste_stelselgroep_id = _geneste_stelselgroep_id(
        gedeeld_met_adressen_criterium_id,
        Woningwaarderingstelselgroep.verkoeling_en_verwarming.name,
    )
    details: list[WoningwaarderingResultatenWoningwaardering] = []
    groeperingen: dict[str, WoningwaarderingResultatenWoningwaardering] = {}
    geneste_stelselgroep_naam = (
        Woningwaarderingstelselgroep.verkoeling_en_verwarming.name
    )

    for _ruimte, bron in verkoeling_resultaten:
        if bron.criterium is None or bron.criterium.id is None:
            continue
        suffix = _suffix_na_stelselgroep(bron.criterium.id, geneste_stelselgroep_naam)
        if suffix is None or "__" not in suffix:
            continue

        groepering_deel, detail_deel = suffix.split("__", 1)
        groepering_id = geneste_stelselgroep_id.met_onderliggend(groepering_deel)
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

    geneste_stelselgroep_waardering = WoningwaarderingResultatenWoningwaardering(
        criterium=geneste_stelselgroep_id.met_criterium(
            Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam
        ),
    )
    return [geneste_stelselgroep_waardering, *groeperingen.values(), *details]


def _bouw_geneste_stelselgroep_keuken(
    ruimten: list[EenhedenRuimte],
    stelsel: WoningwaarderingstelselReferentiedata,
    gedeeld_met_adressen_criterium_id: CriteriumId,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    """Bouwt keuken-output met ruimte-laag en installatiedetails onder gedeeld-met.

    Roept ``waardeer_keuken`` per ruimte aan en herschrijft via
    ``_herschrijf_onder_geneste_stelselgroep`` met ``met_ruimte_laag=True``.

    Args:
        ruimten (list[EenhedenRuimte]): Ruimten in de deelgroep.
        stelsel (WoningwaarderingstelselReferentiedata): Zelfstandig of onzelfstandig stelsel.
        gedeeld_met_adressen_criterium_id (CriteriumId): Gedeeld-met-criterium voor adressen.
        factor (Decimal): Deler voor punten (onz × adressen).

    Returns:
        list[WoningwaarderingResultatenWoningwaardering]: Lege lijst of geneste stelselgroep + ruimten + details.

    Example:
        ``...__keuken__Space_1`` → ``...__lengte_aanrecht`` (punten gedeeld door factor).
    """
    geneste_stelselgroep_id = _geneste_stelselgroep_id(
        gedeeld_met_adressen_criterium_id, Woningwaarderingstelselgroep.keuken.name
    )
    ruimte_criteria: dict[str, WoningwaarderingResultatenWoningwaardering] = {}
    details: list[WoningwaarderingResultatenWoningwaardering] = []

    for ruimte in ruimten:
        if ruimte.id is None or ruimte.detail_soort is None:
            continue
        ruimte_details: list[WoningwaarderingResultatenWoningwaardering] = []
        ruimte_criterium_id = CriteriumId(
            path=str(geneste_stelselgroep_id.met_onderliggend(ruimte.id)),
            bovenliggend=geneste_stelselgroep_id,
        )
        for bron in waardeer_keuken(ruimte, stelsel):
            if bron.criterium is None or not bron.punten:
                continue
            detail = _herschrijf_onder_geneste_stelselgroep(
                bron,
                geneste_stelselgroep_id=geneste_stelselgroep_id,
                factor=factor,
                geneste_stelselgroep_naam=Woningwaarderingstelselgroep.keuken.name,
                bovenliggende_override=ruimte_criterium_id,
                met_ruimte_laag=True,
                ruimte_id=ruimte.id,
            )
            if detail is not None:
                ruimte_details.append(detail)
        if ruimte_details:
            ruimte_criteria[ruimte.id] = _maak_ruimte_criterium(
                geneste_stelselgroep_id, ruimte
            )
            details.extend(ruimte_details)

    if not details:
        return []

    geneste_stelselgroep_waardering = WoningwaarderingResultatenWoningwaardering(
        criterium=geneste_stelselgroep_id.met_criterium(
            Woningwaarderingstelselgroep.keuken.naam
        ),
    )
    return [
        geneste_stelselgroep_waardering,
        *[ruimte_criteria[ruimte_id] for ruimte_id in sorted(ruimte_criteria)],
        *details,
    ]


def _bouw_geneste_stelselgroep_sanitair(
    ruimten: list[EenhedenRuimte],
    sanitair_voor_ruimten: SanitairVoorRuimten,
    gedeeld_met_adressen_criterium_id: CriteriumId,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    """Bouwt sanitair-output met ruimte-laag onder gedeeld-met.

    Zelfde patroon als keuken; sanitair wordt via ``sanitair_voor_ruimten``
    batchgewijs aangeleverd (onzelfstandig vs. zelfstandig).

    Args:
        ruimten (list[EenhedenRuimte]): Ruimten in de deelgroep.
        sanitair_voor_ruimten (SanitairVoorRuimten): Sanitair-waardering per deelgroep.
        gedeeld_met_adressen_criterium_id (CriteriumId): Gedeeld-met-criterium voor adressen.
        factor (Decimal): Deler voor punten (onz × adressen).

    Returns:
        list[WoningwaarderingResultatenWoningwaardering]: Lege lijst of geneste stelselgroep + ruimten + details.

    Example:
        ``...__sanitair__Space_1__douche`` met punten / factor.
    """
    geneste_stelselgroep_id = _geneste_stelselgroep_id(
        gedeeld_met_adressen_criterium_id, Woningwaarderingstelselgroep.sanitair.name
    )
    ruimte_criteria: dict[str, WoningwaarderingResultatenWoningwaardering] = {}
    details: list[WoningwaarderingResultatenWoningwaardering] = []

    for ruimte, bronnen in sanitair_voor_ruimten(ruimten):
        if ruimte.id is None:
            continue
        ruimte_details: list[WoningwaarderingResultatenWoningwaardering] = []
        ruimte_criterium_id = CriteriumId(
            path=str(geneste_stelselgroep_id.met_onderliggend(ruimte.id)),
            bovenliggend=geneste_stelselgroep_id,
        )
        for bron in bronnen:
            if bron.criterium is None or not bron.punten:
                continue
            detail = _herschrijf_onder_geneste_stelselgroep(
                bron,
                geneste_stelselgroep_id=geneste_stelselgroep_id,
                factor=factor,
                geneste_stelselgroep_naam=Woningwaarderingstelselgroep.sanitair.name,
                bovenliggende_override=ruimte_criterium_id,
                met_ruimte_laag=True,
                ruimte_id=ruimte.id,
            )
            if detail is not None:
                ruimte_details.append(detail)
        if ruimte_details:
            ruimte_criteria[ruimte.id] = _maak_ruimte_criterium(
                geneste_stelselgroep_id, ruimte
            )
            details.extend(ruimte_details)

    if not details:
        return []

    geneste_stelselgroep_waardering = WoningwaarderingResultatenWoningwaardering(
        criterium=geneste_stelselgroep_id.met_criterium(
            Woningwaarderingstelselgroep.sanitair.naam
        ),
    )
    return [
        geneste_stelselgroep_waardering,
        *[ruimte_criteria[ruimte_id] for ruimte_id in sorted(ruimte_criteria)],
        *details,
    ]
