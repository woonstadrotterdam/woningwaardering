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
from woningwaardering.vera.utils import get_bouwkundige_elementen


class Keuken2024(Stelselgroepversie):
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
            keukens.add(ruimte.id)

            aanrechten = list(
                get_bouwkundige_elementen(ruimte, Bouwkundigelementdetailsoort.aanrecht)
            )

            if any(aanrechten):
                logger.debug(
                    f"Ruimte {ruimte.id} is een keuken met {Bouwkundigelementdetailsoort.aanrecht.naam} en komt in aanmerking voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
                )
            elif ruimte.detail_soort.code in [
                Ruimtedetailsoort.keuken.code,
                Ruimtedetailsoort.woonkamer_en_of_keuken.code,
            ]:
                logger.warning(
                    f"Ruimte {ruimte.id} is een (open) keuken zonder aanrecht."
                )
                continue

            for aanrecht in aanrechten:
                if not aanrecht.lengte:
                    logger.warning(
                        f"{Bouwkundigelementdetailsoort.aanrecht.naam} {aanrecht.id} in ruimte {ruimte.id} heeft geen lengte en kan daardoor niet gewaardeerd worden."
                    )
                    continue

                if aanrecht.lengte:
                    if aanrecht.lengte < 1000:
                        punten = 0.0
                    elif aanrecht.lengte >= 2000:
                        punten = 7.0
                    else:
                        punten = 4.0

                    logger.info(
                        f"Ruimte {ruimte.id} is een keuken met een aanrecht met lengte {aanrecht.lengte} millimeter en krijgt {punten} punten voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
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

        if not keukens:
            logger.warning(
                f"Geen keuken met aanrecht gevonden in eenheid {eenheid.id}."
            )
            return woningwaardering_groep

        totaal_punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        ).quantize(Decimal("1"), ROUND_HALF_UP) * Decimal("1")
        woningwaardering_groep.punten = float(totaal_punten)

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    keuken2024 = Keuken2024()
    with open(
        "tests/data/zelfstandige_woonruimten/stelselgroepen/keuken/input/aanrecht_zonder_lengte.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

        woningwaardering_resultaat = keuken2024.bereken(eenheid)

        print(
            woningwaardering_resultaat.model_dump_json(
                by_alias=True, indent=2, exclude_none=True
            )
        )

        tabel = naar_tabel(woningwaardering_resultaat)

        print(tabel)
