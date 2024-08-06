from datetime import date
from decimal import Decimal
import warnings

from loguru import logger


from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.zelfstandige_woonruimten.punten_voor_de_woz_waarde import (
    PuntenVoorDeWozWaardeJan2024,
)
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


class RenovatieJan2024(Stelselgroepversie):
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
                stelselgroep=Woningwaarderingstelselgroep.renovatie.value,
            )
        )

        if eenheid.renovatie is not None:
            if eenheid.renovatie.datum is None:
                warnings.warn(
                    f"Eenheid {eenheid.id}: renovatiedatum mist.", UserWarning
                )
                return woningwaardering_groep

            if eenheid.renovatie.bedrag_investering is None:
                warnings.warn(
                    f"Eenheid {eenheid.id}: bedrag investering van renovatie mist.",
                    UserWarning,
                )
                return woningwaardering_groep

            # Volgens het woningwaarderingsstelsel kan aan een woning punten voor
            # renovatie worden toegekend. Om voor punten voor dit onderdeel in
            # aanmerking te komen, dient er voor de renovatie een investering te zijn
            # gedaan van minimaal € 10.000.
            if eenheid.renovatie.bedrag_investering < 10000:
                logger.info(
                    f"Eenheid {eenheid.id}: De investering van renovatie in {eenheid.renovatie.datum.year} is te laag. komt niet aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.renovatie.naam}."
                )
                return woningwaardering_groep

            # Deze punten kunnen worden doorberekend vanaf het jaar waarin de
            # renovatie is gerealiseerd en gedurende de vijf daaropvolgende
            # kalenderjaren. Dus in totaal maximaal zes jaar. De Huurcommissie kent
            # renovatiepunten toe indien de renovatie heeft plaatsgevonden en is
            # gereedgekomen op of ná 1 oktober 2016.
            if (
                eenheid.renovatie.datum >= date(2016, 10, 1)
                and eenheid.renovatie.datum.year <= self.peildatum.year
                and eenheid.renovatie.datum.year + 5 >= self.peildatum.year
            ):
                # Er worden geen renovatiepunten toegekend indien een zogenoemde
                # hoogniveau renovatie heeft plaatsgevonden in de jaren 2015-2019 die
                # op grond van rubriek 9.2 van het woningwaarderingsstelsel heeft
                # geleid tot minima`al 40 punten voor de WOZ-waarde.
                if (
                    2015 <= eenheid.renovatie.datum.year <= 2019
                    and PuntenVoorDeWozWaardeJan2024.hoogniveau_renovatie(
                        eenheid, self.peildatum
                    )
                ):
                    logger.info(
                        f"Eenheid {eenheid.id}: Hoogniveau renovatie in 2015-2019 komt niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.renovatie.naam}."
                    )
                    return woningwaardering_groep

                woningwaardering_groep.woningwaarderingen = []
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"Renovatie {eenheid.renovatie.datum.year}"
                        ),
                        # Per geïnvesteerd bedrag van € 1.000 wordt met 0,2 punt
                        # gewaardeerd.
                        punten=Decimal(str(eenheid.renovatie.bedrag_investering))
                        / 1000
                        * Decimal("0.2"),
                    )
                )
            else:
                logger.info(
                    f"Eenheid {eenheid.id}: Renovatie met datum {eenheid.renovatie.datum} komt niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.renovatie.naam}."
                )
                return woningwaardering_groep

        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.renovatie.naam}"
        )
        return woningwaardering_groep
