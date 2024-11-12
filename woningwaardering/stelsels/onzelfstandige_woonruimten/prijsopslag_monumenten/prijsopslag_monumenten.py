from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.prijsopslag_monumenten_en_nieuwbouw.prijsopslag_monumenten_en_nieuwbouw import (
    PrijsopslagMonumentenEnNieuwbouw,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
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
        super().__init__(
            begindatum=date(2024, 7, 1),
            einddatum=date.max,
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.prijsopslag_monumenten

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel.value,
                stelselgroep=self.stelselgroep.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = list(
            woningwaardering
            for woningwaardering in self._genereer_woningwaarderingen(
                self.peildatum, eenheid, woningwaardering_resultaat
            )
            if woningwaardering is not None
        )

        opslagpercentage = Decimal(
            sum(
                Decimal(str(woningwaardering.opslagpercentage))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.opslagpercentage is not None
            )
        )

        woningwaardering_groep.opslagpercentage = float(opslagpercentage)
        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep

    @staticmethod
    def _genereer_woningwaarderingen(
        peildatum: date,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering | None]:
        PrijsopslagMonumentenEnNieuwbouw._check_monumenten_attribuut(eenheid)

        yield PrijsopslagMonumentenEnNieuwbouw._opslag_rijksmonument(
            peildatum,
            eenheid,
            stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten,
        )
        yield PrijsopslagMonumentenEnNieuwbouw._opslag_gemeentelijk_of_provinciaal_monument(
            eenheid,
            stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten,
        )
        yield PrijsopslagMonumentenEnNieuwbouw._opslag_beschermd_stads_of_dorpsgezicht(
            eenheid,
            stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten,
        )


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    prijsopslag_monumenten_en_nieuwbouw = PrijsopslagMonumenten()
    with open(
        "tests/data/zelfstandige_woonruimten/input/23109000031.json", "r+"
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

        woningwaardering_resultaat = prijsopslag_monumenten_en_nieuwbouw.bereken(
            eenheid
        )

        print(
            woningwaardering_resultaat.model_dump_json(
                by_alias=True, indent=2, exclude_none=True
            )
        )

        tabel = utils.naar_tabel(woningwaardering_resultaat)

        print(tabel)