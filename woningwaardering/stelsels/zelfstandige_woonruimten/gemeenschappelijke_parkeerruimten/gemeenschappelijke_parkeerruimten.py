from datetime import date
from decimal import Decimal
from typing import Literal
import warnings

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import classificeer_ruimte
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
from woningwaardering.vera.utils import aantal_bouwkundige_elementen


class GemeenschappelijkeParkeerruimten(Stelselgroep):
    type_parkeerpunten = {
        "type_I": Decimal("9.0"),
        "type_II": Decimal("6.0"),
        "type_III": Decimal("3.0"),
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

        if eenheid.ruimten is None:
            warnings.warn(f"Eenheid {eenheid.id} heeft geen 'ruimten'")
            return woningwaardering_groep

        for ruimte in eenheid.ruimten:
            type_parkeerruimte = GemeenschappelijkeParkeerruimten.bepaal_type_gemeenschappelijke_parkeerruimten(
                ruimte
            )

            if type_parkeerruimte is not None:
                criterium = f"{type_parkeerruimte} gedeeld met {ruimte.gedeeld_met_aantal_eenheden} eenheden"

                punten_voor_deling = self.type_parkeerpunten[type_parkeerruimte]

                # TODO: what if parkeergarage/parkeerterrein met meedere laadpalen? worden deze laadpalen allemaal op de ruimte gezet?
                aantal_laadpaden = aantal_bouwkundige_elementen(
                    ruimte, Bouwkundigelementdetailsoort.laadpaal
                )

                punten_voor_deling += Decimal("2.0") * Decimal(str(aantal_laadpaden))

                if aantal_laadpaden > 0:
                    logger.info(
                        f"Ruimte {ruimte.id} heeft {aantal_laadpaden} laadpalen"
                    )
                    criterium += f" + {aantal_laadpaden} {'laadpalen' if aantal_laadpaden > 1 else 'laadpaal'}"

                punten: Decimal = utils.rond_af_op_kwart(
                    punten_voor_deling
                    / Decimal(str(ruimte.gedeeld_met_aantal_eenheden))
                )

                woningwaardering = WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=criterium
                    ),
                    punten=float(punten),
                )

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

            else:
                logger.info(
                    f"Ruimte {ruimte.id} is geen gedeelde parkeerruimte en komt niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}."
                )
                continue

        punten = utils.rond_af(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
            decimalen=0,
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}"
        )
        return woningwaardering_groep

    @staticmethod
    def bepaal_type_gemeenschappelijke_parkeerruimten(
        ruimte: EenhedenRuimte,
    ) -> Literal["type_I", "type_II", "type_III"] | None:
        if ruimte.oppervlakte is None:
            warnings.warn(f"Ruimte {ruimte.id} heeft geen 'oppervlakte'")
            return None

        if (
            classificeer_ruimte(ruimte) is None
            and ruimte.gedeeld_met_aantal_eenheden is not None
            and ruimte.gedeeld_met_aantal_eenheden > 1
        ):
            if ruimte.code in [
                Ruimtedetailsoort.parkeervak_auto_binnen.code,
                Ruimtedetailsoort.parkeervak_motorfiets_binnen.code,
                Ruimtedetailsoort.parkeervak_scootmobiel_binnen.code,
            ]:
                # Er is voor gekozen om een parkeervak_auto_binnen te toetsen op de oppervlakte eis van een parkeervak
                if ruimte.code == Ruimtedetailsoort.parkeervak_auto_binnen.code:
                    if not ruimte.oppervlakte >= 12.0:
                        logger.info(
                            f"Ruimte {ruimte.id} voldoet niet aan de eisen van 12m2 voor een parkeervakn"
                        )
                        return None

                logger.info(
                    f"Ruimte {ruimte.id} is een gemeenschappelijke parkeerruimte type_I"
                )
                return "type_I"
            elif ruimte.code in [
                Ruimtedetailsoort.carport.code,
                Ruimtedetailsoort.stalling_extern.code,
                Ruimtedetailsoort.stalling_intern.code,
            ]:
                # Er is voor gekozen om een carport te toetsen op de oppervlakte eis van een parkeervak
                if ruimte.code == Ruimtedetailsoort.carport.code:
                    if not ruimte.oppervlakte >= 12.0:
                        logger.info(
                            f"Ruimte {ruimte.id} voldoet niet aan de eisen van 12m2 voor een parkeervak"
                        )
                        return None

                logger.info(
                    f"Ruimte {ruimte.id} is een gemeenschappelijke parkeerruimte type_II"
                )
                return "type_II"

            elif ruimte.code in [
                Ruimtedetailsoort.parkeerterrein.code,
                Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt.code,
                Ruimtedetailsoort.parkeervak_motorfiets_buiten_niet_overdekt.code,
                Ruimtedetailsoort.parkeervak_scootmobiel_buiten.code,
            ]:
                logger.info(
                    f"Ruimte {ruimte.id} is een gemeenschappelijke parkeerruimte type_III"
                )
                return "type_III"

        return None


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
