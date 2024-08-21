from datetime import date
from decimal import Decimal
from typing import List, Optional

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
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
from woningwaardering.vera.utils import aantal_bouwkundige_elementen


class Sanitair(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        raise NotImplementedError(
            "De stelselgroep Sanitair is nog niet geïmplementeerd."
        )
        super().__init__(
            begindatum=date(2024, 1, 1),
            einddatum=date(2024, 6, 30),
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.sanitair

    @staticmethod
    def _waardeer_bouwkundig_element_detailsoort(
        woningwaarderingen: List[WoningwaarderingResultatenWoningwaardering],
        ruimte: EenhedenRuimte,
        punten_per_element: float,
        gedeeld_met_aantal_eenheden: Optional[int] = None,
        *elementdetailsoort: Bouwkundigelementdetailsoort,
    ) -> bool:
        """
        Berekent de punten voor een specifiek type bouwkundig element detail.

        Args:
            woningwaarderingen (List[WoningwaarderingResultatenWoningwaardering]): Een list met woningwaarderingen.
            ruimte (EenhedenRuimte): Een instantie van de klasse EenhedenRuimte die de ruimte vertegenwoordigt.
            punten_per_element (float): Het aantal punten dat aan elk element wordt toegekend.
            gedeeld_met_aantal_eenheden (Optional[int]): Het aantal eenheden waarmee de ruimte waarin de bouwkundig element zich bevindt gedeeld wordt. Defaults to None.
            *elementdetailsoort (Bouwkundigelementdetailsoort): Een instantie van de klasse Bouwkundigelementdetailsoort die het element detailsoort vertegenwoordigt.

        Returns:
            bool: True wanneer er punten gewaardeerd zijn
        """
        aantal = aantal_bouwkundige_elementen(ruimte, *elementdetailsoort)
        gedeelde_ruimte = (
            ruimte.gedeeld_met_aantal_eenheden
            and ruimte.gedeeld_met_aantal_eenheden >= 2
        )
        if aantal > 0:
            soorten = " en ".join(
                detailsoort.naam
                for detailsoort in elementdetailsoort
                if detailsoort.naam is not None
            )

            logger.debug(
                f"Ruimte {ruimte.naam} ({ruimte.id}): {aantal} aantal '{soorten}'"
            )

            naam = (
                soorten
                if not gedeelde_ruimte
                else f"{soorten} (gedeeld met {ruimte.gedeeld_met_aantal_eenheden})"
            )
            if len(elementdetailsoort) > 1:
                naam += " in zelfde ruimte"

            woningwaardering = next(
                (
                    woningwaardering
                    for woningwaardering in woningwaarderingen
                    if woningwaardering.criterium is not None
                    and woningwaardering.criterium.naam == naam
                ),
                None,
            )

            if woningwaardering is None:
                woningwaardering = WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=naam
                    )
                )
                woningwaarderingen.append(woningwaardering)

            woningwaardering.punten = float(
                utils.rond_af(
                    (woningwaardering.punten or 0.0)
                    + (
                        punten_per_element
                        * aantal
                        / (ruimte.gedeeld_met_aantal_eenheden or 1)
                    ),
                    decimalen=2,
                )
            )

            woningwaardering.aantal = float(
                utils.rond_af(
                    (woningwaardering.aantal or 0.0) + aantal,
                    decimalen=2,
                )
            )

            return True
        else:
            return False

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
                stelselgroep=Woningwaarderingstelselgroep.sanitair.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        for ruimte in eenheid.ruimten or []:
            Sanitair._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                3,
                ruimte.gedeeld_met_aantal_eenheden,
                Bouwkundigelementdetailsoort.closetcombinatie,
            )
            Sanitair._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                1,
                ruimte.gedeeld_met_aantal_eenheden,
                Bouwkundigelementdetailsoort.wastafel,
            )
            Sanitair._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                1,
                ruimte.gedeeld_met_aantal_eenheden,
                Bouwkundigelementdetailsoort.bidet,
            )
            Sanitair._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                1,
                ruimte.gedeeld_met_aantal_eenheden,
                Bouwkundigelementdetailsoort.lavet,
            )

            if not Sanitair._waardeer_bouwkundig_element_detailsoort(
                woningwaardering_groep.woningwaarderingen,
                ruimte,
                7,
                ruimte.gedeeld_met_aantal_eenheden,
                Bouwkundigelementdetailsoort.bad,
                Bouwkundigelementdetailsoort.douche,
            ):
                Sanitair._waardeer_bouwkundig_element_detailsoort(
                    woningwaardering_groep.woningwaarderingen,
                    ruimte,
                    6,
                    ruimte.gedeeld_met_aantal_eenheden,
                    Bouwkundigelementdetailsoort.bad,
                )

                Sanitair._waardeer_bouwkundig_element_detailsoort(
                    woningwaardering_groep.woningwaarderingen,
                    ruimte,
                    4,
                    ruimte.gedeeld_met_aantal_eenheden,
                    Bouwkundigelementdetailsoort.douche,
                )

        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    sanitair = Sanitair()
    with open("tests/data/generiek/input/37101000032.json", "r+") as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = sanitair.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
