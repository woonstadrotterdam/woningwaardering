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

        geldige_ruimtes = [
            ruimte
            for ruimte in eenheid.ruimten or []
            # check of een ruimte behoort tot te ruimtesoorten die in aanmerking komen voor de stelselgroep keuken
            if ruimte.detail_soort
            and (
                ruimte.detail_soort.code
                in [
                    Ruimtedetailsoort.keuken.code,
                    Ruimtedetailsoort.woonkamer_en_of_keuken.code,
                    Ruimtedetailsoort.woonkamer.code,
                    Ruimtedetailsoort.woon_en_of_slaapkamer.code,
                    Ruimtedetailsoort.slaapkamer.code,
                ]
            )
        ]

        if not geldige_ruimtes:
            logger.warning(
                f"Kan geen punten geven voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}: Geen geldige ruimte detailsoort gevonden in eenheid {eenheid.id}."
                f"Geldige ruimtedetailsoorten: {Ruimtedetailsoort.keuken.naam}, {Ruimtedetailsoort.woonkamer_en_of_keuken.naam}, {Ruimtedetailsoort.woonkamer.naam}, {Ruimtedetailsoort.woon_en_of_slaapkamer.naam} {Ruimtedetailsoort.slaapkamer.naam}."
            )
            return woningwaardering_groep

        ruimten_met_aanrecht = [
            (ruimte, bouwkundig_element)
            for ruimte in geldige_ruimtes
            # check of de ruimte een aanrecht heeft
            if ruimte.bouwkundige_elementen
            for bouwkundig_element in ruimte.bouwkundige_elementen
            if bouwkundig_element.detail_soort
            and bouwkundig_element.detail_soort.code
            == Bouwkundigelementdetailsoort.aanrecht.code
        ]

        if not ruimten_met_aanrecht:
            logger.warning(
                f"Kan geen punten geven voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}: Geen ruimte met een {Bouwkundigelementdetailsoort.aanrecht.naam} gevonden voor eenheid {eenheid.id}"
            )
            return woningwaardering_groep

        if ruimten_met_aanrecht:
            ruimten_met_aanrecht_lengte = [
                ruimte
                for ruimte in ruimten_met_aanrecht
                if ruimte.bouwkundige_elementen
                # Check of de aanrechten een lengte hebben
                for aanrecht in ruimte.bouwkundige_elementen
                if aanrecht.lengte
            ]

        if not ruimten_met_aanrecht_lengte:
            logger.warning(
                f"Kan geen punten geven voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}: Ruimte met een {Bouwkundigelementdetailsoort.aanrecht.naam} heeft geen  {Bouwkundigelementdetailsoort.aanrecht.naam}lengte voor eenheid {eenheid.id}"
            )
            return woningwaardering_groep

        for (ruimte, aanrecht) in ruimten_met_aanrecht_lengte:
            logger.debug(
                f"Ruimte {ruimte.id} is een {ruimte.detail_soort} met een {Bouwkundigelementdetailsoort.aanrecht.naam} van {aanrecht.lengte} {Meeteenheid.millimeter.value} en komt in aanmerking voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
            )
            if aanrecht.lengte:
                if aanrecht.lengte < 1000:
                    punten = 0.0
                elif aanrecht.lengte >= 2000:
                    punten = 7.0
                else:
                    punten = 4.0

                logger.info(
                    f"Ruimte {ruimte.naam} met aanrecht lengte {aanrecht.lengte} millimeter krijgt {punten} punten voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
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
