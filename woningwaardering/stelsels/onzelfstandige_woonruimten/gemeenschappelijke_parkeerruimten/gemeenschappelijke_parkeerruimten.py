import re
import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.criterium import GedeeldMetSoort
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

        # De gedeelde helper bevat de classificatielogica. We laten die in een
        # tijdelijke waarderingsgroep_bouwer opbouwen en plaatsen de waarderingen daarna onder de juiste
        # gedeeld-met-criteria (eerst onzelfstandige woonruimten, dan adressen).
        tijdelijk = WaarderingsgroepBouwer(self.stelsel, self.stelselgroep)

        for ruimte in eenheid.ruimten:
            for bron in waardeer_gemeenschappelijke_parkeerruimte(
                ruimte, waarderingsgroep_bouwer=tijdelijk
            ):
                if not utils.gedeeld_met_eenheden(ruimte):
                    logger.debug(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}) is niet gedeeld met andere eenheden en telt daarom niet voor {self.stelselgroep.naam}."
                    )
                    continue

                aantal_onz = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

                adressen_bovenliggende: WaarderingsgroepBouwer | WaarderingBouwer = (
                    waarderingsgroep_bouwer
                )
                if aantal_onz > 1:
                    adressen_bovenliggende = waarderingsgroep_bouwer.gedeeld_met(
                        aantal=aantal_onz,
                        soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                    )

                adressen_gedeeld_met = adressen_bovenliggende.gedeeld_met(
                    aantal=aantal_eenheden,
                    soort=GedeeldMetSoort.adressen,
                )

                punten = bron.punten
                if punten is not None:
                    punten = float(
                        utils.rond_af(
                            Decimal(str(punten)) / Decimal(str(aantal_onz)),
                            decimalen=2,
                        )
                    )

                naam = re.sub(r" \(gedeeld met \d+ adressen\)$", "", bron.naam or "")

                adressen_gedeeld_met.maak_onderliggende(
                    id=ruimte.id or "ruimte",
                    naam=naam,
                    punten=punten,
                    aantal=bron.aantal,
                    meeteenheid=bron.meeteenheid,
                )

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeParkeerruimten(peildatum=date(2026, 1, 1)),
        strict=False,
        log_level="DEBUG",
    ) as waarderingsgroep_bouwer:
        waarderingsgroep_bouwer.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_parkeerruimten/input/voorbeeld_beleidsboek.json"
        )
