from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.criterium import GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_verkoeling_en_verwarming,
)
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
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden == 1
        ]

        # De gedeelde helper bevat de classificatie- en maximeringslogica. We laten
        # die in een tijdelijke waarderingsgroep_bouwer opbouwen en hangen de waarderingen daarna onder het
        # juiste gedeeld-met-criterium met door het aantal onzelfstandige woonruimten
        # gedeelde punten.
        tijdelijk = WaarderingsgroepBouwer(self.stelsel, self.stelselgroep)
        subgroep_cache: dict[tuple[WaarderingBouwer, str], WaarderingBouwer] = {}

        for ruimte, bron in waardeer_verkoeling_en_verwarming(
            ruimten, waarderingsgroep_bouwer=tijdelijk
        ):
            self._hang_onder_gedeeld_met(
                ruimte,
                bron,
                waarderingsgroep_bouwer=waarderingsgroep_bouwer,
                subgroep_cache=subgroep_cache,
            )

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    @staticmethod
    def _hang_onder_gedeeld_met(
        ruimte: EenhedenRuimte,
        bron: WaarderingBouwer,
        *,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        subgroep_cache: dict[tuple[WaarderingBouwer, str], WaarderingBouwer],
    ) -> None:
        """Bouw een kopie van ``bron`` onder het juiste gedeeld-met-criterium.

        De punten worden verdeeld over het aantal onzelfstandige woonruimten en de
        eventuele subgroep (bijv. "verwarmde vertrekken") wordt onder het
        gedeeld-met-criterium opnieuw opgebouwd (en gededupliceerd).
        """
        punten = bron.punten
        if (
            gedeeld_met_onzelfstandige_woonruimten(ruimte)
            and punten
            and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
        ):
            punten = float(
                rond_af(
                    rond_af(Decimal(str(punten)), decimalen=2)
                    / ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten,
                    decimalen=2,
                )
            )

        deler = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
        gedeeld_met = waarderingsgroep_bouwer.gedeeld_met(
            aantal=deler,
            soort=GedeeldMetSoort.onzelfstandige_woonruimten,
        )

        ouder = bron.bovenliggende
        if isinstance(ouder, WaarderingBouwer):
            parent_segment = ouder.segment
            subgroep_key = (gedeeld_met, parent_segment)
            if subgroep_key not in subgroep_cache:
                subgroep_cache[subgroep_key] = gedeeld_met.maak_onderliggende(
                    id=parent_segment,
                    naam=parent_segment.replace("_", " ").capitalize(),
                )
            subgroep = subgroep_cache[subgroep_key]
            subgroep.maak_onderliggende(
                id=bron.segment,
                naam=bron.naam or bron.segment,
                punten=punten,
            )
            return

        gedeeld_met.maak_onderliggende(
            id=bron.segment,
            naam=bron.naam or bron.segment,
            punten=punten,
        )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=VerkoelingEnVerwarming(peildatum=date(2026, 1, 1)),
        strict=False,
        log_level="DEBUG",
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/verkoeling_en_verwarming/input/vertrek_verkoeld_en_verwarmd_onz.json"
        )
