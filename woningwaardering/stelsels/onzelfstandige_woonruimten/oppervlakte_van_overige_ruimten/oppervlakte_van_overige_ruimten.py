from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    is_zolder_zonder_vaste_trap,
    maak_zolder_correctie_waardering,
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.woningwaardering_groep import WoningwaarderingGroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    Referentiedata,
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
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            peildatum=peildatum,
        )

    @staticmethod
    def _gedeeld_met_aantal(ruimte: EenhedenRuimte) -> int:
        """Bepaalt gedeeld_met_aantal van een ruimte.

        Sleutel 1 = privé; anders ``gedeeld_met_aantal_onzelfstandige_woonruimten``.
        """
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

        # Bereken vooraf het totale (op 2 decimalen afgeronde) oppervlak van de overige
        # ruimten per gedeeld_met_aantal (sleutel 1 = privé). De zoldercorrectie
        # (vlizotrap) gebruikt het verschil in het op hele m² afgeronde totaal per
        # gedeeld_met_aantal met en zonder zolder.
        totaal_oppervlakte_per_gedeeld_met_aantal: defaultdict[int, Decimal] = (
            defaultdict(Decimal)
        )
        for ruimte in ruimten:
            if (
                ruimte.oppervlakte is not None
                and utils.classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
            ):
                gedeeld_met_aantal = self._gedeeld_met_aantal(ruimte)
                totaal_oppervlakte_per_gedeeld_met_aantal[gedeeld_met_aantal] += (
                    utils.rond_af(ruimte.oppervlakte, decimalen=2)
                )

        gedeeld_met_counter: defaultdict[int, Decimal] = defaultdict(Decimal)
        waarderingen_per_onz: defaultdict[
            int, list[tuple[str, str, Referentiedata | None, float | None]]
        ] = defaultdict(list)
        uitgestelde_correcties: list[tuple[EenhedenRuimte, float]] = []
        for onz_aantal, groep_ruimten in _groepeer_ruimten_per_onz(ruimten).items():
            for ruimte in groep_ruimten:
                for bron in waardeer_oppervlakte_van_overige_ruimte(ruimte):
                    if bron.criterium is None:
                        continue
                    if bron.aantal is not None:
                        # houd bij of de ruimte gedeeld is met andere onzelfstandige woonruimten zodat later de punten kunnen worden gedeeld
                        gedeeld_met_counter[onz_aantal] += utils.rond_af(
                            bron.aantal, decimalen=2
                        )
                        onderliggend_id = utils.criteriumid_onder_stelselgroep(
                            bron.criterium.id, self.stelselgroep.name
                        )
                        if onderliggend_id is not None:
                            waarderingen_per_onz[onz_aantal].append(
                                (
                                    onderliggend_id,
                                    bron.criterium.naam or "",
                                    bron.criterium.meeteenheid,
                                    bron.aantal,
                                )
                            )

                # 2.2.2.3 Zolderruimte zonder vaste trap
                # Correctie op basis van het verschil dat de zolder maakt in het op hele m²
                # afgeronde totaal per gedeeld_met_aantal (niet op de los afgeronde
                # zolderoppervlakte).
                # Zelfde formule als bij de zelfstandige variant. Bij gedeelde correcties
                # blijft de deling door gedeeld_met_aantal_onzelfstandige_woonruimten
                # van toepassing.
                if is_zolder_zonder_vaste_trap(ruimte):
                    totaal_oppervlakte = totaal_oppervlakte_per_gedeeld_met_aantal[
                        self._gedeeld_met_aantal(ruimte)
                    ]
                    correctie = maak_zolder_correctie_waardering(
                        ruimte, totaal_oppervlakte, self.stelselgroep
                    )
                    if correctie.punten is not None:
                        uitgestelde_correcties.append((ruimte, float(correctie.punten)))

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        for onz_aantal, oppervlakte in gedeeld_met_counter.items():
            punten = float(
                utils.rond_af_op_kwart(
                    (utils.rond_af(oppervlakte, decimalen=0) * Decimal("0.75"))
                    / Decimal(str(onz_aantal))
                )
            )
            gedeeld_met_id = CriteriumId.voor_stelselgroep(
                self.stelselgroep
            ).gedeeld_met_criterium(
                onz_aantal,
                GedeeldMetSoort.onzelfstandige_woonruimten if onz_aantal > 1 else None,
            )
            toevoeging = str(gedeeld_met_id).split("__", 1)[1]
            gedeeld_met_handle = woningwaardering_groep.met_onderliggend(
                toevoeging,
                naam=utils.naam_gedeeld_met_groep(
                    onz_aantal,
                    soort=GedeeldMetSoort.onzelfstandige_woonruimten
                    if onz_aantal > 1
                    else None,
                ),
                punten=punten,
            )

            for onderliggend_id, naam, meeteenheid, aantal in waarderingen_per_onz[
                onz_aantal
            ]:
                gedeeld_met_handle.met_onderliggend(
                    onderliggend_id,
                    naam=naam,
                    aantal=aantal,
                    meeteenheid=meeteenheid,
                )

        if woningwaardering_groep.woningwaarderingen is not None:
            woningwaardering_groep.woningwaarderingen = (
                utils.herordenen_fluent_waarderingen(
                    woningwaardering_groep.woningwaarderingen
                )
            )

        # voeg de correcties als laatste toe
        for ruimte, punten in uitgestelde_correcties:
            if (
                utils.gedeeld_met_onzelfstandige_woonruimten(ruimte)
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
            ):
                punten = float(
                    utils.rond_af(
                        Decimal(str(punten))
                        / Decimal(
                            str(ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten)
                        ),
                        decimalen=2,
                    )
                )
            woningwaardering_groep.met_onderliggend(
                f"{ruimte.id}__correctie_zolder_zonder_vaste_trap",
                naam="Correctie: zolder zonder vaste trap",
                punten=punten,
            )

        if len(gedeeld_met_counter) == 1 and woningwaardering_groep.woningwaarderingen:
            woningwaardering_groep.woningwaarderingen = (
                utils.herordenen_fluent_waarderingen(
                    woningwaardering_groep.woningwaarderingen
                )
            )

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
        instance=OppervlakteVanOverigeRuimten(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
