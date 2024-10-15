from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Literal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import (
    deel_punten_door_aantal_onzelfstandige_woonruimten,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.verkoeling_en_verwarming.verkoeling_en_verwarming import (
    VerkoelingEnVerwarming as ZelfstandigeWoonruimtenVerkoelingEnVerwarming,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
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


class VerkoelingEnVerwarming(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.verkoeling_en_verwarming  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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
                stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.verkoeling_en_verwarming.value,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaardering_groep.woningwaarderingen = []
        woningwaarderingen_voor_gedeeld = []

        totalen: dict[
            Literal[
                "verwarmde_overige_en_verkeersruimten",
                "verkoelde_en_verwarmde_vertrekken",
                "open_keuken",
                "verwarmde_vertrekken",
            ],
            Decimal,
        ] = {
            "verwarmde_overige_en_verkeersruimten": Decimal(
                "0"
            ),  # max 4 punten per eenheid voor verwarmde overige- en verkeersruimten.
            "verkoelde_en_verwarmde_vertrekken": Decimal(
                "0"
            ),  # max 2 extra punten per eenheid voor vertrekken die en verwarmd en verkoeld zijn. 1 punt extra per vertrek.
            "open_keuken": Decimal("0"),
            "verwarmde_vertrekken": Decimal("0"),
        }

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden == 1
        ]

        for ruimte in ruimten:
            woningwaarderingen = ZelfstandigeWoonruimtenVerkoelingEnVerwarming.genereer_woningwaarderingen(
                ruimte,
                self.stelselgroep,
                totalen,
            )

            woningwaarderingen_voor_gedeeld.append((ruimte, woningwaarderingen))

        for ruimte, woningwaarderingen in woningwaarderingen_voor_gedeeld:
            woningwaardering_groep.woningwaarderingen.extend(
                deel_punten_door_aantal_onzelfstandige_woonruimten(
                    ruimte, woningwaarderingen
                )
            )

        # maximering is op basis van de punten voordat ze gedeeld worden door het aantal onzelfstandige wonruimten
        # vandaar het gebruik van totalen
        woningwaardering_groep.woningwaarderingen.extend(
            ZelfstandigeWoonruimtenVerkoelingEnVerwarming.maximering(totalen)
        )

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium.bovenliggende_criterium is not None
            ),
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.oppervlakte_onzelfstandige_woonruimte.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    stelselgroep = VerkoelingEnVerwarming()
    with open(
        "tests/data/onzelfstandige_woonruimten/stelselgroepen/verkoeling_en_verwarming/input/max_2_punten_verkoelde_en_verwarmde_vertrekken.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
