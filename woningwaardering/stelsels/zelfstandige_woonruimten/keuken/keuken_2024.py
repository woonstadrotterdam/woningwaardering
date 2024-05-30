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

        keukens = set()

        for ruimte in eenheid.ruimten or []:
            if not ruimte.detail_soort:
                logger.warning(f"Ruimte {ruimte.id} heeft geen detail_soort.")
                continue

            if ruimte.detail_soort.code not in [
                Ruimtedetailsoort.keuken.code,
                Ruimtedetailsoort.woonkamer_en_of_keuken.code,
                Ruimtedetailsoort.woonkamer.code,
                Ruimtedetailsoort.woon_en_of_slaapkamer.code,
                Ruimtedetailsoort.slaapkamer.code,
            ]:
                continue
            if ruimte.bouwkundige_elementen:
                for bouwkundig_element in ruimte.bouwkundige_elementen:
                    if not bouwkundig_element.detail_soort:
                        logger.warning(
                            f"Bouwkundig element in ruimte {ruimte.id} heeft geen detail_soort."
                        )
                        continue

                    if (
                        bouwkundig_element.detail_soort.code
                        == Bouwkundigelementdetailsoort.aanrecht.code
                    ):
                        keukens.add(ruimte.id)
                        if not bouwkundig_element.lengte:
                            logger.warning(
                                f"Aanrecht in ruimte {ruimte.id} heeft geen lengte."
                            )
                            continue

                        logger.debug(
                            f"Ruimte {ruimte.id} is een keuken met aanrecht en komt in aanmerking voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
                        )
                        if bouwkundig_element.lengte:
                            if bouwkundig_element.lengte < 1000:
                                punten = 0.0
                            elif bouwkundig_element.lengte >= 2000:
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

                    elif ruimte.detail_soort in [
                        Ruimtedetailsoort.keuken.code,
                        Ruimtedetailsoort.woonkamer_en_of_keuken.code,
                    ]:
                        keukens.add(ruimte.id)
                        logger.warning(
                            f"Ruimte {ruimte.id} is een (open) keuken zonder aanrecht."
                        )
                        continue

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
