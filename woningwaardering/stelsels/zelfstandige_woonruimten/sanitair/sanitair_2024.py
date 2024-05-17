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
                totals["closetcombinatie"]["punten"] += Decimal("3")
                totals["closetcombinatie"]["aantal"] += 1

            if heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.wastafel.code
            ):
                totals["wastafel"]["punten"] += Decimal("1")
                totals["wastafel"]["aantal"] += 1

            if heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.bidet.code
            ):
                totals["bidet"]["punten"] += Decimal("1")
                totals["bidet"]["aantal"] += 1

            if heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.lavet.code
            ):
                totals["lavet"]["punten"] += Decimal("1")
                totals["lavet"]["aantal"] += 1

            # code voor bad en douche, of bad-douche in zelfde ruimte
            bad_aanwezig = heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.bad.code
            )
            douche_aanwezig = heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.douche.code
            )
            if bad_aanwezig and douche_aanwezig:
                totals["bad en douche in zelfde ruimte"]["punten"] += Decimal("7")
                totals["bad en douche in zelfde ruimte"]["aantal"] += 1

            elif bad_aanwezig:
                totals["bad"]["punten"] += Decimal("6")
                totals["bad"]["aantal"] += 1

            elif douche_aanwezig:
                totals["douche"]["punten"] += Decimal("4")
                totals["douche"]["aantal"] += 1

        for element, values in totals.items():
            naam = f"{element.capitalize()}"
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=naam
                    ),
                    punten=values["punten"],
                    aantal=values["aantal"],
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
