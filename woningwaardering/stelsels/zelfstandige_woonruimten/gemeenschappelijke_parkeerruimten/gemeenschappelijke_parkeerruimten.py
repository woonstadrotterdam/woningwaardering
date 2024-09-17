from datetime import date
from decimal import Decimal
import warnings

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import classificeer_ruimte
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
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.utils import heeft_bouwkundig_element


class GemeenschappelijkeParkeerruimten(Stelselgroep):
    parkeertype_punten_mapping = {
        Ruimtedetailsoort.parkeervak_auto_binnen.code: {"Type I": Decimal("9.0")},
        Ruimtedetailsoort.carport.code: {"Type II": Decimal("6.0")},
        Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt.code: {
            "Type III": Decimal("3.0")
        },
    }

    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = (
            Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten
        )
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        max_gedeeld_met_aantal_eenheden = 1

        if eenheid.ruimten is None:
            warnings.warn(f"Eenheid {eenheid.id} heeft geen 'ruimten'")
            return woningwaardering_groep

        for ruimte in eenheid.ruimten:
            # Het beleidsboek geeft niet aan hoe er punten gegeven moeten worden voor onderstaande ruimtes
            if ruimte.code in [
                Ruimtedetailsoort.parkeervak_motorfiets_binnen.code,
                Ruimtedetailsoort.parkeervak_scootmobiel_binnen.code,
                Ruimtedetailsoort.stalling_extern.code,
                Ruimtedetailsoort.stalling_intern.code,
                Ruimtedetailsoort.parkeervak_motorfiets_buiten_niet_overdekt.code,
                Ruimtedetailsoort.parkeervak_scootmobiel_buiten.code,
            ]:
                logger.warning(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) is een parkeerplek die niet gewaardeerd wordt in het woningwaardering stelsel volgens het beleidsboek."
                )
                continue

            if ruimte.code in [
                Ruimtedetailsoort.parkeerterrein.code,
                Ruimtedetailsoort.parkeergarage.code,
            ]:
                logger.warning(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) is een {Ruimtedetailsoort.parkeerterrein.naam if ruimte.code==Ruimtedetailsoort.parkeerterrein.code else Ruimtedetailsoort.parkeergarage.naam} en kan momenteel niet gewaardeerd worden in de woningwaardering package. Voeg parkeerplekken los toe aan de eenheden om deze in aanmerking te laten komen voor een waardering onder {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}."
                )
                continue

            if ruimte.code not in [
                Ruimtedetailsoort.parkeervak_auto_binnen.code,
                Ruimtedetailsoort.carport.code,
                Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt.code,
            ]:
                logger.info(
                    f"Ruimte {ruimte.id} is geen gemeenschappelijke parkeerruimte en wordt niet gewaardeerd onder rubriek {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}."
                )
                continue

            if classificeer_ruimte(ruimte) is not None:
                logger.info(
                    f"Eenheid {eenheid.id} wordt gewaardeerd onder de rubriek {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}."
                )
                continue

            if ruimte.oppervlakte is None:
                warnings.warn(f"Ruimte {ruimte.id} heeft geen 'oppervlakte'")
                continue

            if not ruimte.oppervlakte >= 12.0:
                logger.info(
                    f"Ruimte {ruimte.id} voldoet niet aan de eisen van 12m2 voor een parkeervak"
                )
                continue

            for criterium, punten in self.parkeertype_punten_mapping[
                ruimte.code
            ].items():
                if heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.laadpaal
                ):  # gaat uit van 1 laadpaal per parkeervak
                    punten += Decimal("2.0")
                    criterium += " + laadpaal"

                logger.info(
                    f"Ruimte {ruimte.id} is een gemeenschappelijke parkeerruimte {criterium}"
                )

                # update de max_gedeeld_met_aantal_eenheden variabele
                if ruimte.gedeeld_met_aantal_eenheden is not None:
                    if (
                        ruimte.gedeeld_met_aantal_eenheden
                        > max_gedeeld_met_aantal_eenheden
                    ):
                        max_gedeeld_met_aantal_eenheden = (
                            ruimte.gedeeld_met_aantal_eenheden
                        )

                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=criterium
                        ),
                        punten=punten,
                    ),
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
                / Decimal(str(max_gedeeld_met_aantal_eenheden))
            )
        )

        if punten_totaal > 0:
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Gedeeld met aantal eenheden",
                        aantal=max_gedeeld_met_aantal_eenheden,
                    )
                )
            )

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {punten_totaal} punten voor stelselgroep {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}"
        )

        woningwaardering_groep.punten = punten_totaal

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    gemeenschappelijke_parkeerruimten = GemeenschappelijkeParkeerruimten(
        peildatum=date.fromisoformat("2024-07-01")
    )

    with open("tests/data/generiek/input/37101000032.json", "r+") as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = gemeenschappelijke_parkeerruimten.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
