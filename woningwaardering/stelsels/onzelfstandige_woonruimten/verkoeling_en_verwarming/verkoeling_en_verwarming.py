from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import waardeer
from woningwaardering.stelsels.gedeelde_logica import (
    maximeer_verkoeling_en_verwarming,
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    deel_punten_door_aantal_onzelfstandige_woonruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
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

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel.value,
                stelselgroep=self.stelselgroep.value,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaardering_groep.woningwaarderingen = []
        woningwaarderingen_voor_gedeeld = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden == 1
        ]

        for ruimte in ruimten:
            woningwaarderingen = list(waardeer_verkoeling_en_verwarming(ruimte))

            woningwaarderingen_voor_gedeeld.append((ruimte, woningwaarderingen))

        # maximering is op basis van de punten voordat ze gedeeld worden door het aantal onzelfstandige woonruimten
        maximering = list(
            maximeer_verkoeling_en_verwarming(
                [
                    woningwaardering
                    for ruimte, woningwaarderingen in woningwaarderingen_voor_gedeeld
                    for woningwaardering in woningwaarderingen
                ]
            )
        )

        for ruimte, woningwaarderingen in woningwaarderingen_voor_gedeeld:
            woningwaardering_groep.woningwaarderingen.extend(
                deel_punten_door_aantal_onzelfstandige_woonruimten(
                    ruimte, woningwaarderingen
                )
            )

        # maximering hier pas toevoegen voor meer intuitieve volgorde
        woningwaardering_groep.woningwaarderingen.extend(maximering)

        woningwaardering_groep.woningwaarderingen.extend(
            self.criteriumsleutel_resultaten(woningwaardering_groep)
        )
        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium
                and woningwaardering.criterium.bovenliggende_criterium is None
            ),
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    waardeer(
        instance=VerkoelingEnVerwarming(),
        eenheid_input="tests/data/onzelfstandige_woonruimten/input/15004000185.json",
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    )
