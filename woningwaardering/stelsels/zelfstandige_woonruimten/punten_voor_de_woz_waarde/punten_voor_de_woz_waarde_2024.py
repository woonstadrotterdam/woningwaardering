from decimal import ROUND_HALF_UP, Decimal
from datetime import date

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

        if not woningwaardering_resultaat:
            raise ValueError("Geen woningwaardering resultaat gevonden")

        if not eenheid.bouwjaar:
            logger.warning(f"Geen bouwjaar gevonden voor eenheid {eenheid.id}")

        minimum_punten = self._bereken_minimum_punten(
            eenheid.bouwjaar, woningwaardering_resultaat
        )
        woz_waarde = self.bepaal_woz_waarde(eenheid)

        woningwaardering_groep.woningwaarderingen = []
        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Onderdeel I"
                ),
                punten=woz_waarde / 14146.0,
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
        bouwjaar: int | None,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> float:
        """
        Berekent de minimum punten voor steselgroep WOZ-waarde.

        Args:
            eenheid (EenhedenEenheid): De eenheid waarvoor de punten worden berekend.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten

        Returns:
            float: De minimum punten voor stelselgroep WOZ-waarde.
        """

        minimum_punten = 0

        if bouwjaar:
            if 2015 <= bouwjaar <= 2019:
                punten_critische_stelselgroepen = sum(
                    groep.punten or 0
                    for groep in woningwaardering_resultaat.groepen or []
                    if groep.punten
                    and groep.criterium_groep
                    and groep.criterium_groep.stelselgroep
                    and groep.criterium_groep.stelselgroep.code
                    and groep.criterium_groep.stelselgroep.code
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
                )

                if punten_critische_stelselgroepen >= 110:
                    minimum_punten = 40

        return minimum_punten

    def bepaal_woz_waarde(self, eenheid: EenhedenEenheid) -> float:
        woz_waardepeildatum = date(self.peildatum.year - 1, 1, 1)

        woz_eenheid = next(
            (
                woz_eenheid
                for woz_eenheid in eenheid.woz_eenheden or []
                if woz_eenheid.waardepeildatum == woz_waardepeildatum
            ),
            None,
        )

        if woz_eenheid is None or woz_eenheid.vastgestelde_waarde is None:
            raise ValueError(
                f"Geen WOZ-waarde gevonden met waardepeildatum: {woz_waardepeildatum}"
            )

        logger.info(
            f"WOZ-waarde gevonden met waardepeildatum {woz_waardepeildatum}: {woz_eenheid.vastgestelde_waarde}"
        )

        return woz_eenheid.vastgestelde_waarde


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
