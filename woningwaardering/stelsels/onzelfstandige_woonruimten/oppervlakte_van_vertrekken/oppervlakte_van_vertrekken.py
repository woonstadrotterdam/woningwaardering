from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_oppervlakte_van_vertrek,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.woningwaardering_groep import WoningwaarderingGroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class OppervlakteVanVertrekken(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_vertrekken  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            peildatum=peildatum,
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingGroep(
            stelsel=self.stelsel,
            stelselgroep=self.stelselgroep,
        )

        # wordt gewaardeerd volgens Rubriek "gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not ruimte.gedeeld_met_aantal_eenheden
        ]

        gedeeld_met_counter: defaultdict[int, Decimal] = defaultdict(Decimal)

        for onz_aantal, groep_ruimten in _groepeer_ruimten_per_onz(ruimten).items():
            if onz_aantal > 1:
                gedeeld_met_handle = woningwaardering_groep.met_gedeeld_met_criterium(
                    onz_aantal,
                    GedeeldMetSoort.onzelfstandige_woonruimten,
                    naam=utils.naam_gedeeld_met_groep(
                        onz_aantal,
                        soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                    ),
                )
            else:
                gedeeld_met_handle = woningwaardering_groep.met_gedeeld_met_criterium(
                    1, naam=utils.naam_gedeeld_met_groep(1)
                )

            for ruimte in groep_ruimten:
                for bron in waardeer_oppervlakte_van_vertrek(ruimte):
                    if bron.criterium is None or bron.aantal is None:
                        continue
                    onderliggend_id = utils.criteriumid_onder_stelselgroep(
                        bron.criterium.id, self.stelselgroep.name
                    )
                    if onderliggend_id is None:
                        continue
                    gedeeld_met_handle.met_onderliggend(
                        onderliggend_id,
                        naam=bron.criterium.naam,
                        aantal=bron.aantal,
                        meeteenheid=bron.criterium.meeteenheid,
                    )
                    # houd bij of de ruimte gedeeld is met andere onzelfstandige woonruimten zodat later de punten kunnen worden gedeeld
                    gedeeld_met_counter[onz_aantal] += utils.rond_af(
                        bron.aantal, decimalen=2
                    )

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        oppervlakte_totaal_na_delen = Decimal("0")
        for aantal_onz, oppervlakte in gedeeld_met_counter.items():
            oppervlakte_totaal_na_delen += utils.rond_af(
                oppervlakte, decimalen=2
            ) / Decimal(str(aantal_onz))

        punten = float(utils.rond_af(oppervlakte_totaal_na_delen, decimalen=0))
        woningwaardering_groep.punten = punten

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        if woningwaardering_groep.woningwaarderingen is not None:
            woningwaardering_groep.woningwaarderingen = (
                utils.herordenen_fluent_waarderingen(
                    woningwaardering_groep.woningwaarderingen
                )
            )
        return woningwaardering_groep


def _groepeer_ruimten_per_onz(
    ruimten: list[EenhedenRuimte],
) -> dict[int, list[EenhedenRuimte]]:
    groepen: dict[int, list[EenhedenRuimte]] = defaultdict(list)
    for ruimte in ruimten:
        onz_aantal = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
        groepen[onz_aantal].append(ruimte)
    return groepen


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=OppervlakteVanVertrekken(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
