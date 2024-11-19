from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import bereken
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Voorzieningsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import (
    aantal_bouwkundige_elementen,
)


class BijzondereVoorzieningen(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.bijzondere_voorzieningen
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

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
                stelselgroep=Woningwaarderingstelselgroep.bijzondere_voorzieningen.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = list(
            self._genereer_woningwaarderingen(
                peildatum=self.peildatum,
                eenheid=eenheid,
                stelselgroepen_zonder_opslag=[
                    Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
                    self.stelselgroep,
                ],
                woningwaardering_resultaat=woningwaardering_resultaat,
            )
        )

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def _genereer_woningwaarderingen(
        peildatum: date,
        eenheid: EenhedenEenheid,
        stelselgroepen_zonder_opslag: list[Woningwaarderingstelselgroep],
        stelsel: Woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        # Als sprake is van een zorgwoning, dan wordt het puntentotaal van de rubrieken
        # 1 tot en met 11 (of 1 tot en met 10 voor onzelfstandige woonruimten) van het woningwaarderingsstelsel met 35% verhoogd. Dit
        # resulteert in een hogere maximale huurprijs.
        if (
            eenheid.doelgroep is not None
            and eenheid.doelgroep.code == Doelgroep.zorg.code
        ):
            if not woningwaardering_resultaat or not woningwaardering_resultaat.groepen:
                logger.warning(
                    "Geen woningwaardering resultaat gevonden: Woningwaarderingresultaat wordt aangemaakt"
                )
                if stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten:
                    from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
                        ZelfstandigeWoonruimten,
                    )

                    woningwaardering_resultaat = ZelfstandigeWoonruimten(
                        peildatum=peildatum
                    ).bereken(eenheid, negeer_stelselgroep=BijzondereVoorzieningen)

                elif stelsel == Woningwaarderingstelsel.onzelfstandige_woonruimten:
                    from woningwaardering.stelsels.onzelfstandige_woonruimten.bijzondere_voorzieningen.bijzondere_voorzieningen import (
                        BijzondereVoorzieningen as BijzondereVoorzieningenOnzelfstandigeWoonruimten,
                    )
                    from woningwaardering.stelsels.onzelfstandige_woonruimten.onzelfstandige_woonruimten import (
                        OnzelfstandigeWoonruimten,
                    )

                    woningwaardering_resultaat = OnzelfstandigeWoonruimten(
                        peildatum=peildatum
                    ).bereken(
                        eenheid,
                        negeer_stelselgroep=BijzondereVoorzieningenOnzelfstandigeWoonruimten,
                    )
                else:
                    raise ValueError(
                        f"Invalid stelsel {stelsel}. Bijzondere voorzieningen zijn alleen gedefinieerd voor {Woningwaarderingstelsel.zelfstandige_woonruimten.naam} en {Woningwaarderingstelsel.onzelfstandige_woonruimten.naam}"
                    )

            puntentotaal = utils.rond_af(
                sum(
                    Decimal(str(groep.punten or "0")) or Decimal()
                    for groep in woningwaardering_resultaat.groepen or []
                    if (
                        groep.punten
                        and groep.criterium_groep
                        and groep.criterium_groep.stelselgroep
                        and groep.criterium_groep.stelselgroep.code
                        not in [
                            stelselgroep.code
                            for stelselgroep in stelselgroepen_zonder_opslag
                        ]
                    )
                ),
                0,
            )

            logger.info(
                f"Eenheid {eenheid.id}: Puntentotaal van de rubrieken 1 tot en met 11 van het woningwaarderingsstelsel is {puntentotaal}"
            )

            verhoging = puntentotaal * Decimal("0.35")

            logger.info(
                f"Eenheid {eenheid.id} is een zorgwoning en wordt gewaardeerd met een verhoging van {verhoging} punten voor stelselgroep {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
            )

            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Zorgwoning 35% puntenverhoging",
                ),
                punten=float(verhoging),
            )

        # Een aanbelfunctie met video- en audioverbinding waarbij de voordeur
        # automatisch kan worden geopend vanuit de woning wordt gewaardeerd
        # met 0,25 punt.
        if any(
            installatie.code
            == Voorzieningsoort.aanbelfunctie_met_video_en_audioverbinding.code
            for ruimte in (eenheid.ruimten or [])
            for installatie in (ruimte.installaties or [])
        ):
            logger.info(
                f"Eenheid {eenheid.id} heeft een aanbelfunctie met video en audioverbinding en wordt met 0,25 punt gewaardeerd voor stelselgroep {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
            )

            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Aanbelfunctie met video- en audioverbinding",
                ),
                punten=0.25,
            )

        # Een laadpaal voor elektrisch rijden die exclusief bestemd is voor gebruik
        # door de bewoners wordt gewaardeerd met 2 punten.
        aantal_laadpalen = sum(
            aantal_bouwkundige_elementen(ruimte, Bouwkundigelementdetailsoort.laadpaal)
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        )

        if aantal_laadpalen > 0:
            punten_laadpalen = aantal_laadpalen * 2

            logger.info(
                f"Eenheid {eenheid.id} heeft {aantal_laadpalen} {'laadpaal' if aantal_laadpalen == 1 else 'laadpalen'} en wordt met {punten_laadpalen} punten gewaardeerd voor stelselgroep {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
            )

            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Laadpalen",
                ),
                aantal=aantal_laadpalen,
                punten=punten_laadpalen,
            )


if __name__ == "__main__":  # pragma: no cover
    bereken(
        instance=BijzondereVoorzieningen(),
        eenheid_input="tests/data/generiek/input/37101000032.json",
        strict=False,
    )
