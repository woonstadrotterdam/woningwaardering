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

        keuken_gevonden = False

        for ruimte in eenheid.ruimten or []:
            if not (
                ruimte.detail_soort
                and ruimte.detail_soort.code == Ruimtedetailsoort.keuken.code
                and ruimte.bouwkundige_elementen
            ):
                continue

            for bouwkundig_element in ruimte.bouwkundige_elementen:
                if (
                    bouwkundig_element.detail_soort
                    and bouwkundig_element.detail_soort.code
                    and bouwkundig_element.detail_soort.code
                    == Bouwkundigelementdetailsoort.aanrecht.code
                    and bouwkundig_element.lengte
                ):
                    logger.debug(
                        f"Ruimte {ruimte.id} is een keuken met aanrecht en komt in aanmerking voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
                    )

                    if not keuken_gevonden:
                        keuken_gevonden = True

                    if bouwkundig_element.lengte < 1000:
                        punten = 0.0
                    if bouwkundig_element.lengte >= 2000:
                        punten = 7.0
                    else:
                        punten = 4.0

                    logger.debug(
                        f"Ruimte {ruimte.id} is een keuken met aanrecht lengte {bouwkundig_element.lengte} millimeter en krijgt {punten} punten voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
                    )

                    woningwaardering_groep.woningwaarderingen.append(
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam="Lengte aanrecht",
                                meeteenheid=Meeteenheid.millimeter.value,
                            ),
                            aantal=bouwkundig_element.lengte,
                            punten=punten,
                        )
                    )

        if not keuken_gevonden:
            logger.warning(
                f"Kan geen punten geven voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}: Geen keuken met aanrecht gevonden voor eenheid {eenheid.id}"
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
        "tests/data/input/zelfstandige_woonruimten/12006000004.json",
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
