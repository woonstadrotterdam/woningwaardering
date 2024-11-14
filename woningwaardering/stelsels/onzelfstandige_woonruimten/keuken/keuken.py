from collections import defaultdict
from datetime import date

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import bereken
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.keuken.keuken import (
    Keuken as ZelfstandigeWoonruimtenKeuken,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
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


class Keuken(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.keuken  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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
                stelselgroep=Woningwaarderingstelselgroep.keuken.value,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        gedeeld_met_counter: defaultdict[int, float] = defaultdict(float)

        for ruimte in eenheid.ruimten or []:
            woningwaarderingen = list(
                ZelfstandigeWoonruimtenKeuken.genereer_woningwaarderingen(
                    ruimte, self.stelselgroep, self.stelsel
                )
            )
            # houd bij of de ruimte gedeeld is met andere onzelfstandige woonruimten zodat later de punten kunnen worden gedeeld
            for woningwaardering in woningwaarderingen:
                if woningwaardering.criterium is not None:
                    if (
                        woningwaardering.punten
                        and utils.gedeeld_met_onzelfstandige_woonruimten(ruimte)
                        and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                        is not None
                    ):
                        gedeeld_met_counter[
                            ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                        ] += woningwaardering.punten
                        woningwaardering.criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                            id=f"{self.stelselgroep.name}_gedeeld_met_{ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten}_onzelfstandige_woonruimten"
                        )
                        woningwaardering.punten = float(
                            utils.rond_af(
                                woningwaardering.punten
                                / ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten,
                                decimalen=2,
                            )
                        )
                    elif woningwaardering.punten:
                        gedeeld_met_counter[1] += woningwaardering.punten
                        woningwaardering.criterium.bovenliggende_criterium = (
                            WoningwaarderingCriteriumSleutels(
                                id=f"{self.stelselgroep.name}_prive"
                            )
                        )

            woningwaardering_groep.woningwaarderingen.extend(woningwaarderingen)

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        for aantal, punten in gedeeld_met_counter.items():
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=f"Totaal (gedeeld met {aantal})"
                if aantal > 1
                else "Totaal (privé)",
                id=f"{self.stelselgroep.name}_gedeeld_met_{aantal}_onzelfstandige_woonruimten"
                if aantal > 1
                else f"{self.stelselgroep.name}_prive",
            )
            woningwaardering.punten = float(utils.rond_af_op_kwart(punten / aantal))
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        woningwaardering_groep.punten = sum(
            woningwaardering.punten
            for woningwaardering in woningwaardering_groep.woningwaarderingen or []
            if woningwaardering.punten is not None
            and woningwaardering.criterium is not None
            and woningwaardering.criterium.bovenliggende_criterium is None
        )

        logger.info(
            f"Eenheid ({eenheid.id}) wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    bereken(
        class_=Keuken(),
        eenheid_input="tests/data/onzelfstandige_woonruimten/input/15004000185.json",
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    )
