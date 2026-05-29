from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Meeteenheid,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element


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
    def _gedeeld_met_groep(ruimte: EenhedenRuimte) -> int:
        """Bepaalt gedeeld_met_aantal van een ruimte: het aantal onzelfstandige
        woonruimten waarmee de ruimte gedeeld wordt; sleutel 1 = privé."""
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
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaardering_groep.woningwaarderingen = []
        woningwaardering_correcties = []

        gedeeld_met_counter: defaultdict[int, Decimal] = defaultdict(Decimal)

        # Bereken vooraf het totale (op 2 decimalen afgeronde) oppervlak van de overige
        # ruimten per gedeeld_met_aantal (sleutel 1 = privé). De zoldercorrectie
        # (vlizotrap) gebruikt het verschil in het op hele m² afgeronde totaal per
        # gedeeld_met_aantal met en zonder zolder.
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
                gedeeld_met_aantal = self._gedeeld_met_groep(ruimte)
                totaal_oppervlakte_per_gedeeld_met_aantal[gedeeld_met_aantal] += (
                    utils.rond_af(ruimte.oppervlakte, decimalen=2)
                )

        for ruimte in eenheid.ruimten or []:
            if ruimte.gedeeld_met_aantal_eenheden:
                continue  # wordt gewaardeerd volgens Rubriek "gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
            woningwaarderingen = list(waardeer_oppervlakte_van_overige_ruimte(ruimte))

            # 2.2.2.3 Zolderruimte zonder vaste trap
            # Correctie op basis van het verschil dat de zolder maakt in het op hele m²
            # afgeronde totaal per gedeeld_met_aantal (niet op de los afgeronde
            # zolderoppervlakte).
            # Zelfde formule als bij de zelfstandige variant. Bij gedeelde correcties
            # blijft de deling door gedeeld_met_aantal_onzelfstandige_woonruimten
            # van toepassing.
            if (
                ruimte.detail_soort == Ruimtedetailsoort.zolder
                and ruimte.oppervlakte is not None
                and heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.vlizotrap
                )
                and utils.classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
            ):
                totaal_oppervlakte = totaal_oppervlakte_per_gedeeld_met_aantal[
                    self._gedeeld_met_groep(ruimte)
                ]
                zolder_opp = utils.rond_af(ruimte.oppervlakte, decimalen=2)
                correctie = min(
                    Decimal("5"),
                    (
                        utils.rond_af(totaal_oppervlakte, decimalen=0)
                        - utils.rond_af(totaal_oppervlakte - zolder_opp, decimalen=0)
                    )
                    * Decimal("0.75"),
                )
                for woningwaardering in woningwaarderingen:
                    if (
                        woningwaardering.criterium is not None
                        and woningwaardering.criterium.id is not None
                        and woningwaardering.criterium.id.endswith(
                            "__correctie_zolder_zonder_vaste_trap"
                        )
                    ):
                        woningwaardering.punten = float(correctie * Decimal("-1"))
                        break
            # houd bij of de ruimte gedeeld is met andere onzelfstandige woonruimten zodat later de punten kunnen worden gedeeld
            for idx, woningwaardering in enumerate(woningwaarderingen):
                if woningwaardering.criterium is not None:
                    if (
                        woningwaardering.aantal
                        and utils.gedeeld_met_onzelfstandige_woonruimten(ruimte)
                        and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                        is not None
                    ):
                        gedeeld_met_counter[
                            ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                        ] += utils.rond_af(woningwaardering.aantal, decimalen=2)
                        woningwaardering.criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                            id=str(
                                CriteriumId(
                                    stelselgroep=self.stelselgroep,
                                    gedeeld_met_aantal=ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten,
                                    gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                                    is_totaal=True,
                                )
                            ),
                        )
                    elif woningwaardering.aantal is not None:
                        gedeeld_met_counter[1] += utils.rond_af(
                            woningwaardering.aantal, decimalen=2
                        )
                        woningwaardering.criterium.bovenliggende_criterium = (
                            WoningwaarderingCriteriumSleutels(
                                id=str(
                                    CriteriumId(
                                        stelselgroep=self.stelselgroep,
                                        gedeeld_met_aantal=1,
                                        is_totaal=True,
                                    )
                                ),
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
        for aantal_onz, oppervlakte in gedeeld_met_counter.items():
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                meeteenheid=Meeteenheid.vierkante_meter_m2,
                naam=f"Totaal (gedeeld met {aantal_onz} onzelfstandige woonruimten)"
                if aantal_onz > 1
                else "Totaal (privé)",
                id=str(
                    CriteriumId(
                        stelselgroep=self.stelselgroep,
                        gedeeld_met_aantal=aantal_onz,
                        gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                        is_totaal=True,
                    )
                ),
            )
            woningwaardering.punten = float(
                utils.rond_af_op_kwart(
                    (utils.rond_af(oppervlakte, decimalen=0) * Decimal("0.75"))
                    / Decimal(str(aantal_onz))
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
