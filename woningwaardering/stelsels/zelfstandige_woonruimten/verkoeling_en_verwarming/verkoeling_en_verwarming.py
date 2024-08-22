import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import classificeer_ruimte
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
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort
from woningwaardering.vera.utils import heeft_bouwkundig_element


class VerkoelingEnVerwarming(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.verkoeling_en_verwarming
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
                stelselgroep=Woningwaarderingstelselgroep.verkoeling_en_verwarming.value,
            )
        )

        logger.debug(f"Punten per verwarmd {Ruimtesoort.vertrek.naam}: 2")
        logger.debug(
            f"Extra punt voor {Ruimtesoort.vertrek.naam} met ook een koelfunctie. Maximaal 2 extra punten per eenheid."
        )
        logger.debug(
            f"Punten per verwarmd {Ruimtesoort.overige_ruimten.naam} of verkeersruimte (met totaal van max 4 punten per eenheid): 1."
        )

        woningwaardering_groep.woningwaarderingen = []
        totaal_punten_overige_ruimten = Decimal("0")
        totaal_punten_verkoeld_en_verwarmd = Decimal(
            "0"
        )  # max 2 punten per eenheid voor vertrekken die en verwarmd en verkoeld zijn. 1 punt per vertrek.

        for ruimte in eenheid.ruimten or []:
            if ruimte.detail_soort is None:
                warnings.warn(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detailsoort.",
                    UserWarning,
                )
                continue

            ruimtesoort = classificeer_ruimte(ruimte)

            if ruimtesoort is None:
                if ruimte.detail_soort.code in [
                    Ruimtedetailsoort.hal.code,
                    Ruimtedetailsoort.overloop.code,
                    Ruimtedetailsoort.entree.code,
                    Ruimtedetailsoort.gang.code,
                ]:  # verkeersruimten tellen ook mee
                    ruimtesoort = Ruimtesoort.overige_ruimten

            if (
                not ruimtesoort
                or ruimtesoort.code
                not in [Ruimtesoort.overige_ruimten.code, Ruimtesoort.vertrek.code]
                or not ruimte.verwarmd
            ):
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) komt niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.verwarming.naam}"
                )
                continue

            woningwaardering = WoningwaarderingResultatenWoningwaardering()

            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=ruimte.naam,
                )
            )

            punten = Decimal(
                str(
                    {Ruimtesoort.vertrek.code: 2, Ruimtesoort.overige_ruimten.code: 1}[
                        ruimtesoort.code
                    ]
                )
            )

            if ruimtesoort == Ruimtesoort.overige_ruimten:
                if totaal_punten_overige_ruimten >= Decimal("4.0"):
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) wordt niet meegeteld voor {Woningwaarderingstelselgroep.verwarming.naam}, omdat de overige ruimten bij elkaar {totaal_punten_overige_ruimten} punten hebben behaald."
                    )
                    continue

                # Als de punten de maximum van 4.0 overschrijden, dan wordt het aantal punten dat nog mag worden gegeven voor de ruimte aangepast
                if (totaal_punten_overige_ruimten + punten) >= Decimal("4.0"):
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}): punten worden gecorrigeerd. De maximum punten voor {Ruimtesoort.overige_ruimten.naam} zijn behaald."
                    )
                    punten = Decimal("4.0") - totaal_punten_overige_ruimten

                totaal_punten_overige_ruimten += punten
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) telt als verwarmde {Ruimtesoort.overige_ruimten.naam} en krijgt {punten} punt."
                )

            else:
                if (
                    ruimte.verkoeld
                    and totaal_punten_verkoeld_en_verwarmd + 1 <= Decimal("2")
                ):
                    punten += Decimal("1")
                    totaal_punten_verkoeld_en_verwarmd += Decimal("1")
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) telt als verwarmde en verkoelde {Ruimtesoort.vertrek.naam} en krijgt {punten} punten."
                    )
                else:
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) telt als verwarmd {Ruimtesoort.vertrek.naam} en krijgt {punten} punten."
                    )

            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=ruimte.naam,
                    ),
                    punten=punten,
                )
            )

            # Voor deze rubriek wordt een verwarmde open keuken als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten.
            if (
                ruimte.detail_soort.code
                == Ruimtedetailsoort.woonkamer_en_of_keuken.code
                or ruimte.detail_soort.code
                in [
                    Ruimtedetailsoort.woonkamer.code,
                    Ruimtedetailsoort.woon_en_of_slaapkamer.code,
                    Ruimtedetailsoort.slaapkamer.code,
                ]
                and heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.aanrecht
                )
            ):
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"Open keuken in {ruimte.naam}",
                        ),
                        punten=punten,
                    )
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
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punt(en) voor stelselgroep {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    verkoeling_en_verwarming = VerkoelingEnVerwarming(
        peildatum=date.fromisoformat("2024-07-01")
    )

    with open(
        "tests/data/generiek/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[verkoeling_en_verwarming.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
