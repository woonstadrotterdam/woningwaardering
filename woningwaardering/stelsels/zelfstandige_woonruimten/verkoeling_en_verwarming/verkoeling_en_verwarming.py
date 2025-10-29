from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
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
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.verkoeling_en_verwarming
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
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        woningwaardering_groep.woningwaarderingen.extend(
            waardering for _, waardering in waardeer_verkoeling_en_verwarming(ruimten)
        )

        woningwaardering_groep.woningwaarderingen.extend(
            self._maak_totalen(woningwaardering_groep)
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
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    def _maak_totalen(
        self, woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        criteriumsleutelpunten: dict[str, float] = defaultdict(float)
        for woningwaardering in woningwaardering_groep.woningwaarderingen or []:
            if (
                woningwaardering.criterium
                and woningwaardering.criterium.bovenliggende_criterium
                and woningwaardering.criterium.bovenliggende_criterium.id
                and isinstance(woningwaardering.punten, float)
            ):
                criteriumsleutelpunten[
                    woningwaardering.criterium.bovenliggende_criterium.id
                ] += woningwaardering.punten

        for id, punten in criteriumsleutelpunten.items():
            onderdelen = id.split("__")
            naam = onderdelen[-1].capitalize().replace("_", " ")
            criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=naam,
                id=id,
            )
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=criterium,
                punten=punten,
            )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=VerkoelingEnVerwarming(peildatum=date(2025, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
