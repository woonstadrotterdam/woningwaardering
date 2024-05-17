from collections import defaultdict
from decimal import ROUND_HALF_UP, Decimal

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
    def _punten_voor_bouwkundig_element_detailsoort(
        dict_: dict[str, dict[str, Decimal]],
        ruimte: EenhedenRuimte,
        element: Bouwkundigelementdetailsoort,
        punten_per_element: float,
    ) -> dict[str, dict[str, Decimal]]:
        """
        Berekent de punten voor een specifiek type bouwkundig element detail.

        Args:
            dict_ (dict[str, dict[str, Decimal]]): Een dictionary met de punten en het aantal elementen voor elk detailsoort.
            ruimte (EenhedenRuimte): Een instantie van de klasse EenhedenRuimte die de ruimte vertegenwoordigt.
            element (Bouwkundigelementdetailsoort): Een instantie van de klasse Bouwkundigelementdetailsoort die het element detailsoort vertegenwoordigt.
            punten_per_element (float): Het aantal punten dat aan elk element wordt toegekend.

        Returns:
            dict[str, dict[str, Decimal]]: Een dictionary met de bijgewerkte punten en het aantal elementen voor elk detailsoort.
        """

        aantal = aantal_bouwkundige_elementen(ruimte, element.code)
        if aantal > 0:
            logger.debug(f"Aantal '{element.naam}' in {ruimte.naam}: {aantal}")
            dict_[element.naam]["punten"] += Decimal(punten_per_element) * aantal
            dict_[element.naam]["aantal"] += aantal

        return dict_

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
        totals = defaultdict(lambda: {"punten": Decimal("0"), "aantal": 0})

        for ruimte in eenheid.ruimten or []:
            # closetcombinatie

            totals = Sanitair2024._punten_voor_bouwkundig_element_detailsoort(
                totals, ruimte, Bouwkundigelementdetailsoort.closetcombinatie, 3
            )
            totals = Sanitair2024._punten_voor_bouwkundig_element_detailsoort(
                totals, ruimte, Bouwkundigelementdetailsoort.wastafel, 1
            )
            totals = Sanitair2024._punten_voor_bouwkundig_element_detailsoort(
                totals, ruimte, Bouwkundigelementdetailsoort.bidet, 1
            )
            totals = Sanitair2024._punten_voor_bouwkundig_element_detailsoort(
                totals, ruimte, Bouwkundigelementdetailsoort.lavet, 1
            )

            # code voor bad en douche, of bad-douche in zelfde ruimte
            bad_aanwezig = heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.bad.code
            )
            douche_aanwezig = heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.douche.code
            )
            if bad_aanwezig and douche_aanwezig:
                totals[
                    f"{Bouwkundigelementdetailsoort.bad.naam} en {Bouwkundigelementdetailsoort.douche.naam} in zelfde ruimte"
                ]["punten"] += Decimal("7")
                totals[
                    f"{Bouwkundigelementdetailsoort.bad.naam} en {Bouwkundigelementdetailsoort.douche.naam} in zelfde ruimte"
                ]["aantal"] += 1

            elif bad_aanwezig:
                totals[Bouwkundigelementdetailsoort.bad.naam]["punten"] += Decimal("6")
                totals[Bouwkundigelementdetailsoort.bad.naam]["aantal"] += 1

            elif douche_aanwezig:
                totals[Bouwkundigelementdetailsoort.douche.naam]["punten"] += Decimal(
                    "4"
                )
                totals[Bouwkundigelementdetailsoort.douche.naam]["aantal"] += 1

        for naam, waarden in totals.items():
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=naam
                    ),
                    punten=waarden["punten"],
                    aantal=waarden["aantal"],
                )
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
