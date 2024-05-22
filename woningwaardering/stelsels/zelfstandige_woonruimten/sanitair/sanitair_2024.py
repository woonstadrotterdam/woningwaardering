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
    heeft_bouwkundig_element,
)


class Sanitair2024(Stelselgroepversie):
    @staticmethod
    def _waardeer_bouwkundig_element_detailsoort(
        woningwaarderingen: List[WoningwaarderingResultatenWoningwaardering],
        ruimte: EenhedenRuimte,
        elementdetailsoort: Bouwkundigelementdetailsoort,
        punten_per_element: float,
    ) -> None:
        """
        Berekent de punten voor een specifiek type bouwkundig element detail.

        Args:
            woningwaarderingen (List[WoningwaarderingResultatenWoningwaardering]): Een list met woningwaarderingen.
            ruimte (EenhedenRuimte): Een instantie van de klasse EenhedenRuimte die de ruimte vertegenwoordigt.
            elementdetailsoort (Bouwkundigelementdetailsoort): Een instantie van de klasse Bouwkundigelementdetailsoort die het element detailsoort vertegenwoordigt.
            punten_per_element (float): Het aantal punten dat aan elk element wordt toegekend.
        """
        aantal = aantal_bouwkundige_elementen(ruimte, elementdetailsoort)
        if aantal > 0:
            logger.debug(
                f"Aantal '{elementdetailsoort.naam}' in {ruimte.naam}: {aantal}"
            )

            woningwaardering = next(
                (
                    woningwaardering
                    for woningwaardering in woningwaarderingen
                    if woningwaardering.criterium is not None
                    and woningwaardering.criterium.naam == elementdetailsoort.naam
                ),
                None,
            )

            if woningwaardering is None:
                woningwaardering = WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=elementdetailsoort.naam
                    )
                )
                woningwaarderingen.append(woningwaardering)

            woningwaardering.punten = (
                woningwaardering.punten or 0.0
            ) + punten_per_element * aantal
            woningwaardering.aantal = (woningwaardering.aantal or 0.0) + aantal

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
                Bouwkundigelementdetailsoort.closetcombinatie,
                3,
            )
            Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                Bouwkundigelementdetailsoort.wastafel,
                1,
            )
            Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                Bouwkundigelementdetailsoort.bidet,
                1,
            )
            Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                Bouwkundigelementdetailsoort.lavet,
                1,
            )

            # code voor bad en douche, of bad-douche in zelfde ruimte
            bad_en_douche = heeft_bouwkundig_element(
                ruimte,
                Bouwkundigelementdetailsoort.bad,
                Bouwkundigelementdetailsoort.douche,
            )

            if bad_en_douche:
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"{Bouwkundigelementdetailsoort.bad.naam} en {Bouwkundigelementdetailsoort.douche.naam} in zelfde ruimte"
                        ),
                        punten=Decimal("7"),
                        aantal=1,
                    )
                )

            else:
                Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                    woningwaardering_groep.woningwaarderingen,
                    ruimte,
                    Bouwkundigelementdetailsoort.bad,
                    6,
                )

                Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                    woningwaardering_groep.woningwaarderingen,
                    ruimte,
                    Bouwkundigelementdetailsoort.douche,
                    4,
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
