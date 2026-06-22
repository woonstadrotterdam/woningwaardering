from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.onzelfstandige_woonruimten.oppervlakte_van_vertrekken import (
    OppervlakteVanVertrekken,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.woningwaardering_groep import WoningwaarderingGroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class Aftrekpunten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.aftrekpunten
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
        woningwaardering_groep = WoningwaarderingGroep(
            stelsel=self.stelsel,
            stelselgroep=self.stelselgroep,
        )

        totale_oppervlakte_vertrekken = self._totale_oppervlakte_vertrekken(
            eenheid, woningwaardering_resultaat
        )
        if (
            totale_oppervlakte_vertrekken is not None
            and totale_oppervlakte_vertrekken < Decimal("8")
        ):
            # 4 punten aftrek als de totale oppervlakte van de vertrekken minder is dan 8 m2
            aftrekpunten = -4.0
            logger.info(
                f"Eenheid ({eenheid.id}): oppervlakte van de vertrekken < 8m2 ({totale_oppervlakte_vertrekken:.2f}m2), {aftrekpunten} punten voor {self.stelselgroep.naam}"
            )
            woningwaardering_groep.met_onderliggend(
                f"{Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.name}_minder_dan_8m2",
                naam=f"Totale oppervlakte in Rubriek '{Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}' is minder dan 8m2",
                aantal=float(utils.rond_af(totale_oppervlakte_vertrekken, 2)),
                punten=aftrekpunten,
                meeteenheid=Meeteenheid.vierkante_meter_m2,
            )
        elif totale_oppervlakte_vertrekken is not None:
            logger.debug(
                f"Eenheid ({eenheid.id}): oppervlakte van de vertrekken >= 8m2 ({totale_oppervlakte_vertrekken:.2f}m2), geen aftrek hiervoor voor {self.stelselgroep.naam}"
            )

        woningwaardering_groep.punten = utils.som_punten_waarderingen(
            woningwaardering_groep.woningwaarderingen
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _totale_oppervlakte_vertrekken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> Decimal | None:
        """Berekent de totale oppervlakte van vertrekken uit resultaat of opnieuw.

        Args:
            eenheid (EenhedenEenheid): Eenheid om de aftrekpunten voor de oppervlakte van de vertrekken te berekenen.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None): Woningwaarderingresultaat om de oppervlakte van de vertrekken te berekenen.

        Returns:
            Decimal | None: Totale oppervlakte van vertrekken, of ``None`` bij geen waarderingen.
        """
        oppervlakte_resultaat = None
        # check of de oppervlakte van de vertrekken al berekend is
        if woningwaardering_resultaat:
            oppervlakte_resultaat = next(
                (
                    groep
                    for groep in woningwaardering_resultaat.groepen or []
                    if groep.criterium_groep
                    and groep.criterium_groep.stelselgroep
                    and groep.criterium_groep.stelselgroep.naam
                    == Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam
                ),
                None,
            )

        # Bereken de oppervlakte van de vertrekken als deze nog niet berekend is on het woningwaarderingresultaat
        if oppervlakte_resultaat is None:
            oppervlakte_resultaat = OppervlakteVanVertrekken(
                peildatum=self.peildatum
            ).waardeer(eenheid)

        if oppervlakte_resultaat.woningwaarderingen:
            return utils.som_effectieve_aantal_waarderingen(
                oppervlakte_resultaat.woningwaarderingen
            )
        return None


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Aftrekpunten(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
