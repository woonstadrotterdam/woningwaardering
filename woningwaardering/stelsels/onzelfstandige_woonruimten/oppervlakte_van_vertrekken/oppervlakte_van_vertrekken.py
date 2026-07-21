from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import WaarderingsgroepBouwer
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_oppervlakte_van_vertrek,
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


class OppervlakteVanVertrekken(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_vertrekken  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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

        gedeeld_met_counter: defaultdict[int, Decimal] = defaultdict(Decimal)

        for ruimte in eenheid.ruimten or []:
            if ruimte.gedeeld_met_aantal_adressen:
                continue  # wordt gewaardeerd volgens Rubriek "gemeenschappelijke binnenruimten gedeeld met meerdere adressen"

            deler = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1

            gedeeld_met = waarderingsgroep_bouwer.gedeeld_met(
                aantal_onzelfstandige_woonruimten=deler,
            )
            waarderingen = waardeer_oppervlakte_van_vertrek(
                ruimte, waarderingsgroep_bouwer=gedeeld_met
            )
            for waardering in waarderingen:
                if waardering.aantal is None:
                    continue
                # houd bij of de ruimte gedeeld is met andere onzelfstandige woonruimten zodat later de punten kunnen worden gedeeld
                gedeeld_met_counter[deler] += utils.rond_af(
                    waardering.aantal, decimalen=2
                )

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        oppervlakte_totaal_na_delen = Decimal("0")
        for aantal_onz, oppervlakte in gedeeld_met_counter.items():
            oppervlakte_na_delen = utils.rond_af(oppervlakte, decimalen=2) / Decimal(
                str(aantal_onz)
            )
            oppervlakte_totaal_na_delen += oppervlakte_na_delen

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()
        woningwaardering_groep.punten = float(
            utils.rond_af(oppervlakte_totaal_na_delen, decimalen=0)
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=OppervlakteVanVertrekken(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
