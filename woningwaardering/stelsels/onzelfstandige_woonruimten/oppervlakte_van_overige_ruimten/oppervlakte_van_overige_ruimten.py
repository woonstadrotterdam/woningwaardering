from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    OppervlakteVanOverigeRuimten as ZelfstandigeWoonruimtenOppervlakteVanOverigeruimten,
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


class OppervlakteVanOverigeRuimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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
                stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.value,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        for ruimte in eenheid.ruimten or []:
            woningwaarderingen = ZelfstandigeWoonruimtenOppervlakteVanOverigeruimten.genereer_woningwaarderingen(
                ruimte, self.stelselgroep
            )
            gedeelde_ruimte = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 2
            )
            for woningwaardering in woningwaarderingen:
                if (
                    gedeelde_ruimte
                    and woningwaardering.criterium
                    and woningwaardering.aantal
                    and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten  # nodig voor mypy
                ):
                    woningwaardering.criterium.naam = f"{woningwaardering.criterium.naam} (gedeeld met {ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten})"
                    woningwaardering.punten = float(
                        utils.rond_af(
                            utils.rond_af(woningwaardering.aantal, decimalen=2)
                            * Decimal(".75")
                            / ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten,
                            decimalen=2,
                        )
                    )

                else:
                    woningwaardering.punten = float(
                        utils.rond_af(
                            Decimal(str(woningwaardering.aantal)), decimalen=2
                        )
                    )
                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = utils.rond_af_op_kwart(
            float(
                utils.rond_af(
                    sum(
                        Decimal(str(woningwaardering.punten))
                        for woningwaardering in woningwaardering_groep.woningwaarderingen
                        or []
                        if woningwaardering.punten is not None
                    ),
                    decimalen=2,
                )
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.oppervlakte_onzelfstandige_woonruimte.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    stelselgroep = OppervlakteVanOverigeRuimten()
    with open(
        "tests/data/onzelfstandige_woonruimten/stelselgroepen/oppervlakte_van_overige_ruimten/input/voorbeeld_beleidsboek.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
