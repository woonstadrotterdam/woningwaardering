from collections import defaultdict
from decimal import ROUND_HALF_UP, Decimal

from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
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
from woningwaardering.vera.utils import heeft_bouwkundig_element


class Sanitair2024(Stelselgroepversie):
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
            if heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.closetcombinatie.code
            ):
                totals[Bouwkundigelementdetailsoort.closetcombinatie.naam][
                    "punten"
                ] += Decimal("3")
                totals[Bouwkundigelementdetailsoort.closetcombinatie.naam][
                    "aantal"
                ] += 1

            if heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.wastafel.code
            ):
                totals[Bouwkundigelementdetailsoort.wastafel.naam]["punten"] += Decimal(
                    "1"
                )
                totals[Bouwkundigelementdetailsoort.wastafel.naam]["aantal"] += 1

            if heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.bidet.code
            ):
                totals[Bouwkundigelementdetailsoort.bidet.naam]["punten"] += Decimal(
                    "1"
                )
                totals[Bouwkundigelementdetailsoort.bidet.naam]["aantal"] += 1

            if heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.lavet.code
            ):
                totals[Bouwkundigelementdetailsoort.lavet.naam]["punten"] += Decimal(
                    "1"
                )
                totals[Bouwkundigelementdetailsoort.lavet.naam]["aantal"] += 1

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
