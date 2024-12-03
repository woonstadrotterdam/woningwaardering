from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.onzelfstandige_woonruimten.oppervlakte_van_vertrekken import (
    OppervlakteVanVertrekken,
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
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid


class Aftrekpunten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.aftrekpunten
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
            criterium_groep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel.value,
                stelselgroep=self.stelselgroep.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        # check of de oppervlakte van de vertrekken al berekend is
        oppervlakte_resultaat = None
        if woningwaardering_resultaat:
            oppervlakte_resultaat = next(
                (
                    groep
                    for groep in woningwaardering_resultaat.groepen or []
                    if groep.criterium_groep
                    and groep.criterium_groep.stelselgroep
                    and groep.criterium_groep.stelselgroep.naam
                    == Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.value.naam
                ),
                None,
            )

        # Bereken de oppervlakte van de vertrekken als deze nog niet berekend is on het woningwaarderingresultaat
        if oppervlakte_resultaat is None:
            oppervlakte_resultaat = OppervlakteVanVertrekken(
                peildatum=self.peildatum
            ).waardeer(eenheid)

        if oppervlakte_resultaat.woningwaarderingen:
            totale_oppervlakte_vertrekken = sum(
                Decimal(str(woningwaardering.aantal))
                for woningwaardering in oppervlakte_resultaat.woningwaarderingen
                if (
                    woningwaardering.criterium
                    and woningwaardering.criterium.bovenliggende_criterium is None
                    and woningwaardering.aantal is not None
                )
            )

            # 4 punten aftrek als de totale oppervlakte van de vertrekken minder is dan 8 m2
            if totale_oppervlakte_vertrekken < Decimal("8"):
                woningwaardering = WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"Totale oppervlakte in Rubriek '{Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}' is minder dan 8m2",
                        meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                    )
                )
                woningwaardering.aantal = float(
                    utils.rond_af(totale_oppervlakte_vertrekken, 2)
                )
                woningwaardering.punten = -4.0
                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium is not None
                and woningwaardering.criterium.bovenliggende_criterium is None
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Aftrekpunten(),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
