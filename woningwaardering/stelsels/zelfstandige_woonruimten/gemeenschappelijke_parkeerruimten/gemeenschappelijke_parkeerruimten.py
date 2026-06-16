import re
import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import (
    CriteriumId,
    GedeeldMetSoort,
    nest_onder,
)
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_gemeenschappelijke_parkeerruimte,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingCriteriumSleutels,
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
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,
            )
        )
        woningwaardering_groep.woningwaarderingen = []

        if not eenheid.ruimten:
            warnings.warn(f"Eenheid ({eenheid.id}): geen ruimten gevonden")
            return woningwaardering_groep

        gedeeld_met_eenheden: set[int] = set()

        for ruimte in eenheid.ruimten:
            waarderingen = waardeer_gemeenschappelijke_parkeerruimte(ruimte)
            if waarderingen is None:
                continue

            for waardering in waarderingen:
                if (
                    waardering.criterium is not None
                    and ruimte.gedeeld_met_aantal_eenheden
                    and ruimte.gedeeld_met_aantal_eenheden >= 2
                    and waardering.criterium.id is not None
                ):
                    aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden
                    gedeeld_met_eenheden.add(aantal_eenheden)
                    adressen_id = str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            gedeeld_met_aantal=aantal_eenheden,
                            gedeeld_met_soort=GedeeldMetSoort.adressen,
                        )
                    )
                    waardering.criterium.id = nest_onder(
                        adressen_id, waardering.criterium.id
                    )
                    if waardering.criterium.naam is not None:
                        waardering.criterium.naam = re.sub(
                            r" \(gedeeld met \d+ adressen\)$",
                            "",
                            waardering.criterium.naam,
                        )
                    waardering.criterium.bovenliggende_criterium = (
                        WoningwaarderingCriteriumSleutels(id=adressen_id)
                    )
                elif waardering.criterium is not None and waardering.criterium.naam:
                    waardering.criterium.naam = re.sub(
                        r" \(privé\)$",
                        "",
                        waardering.criterium.naam,
                    )

                woningwaardering_groep.woningwaarderingen.append(waardering)

        for aantal_eenheden in sorted(gedeeld_met_eenheden):
            adressen_id = str(
                CriteriumId(
                    stelselgroep=self.stelselgroep,
                    gedeeld_met_aantal=aantal_eenheden,
                    gedeeld_met_soort=GedeeldMetSoort.adressen,
                )
            )
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        id=adressen_id,
                        naam=utils.naam_gedeeld_met_groep(
                            aantal_eenheden,
                            soort=GedeeldMetSoort.adressen,
                        ),
                    ),
                )
            )

        punten_totaal = float(
            utils.rond_af_op_kwart(
                Decimal(
                    str(
                        sum(
                            woningwaardering.punten
                            for woningwaardering in woningwaardering_groep.woningwaarderingen
                            or []
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
    ) as context:
        context.waardeer("warnings.json")
