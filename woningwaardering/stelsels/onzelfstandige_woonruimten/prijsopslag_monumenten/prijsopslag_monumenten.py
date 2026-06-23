from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.gedeelde_logica.prijsopslag_monumenten import (
    check_monumenten_attribuut,
    opslag_beschermd_stads_of_dorpsgezicht,
    opslag_gemeentelijk_of_provinciaal_monument,
    opslag_rijksmonument,
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


class PrijsopslagMonumenten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.prijsopslag_monumenten
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

        # De helpers hechten hun waarderingen via de waarderingsgroep_bouwer aan; consumeer de generator.
        for _ in self._genereer_woningwaarderingen(
            self.peildatum,
            eenheid,
            waarderingsgroep_bouwer,
        ):
            pass

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        opslagpercentage = float(
            sum(
                Decimal(str(woningwaardering.opslagpercentage))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.opslagpercentage is not None
            )
        )

        woningwaardering_groep.opslagpercentage = opslagpercentage
        woningwaardering_groep.punten = float(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    @staticmethod
    def _genereer_woningwaarderingen(
        peildatum: date,
        eenheid: EenhedenEenheid,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
    ) -> Iterator[WaarderingBouwer | None]:
        check_monumenten_attribuut(eenheid)

        yield opslag_rijksmonument(
            peildatum,
            eenheid,
            waarderingsgroep_bouwer=waarderingsgroep_bouwer,
        )
        yield opslag_gemeentelijk_of_provinciaal_monument(
            eenheid,
            waarderingsgroep_bouwer=waarderingsgroep_bouwer,
        )
        yield opslag_beschermd_stads_of_dorpsgezicht(
            eenheid,
            waarderingsgroep_bouwer=waarderingsgroep_bouwer,
        )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=PrijsopslagMonumenten(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as waarderingsgroep_bouwer:
        waarderingsgroep_bouwer.waardeer(
            "tests/data/onzelfstandige_woonruimten/input/15004000185.json"
        )
