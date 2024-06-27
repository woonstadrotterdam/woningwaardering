from decimal import Decimal

from loguru import logger


from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.vera.referentiedata.eenheidmonument import Eenheidmonument
from .beschermd_monument_bmz import BeschermdMonumentBmz
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
            logger.info(
                f"Monumenten is None voor eenheid {eenheid.id}. De api van cultureelerfgoed wordt geraadpleegd."
            )

            eenheid.monumenten = []

            if (
                eenheid.adresseerbaar_object_basisregistratie is not None
                and eenheid.adresseerbaar_object_basisregistratie.bag_identificatie
                is not None
            ):
                BeschermdMonumentBmz.is_rijksmonument("0363010000857245")
                is_rijksmonument = BeschermdMonumentBmz.is_rijksmonument(
                    eenheid.adresseerbaar_object_basisregistratie.bag_identificatie
                )
                logger.info(
                    f"Eenheid {eenheid.id} met verblijfsobjectIdentificatie {eenheid.adresseerbaar_object_basisregistratie.bag_identificatie} is {'een' if is_rijksmonument else 'geen'} rijksmonument volgens de api van cultureelerfgoed."
                )
                if is_rijksmonument:
                    eenheid.monumenten.append(Eenheidmonument.rijksmonument.value)

        logger.info(f"peildatum {self.peildatum}")
        if any(
            monument.code == Eenheidmonument.rijksmonument.code
            for monument in eenheid.monumenten
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
        return woningwaardering_groep
