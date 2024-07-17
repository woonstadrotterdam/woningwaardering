from decimal import Decimal
import warnings

from loguru import logger


from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import update_eenheid_monumenten
from woningwaardering.vera.referentiedata.eenheidmonument import Eenheidmonument
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


class BeschermdMonumentBmzJan2024(Stelselgroepversie):
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

            update_eenheid_monumenten(eenheid)

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
