from datetime import date

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.criterium import (
    GedeeldMetSoort,
)
from woningwaardering.stelsels.gedeelde_logica import (
    maximeer_wastafels,
    waardeer_sanitair,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class Sanitair(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.sanitair  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            peildatum=peildatum,
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        waarderingsgroep_bouwer = WaarderingsgroepBouwer(
            self.stelsel, self.stelselgroep
        )

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        # Waardeer elke ruimte onder het bijbehorende gedeeld-met-criterium.
        ruimte_waarderingen: list[
            tuple[
                EenhedenRuimte,
                WaarderingBouwer,
                list[WaarderingBouwer],
            ]
        ] = []

        for ruimte in ruimten:
            aantal_gedeeld = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
            if aantal_gedeeld is not None and aantal_gedeeld > 1:
                deler = aantal_gedeeld
            else:
                deler = 1
            gedeeld_met = waarderingsgroep_bouwer.gedeeld_met(
                aantal=deler,
                soort=GedeeldMetSoort.onzelfstandige_woonruimten,
            )

            waarderingen = waardeer_sanitair(
                ruimte,
                self.stelsel,
                waarderingsgroep_bouwer=gedeeld_met,
                deler=deler,
            )
            if not waarderingen:
                if gedeeld_met.is_leeg:
                    gedeeld_met.verwijder()
                continue

            ruimte_criterium = waarderingen[0]
            ruimte_waarderingen.append((ruimte, ruimte_criterium, waarderingen))

        maximeer_wastafels(ruimte_waarderingen)

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Sanitair(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
