from collections import defaultdict
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.criteriumsleutels import (
    CriteriumSleutels,
)
from woningwaardering.stelsels.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort
from woningwaardering.vera.utils import heeft_bouwkundig_element


def verwarmde_overige_ruimten(
    ruimte: EenhedenRuimte,
) -> WoningwaarderingResultatenWoningwaardering | None:
    """
    Verwarmde overige ruimten tellen als 1 punt voor verwarmde overige ruimten.

    Args:
        ruimte (EenhedenRuimte): Ruimte om te waarderen

    Returns:
        WoningwaarderingResultatenWoningwaardering | None: Waardering voor verwarmde overige ruimten
    """
    ruimtesoort = classificeer_ruimte(ruimte)
    if (
        ruimtesoort
        and ruimtesoort.code
        in [
            Ruimtesoort.overige_ruimten.code,
            Ruimtesoort.verkeersruimte.code,
        ]
        and ruimte.verwarmd
    ):
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmde overige- of verkeersruimte en krijgt 1 punt"
        )
        return WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=ruimte.naam,
                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                    id=CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id,
                ),
            ),
            punten=1.0,
        )
    return None


def verkoelde_en_of_verwarmde_vertrekken(
    ruimte: EenhedenRuimte,
) -> WoningwaarderingResultatenWoningwaardering | None:
    """
    Verkoelde en verwarmde vertrekken tellen voor 2 punten per verwarmd vertrek.
    Een verkoeld en verwarmd vertrek telt voor 3 punten.

    Args:
        ruimte (EenhedenRuimte): Ruimte om te waarderen

    Returns:
        WoningwaarderingResultatenWoningwaardering | None: Waardering voor verkoelde en verwarmde vertrekken
    """
    punten = 2
    ruimtesoort = classificeer_ruimte(ruimte)
    if ruimte.verwarmd and ruimtesoort and ruimtesoort.code == Ruimtesoort.vertrek.code:
        if ruimte.verkoeld:
            punten += 1  # 1 punt extra per vertrek wanneer verwarmd en verkoeld
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verkoeld en verwarmd vertrek en krijgt {punten} punten"
            )
            return WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=ruimte.naam,
                    bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                        id=CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id,
                    ),
                ),
                punten=punten,
            )

        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmd vertrek en krijgt {punten} punten"
        )
        return WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=ruimte.naam,
                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                    id=CriteriumSleutels.verwarmde_vertrekken.value.id,
                ),
            ),
            punten=punten,
        )
    return None


def open_keuken(
    ruimte: EenhedenRuimte,
) -> WoningwaarderingResultatenWoningwaardering | None:
    """
    Open keuken tellen voor 2 punten per verwarmd vertrek.

    Args:
        ruimte (EenhedenRuimte): Ruimte om te waarderen

    Returns:
        WoningwaarderingResultatenWoningwaardering | None: Waardering voor open keuken
    """
    if (
        ruimte.verwarmd
        and ruimte.detail_soort
        and (  # detailsoort is woonkamer/keuken of een woonkamer/slaapkamer met aanrecht
            ruimte.detail_soort.code == Ruimtedetailsoort.woonkamer_en_of_keuken.code
            or (
                ruimte.detail_soort.code
                in [
                    Ruimtedetailsoort.woonkamer.code,
                    Ruimtedetailsoort.woon_en_of_slaapkamer.code,
                    Ruimtedetailsoort.slaapkamer.code,
                ]
                and heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.aanrecht
                )
            )
        )
    ):
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als open keuken en krijgt 2 punten"
        )
        return WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=ruimte.naam,
                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                    id=CriteriumSleutels.open_keuken.value.id,
                ),
            ),
            punten=2.0,
        )
    return None


def waardeer(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    waarderingen = (
        waardering
        for waardering in [
            verwarmde_overige_ruimten(ruimte),
            verkoelde_en_of_verwarmde_vertrekken(ruimte),
            open_keuken(ruimte),
        ]
        if waardering is not None
    )

    # check of er een waardering is
    first = next(waarderingen, None)
    if first is None:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
        )
        return

    yield first  # Yield de eerste waardering
    yield from waarderingen  # Yield de resterende waarderingen


def maximeer(
    woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering],
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    # som van punten per criteriumsleutel
    criteriumsleutelpunten: dict[str | None, float] = defaultdict(float)
    for woningwaardering in woningwaarderingen or []:
        if (
            woningwaardering.criterium
            and woningwaardering.criterium.bovenliggende_criterium
            and woningwaardering.criterium.bovenliggende_criterium.id
            and isinstance(woningwaardering.punten, float)
        ):
            criteriumsleutelpunten[
                woningwaardering.criterium.bovenliggende_criterium.id
            ] += woningwaardering.punten

    max_punten_overige_ruimten = 4
    if (
        criteriumsleutelpunten.get(
            CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id,
            0,
        )
        > max_punten_overige_ruimten
    ):
        aftrek = max_punten_overige_ruimten - criteriumsleutelpunten.get(
            CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id,
            0,
        )

        logger.info(
            f"Maximaal aantal punten voor verwarmde overige- en verkeersruimten overschreden ({criteriumsleutelpunten[CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id]} > {max_punten_overige_ruimten}). Een aftrek van {aftrek} punt(en) wordt toegepast."
        )
        yield WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam="Maximaal 4 punten",
                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                    id=CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id,
                ),
            ),
            punten=aftrek,
        )

    max_punten_verkoeld_en_verwarmd_zonder_aftrek = 6  # 6 want maximaal 2 extra punten per verkoeld en verwarmd vertrek, en 3 punten per verkoeld en verwarmd vertrek
    if (
        criteriumsleutelpunten.get(
            CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id,
            0,
        )
        > max_punten_verkoeld_en_verwarmd_zonder_aftrek
    ):
        # maximaal 2 extra punten voor verkoelde en verwarmde vertrekken.
        # 3 punten per verkoeld en verwarmd vertrek
        # aantal extra punten meer dan 2 = (6 - aantal punten voor verkoelde en verwarmde vertrekken) / 3
        aftrek = (
            max_punten_verkoeld_en_verwarmd_zonder_aftrek
            - criteriumsleutelpunten.get(
                CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id,
                0,
            )
        ) / 3

        logger.info(
            f"Maximaal aantal extra punten voor verwarmde en verkoelde vertrekken overschreden ({criteriumsleutelpunten[CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id]} > {max_punten_verkoeld_en_verwarmd_zonder_aftrek}). Een aftrek van {aftrek} punt(en) wordt toegepast."
        )
        yield WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam="Maximaal 2 extra punten",
                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                    id=CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id,
                ),
            ),
            punten=aftrek,
        )
