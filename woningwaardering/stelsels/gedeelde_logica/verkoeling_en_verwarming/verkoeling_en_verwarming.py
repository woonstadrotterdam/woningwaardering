from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element


def _subgroep_naam(subgroep_id: str) -> str:
    return subgroep_id.capitalize().replace("_", " ")


def _subgroep(
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
    subgroepen: dict[str, WaarderingBouwer],
    subgroep_id: str,
) -> WaarderingBouwer:
    if subgroep_id not in subgroepen:
        subgroepen[subgroep_id] = waarderingsgroep_bouwer.maak_onderliggende(
            id=subgroep_id,
            naam=_subgroep_naam(subgroep_id),
        )
    return subgroepen[subgroep_id]


def waardeer_verkoeling_en_verwarming(
    ruimten: list[EenhedenRuimte],
    *,
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
) -> Iterator[tuple[EenhedenRuimte, WaarderingBouwer]]:
    yield from _waardeer_verkoeld_en_of_verwarmd_vertrek(
        ruimten, waarderingsgroep_bouwer
    )
    yield from _waardeer_verwarmde_overige_ruimte(ruimten, waarderingsgroep_bouwer)
    yield from _waardeer_open_keuken(ruimten, waarderingsgroep_bouwer)


def _waardeer_verwarmde_overige_ruimte(
    ruimten: list[EenhedenRuimte],
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
) -> Iterator[tuple[EenhedenRuimte, WaarderingBouwer]]:
    """
    Verwarmde overige ruimten tellen als 1 punt voor verwarmde overige ruimten tot een maximum van 4 punten.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen
        waarderingsgroep_bouwer (WaarderingsgroepBouwer | WaarderingBouwer): waarderingsgroep of bestaande waardering in de hiërarchie.

    Yields:
        tuple[EenhedenRuimte, WaarderingBouwer]: Tuple van ruimte en waardering voor verwarmde overige ruimten
    """
    subgroep_id = "verwarmde_overige_en_verkeersruimten"
    subgroepen: dict[str, WaarderingBouwer] = {}
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
                _subgroep(
                    waarderingsgroep_bouwer, subgroepen, subgroep_id
                ).maak_onderliggende(
                    id=ruimte.id,
                    naam=ruimte.naam or ruimte.id or "",
                    punten=1.0,
                ),
            )
            totaal_punten += 1
            if totaal_punten > 4:
                yield (
                    ruimte,
                    _subgroep(
                        waarderingsgroep_bouwer, subgroepen, subgroep_id
                    ).maak_onderliggende(
                        id="max_aantal_punten",
                        naam="Maximaal 4 punten",
                        punten=-1,
                    ),
                )


def _waardeer_verkoeld_en_of_verwarmd_vertrek(
    ruimten: list[EenhedenRuimte],
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
) -> Iterator[tuple[EenhedenRuimte, WaarderingBouwer]]:
    """
    Verkoelde en verwarmde vertrekken tellen voor 2 punten per verwarmd vertrek.
    Indien een verwarmd vertrek ook verkoeld is, wordt er 1 punt extra toegekend.
    Het maximum aantal extra punten voor vertrekken die verkoeld en verwarmd zijn is 2.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen
        waarderingsgroep_bouwer (WaarderingsgroepBouwer | WaarderingBouwer): waarderingsgroep of bestaande waardering in de hiërarchie.

    Yields:
        tuple[EenhedenRuimte, WaarderingBouwer]: Tuple van ruimte en waardering voor verkoelde en verwarmde vertrekken
    """
    subgroepen: dict[str, WaarderingBouwer] = {}
    totaal_punten_verkoeld = 0
    for ruimte in ruimten:
        if not ruimte.verwarmd:
            continue

        ruimtesoort = classificeer_ruimte(ruimte)
        if ruimtesoort == Ruimtesoort.vertrek:
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmd vertrek mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
            )
            yield (
                ruimte,
                _subgroep(
                    waarderingsgroep_bouwer, subgroepen, "verwarmde_vertrekken"
                ).maak_onderliggende(
                    id=ruimte.id,
                    naam=ruimte.naam or ruimte.id or "",
                    punten=2,
                ),
            )

            if ruimte.verkoeld:
                totaal_punten_verkoeld += 1
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verkoeld vertrek mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
                )
                yield (
                    ruimte,
                    _subgroep(
                        waarderingsgroep_bouwer, subgroepen, "verkoelde_vertrekken"
                    ).maak_onderliggende(
                        id=ruimte.id,
                        naam=ruimte.naam or ruimte.id or "",
                        punten=1,
                    ),
                )
                if totaal_punten_verkoeld > 2:
                    logger.info(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}): Maximaal aantal punten voor verkoelde vertrekken overschreden ({totaal_punten_verkoeld} > 2). Een aftrek van 1 punt wordt toegepast."
                    )
                    yield (
                        ruimte,
                        _subgroep(
                            waarderingsgroep_bouwer, subgroepen, "verkoelde_vertrekken"
                        ).maak_onderliggende(
                            id="max_aantal_punten",
                            naam="Maximaal 2 punten",
                            punten=-1,
                        ),
                    )


def _waardeer_open_keuken(
    ruimten: list[EenhedenRuimte],
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
) -> Iterator[tuple[EenhedenRuimte, WaarderingBouwer]]:
    """
    Open keuken tellen voor 2 punten per verwarmd vertrek.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen
        waarderingsgroep_bouwer (WaarderingsgroepBouwer | WaarderingBouwer): waarderingsgroep of bestaande waardering in de hiërarchie.

    Yields:
        tuple[EenhedenRuimte, WaarderingBouwer]: Tuple van ruimte en waardering voor open keuken
    """
    subgroepen: dict[str, WaarderingBouwer] = {}
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
                _subgroep(
                    waarderingsgroep_bouwer, subgroepen, "open_keuken"
                ).maak_onderliggende(
                    id=ruimte.id,
                    naam=ruimte.naam or ruimte.id or "",
                    punten=2.0,
                ),
            )
