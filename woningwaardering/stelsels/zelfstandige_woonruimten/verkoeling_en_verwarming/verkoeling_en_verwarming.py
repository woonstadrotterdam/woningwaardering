from datetime import date
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import (
    laatste_criteriumid_toevoeging,
    weergavenaam_voor,
)
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

        woningwaardering_groep.punten = utils.som_punten_waarderingen(
            woningwaardering_groep.woningwaarderingen
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    def _maak_totalen(
        self, woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        criteriumsleutel_ids: dict[str, None] = {}
        for woningwaardering in woningwaardering_groep.woningwaarderingen or []:
            if (
                woningwaardering.criterium
                and woningwaardering.criterium.bovenliggende_criterium
                and woningwaardering.criterium.bovenliggende_criterium.id
                and isinstance(woningwaardering.punten, float)
            ):
                criteriumsleutel_ids[
                    woningwaardering.criterium.bovenliggende_criterium.id
                ] = None

        for criterium_id in criteriumsleutel_ids:
            naam = weergavenaam_voor(laatste_criteriumid_toevoeging(criterium_id))
            criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=naam,
                id=criterium_id,
            )
            yield WoningwaarderingResultatenWoningwaardering(criterium=criterium)


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=VerkoelingEnVerwarming(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
