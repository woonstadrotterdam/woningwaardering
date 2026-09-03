from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_oppervlakte_van_vertrek,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    gedeeld_met_adressen,
    toe_te_rekenen_oppervlakte,
)
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
        waarderingsgroep_builder = WaarderingsgroepBuilder(
            self.stelsel, self.stelselgroep
        )

        # Eerst per ruimte delen, daarna salderen, daarna éénmaal afronden op hele m²
        # (#391). Wettekst en beleidsboek zijn niet sluitend; de huurprijscheck volgt
        # deze volgorde. Punten staan op de stelselgroep, niet op de gedeeld-met-laag
        # (#393).
        oppervlakte_totaal_na_delen = Decimal("0")

        for ruimte in eenheid.ruimten or []:
            if gedeeld_met_adressen(ruimte):
                continue  # wordt gewaardeerd volgens Rubriek "gemeenschappelijke binnenruimten gedeeld met meerdere adressen"

            deler = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1

            gedeeld_met = waarderingsgroep_builder.gedeeld_met(
                aantal_onzelfstandige_woonruimten=deler,
            )
            waarderingen = waardeer_oppervlakte_van_vertrek(
                ruimte, waarderingsgroep_builder=gedeeld_met
            )
            if waarderingen:
                oppervlakte_totaal_na_delen += toe_te_rekenen_oppervlakte(ruimte)

        woningwaardering_groep = waarderingsgroep_builder.build()
        woningwaardering_groep.punten = float(
            utils.rond_af(oppervlakte_totaal_na_delen, decimalen=0)
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=OppervlakteVanVertrekken(peildatum=date(2026, 7, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
