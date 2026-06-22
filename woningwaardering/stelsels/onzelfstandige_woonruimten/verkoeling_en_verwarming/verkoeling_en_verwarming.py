from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    VerkoelingEnVerwarmingResultaat,
    bouw_verkoeling_en_verwarming,
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.woningwaardering_groep import WoningwaarderingGroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
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
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden == 1
        ]

        resultaten = list(waardeer_verkoeling_en_verwarming(ruimten))
        for onz_aantal, groep_resultaten in _groepeer_per_onz(resultaten).items():
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
            bouw_verkoeling_en_verwarming(
                groep_resultaten,
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


def _groepeer_per_onz(
    resultaten: list[VerkoelingEnVerwarmingResultaat],
) -> dict[int, list[VerkoelingEnVerwarmingResultaat]]:
    groepen: dict[int, list[VerkoelingEnVerwarmingResultaat]] = defaultdict(list)
    for ruimte, bron in resultaten:
        onz_aantal = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
        groepen[onz_aantal].append((ruimte, bron))
    return groepen


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=VerkoelingEnVerwarming(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/verkoeling_en_verwarming/input/vertrek_verkoeld_en_verwarmd_onz.json"
        )
