from decimal import Decimal

from loguru import logger


from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import (
    vertrek_telt_als_vertrek,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    Referentiedata,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Eenheidklimaatbeheersingsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class Verwarming2024(Stelselgroepversie):
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
                stelselgroep=Woningwaarderingstelselgroep.verwarming.value,
            )
        )

        punten_per_ruimte = Verwarming2024.punten_per_ruimte(
            eenheid.klimaatbeheersingsoort
        )

        logger.debug(
            f"Punten per verwarmd vertrek: {punten_per_ruimte[Ruimtesoort.vertrek.code]}"
        )
        logger.debug(
            f"Punten per verwarmd overige ruimte: {punten_per_ruimte[Ruimtesoort.overige_ruimtes.code]}"
        )

        woningwaardering_groep.woningwaarderingen = []
        totaal_punten_overige_ruimten = Decimal("0")

        for ruimte in eenheid.ruimten or []:
            if ruimte.soort is None:
                logger.error(f"Ruimte {ruimte.id} {ruimte.naam} heeft geen soort.")
            if ruimte.soort is not None and ruimte.soort.code is None:
                logger.error(f"Ruimtesoort {ruimte.id} {ruimte.naam} heeft geen code.")
            if not (
                ruimte.soort is not None
                and ruimte.soort.code is not None
                and ruimte.soort.code
                in [
                    Ruimtesoort.vertrek.code,
                    Ruimtesoort.overige_ruimtes.code,
                ]
                and ruimte.verwarmd
            ):
                logger.debug(
                    f"Ruimte {ruimte.id} {ruimte.naam} komt niet in aanmerking voor punten voor Verwarming."
                )
                continue

            woningwaardering = WoningwaarderingResultatenWoningwaardering()

            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=ruimte.naam,
                )
            )

            punten = Decimal(str(punten_per_ruimte[Ruimtesoort.vertrek.code]))

            if not vertrek_telt_als_vertrek(ruimte):
                punten = Decimal(
                    str(punten_per_ruimte[Ruimtesoort.overige_ruimtes.code])
                )

                if totaal_punten_overige_ruimten >= Decimal("4.0"):
                    logger.debug(
                        f"De overige ruimten hebben bij elkaar {totaal_punten_overige_ruimten} punten behaald: {ruimte.id} {ruimte.naam} wordt niet meegeteld voor Verwarming."
                    )
                    continue

                # Als de punten de maximum van 4.0 overschrijden, dan wordt het aantal punten dat nog mag worden gegeven voor de ruimte aangepast
                if (totaal_punten_overige_ruimten + punten) >= Decimal("4.0"):
                    logger.debug(
                        f"De maximum punten voor {Ruimtesoort.overige_ruimtes.naam} zijn behaald: punten voor {ruimte.id} {ruimte.naam} worden gecorrigeerd."
                    )
                    punten = Decimal("4.0") - totaal_punten_overige_ruimten

                totaal_punten_overige_ruimten += punten
                logger.debug(
                    f"Ruimte {ruimte.id} {ruimte.naam} telt als verwarmde {Ruimtesoort.overige_ruimtes.naam} en krijgt {punten} punten."
                )

            else:
                logger.debug(
                    f"Ruimte {ruimte.id} {ruimte.naam} telt als verwarmd {Ruimtesoort.vertrek.naam} en krijgt {punten} punten."
                )

            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=ruimte.naam,
                    ),
                    aantal=punten,
                )
            )

        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.aantal))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.aantal is not None
            )
        )

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep

    @staticmethod
    def punten_per_ruimte(
        klimaatbeheersingsoort: Referentiedata | None,
    ) -> dict[str, float]:
        punten_mapping: dict[str, dict[str, float]] = {
            Eenheidklimaatbeheersingsoort.individueel.code: {
                Ruimtesoort.vertrek.code: 2,
                Ruimtesoort.overige_ruimtes.code: 1.5,
            },
            Eenheidklimaatbeheersingsoort.collectief.code: {
                Ruimtesoort.vertrek.code: 1,
                Ruimtesoort.overige_ruimtes.code: 0.75,
            },
        }

        punten_per_ruimte = punten_mapping[
            klimaatbeheersingsoort.code
            if klimaatbeheersingsoort is not None
            and klimaatbeheersingsoort.code is not None
            else Eenheidklimaatbeheersingsoort.individueel.code
        ]
        return punten_per_ruimte


if __name__ == "__main__":
    file = open(
        "tests/data/input/zelfstandige_woonruimten/12006000004.json",
        "r+",
    )
    eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = Verwarming2024.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
