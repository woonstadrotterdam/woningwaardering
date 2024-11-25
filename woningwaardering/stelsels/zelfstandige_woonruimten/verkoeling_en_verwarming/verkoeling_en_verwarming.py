import warnings
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import bereken
from woningwaardering.stelsels.criteriumsleutels import (
    CriteriumSleutels,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort
from woningwaardering.vera.utils import heeft_bouwkundig_element


class VerkoelingEnVerwarming(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.verkoeling_en_verwarming
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.verkoeling_en_verwarming.value,
            )
        )

        logger.debug(f"Punten per verwarmd {Ruimtesoort.vertrek.naam}: 2")
        logger.debug(
            f"Extra punt voor {Ruimtesoort.vertrek.naam} met ook een koelfunctie. Maximaal 2 extra punten per eenheid."
        )
        logger.debug(
            f"Punten per verwarmd {Ruimtesoort.overige_ruimten.naam} of verkeersruimte (met totaal van max 4 punten per eenheid): 1."
        )

        woningwaardering_groep.woningwaarderingen = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden == 1
        ]

        resultaten = list(
            VerkoelingEnVerwarming.genereer_woningwaarderingen(
                ruimten,
                self.stelselgroep,
            )
        )

        woningwaarderingen = [woningwaardering for _, woningwaardering in resultaten]

        woningwaardering_groep.woningwaarderingen.extend(woningwaarderingen)

        woningwaardering_groep.woningwaarderingen.extend(
            list(self.criteriumsleutel_resultaten(woningwaardering_groep))
        )

        punten = utils.rond_af_op_kwart(
            Decimal(
                sum(
                    Decimal(str(woningwaardering.punten))
                    for woningwaardering in woningwaardering_groep.woningwaarderingen
                    or []
                    if woningwaardering.punten is not None
                    and woningwaardering.criterium is not None
                    and woningwaardering.criterium.bovenliggende_criterium is None
                )
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punt(en) voor stelselgroep {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def genereer_woningwaarderingen(
        ruimten: list[EenhedenRuimte],
        stelselgroep: Woningwaarderingstelselgroep,
    ) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
        criterium_sleutel_punten_regristratie: dict[str | None, Decimal] = {
            CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id: Decimal(
                "0"
            ),
            CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id: Decimal("0"),
            CriteriumSleutels.open_keuken.value.id: Decimal("0"),
        }

        for ruimte in ruimten:
            if ruimte.detail_soort is None:
                warnings.warn(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detailsoort.",
                    UserWarning,
                )
                continue

            ruimtesoort = classificeer_ruimte(ruimte)

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
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) komt niet in aanmerking voor waardering onder stelselgroep {stelselgroep.naam}"
                )
                continue

            punten = {
                Ruimtesoort.vertrek.code: Decimal("2"),
                Ruimtesoort.overige_ruimten.code: Decimal("1"),
            }[ruimtesoort.code]

            if ruimtesoort == Ruimtesoort.overige_ruimten:
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) telt als verwarmde {Ruimtesoort.overige_ruimten.naam} en krijgt {punten} punt."
                )
                yield (
                    ruimte,
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=ruimte.naam,
                            bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                                id=CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id,
                            ),
                        ),
                        punten=punten,
                    ),
                )

                criterium_sleutel_punten_regristratie[
                    CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id
                ] += punten
                aftrek = criterium_sleutel_punten_regristratie[
                    CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id
                ] - Decimal("4")
                if aftrek > Decimal("0"):
                    yield (
                        ruimte,
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=f"{ruimte.naam}: Maximaal 4 punten voor verwarmde overige- en verkeersruimten",
                                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                                    id=CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id,
                                ),
                            ),
                            punten=aftrek * Decimal("-1"),
                        ),
                    )

                    criterium_sleutel_punten_regristratie[
                        CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id
                    ] += aftrek * Decimal("-1")

            else:
                if ruimte.verkoeld:
                    punten += Decimal(
                        "1"
                    )  # 1 punt extra per vertrek wanneer verwarmd en verkoeld

                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) telt als verwarmd en verkoeld vertrek en krijgt {punten} punten."
                    )
                    yield (
                        ruimte,
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=ruimte.naam,
                                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                                    id=CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id,
                                ),
                            ),
                            punten=punten,
                        ),
                    )
                    criterium_sleutel_punten_regristratie[
                        CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id
                    ] += punten
                    grens = criterium_sleutel_punten_regristratie[
                        CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id
                    ] - Decimal("6")
                    if grens > Decimal("0"):
                        yield (
                            ruimte,
                            WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=f"{ruimte.naam}: Maximaal 2 extra punten voor verkoelde en verwarmde vertrekken",
                                    bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                                        id=CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id,
                                    ),
                                ),
                                punten=Decimal("-1"),
                            ),
                        )

                        logger.info(
                            f"Maximaal aantal punten voor verwarmde overige- en verkeersruimten overschreden ({criterium_sleutel_punten_regristratie[CriteriumSleutels.verwarmde_overige_en_verkeersruimten.value.id]} > {6}). Een aftrek van {-1} punt wordt toegepast."
                        )

                        criterium_sleutel_punten_regristratie[
                            CriteriumSleutels.verkoelde_en_verwarmde_vertrekken.value.id
                        ] += Decimal("-1")

                else:
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) telt als verwarmd vertrek en krijgt {punten} punten."
                    )
                    yield (
                        ruimte,
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=ruimte.naam,
                                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                                    id=CriteriumSleutels.verwarmde_vertrekken.value.id,
                                ),
                            ),
                            punten=punten,
                        ),
                    )

            # Voor deze rubriek wordt een verwarmde open keuken als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten.
            if (
                ruimte.detail_soort.code
                == Ruimtedetailsoort.woonkamer_en_of_keuken.code
                or ruimte.detail_soort.code
                in [
                    Ruimtedetailsoort.woonkamer.code,
                    Ruimtedetailsoort.woon_en_of_slaapkamer.code,
                    Ruimtedetailsoort.slaapkamer.code,
                ]
                and heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.aanrecht
                )
            ):
                yield (
                    ruimte,
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=ruimte.naam,
                            bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                                id=CriteriumSleutels.open_keuken.value.id,
                            ),
                        ),
                        punten=punten,
                    ),
                )


if __name__ == "__main__":  # pragma: no cover
    bereken(
        instance=VerkoelingEnVerwarming(),
        eenheid_input="tests/data/generiek/input/37101000032.json",
        strict=False,
    )
