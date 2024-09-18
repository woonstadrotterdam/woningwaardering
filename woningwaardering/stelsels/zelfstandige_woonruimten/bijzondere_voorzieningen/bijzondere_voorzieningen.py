from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
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
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import (
    aantal_bouwkundige_elementen,
    heeft_bouwkundig_element,
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

        woningwaardering_groep.woningwaarderingen = []

        # Als sprake is van een zorgwoning, dan wordt het puntentotaal van de rubrieken
        # 1 tot en met 11 van het woningwaarderingsstelsel met 35% verhoogd. Dit
        # resulteert in een hogere maximale huurprijs.
        if (
            eenheid.doelgroep is not None
            and eenheid.doelgroep.code == Doelgroep.zorg.code
        ):
            if not woningwaardering_resultaat or not woningwaardering_resultaat.groepen:
                logger.warning(
                    "Geen woningwaardering resultaat gevonden: Woningwaarderingresultaat wordt aangemaakt"
                )
                from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
                    ZelfstandigeWoonruimten,
                )

                woningwaardering_resultaat = ZelfstandigeWoonruimten(
                    peildatum=self.peildatum
                ).bereken(eenheid, negeer_stelselgroep=BijzondereVoorzieningen)

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
                            Woningwaarderingstelselgroep.bijzondere_voorzieningen.code,
                            Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw.code,
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

            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Zorgwoning 35% puntenverhoging",
                    ),
                    punten=float(verhoging),
                )
            )

        # Een aanbelfunctie met video- en audioverbinding waarbij de voordeur
        # automatisch kan worden geopend vanuit de woning wordt gewaardeerd
        # met 0,25 punt.
        if any(
            heeft_bouwkundig_element(
                ruimte,
                Bouwkundigelementdetailsoort.aanbelfunctie_met_video_en_audioverbinding,
            )
            for ruimte in eenheid.ruimten or []
        ):
            logger.info(
                f"Eenheid {eenheid.id} heeft een aanbelfunctie met video en audioverbinding en wordt met 0,25 punt gewaardeerd voor stelselgroep {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
            )

            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Aanbelfunctie met video- en audioverbinding",
                    ),
                    punten=0.25,
                )
            )

        # Een laadpaal voor elektrisch rijden die exclusief bestemd is voor gebruik
        # door de bewoners wordt gewaardeerd met 2 punten.
        aantal_laadpalen = sum(
            aantal_bouwkundige_elementen(ruimte, Bouwkundigelementdetailsoort.laadpaal)
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden < 2
        )

        if aantal_laadpalen > 0:
            punten_laadpalen = aantal_laadpalen * 2

            logger.info(
                f"Eenheid {eenheid.id} heeft {aantal_laadpalen} {'laadpaal' if aantal_laadpalen == 1 else 'laadpalen'} en wordt met {punten_laadpalen} punten gewaardeerd voor stelselgroep {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
            )

            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Laadpalen",
                    ),
                    aantal=aantal_laadpalen,
                    punten=punten_laadpalen,
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
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    bijzondere_voorzieningen = BijzondereVoorzieningen(
        peildatum=date.fromisoformat("2024-07-01")
    )

    with open("tests/data/generiek/input/37101000032.json", "r+") as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[bijzondere_voorzieningen.bereken(eenheid)]
    )

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
