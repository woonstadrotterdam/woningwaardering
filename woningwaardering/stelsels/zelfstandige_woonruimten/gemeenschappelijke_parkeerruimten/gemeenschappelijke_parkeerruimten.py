import re
import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import WaarderingsgroepBouwer
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
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = (
            Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten
        )
        super().__init__(
            peildatum=peildatum,
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
        | None = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        waarderingsgroep_bouwer = WaarderingsgroepBouwer(
            self.stelsel, self.stelselgroep
        )

        if not eenheid.ruimten:
            warnings.warn(f"Eenheid ({eenheid.id}): geen ruimten gevonden")
            return waarderingsgroep_bouwer.bouw()

        # De gedeelde helper bevat de classificatielogica. We laten die in een
        # tijdelijke waarderingsgroep_bouwer opbouwen en plaatsen de waarderingen daarna onder het juiste
        # gedeeld-met-criterium met opgeschoonde naam.
        tijdelijk = WaarderingsgroepBouwer(self.stelsel, self.stelselgroep)

        for ruimte in eenheid.ruimten:
            for bron in waardeer_gemeenschappelijke_parkeerruimte(
                ruimte, waarderingsgroep_bouwer=tijdelijk
            ):
                if (
                    ruimte.gedeeld_met_aantal_eenheden
                    and ruimte.gedeeld_met_aantal_eenheden >= 2
                ):
                    gedeeld_met = waarderingsgroep_bouwer.gedeeld_met(
                        aantal=ruimte.gedeeld_met_aantal_eenheden,
                        soort=GedeeldMetSoort.adressen,
                    )
                    naam = re.sub(
                        r" \(gedeeld met \d+ adressen\)$",
                        "",
                        bron.naam or "",
                    )
                    gedeeld_met.maak_onderliggende(
                        id=ruimte.id or "ruimte",
                        naam=naam,
                        punten=bron.punten,
                        aantal=bron.aantal,
                        meeteenheid=bron.meeteenheid,
                    )
                elif bron.naam:
                    naam = re.sub(r" \(privé\)$", "", bron.naam)
                    waarderingsgroep_bouwer.maak_onderliggende(
                        id=ruimte.id,
                        naam=naam,
                        punten=bron.punten,
                        aantal=bron.aantal,
                        meeteenheid=bron.meeteenheid,
                    )

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        punten_totaal = float(
            utils.rond_af_op_kwart(
                Decimal(
                    str(
                        sum(
                            woningwaardering.punten
                            for woningwaardering in (
                                woningwaardering_groep.woningwaarderingen or []
                            )
                            if woningwaardering.punten is not None
                        )
                    )
                )
            )
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt {punten_totaal} punten voor {self.stelselgroep.naam}"
        )

        woningwaardering_groep.punten = punten_totaal

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeParkeerruimten(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as waarderingsgroep_bouwer:
        waarderingsgroep_bouwer.waardeer("warnings.json")
