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
from woningwaardering.stelsels.gedeelde_logica import (
    is_zolder_zonder_vaste_trap,
    maak_zolder_correctie_waardering,
    structureer_subtotaal_bij_correcties,
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
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

        # Bereken vooraf het totale (op 2 decimalen afgeronde) oppervlak van de overige
        # ruimten per gedeeld_met_aantal (sleutel 1 = privé). De zoldercorrectie
        # (vlizotrap) gebruikt het verschil in het op hele m² afgeronde totaal per
        # gedeeld_met_aantal met en zonder zolder.
        totaal_oppervlakte_per_gedeeld_met_aantal: defaultdict[int, Decimal] = (
            defaultdict(Decimal)
        )
        for ruimte in eenheid.ruimten or []:
            if ruimte.gedeeld_met_aantal_eenheden:
                continue  # wordt gewaardeerd volgens Rubriek "gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
            if (
                ruimte.oppervlakte is not None
                and utils.classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
            ):
                gedeeld_met_aantal = (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                )
                totaal_oppervlakte_per_gedeeld_met_aantal[gedeeld_met_aantal] += (
                    utils.rond_af(ruimte.oppervlakte, decimalen=2)
                )

        for ruimte in eenheid.ruimten or []:
            if ruimte.gedeeld_met_aantal_eenheden:
                continue  # wordt gewaardeerd volgens Rubriek "gemeenschappelijke binnenruimten gedeeld met meerdere adressen"

            deler = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            if deler not in gedeeld_met_lagen:
                gedeeld_met_lagen[deler] = waarderingsgroep_bouwer.gedeeld_met(
                    aantal_onzelfstandige_woonruimten=deler,
                )
            gedeeld_met = gedeeld_met_lagen[deler]

            waarderingen = waardeer_oppervlakte_van_overige_ruimte(
                ruimte, waarderingsgroep_bouwer=gedeeld_met
            )

            # 2.2.2.3 Zolderruimte zonder vaste trap
            # Correctie op basis van het verschil dat de zolder maakt in het op hele m²
            # afgeronde totaal per gedeeld_met_aantal (niet op de los afgeronde
            # zolderoppervlakte).
            # Zelfde formule als bij de zelfstandige variant. Bij gedeelde correcties
            # blijft de deling door gedeeld_met_aantal_onzelfstandige_woonruimten
            # van toepassing.
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

        # bereken de som van de woningwaarderingen per aantal gedeelde onzelfstandige woonruimten
        for deler, waarderingen in per_deler_waarderingen.items():
            gedeeld_met = gedeeld_met_lagen[deler]
            heeft_correctie = any(w.punten is not None for w in waarderingen)
            if heeft_correctie:
                structureer_subtotaal_bij_correcties(
                    waarderingen,
                    waarderingsgroep_bouwer=gedeeld_met,
                    factor=Decimal("0.75"),
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
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
