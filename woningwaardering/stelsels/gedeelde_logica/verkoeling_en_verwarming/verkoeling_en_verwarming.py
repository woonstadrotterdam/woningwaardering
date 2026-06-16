from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element

_STELSELGROEP_ID = CriteriumId.voor_stelselgroep(
    Woningwaarderingstelselgroep.verkoeling_en_verwarming
)
_VERWARMDE_OVERIGE = _STELSELGROEP_ID.met_onderliggend(
    "verwarmde_overige_en_verkeersruimten"
)
_VERKOELDE_EN_VERWARMDE = _STELSELGROEP_ID.met_onderliggend(
    "verkoelde_en_verwarmde_vertrekken"
)
_VERWARMDE_VERTREKKEN = _STELSELGROEP_ID.met_onderliggend("verwarmde_vertrekken")
_OPEN_KEUKEN = _STELSELGROEP_ID.met_onderliggend("open_keuken")


def waardeer_verkoeling_en_verwarming(
    ruimten: list[EenhedenRuimte],
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    yield from _waardeer_verkoeld_en_of_verwarmd_vertrek(ruimten)
    yield from _waardeer_verwarmde_overige_ruimte(ruimten)
    yield from _waardeer_open_keuken(ruimten)


def _waardeer_verwarmde_overige_ruimte(
    ruimten: list[EenhedenRuimte],
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    """
    Verwarmde overige ruimten tellen als 1 punt voor verwarmde overige ruimten tot een maximum van 4 punten.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen

    Yields:
        tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]: Tuple van ruimte en waardering voor verwarmde overige ruimten
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
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmde overige- of verkeersruimte mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
            )
            yield (
                ruimte,
                _VERWARMDE_OVERIGE.met_onderliggend(ruimte.id).met_waardering(
                    ruimte.naam, punten=1.0
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
                                _VERWARMDE_OVERIGE.met_onderliggend(
                                    f"{ruimte.id}__max_aantal_punten"
                                )
                            ),
                            bovenliggende_criterium=_VERWARMDE_OVERIGE.naar_criterium_sleutels(),
                        ),
                        punten=-1,
                    ),
                )


def _waardeer_verkoeld_en_of_verwarmd_vertrek(
    ruimten: list[EenhedenRuimte],
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    """
    Verkoelde en verwarmde vertrekken tellen voor 2 punten per verwarmd vertrek.
    Indien een verwarmd vertrek ook verkoeld is, wordt er 1 punt extra toegekend.
    Het maximum aantal extra punten voor vertrekken die verkoeld en verwarmd zijn is 2.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen

    Yields:
        tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]: Tuple van ruimte en waardering voor verkoelde en verwarmde vertrekken
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
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verkoeld en verwarmd vertrek mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
                )
                yield (
                    ruimte,
                    _VERKOELDE_EN_VERWARMDE.met_onderliggend(ruimte.id).met_waardering(
                        ruimte.naam, punten=punten
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
                                    _VERKOELDE_EN_VERWARMDE.met_onderliggend(
                                        f"{ruimte.id}__max_aantal_extra_punten"
                                    )
                                ),
                                bovenliggende_criterium=_VERKOELDE_EN_VERWARMDE.naar_criterium_sleutels(),
                            ),
                            punten=-1,
                        ),
                    )
            else:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmd vertrek mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
                )
                yield (
                    ruimte,
                    _VERWARMDE_VERTREKKEN.met_onderliggend(ruimte.id).met_waardering(
                        ruimte.naam, punten=punten
                    ),
                )


def _waardeer_open_keuken(
    ruimten: list[EenhedenRuimte],
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    """
    Open keuken tellen voor 2 punten per verwarmd vertrek.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen

    Yields:
        tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]: Tuple van ruimte en waardering voor open keuken
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
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als open keuken mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
            )
            yield (
                ruimte,
                _OPEN_KEUKEN.met_onderliggend(ruimte.id).met_waardering(
                    ruimte.naam, punten=2.0
                ),
            )
