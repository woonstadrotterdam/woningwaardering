import warnings
from datetime import date

from loguru import logger

from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import WaarderingsgroepBouwer
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_gemeenschappelijke_parkeerruimte,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class GemeenschappelijkeParkeerruimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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

        if not eenheid.ruimten:
            warnings.warn(f"Eenheid ({eenheid.id}): geen ruimten gevonden")
            return waarderingsgroep_bouwer.bouw()

        for ruimte in eenheid.ruimten:
            waardeer_gemeenschappelijke_parkeerruimte(
                ruimte, waarderingsgroep_bouwer=waarderingsgroep_bouwer
            )

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeParkeerruimten(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_parkeerruimten/input/voorbeeld_beleidsboek.json"
        )
