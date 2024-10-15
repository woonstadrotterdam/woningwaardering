import warnings
from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import classificeer_ruimte
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

        for ruimte in ruimten:
            woningwaarderingen = VerkoelingEnVerwarming.genereer_woningwaarderingen(
                ruimte,
                self.stelselgroep,
            )

            woningwaardering_groep.woningwaarderingen.extend(woningwaarderingen)

        woningwaardering_groep.woningwaarderingen.extend(
            VerkoelingEnVerwarming.maximering(woningwaardering_groep.woningwaarderingen)
        )
        woningwaardering_groep.woningwaarderingen.extend(
            self.som_criterium_sleutels(woningwaardering_groep)
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
        ruimte: EenhedenRuimte,
        stelselgroep: Woningwaarderingstelselgroep,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        if ruimte.detail_soort is None:
            warnings.warn(
                f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detailsoort.",
                UserWarning,
            )
            return

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
                f"Ruimte {ruimte.naam} ({ruimte.id}) telt als verwarmde {Ruimtesoort.overige_ruimten.naam} en krijgt {punten} punt."
            )
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=ruimte.naam,
                    bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                        id="verwarmde_overige_en_verkeersruimten",
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
                    f"Ruimte {ruimte.naam} ({ruimte.id}) telt als verwarmd en verkoeld vertrek en krijgt {punten} punten."
                )
                yield WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=ruimte.naam,
                        bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                            id="verkoelde_en_verwarmde_vertrekken",
                        ),
                    ),
                    punten=punten,
                )
            else:
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) telt als verwarmd vertrek en krijgt {punten} punten."
                )
                yield WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=ruimte.naam,
                        bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                            id="verwarmde_vertrekken",
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
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=ruimte.naam,
                    bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                        id="open_keuken",
                    ),
                ),
                punten=punten,
            )

    @staticmethod
    def maximering(
        woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering],
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        # som van punten per criteriumsleutel
        criteriumsleutelpunten: dict[str, float] = defaultdict(float)
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
            criteriumsleutelpunten.get("verwarmde_overige_en_verkeersruimten", 0)
            > max_punten_overige_ruimten
        ):
            aftrek = max_punten_overige_ruimten - criteriumsleutelpunten.get(
                "verwarmde_overige_en_verkeersruimten", 0
            )

            logger.info(
                f'Maximaal aantal punten voor verwarmde overige- en verkeersruimten overschreden ({criteriumsleutelpunten["verwarmde_overige_en_verkeersruimten"]} > {max_punten_overige_ruimten}). Een aftrek van {aftrek} punt(en) wordt toegepast.'
            )
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Maximaal 4 punten",
                    bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                        id="verwarmde_overige_en_verkeersruimten",
                    ),
                ),
                punten=aftrek,
            )

        max_punten_verkoeld_en_verwarmd_zonder_aftrek = 6  # 6 want maximaal 2 extra punten per verkoeld en verwarmd vertrek, en 3 punten per verkoeld en verwarmd vertrek
        if (
            criteriumsleutelpunten.get("verkoelde_en_verwarmde_vertrekken", 0)
            > max_punten_verkoeld_en_verwarmd_zonder_aftrek
        ):
            # maximaal 2 extra punten voor verkoelde en verwarmde vertrekken.
            # 3 punten per verkoeld en verwarmd vertrek
            # aantal extra punten meer dan 2 = (6 - aantal punten voor verkoelde en verwarmde vertrekken) / 3
            aftrek = (
                max_punten_verkoeld_en_verwarmd_zonder_aftrek
                - criteriumsleutelpunten.get("verkoelde_en_verwarmde_vertrekken", 0)
            ) / 3

            logger.info(
                f'Maximaal aantal extra punten voor verwarmde en verkoelde vertrekken overschreden ({criteriumsleutelpunten["verkoelde_en_verwarmde_vertrekken"]} > {max_punten_verkoeld_en_verwarmd_zonder_aftrek}). Een aftrek van {aftrek} punt(en) wordt toegepast.'
            )
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Maximaal 2 extra punten",
                    bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                        id="verkoelde_en_verwarmde_vertrekken",
                    ),
                ),
                punten=aftrek,
            )


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    verkoeling_en_verwarming = VerkoelingEnVerwarming(
        peildatum=date.fromisoformat("2024-07-01")
    )

    with open(
        "tests/data/zelfstandige_woonruimten/stelselgroepen/verkoeling_en_verwarming/input/max_4_punten_overige_ruimten.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[verkoeling_en_verwarming.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
