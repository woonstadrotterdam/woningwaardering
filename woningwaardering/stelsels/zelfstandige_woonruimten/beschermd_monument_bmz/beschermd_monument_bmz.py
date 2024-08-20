import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
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
from woningwaardering.vera.referentiedata.eenheidmonument import Eenheidmonument


class BeschermdMonumentBmz(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            begindatum=date(2024, 1, 1),
            einddatum=date(2024, 6, 30),
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.beschermd_monument_bmz

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
                stelselgroep=Woningwaarderingstelselgroep.beschermd_monument_bmz.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        if eenheid.monumenten is None:
            warnings.warn(f"Eenheid {eenheid.id}: Monumenten is None.", UserWarning)
            logger.info(
                f"Eenheid {eenheid.id}: De api van cultureelerfgoed wordt geraadpleegd voor monumenten."
            )

            utils.update_eenheid_monumenten(eenheid)

        if any(
            monument.code == Eenheidmonument.rijksmonument.code
            for monument in eenheid.monumenten or []
        ):
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=Eenheidmonument.rijksmonument.naam,
                    ),
                    punten=50.0,
                )
            )

        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.beschermd_monument_bmz.naam}."
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")
    warnings.simplefilter("default", UserWarning)
    beschermd_monument_bmz = BeschermdMonumentBmz(peildatum=date(2024, 5, 1))
    with open("tests/data/generiek/input/37101000032.json", "r+") as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

        woningwaardering_resultaat = beschermd_monument_bmz.bereken(eenheid)

        print(
            woningwaardering_resultaat.model_dump_json(
                by_alias=True, indent=2, exclude_none=True
            )
        )

        tabel = utils.naar_tabel(woningwaardering_resultaat)

        print(tabel)
