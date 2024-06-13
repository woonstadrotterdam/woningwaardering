from decimal import ROUND_HALF_UP, Decimal
from datetime import date

from loguru import logger


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

        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        ).quantize(Decimal("1"), ROUND_HALF_UP) * Decimal("1")

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep

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
