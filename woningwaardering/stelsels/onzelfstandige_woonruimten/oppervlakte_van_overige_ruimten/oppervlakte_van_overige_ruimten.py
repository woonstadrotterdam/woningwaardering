from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import cast

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    OppervlakteVanOverigeRuimten as ZelfstandigeWoonruimtenOppervlakteVanOverigeruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingCriteriumSleutels,
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
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid


class OppervlakteVanOverigeRuimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten
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
                stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.value,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaardering_groep.woningwaarderingen = []
        woningwaardering_correcties = []

        gedeeld_met_counter: defaultdict[int, float] = defaultdict(float)

        for ruimte in eenheid.ruimten or []:
            woningwaarderingen = list(
                ZelfstandigeWoonruimtenOppervlakteVanOverigeruimten.genereer_woningwaarderingen(
                    ruimte, self.stelselgroep
                )
            )
            # houd bij of de ruimte gedeeld is met andere onzelfstandige woonruimten zodat later de punten kunnen worden gedeeld
            for idx, woningwaardering in enumerate(woningwaarderingen):
                if woningwaardering.criterium is not None:
                    if (
                        woningwaardering.aantal
                        and utils.gedeeld_met_onzelfstandige_woonruimten(ruimte)
                    ):
                        gedeeld_met_counter[
                            cast(
                                int,
                                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten,
                            )
                        ] += float(utils.rond_af(woningwaardering.aantal, decimalen=2))
                        woningwaardering.criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                            id=f"{self.stelselgroep.name}_gedeeld_met_{ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten}_onzelfstandige_woonruimten"
                        )
                    elif woningwaardering.aantal is not None:
                        gedeeld_met_counter[1] += float(
                            utils.rond_af(woningwaardering.aantal, decimalen=2)
                        )
                        woningwaardering.criterium.bovenliggende_criterium = (
                            WoningwaarderingCriteriumSleutels(
                                id=f"{self.stelselgroep.name}_prive"
                            )
                        )
                    elif (
                        woningwaardering.punten
                        and utils.gedeeld_met_onzelfstandige_woonruimten(ruimte)
                    ):
                        woningwaardering.punten = float(
                            utils.rond_af(
                                Decimal(str(woningwaardering.punten))
                                / Decimal(
                                    str(
                                        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                                    )
                                ),
                                decimalen=2,
                            )
                        )
                        woningwaardering_correcties.append(woningwaardering)
                        woningwaarderingen.pop(idx)

            woningwaardering_groep.woningwaarderingen.extend(woningwaarderingen)

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        for aantal, oppervlakte in gedeeld_met_counter.items():
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                naam=f"Totaal (gedeeld met {aantal})"
                if aantal > 1
                else "Totaal (privé)",
                id=f"{self.stelselgroep.name}_gedeeld_met_{aantal}_onzelfstandige_woonruimten"
                if aantal > 1
                else f"{self.stelselgroep.name}_prive",
            )
            woningwaardering.punten = float(
                utils.rond_af_op_kwart(
                    (utils.rond_af(oppervlakte, decimalen=0) * Decimal("0.75")) / aantal
                )
            )
            woningwaardering.aantal = float(utils.rond_af(oppervlakte, decimalen=0))
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        # voeg de correcties als laatste toe
        woningwaardering_groep.woningwaarderingen.extend(woningwaardering_correcties)

        punten = float(
            utils.rond_af_op_kwart(
                sum(
                    Decimal(str(woningwaardering.punten))
                    for woningwaardering in woningwaardering_groep.woningwaarderingen
                    or []
                    if woningwaardering.punten is not None
                )
            )
        )

        woningwaardering_groep.punten = punten

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    stelselgroep = OppervlakteVanOverigeRuimten()
    with open(
        "tests/data/generiek/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
