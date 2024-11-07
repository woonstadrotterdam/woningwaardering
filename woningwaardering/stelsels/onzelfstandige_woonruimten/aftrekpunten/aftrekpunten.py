from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.onzelfstandige_woonruimten.oppervlakte_van_vertrekken import (
    OppervlakteVanVertrekken,
)
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
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class Aftrekpunten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.aftrekpunten
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
            criterium_groep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.aftrekpunten.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        # Bereken de oppervlakte van de vertrekken als deze nog niet berekend is on het woningwaarderingresultaat
        if woningwaardering_resultaat is None or (
            woningwaardering_resultaat
            and not any(
                groep.criterium_groep.stelselgroep.naam
                == Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.value.naam
                for groep in woningwaardering_resultaat.groepen or []
                if groep.criterium_groep
                and groep.criterium_groep.stelselgroep
                and groep.criterium_groep.stelselgroep.naam
            )
        ):
            oppervlakte_resultaat = OppervlakteVanVertrekken(
                peildatum=self.peildatum
            ).bereken(eenheid)

            if oppervlakte_resultaat.woningwaarderingen:
                totale_oppervlakte_vertrekken = sum(
                    woningwaardering.aantal
                    for woningwaardering in oppervlakte_resultaat.woningwaarderingen
                    if (
                        woningwaardering.criterium
                        and woningwaardering.criterium.bovenliggende_criterium is None
                        and woningwaardering.aantal is not None
                    )
                )

                # 4 punten aftrek als de totale oppervlakte van de vertrekken minder is dan 8 m2
                if totale_oppervlakte_vertrekken < 8:
                    woningwaardering = WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam="Totale oppervlakte in Rubriek 1 is minder dan 8 m2"
                        )
                    )
                    woningwaardering.punten = -4.0
                    woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium is not None
                and woningwaardering.criterium.bovenliggende_criterium is None
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.aftrekpunten.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    stelselgroep = Aftrekpunten(peildatum=date.fromisoformat("2024-07-01"))

    with open(
        "tests/data/onzelfstandige_woonruimten/input/15004000185.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )
    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
