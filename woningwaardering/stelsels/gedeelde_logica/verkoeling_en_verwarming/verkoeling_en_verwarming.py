from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.stelsels.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselgroepReferentiedata,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelsel import (
    WoningwaarderingstelselReferentiedata,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element


def _subgroep_criterium_id(
    criterium: str,
    ruimte: EenhedenRuimte,
    stelselgroep: WoningwaarderingstelselgroepReferentiedata,
    stelsel: WoningwaarderingstelselReferentiedata | None = None,
) -> str:
    """Unieke subgroep-id per deel-bucket (onz.: ``prive``/gedeeld; zelfstandig: geen ``prive``)."""
    if stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten:
        gedeeld_met_aantal = ruimte.gedeeld_met_aantal_eenheden or 1
        gedeeld_met_soort = GedeeldMetSoort.adressen if gedeeld_met_aantal > 1 else None
    else:
        gedeeld_met_aantal = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
        gedeeld_met_soort = (
            GedeeldMetSoort.onzelfstandige_woonruimten
            if gedeeld_met_aantal > 1
            else None
        )
    return str(
        CriteriumId.totaal_subgroep(
            stelselgroep,
            criterium,
            gedeeld_met_aantal,
            gedeeld_met_soort=gedeeld_met_soort,
            stelsel=stelsel,
        )
    )


def waardeer_verkoeling_en_verwarming(
    ruimten: list[EenhedenRuimte],
    stelselgroep: WoningwaarderingstelselgroepReferentiedata | None = None,
    stelsel: WoningwaarderingstelselReferentiedata | None = None,
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    stelselgroep = stelselgroep or Woningwaarderingstelselgroep.verkoeling_en_verwarming
    yield from _waardeer_verkoeld_en_of_verwarmd_vertrek(ruimten, stelselgroep, stelsel)
    yield from _waardeer_verwarmde_overige_ruimte(ruimten, stelselgroep, stelsel)
    yield from _waardeer_open_keuken(ruimten, stelselgroep, stelsel)


def _waardeer_verwarmde_overige_ruimte(
    ruimten: list[EenhedenRuimte],
    stelselgroep: WoningwaarderingstelselgroepReferentiedata,
    stelsel: WoningwaarderingstelselReferentiedata | None = None,
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    """
    Verwarmde overige ruimten tellen als 1 punt voor verwarmde overige ruimten tot een maximum van 4 punten.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen.
        stelselgroep (WoningwaarderingstelselgroepReferentiedata): Stelselgroep voor criterium-id's in de output.
        stelsel (WoningwaarderingstelselReferentiedata | None): Stelsel voor bucket-segmenten in id's.

    Yields:
        tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]: Tuple van ruimte en waardering voor verwarmde overige ruimten.
    """
    totaal_punten = 0
    for ruimte in ruimten:
        if not ruimte.verwarmd:
            continue

        ruimtesoort = classificeer_ruimte(ruimte)
        if ruimtesoort in (
            Ruimtesoort.overige_ruimten,
            Ruimtesoort.verkeersruimte,
        ):
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmde overige- of verkeersruimte mee voor {stelselgroep.naam}"
            )
            yield (
                ruimte,
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=ruimte.naam,
                        id=str(CriteriumId.blad_ruimte(stelselgroep, ruimte.id)),
                        bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                            id=_subgroep_criterium_id(
                                "verwarmde_overige_en_verkeersruimten",
                                ruimte,
                                stelselgroep,
                                stelsel,
                            ),
                        ),
                    ),
                    punten=1.0,
                ),
            )
            totaal_punten += 1
            if totaal_punten > 4:
                yield (
                    ruimte,
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"{ruimte.naam}: Maximaal 4 punten",
                            id=str(
                                CriteriumId.blad_criterium(
                                    stelselgroep,
                                    "max_aantal_punten",
                                    ruimte_id=ruimte.id,
                                )
                            ),
                            bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                                id=_subgroep_criterium_id(
                                    "verwarmde_overige_en_verkeersruimten",
                                    ruimte,
                                    stelselgroep,
                                    stelsel,
                                ),
                            ),
                        ),
                        punten=-1,
                    ),
                )


def _waardeer_verkoeld_en_of_verwarmd_vertrek(
    ruimten: list[EenhedenRuimte],
    stelselgroep: WoningwaarderingstelselgroepReferentiedata,
    stelsel: WoningwaarderingstelselReferentiedata | None = None,
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    """
    Verkoelde en verwarmde vertrekken tellen voor 2 punten per verwarmd vertrek.
    Indien een verwarmd vertrek ook verkoeld is, wordt er 1 punt extra toegekend.
    Het maximum aantal extra punten voor vertrekken die verkoeld en verwarmd zijn is 2.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen.
        stelselgroep (WoningwaarderingstelselgroepReferentiedata): Stelselgroep voor criterium-id's in de output.
        stelsel (WoningwaarderingstelselReferentiedata | None): Stelsel voor bucket-segmenten in id's.

    Yields:
        tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]: Tuple van ruimte en waardering voor verkoelde en verwarmde vertrekken.
    """
    totaal_punten_verkoeld_en_verwarmd = 0
    for ruimte in ruimten:
        if not ruimte.verwarmd:
            continue

        punten = 2
        ruimtesoort = classificeer_ruimte(ruimte)
        if ruimtesoort == Ruimtesoort.vertrek:
            if ruimte.verkoeld:
                totaal_punten_verkoeld_en_verwarmd += 1
                punten += 1  # 1 punt extra per vertrek wanneer verwarmd en verkoeld
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verkoeld en verwarmd vertrek mee voor {stelselgroep.naam}"
                )
                yield (
                    ruimte,
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=ruimte.naam,
                            id=str(CriteriumId.blad_ruimte(stelselgroep, ruimte.id)),
                            bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                                id=_subgroep_criterium_id(
                                    "verkoelde_en_verwarmde_vertrekken",
                                    ruimte,
                                    stelselgroep,
                                    stelsel,
                                ),
                            ),
                        ),
                        punten=punten,
                    ),
                )
                if totaal_punten_verkoeld_en_verwarmd > 2:
                    logger.info(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}): Maximaal aantal extra punten voor verwarmde en verkoelde vertrekken overschreden ({totaal_punten_verkoeld_en_verwarmd} > 2). Een aftrek van 1 punt wordt toegepast."
                    )
                    yield (
                        ruimte,
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=f"{ruimte.naam}: Maximaal 2 extra punten",
                                id=str(
                                    CriteriumId.blad_criterium(
                                        stelselgroep,
                                        "max_aantal_extra_punten",
                                        ruimte_id=ruimte.id,
                                    )
                                ),
                                bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                                    id=_subgroep_criterium_id(
                                        "verkoelde_en_verwarmde_vertrekken",
                                        ruimte,
                                        stelselgroep,
                                        stelsel,
                                    ),
                                ),
                            ),
                            punten=-1,
                        ),
                    )
            else:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmd vertrek mee voor {stelselgroep.naam}"
                )
                yield (
                    ruimte,
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=ruimte.naam,
                            id=str(
                                CriteriumId.blad_criterium(
                                    stelselgroep,
                                    "verwarmd_vertrek",
                                    ruimte_id=ruimte.id,
                                )
                            ),
                            bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                                id=_subgroep_criterium_id(
                                    "verwarmde_vertrekken",
                                    ruimte,
                                    stelselgroep,
                                    stelsel,
                                ),
                            ),
                        ),
                        punten=punten,
                    ),
                )


def _waardeer_open_keuken(
    ruimten: list[EenhedenRuimte],
    stelselgroep: WoningwaarderingstelselgroepReferentiedata,
    stelsel: WoningwaarderingstelselReferentiedata | None = None,
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    """
    Open keuken tellen voor 2 punten per verwarmd vertrek.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen.
        stelselgroep (WoningwaarderingstelselgroepReferentiedata): Stelselgroep voor criterium-id's in de output.
        stelsel (WoningwaarderingstelselReferentiedata | None): Stelsel voor bucket-segmenten in id's.

    Yields:
        tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]: Tuple van ruimte en waardering voor open keuken.
    """
    for ruimte in ruimten:
        if ruimte.verwarmd and (
            ruimte.detail_soort == Ruimtedetailsoort.woonkamer_en_of_keuken
            or (
                ruimte.detail_soort
                in [
                    Ruimtedetailsoort.woonkamer,
                    Ruimtedetailsoort.woon_en_of_slaapkamer,
                    Ruimtedetailsoort.slaapkamer,
                ]
                and heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.aanrecht
                )
            )
        ):
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als open keuken mee voor {stelselgroep.naam}"
            )
            yield (
                ruimte,
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=ruimte.naam,
                        id=str(CriteriumId.blad_ruimte(stelselgroep, ruimte.id)),
                        bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                            id=_subgroep_criterium_id(
                                "open_keuken", ruimte, stelselgroep, stelsel
                            ),
                        ),
                    ),
                    punten=2.0,
                ),
            )
