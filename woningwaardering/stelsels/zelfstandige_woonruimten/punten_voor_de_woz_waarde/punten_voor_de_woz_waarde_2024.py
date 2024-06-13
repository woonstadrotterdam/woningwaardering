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


class PuntenVoorDeWozWaarde2024(Stelselgroepversie):
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
                stelselgroep=Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.value,
            )
        )

        minimum_punten = self._bereken_minimum_punten(
            eenheid, woningwaardering_resultaat
        )

        woningwaardering_groep.woningwaarderingen = []
        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="NotImplemented"
                )
            )
        )

        punten = max(
            minimum_punten,
            float(
                Decimal(
                    sum(
                        Decimal(str(woningwaardering.punten))
                        for woningwaardering in woningwaardering_groep.woningwaarderingen
                        or []
                        if woningwaardering.punten is not None
                    )
                ).quantize(Decimal("1"), ROUND_HALF_UP)
                * Decimal("1")
            ),
        )

        woningwaardering_groep.punten = punten
        return woningwaardering_groep

    def _bereken_minimum_punten(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> float:
        """
        Berekent de minimum punten voor steselgroep WOZ-waarde.

        Args:
            eenheid (EenhedenEenheid): De eenheid waarvoor de punten worden berekend.

        Returns:
            float: De minimum punten voor stelselgroep WOZ-waarde.
        """

        minimum_punten = 0

        if 2015 <= eenheid.bouwjaar <= 2019:
            punten_critische_stelselgroepen = (
                Decimal(
                    sum(
                        Decimal(str(groep.punten))
                        for groep in woningwaardering_resultaat.groepen
                        if groep.criterium_groep.stelselgroep.code
                        in [
                            Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.code,
                            Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.code,
                            Woningwaarderingstelselgroep.verwarming.code,
                            Woningwaarderingstelselgroep.energieprestatie.code,
                            Woningwaarderingstelselgroep.keuken.code,
                            Woningwaarderingstelselgroep.sanitair.code,
                            Woningwaarderingstelselgroep.woonvoorzieningen_voor_gehandicapten.code,
                            Woningwaarderingstelselgroep.prive_buitenruimten.code,
                            Woningwaarderingstelselgroep.bijzondere_voorzieningen.code,  # Zorgwoning
                        ]
                        if groep.punten is not None
                    )
                ).quantize(Decimal("1"), ROUND_HALF_UP)
                * Decimal("1")
            )

            if punten_critische_stelselgroepen >= 110:
                minimum_punten = 40

        return minimum_punten


if __name__ == "__main__":
    logger.enable("woningwaardering")

    woz = PuntenVoorDeWozWaarde2024()
    with open(
        "tests/data/zelfstandige_woonruimten/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = woz.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = naar_tabel(woningwaardering_resultaat)

    print(tabel)
