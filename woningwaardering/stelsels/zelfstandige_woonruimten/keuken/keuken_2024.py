from decimal import ROUND_HALF_UP, Decimal

from loguru import logger


from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import naar_tabel
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
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort


class Keuken2024(Stelselgroepversie):
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
                stelselgroep=Woningwaarderingstelselgroep.keuken.value,
            )
        )
        woningwaardering_groep.woningwaarderingen = []

        keukens = [
            ruimte
            for ruimte in eenheid.ruimten or []
            # check of een ruimte een keuken is
            if ruimte.detail_soort
            and ruimte.detail_soort.code == Ruimtedetailsoort.keuken.code
            # check of een keuken een aanrecht heeft
            and ruimte.bouwkundige_elementen
            for bouwkundig_element in ruimte.bouwkundige_elementen
            if bouwkundig_element.detail_soort
            and bouwkundig_element.detail_soort.code
            == Bouwkundigelementdetailsoort.aanrecht.code
            # check of een aanrecht een lengte heeft
            and bouwkundig_element.lengte
        ]

        if keukens:
            for keuken in keukens:
                for aanrecht in keuken.bouwkundige_elementen or []:
                    logger.debug(
                        f"Ruimte {keuken.id} is een keuken met aanrecht en komt in aanmerking voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
                    )
                    if aanrecht.lengte:
                        if aanrecht.lengte < 1000:
                            punten = 0.0
                        elif aanrecht.lengte >= 2000:
                            punten = 7.0
                        else:
                            punten = 4.0

                        logger.debug(
                            f"Ruimte {keuken.id} is een keuken met aanrecht lengte {aanrecht.lengte} millimeter en krijgt {punten} punten voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
                        )

                        woningwaardering_groep.woningwaarderingen.append(
                            WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam="Lengte aanrecht",
                                    meeteenheid=Meeteenheid.millimeter.value,
                                ),
                                aantal=aanrecht.lengte,
                                punten=punten,
                            )
                        )

        else:
            logger.warning(
                f"Kan geen punten geven voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}: Geen keuken, aanrecht of aanrechtlengte gevonden voor eenheid {eenheid.id}"
            )

        totaal_punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        ).quantize(Decimal("1"), ROUND_HALF_UP) * Decimal("1")
        woningwaardering_groep.punten = float(totaal_punten)
        return woningwaardering_groep


if __name__ == "__main__":
    logger.enable("woningwaardering")

    file = open(
        "tests/stelsels/zelfstandige_woonruimten/keuken/data/input/aanrecht_zonder_lengte.json",
        "r+",
    )
    eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = Keuken2024.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = naar_tabel(woningwaardering_resultaat)

    print(tabel)
