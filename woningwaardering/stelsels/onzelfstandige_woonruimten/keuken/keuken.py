from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_keuken,
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


class Keuken(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.keuken  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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
                stelselgroep=self.stelselgroep,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        gedeeld_met_aantallen: dict[int, None] = {}

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        for ruimte in ruimten or []:
            woningwaarderingen = utils.nest_waarderingen_onder_ruimte(
                ruimte,
                list(waardeer_keuken(ruimte, self.stelsel)),
                stelselgroep=self.stelselgroep,
            )
            if not woningwaarderingen:
                continue

            onz_aantal = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            if (
                utils.gedeeld_met_onzelfstandige_woonruimten(ruimte)
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten > 1
            ):
                gedeeld_met_id = CriteriumId.voor_stelselgroep(
                    self.stelselgroep
                ).gedeeld_met_criterium(
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten,
                    GedeeldMetSoort.onzelfstandige_woonruimten,
                )
                gedeeld_met_aantallen[
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                ] = None
            else:
                gedeeld_met_id = CriteriumId.voor_stelselgroep(
                    self.stelselgroep
                ).gedeeld_met_criterium(1)
                gedeeld_met_aantallen[1] = None

            for woningwaardering in woningwaarderingen:
                if woningwaardering.criterium is None:
                    continue
                if onz_aantal > 1 and woningwaardering.punten is not None:
                    woningwaardering.punten = float(
                        utils.rond_af(
                            Decimal(str(woningwaardering.punten))
                            / Decimal(str(onz_aantal)),
                            decimalen=2,
                        )
                    )
                utils.verplaats_waardering_onder_gedeeld_met(
                    woningwaardering,
                    stelselgroep=self.stelselgroep,
                    gedeeld_met_id=gedeeld_met_id,
                )

            woningwaardering_groep.woningwaarderingen.extend(woningwaarderingen)

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        for aantal in gedeeld_met_aantallen:
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=utils.naam_gedeeld_met_groep(
                        aantal,
                        soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                    ),
                    id=str(
                        CriteriumId.voor_stelselgroep(
                            self.stelselgroep
                        ).gedeeld_met_criterium(
                            aantal, GedeeldMetSoort.onzelfstandige_woonruimten
                        )
                    ),
                )
            )
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        woningwaardering_groep.punten = utils.som_punten_waarderingen(
            woningwaardering_groep.woningwaarderingen
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Keuken(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
