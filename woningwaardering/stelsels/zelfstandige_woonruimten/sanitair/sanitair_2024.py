from decimal import Decimal
from typing import List

from loguru import logger

from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
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
    Bouwkundigelementdetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import (
    aantal_bouwkundige_elementen,
)


class Sanitair2024(Stelselgroepversie):
    @staticmethod
    def _waardeer_bouwkundig_element_detailsoort(
        woningwaarderingen: List[WoningwaarderingResultatenWoningwaardering],
        ruimte: EenhedenRuimte,
        punten_per_element: float,
        *elementdetailsoort: Bouwkundigelementdetailsoort,
    ) -> bool:
        """
        Berekent de punten voor een specifiek type bouwkundig element detail.

        Args:
            woningwaarderingen (List[WoningwaarderingResultatenWoningwaardering]): Een list met woningwaarderingen.
            ruimte (EenhedenRuimte): Een instantie van de klasse EenhedenRuimte die de ruimte vertegenwoordigt.
            *elementdetailsoort (Bouwkundigelementdetailsoort): Een instantie van de klasse Bouwkundigelementdetailsoort die het element detailsoort vertegenwoordigt.
            punten_per_element (float): Het aantal punten dat aan elk element wordt toegekend.
        Returns:
            bool: True wanneer er punten gewaardeerd zijn
        """
        aantal = aantal_bouwkundige_elementen(ruimte, *elementdetailsoort)
        if aantal > 0:
            soorten = " en ".join(
                detailsoort.naam
                for detailsoort in elementdetailsoort
                if detailsoort.naam is not None
            )

            logger.debug(f"Aantal '{soorten}' in {ruimte.naam}: {aantal}")

            naam = soorten
            if len(elementdetailsoort) > 1:
                naam += " in zelfde ruimte"

            woningwaardering = next(
                (
                    woningwaardering
                    for woningwaardering in woningwaarderingen
                    if woningwaardering.criterium is not None
                    and woningwaardering.criterium.naam == naam
                ),
                None,
            )

            if woningwaardering is None:
                woningwaardering = WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=naam
                    )
                )
                woningwaarderingen.append(woningwaardering)

            woningwaardering.punten = (
                woningwaardering.punten or 0.0
            ) + punten_per_element * aantal
            woningwaardering.aantal = (woningwaardering.aantal or 0.0) + aantal

            return True
        else:
            return False

    @staticmethod
    def bereken(
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.sanitair.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        for ruimte in eenheid.ruimten or []:
            Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                3,
                Bouwkundigelementdetailsoort.closetcombinatie,
            )
            Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                1,
                Bouwkundigelementdetailsoort.wastafel,
            )
            Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                1,
                Bouwkundigelementdetailsoort.bidet,
            )
            Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                1,
                Bouwkundigelementdetailsoort.lavet,
            )

            if not Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                7,
                Bouwkundigelementdetailsoort.bad,
                Bouwkundigelementdetailsoort.douche,
            ):
                Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                    woningwaardering_groep.woningwaarderingen,
                    ruimte,
                    6,
                    Bouwkundigelementdetailsoort.bad,
                )

                Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                    woningwaardering_groep.woningwaarderingen,
                    ruimte,
                    4,
                    Bouwkundigelementdetailsoort.douche,
                )

        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep
