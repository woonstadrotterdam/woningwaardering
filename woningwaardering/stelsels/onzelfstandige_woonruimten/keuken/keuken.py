from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    bouw_keuken,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.woningwaardering_groep import WoningwaarderingGroep
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


class Keuken(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.keuken  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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
        woningwaardering_groep = WoningwaarderingGroep(
            stelsel=self.stelsel,
            stelselgroep=self.stelselgroep,
        )

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        for onz_aantal, groep_ruimten in _groepeer_ruimten_per_onz(ruimten).items():
            if onz_aantal > 1:
                gedeeld_met_handle = woningwaardering_groep.met_gedeeld_met_criterium(
                    onz_aantal,
                    GedeeldMetSoort.onzelfstandige_woonruimten,
                    naam=utils.naam_gedeeld_met_groep(
                        onz_aantal,
                        soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                    ),
                )
            else:
                gedeeld_met_handle = woningwaardering_groep.met_gedeeld_met_criterium(
                    1, naam=utils.naam_gedeeld_met_groep(1)
                )
            bouw_keuken(
                groep_ruimten,
                self.stelsel,
                gedeeld_met_handle,
                Decimal(str(onz_aantal)),
            )

        woningwaardering_groep.punten = utils.som_punten_waarderingen(
            woningwaardering_groep.woningwaarderingen
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


def _groepeer_ruimten_per_onz(
    ruimten: list[EenhedenRuimte],
) -> dict[int, list[EenhedenRuimte]]:
    groepen: dict[int, list[EenhedenRuimte]] = defaultdict(list)
    for ruimte in ruimten:
        onz_aantal = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
        groepen[onz_aantal].append(ruimte)
    return groepen


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Keuken(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
