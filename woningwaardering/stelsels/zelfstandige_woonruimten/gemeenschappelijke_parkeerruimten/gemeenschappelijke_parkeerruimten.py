import warnings
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import bereken
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
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
            "Type III": Decimal("4.0")
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

    @staticmethod
    def genereer_woningwaarderingen(
        ruimte: EenhedenRuimte,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering] | None:
        if ruimte.detail_soort is None:
            warnings.warn(
                f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen 'detail_soort'."
            )
            return None
        if ruimte.detail_soort.code is None:
            warnings.warn(
                f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen 'code' in 'detail_soort'."
            )
            return None

        if ruimte.detail_soort.code in [
            Ruimtedetailsoort.parkeervak_motorfiets_binnen.code,
            Ruimtedetailsoort.parkeervak_scootmobiel_binnen.code,
            Ruimtedetailsoort.stalling_extern.code,
            Ruimtedetailsoort.stalling_intern.code,
            Ruimtedetailsoort.parkeervak_motorfiets_buiten_niet_overdekt.code,
            Ruimtedetailsoort.parkeervak_scootmobiel_buiten.code,
        ]:
            logger.info(
                f"Ruimte {ruimte.naam} ({ruimte.id}) met ruimtedetailsoort {ruimte.detail_soort.code} is een parkeerplek die niet gewaardeerd wordt in het woningwaardering stelsel volgens het beleidsboek."
            )
            return None

        if ruimte.detail_soort.code in [
            Ruimtedetailsoort.parkeerterrein.code,
            Ruimtedetailsoort.parkeergarage.code,
        ]:
            logger.warning(
                f"Ruimte {ruimte.naam} ({ruimte.id}) is een {Ruimtedetailsoort.parkeerterrein.naam if ruimte.detail_soort.code==Ruimtedetailsoort.parkeerterrein.code else Ruimtedetailsoort.parkeergarage.naam} en kan momenteel niet gewaardeerd worden in de woningwaardering package. Voeg een parkeerplek los toe aan de eenheden om deze in aanmerking te laten komen voor een waardering onder {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}. Raadpleeg docs/implementatietoelichting-beleidsboeken/zelfstandige_woonruimten.md voor meer informatie."
            )
            return None

        if ruimte.detail_soort.code not in [
            Ruimtedetailsoort.parkeervak_auto_binnen.code,
            Ruimtedetailsoort.carport.code,
            Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt.code,
        ]:
            logger.info(
                f"Ruimte {ruimte.naam} ({ruimte.id}) is geen gemeenschappelijke parkeerruimte en wordt niet gewaardeerd onder rubriek {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}."
            )
            return None

        if ruimte.oppervlakte is None:
            warnings.warn(
                f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen 'oppervlakte'."
            )
            return None

        if ruimte.gedeeld_met_aantal_eenheden is None:
            warnings.warn(
                f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen 'gedeeld_met_aantal_eenheden'. Zet 'gedeeld_met_aantal_eenheden' >= 2 wanneer de ruimte gedeeld is. 'gedeeld_met_aantal_eenheden' op 0 of 1 wordt beschouwd als niet gedeeld."
            )
            return None

        if not ruimte.oppervlakte >= 12.0:
            logger.info(
                f"Ruimte {ruimte.naam} ({ruimte.id}) voldoet niet aan de eis van 12m2 voor een parkeervak."
            )
            return None

        for (
            type_parkeeruimte,
            punten,
        ) in GemeenschappelijkeParkeerruimten.parkeertype_punten_mapping[
            ruimte.detail_soort.code
        ].items():
            criterium = f"{type_parkeeruimte}"

            if heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.laadpaal):
                punten += Decimal("2.0")
                criterium += " + laadpaal"

            if ruimte.gedeeld_met_aantal_eenheden >= 2:
                criterium += (
                    f" (gedeeld met {ruimte.gedeeld_met_aantal_eenheden} adressen)"
                )
                totaal_punten_type_parkeeruimte = (
                    punten * Decimal(str(ruimte.aantal))
                ) / Decimal(str(ruimte.gedeeld_met_aantal_eenheden))
            else:
                criterium += " (privé)"
                totaal_punten_type_parkeeruimte = (
                    punten * Decimal(str(ruimte.aantal)) / Decimal("1")
                )

            logger.info(
                f"Ruimte {ruimte.naam} ({ruimte.id}) is een gemeenschappelijke parkeerruimte '{criterium}'."
            )

            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=criterium,
                ),
                aantal=ruimte.aantal,
                punten=utils.rond_af(totaal_punten_type_parkeeruimte, decimalen=2),
            )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
        | None = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.value,
            )
        )
        woningwaardering_groep.woningwaarderingen = []

        if eenheid.ruimten is None:
            warnings.warn(f"Eenheid {eenheid.id} heeft geen 'ruimten'.")
            return woningwaardering_groep

        for ruimte in eenheid.ruimten:
            woningwaardering = (
                GemeenschappelijkeParkeerruimten.genereer_woningwaarderingen(ruimte)
            )
            if woningwaardering is not None:
                woningwaardering_groep.woningwaarderingen.extend(list(woningwaardering))

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
            f"Eenheid {eenheid.id} wordt gewaardeerd met {punten_totaal} punten voor stelselgroep {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}"
        )

        woningwaardering_groep.punten = punten_totaal

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    bereken(
        instance=GemeenschappelijkeParkeerruimten(),
        eenheid_input="tests/data/generiek/input/37101000032.json",
        strict=False,
    )
