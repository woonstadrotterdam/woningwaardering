from datetime import date
from decimal import Decimal

from loguru import logger


from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.zelfstandige_woonruimten.punten_voor_de_woz_waarde import (
    PuntenVoorDeWozWaarde2024,
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


class Renovatie2024(Stelselgroepversie):
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
                logger.info("Renovatiedatum mist")
                return woningwaardering_groep

            if (eenheid.renovatie.investeringsbedrag or 0) < 10000:
                logger.info(
                    f"Investering van renovatie in {eenheid.renovatie.datum.year} is te laag."
                )
                return woningwaardering_groep

            if (
                eenheid.renovatie.datum >= date(2016, 10, 1)
                and eenheid.renovatie.datum.year <= self.peildatum.year
                and eenheid.renovatie.datum.year + 5 >= self.peildatum.year
            ):
                if (
                    2015 <= eenheid.renovatie.datum.year <= 2019
                    and PuntenVoorDeWozWaarde2024.hoogniveau_renovatie(
                        eenheid, self.peildatum
                    )
                ):
                    # 4.11.1 Hoogniveau renovatie in 2015-2019
                    # Er worden geen renovatiepunten toegekend indien een zogenoemde
                    # hoogniveau renovatie heeft plaatsgevonden in de jaren 2015-2019 die
                    # op grond van rubriek 9.2 van het woningwaarderingsstelsel heeft
                    # geleid tot minimaal 40 punten voor de WOZ-waarde.
                    logger.debug(
                        f"Hoogniveau renovatie in 2015-2019 komt niet in aanmerking voor waardering onder {Woningwaarderingstelselgroep.renovatie.naam}"
                    )
                    return woningwaardering_groep

                woningwaardering_groep.woningwaarderingen = []
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"Renovatie {eenheid.renovatie.datum.year}"
                        ),
                        punten=Decimal(str(eenheid.renovatie.investeringsbedrag))
                        / 1000
                        * Decimal("0.2"),
                    )
                )
            else:
                logger.info(
                    f"Renovatie met datum {eenheid.renovatie.datum} komt niet in aanmerking voor waardering."
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
        return woningwaardering_groep
