from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.gedeelde_logica import waardeer_verkoeling_en_verwarming
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    gedeeld_met_onzelfstandige_woonruimten,
    rond_af,
)
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
        waarderingsgroep_bouwer = WaarderingsgroepBouwer(
            self.stelsel, self.stelselgroep
        )

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_adressen is None
            or ruimte.gedeeld_met_aantal_adressen == 1
        ]

        def subgroep(
            ruimte: EenhedenRuimte, subgroep_id: str, subgroep_naam: str
        ) -> WaarderingBouwer:
            deler = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            gedeeld_met = waarderingsgroep_bouwer.gedeeld_met(
                aantal_onzelfstandige_woonruimten=deler,
            )
            return gedeeld_met.categorie(
                id=subgroep_id,
                naam=subgroep_naam,
            )

        for ruimte, waardering in waardeer_verkoeling_en_verwarming(
            ruimten, subgroep=subgroep
        ):
            if waardering.punten is None:
                continue
            if (
                gedeeld_met_onzelfstandige_woonruimten(ruimte)
                and waardering.punten
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
            ):
                deler = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                waardering.punten = float(
                    rond_af(
                        rond_af(Decimal(str(waardering.punten)), decimalen=2) / deler,
                        decimalen=2,
                    )
                )

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=VerkoelingEnVerwarming(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/verkoeling_en_verwarming/input/vertrek_verkoeld_en_verwarmd_onz.json"
        )
