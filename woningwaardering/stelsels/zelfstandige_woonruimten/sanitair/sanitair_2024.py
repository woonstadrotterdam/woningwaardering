from decimal import ROUND_HALF_UP, Decimal
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
        element: Bouwkundigelementdetailsoort,
        punten_per_element: float,
    ) -> None:
        """
        Berekent de punten voor een specifiek type bouwkundig element detail.

        Args:
            woningwaarderingen (List[WoningwaarderingResultatenWoningwaardering]): Een list met woningwaarderingen.
            ruimte (EenhedenRuimte): Een instantie van de klasse EenhedenRuimte die de ruimte vertegenwoordigt.
            element (Bouwkundigelementdetailsoort): Een instantie van de klasse Bouwkundigelementdetailsoort die het element detailsoort vertegenwoordigt.
            punten_per_element (float): Het aantal punten dat aan elk element wordt toegekend.
        """
        aantal = aantal_bouwkundige_elementen(ruimte, element.code)
        if aantal > 0:
            logger.debug(f"Aantal '{element.naam}' in {ruimte.naam}: {aantal}")

            for woningwaardering in woningwaarderingen:
                if woningwaardering.criterium is None:
                    raise TypeError("Woningwaardering criterium is None")
                if woningwaardering.criterium.naam == element.naam:
                    if woningwaardering.punten is None:
                        woningwaardering.punten = 0.0
                    logger.debug(f"{woningwaardering.punten = }")
                    woningwaardering.punten += punten_per_element * aantal
                    if woningwaardering.aantal is None:
                        woningwaardering.aantal = 0.0
                    woningwaardering.aantal += aantal
                    break
            else:
                woningwaardering = WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=element.naam
                    ),
                    punten=Decimal(punten_per_element) * aantal,
                    aantal=aantal,
                )
                woningwaarderingen.append(woningwaardering)

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
            bad_aanwezig = heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.bad.code
            )
            douche_aanwezig = heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.douche.code
            )
            if bad_aanwezig and douche_aanwezig:
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"{Bouwkundigelementdetailsoort.bad.naam} en {Bouwkundigelementdetailsoort.douche.naam} in zelfde ruimte"
                        ),
                        punten=Decimal("7"),
                        aantal=1,
                    )
                )

            elif bad_aanwezig:
                Sanitair2024._waardeer_bouwkundig_element_detailsoort(
                    woningwaardering_groep.woningwaarderingen,
                    ruimte,
                    Bouwkundigelementdetailsoort.bad,
                    6,
                )

            elif douche_aanwezig:
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
        ).quantize(Decimal("1"), ROUND_HALF_UP) * Decimal("1")

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep
