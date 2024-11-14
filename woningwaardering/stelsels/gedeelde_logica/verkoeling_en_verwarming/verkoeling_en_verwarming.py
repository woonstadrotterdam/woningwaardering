from collections import defaultdict
from decimal import Decimal
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


def waardeer(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    ruimtesoort = classificeer_ruimte(ruimte)

    if (
        ruimte.detail_soort is None
    ):  # wordt al gecheckt in classificeer_ruimte, maar extra check voor mypy
        return

    if ruimtesoort is None:
        if ruimte.detail_soort.code in [
            Ruimtedetailsoort.hal.code,
            Ruimtedetailsoort.overloop.code,
            Ruimtedetailsoort.entree.code,
            Ruimtedetailsoort.gang.code,
            Ruimtedetailsoort.trappenhuis.code,
        ]:  # verkeersruimten tellen ook mee
            ruimtesoort = Ruimtesoort.overige_ruimten

    if (
        not ruimtesoort
        or ruimtesoort.code
        not in [Ruimtesoort.overige_ruimten.code, Ruimtesoort.vertrek.code]
        or not ruimte.verwarmd
    ):
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
        )
        return

    punten = Decimal(
        str(
            {Ruimtesoort.vertrek.code: 2, Ruimtesoort.overige_ruimten.code: 1}[
                ruimtesoort.code
            ]
        )
    )

    if ruimtesoort == Ruimtesoort.overige_ruimten:
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmde overige ruimte en krijgt {punten} punt"
        )
        yield WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=ruimte.naam,
                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                    id=CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id,
                ),
            ),
            punten=punten,
        )

    else:
        if ruimte.verkoeld:
            punten += Decimal(
                "1"
            )  # 1 punt extra per vertrek wanneer verwarmd en verkoeld
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmd en verkoeld vertrek en krijgt {punten} punten"
            )
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=ruimte.naam,
                    bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                        id=CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id,
                    ),
                ),
                punten=punten,
            )
        else:
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmd vertrek en krijgt {punten} punten"
            )
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=ruimte.naam,
                    bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                        id=CriteriumSleutels.verwarmde_vertrekken.value.id,
                    ),
                ),
                punten=punten,
            )

    # Voor deze rubriek wordt een verwarmde open keuken als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten.
    if (
        ruimte.detail_soort.code == Ruimtedetailsoort.woonkamer_en_of_keuken.code
        or ruimte.detail_soort.code
        in [
            Ruimtedetailsoort.woonkamer.code,
            Ruimtedetailsoort.woon_en_of_slaapkamer.code,
            Ruimtedetailsoort.slaapkamer.code,
        ]
        and heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.aanrecht)
    ):
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als open keuken en krijgt {punten} punten"
        )
        yield WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=ruimte.naam,
                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                    id=CriteriumSleutels.open_keuken.value.id,
                ),
            ),
            punten=punten,
        )


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
