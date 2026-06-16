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
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        if not eenheid.ruimten:
            warnings.warn(f"Eenheid ({eenheid.id}): geen ruimten gevonden")
            return woningwaardering_groep

        woningwaardering_groep.woningwaarderingen = []

        gedeeld_met_combos: set[tuple[int, int]] = set()

        for ruimte in eenheid.ruimten:
            waarderingen_zelfstandig = waardeer_gemeenschappelijke_parkeerruimte(ruimte)
            if waarderingen_zelfstandig is None:
                continue

            for waardering in waarderingen_zelfstandig:
                if not utils.gedeeld_met_eenheden(ruimte):
                    logger.debug(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}) is niet gedeeld met andere eenheden en telt daarom niet voor {self.stelselgroep.naam}."
                    )
                    continue

                gedeeld_met_aantal_onzelfstandige_woonruimten = (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                )
                aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
                gedeeld_met_combos.add(
                    (gedeeld_met_aantal_onzelfstandige_woonruimten, aantal_eenheden)
                )

                if waardering.punten is not None:
                    waardering.punten = float(
                        utils.rond_af(
                            Decimal(str(waardering.punten))
                            / Decimal(
                                str(gedeeld_met_aantal_onzelfstandige_woonruimten)
                            ),
                            decimalen=2,
                        )
                    )

                if (
                    waardering.criterium is not None
                    and waardering.criterium.id is not None
                ):
                    onz_id = (
                        str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                gedeeld_met_aantal=gedeeld_met_aantal_onzelfstandige_woonruimten,
                                gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                            )
                        )
                        if gedeeld_met_aantal_onzelfstandige_woonruimten > 1
                        else None
                    )
                    adressen_id = str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            gedeeld_met_aantal=aantal_eenheden,
                            gedeeld_met_soort=GedeeldMetSoort.adressen,
                            bovenliggende=onz_id,
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

                woningwaardering_groep.woningwaarderingen.append(waardering)

        for aantal_onz, aantal_eenheden in sorted(gedeeld_met_combos):
            onz_id = (
                str(
                    CriteriumId(
                        stelselgroep=self.stelselgroep,
                        gedeeld_met_aantal=aantal_onz,
                        gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                    )
                )
                if aantal_onz > 1
                else None
            )
            adressen_id = str(
                CriteriumId(
                    stelselgroep=self.stelselgroep,
                    gedeeld_met_aantal=aantal_eenheden,
                    gedeeld_met_soort=GedeeldMetSoort.adressen,
                    bovenliggende=onz_id,
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
                        bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                            id=onz_id
                        )
                        if onz_id is not None
                        else None,
                    ),
                )
            )

        onz_aantallen = {
            aantal_onz for aantal_onz, _ in gedeeld_met_combos if aantal_onz > 1
        }
        for aantal_onz in sorted(onz_aantallen):
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                gedeeld_met_aantal=aantal_onz,
                                gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                            )
                        ),
                        naam=utils.naam_gedeeld_met_groep(
                            aantal_onz,
                            soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                        ),
                    ),
                )
            )

        woningwaardering_groep.punten = utils.som_punten_waarderingen(
            woningwaardering_groep.woningwaarderingen
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeParkeerruimten(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_parkeerruimten/input/voorbeeld_beleidsboek.json"
        )
