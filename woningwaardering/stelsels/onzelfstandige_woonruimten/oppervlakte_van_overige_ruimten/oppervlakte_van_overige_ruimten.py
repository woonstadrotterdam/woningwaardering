from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.criterium import (
    GedeeldMetSoort,
)
from woningwaardering.stelsels.gedeelde_logica import (
    is_zolder_zonder_vaste_trap,
    maak_zolder_correctie_waardering,
    structureer_subtotaal_bij_correcties,
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class OppervlakteVanOverigeRuimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten
        super().__init__(
            peildatum=peildatum,
        )

    @staticmethod
    def _gedeeld_met_aantal(ruimte: EenhedenRuimte) -> int:
        if (
            utils.gedeeld_met_onzelfstandige_woonruimten(ruimte)
            and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
        ):
            return ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
        return 1

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        waarderingsgroep_bouwer = WaarderingsgroepBouwer(
            self.stelsel, self.stelselgroep
        )

        per_deler_waarderingen: defaultdict[int, list[WaarderingBouwer]] = defaultdict(
            list
        )
        gedeeld_met_counter: defaultdict[int, Decimal] = defaultdict(Decimal)
        gedeeld_met_lagen: dict[int, WaarderingBouwer] = {}

        totaal_oppervlakte_per_gedeeld_met_aantal: defaultdict[int, Decimal] = (
            defaultdict(Decimal)
        )
        for ruimte in eenheid.ruimten or []:
            if ruimte.gedeeld_met_aantal_eenheden:
                continue
            if (
                ruimte.oppervlakte is not None
                and utils.classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
            ):
                gedeeld_met_aantal = self._gedeeld_met_aantal(ruimte)
                totaal_oppervlakte_per_gedeeld_met_aantal[gedeeld_met_aantal] += (
                    utils.rond_af(ruimte.oppervlakte, decimalen=2)
                )

        for ruimte in eenheid.ruimten or []:
            if ruimte.gedeeld_met_aantal_eenheden:
                continue

            deler = self._gedeeld_met_aantal(ruimte)
            if deler not in gedeeld_met_lagen:
                gedeeld_met_lagen[deler] = waarderingsgroep_bouwer.gedeeld_met(
                    aantal=deler,
                    soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                )
            gedeeld_met = gedeeld_met_lagen[deler]

            waarderingen = waardeer_oppervlakte_van_overige_ruimte(
                ruimte, waarderingsgroep_bouwer=gedeeld_met
            )

            if is_zolder_zonder_vaste_trap(ruimte):
                totaal_oppervlakte = totaal_oppervlakte_per_gedeeld_met_aantal[deler]
                waarderingen.append(
                    maak_zolder_correctie_waardering(
                        ruimte,
                        totaal_oppervlakte,
                        waarderingsgroep_bouwer=gedeeld_met,
                    )
                )

            for waardering in waarderingen:
                if waardering.punten and utils.gedeeld_met_onzelfstandige_woonruimten(
                    ruimte
                ):
                    waardering.punten = float(
                        utils.rond_af(
                            Decimal(str(waardering.punten)) / Decimal(str(deler)),
                            decimalen=2,
                        )
                    )

                if waardering.aantal is not None:
                    gedeeld_met_counter[deler] += utils.rond_af(
                        waardering.aantal, decimalen=2
                    )

                per_deler_waarderingen[deler].append(waardering)

        # Lege gedeeld-met-lagen (ruimte gaf geen waarderingen) horen niet in de output.
        for deler, gedeeld_met in gedeeld_met_lagen.items():
            if not per_deler_waarderingen.get(deler):
                gedeeld_met.verwijder()

        for deler, waarderingen in per_deler_waarderingen.items():
            gedeeld_met = gedeeld_met_lagen[deler]
            gedeeld_met_id = gedeeld_met.criterium_id
            heeft_correctie = any(w.punten is not None for w in waarderingen)
            if heeft_correctie:
                structureer_subtotaal_bij_correcties(
                    waarderingen,
                    waarderingsgroep_bouwer=gedeeld_met,
                    factor=Decimal("0.75"),
                    onder_criterium_id=gedeeld_met_id,
                    deler=deler,
                )
                continue

            oppervlakte = gedeeld_met_counter[deler]
            gedeeld_met.punten = float(
                utils.rond_af_op_kwart(
                    (utils.rond_af(oppervlakte, decimalen=0) * Decimal("0.75"))
                    / Decimal(str(deler))
                )
            )

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()
        woningwaardering_groep.punten = float(
            utils.rond_af_op_kwart(
                sum(
                    Decimal(str(woningwaardering.punten))
                    for woningwaardering in woningwaardering_groep.woningwaarderingen
                    or []
                    if woningwaardering.punten is not None
                )
            )
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=OppervlakteVanOverigeRuimten(peildatum=date(2026, 1, 1)),
        strict=False,
        log_level="DEBUG",
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
