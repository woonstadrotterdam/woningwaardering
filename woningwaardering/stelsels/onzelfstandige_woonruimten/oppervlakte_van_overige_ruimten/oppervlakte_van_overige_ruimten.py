from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.builders import (
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.gedeelde_logica import (
    bereken_zolder_correctie,
    is_zolder_zonder_vaste_trap,
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    gedeeld_met_adressen,
    toe_te_rekenen_oppervlakte,
)
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
        waarderingsgroep_builder = WaarderingsgroepBuilder(
            self.stelsel, self.stelselgroep
        )

        # Ruimten gedeeld met meerdere adressen worden gewaardeerd volgens Rubriek
        # "gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not gedeeld_met_adressen(ruimte)
        ]

        # Eerst per ruimte delen, daarna salderen, daarna éénmaal afronden op hele m²
        # (#391). Punten staan op de stelselgroep, niet op de gedeeld-met-laag (#393).
        oppervlakte_totaal_na_delen = Decimal("0")
        zolders: list[EenhedenRuimte] = []

        for ruimte in ruimten:
            deler = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            gedeeld_met = waarderingsgroep_builder.gedeeld_met(
                aantal_onzelfstandige_woonruimten=deler,
            )

            waarderingen = waardeer_oppervlakte_van_overige_ruimte(
                ruimte, waarderingsgroep_builder=gedeeld_met
            )
            if not waarderingen:
                continue

            oppervlakte_totaal_na_delen += toe_te_rekenen_oppervlakte(ruimte)
            if is_zolder_zonder_vaste_trap(ruimte):
                zolders.append(ruimte)

        punten_uit_m2 = utils.rond_af(
            oppervlakte_totaal_na_delen, decimalen=0
        ) * Decimal("0.75")

        if zolders:
            # 2.2.2.3 Zolderruimte zonder vaste trap
            # Eén subtotaal direct onder de stelselgroep; correcties als sibling.
            # De maximumaftrek van 5 punten is van de zolder en wordt gedeeld. De zolder
            # blijft in de saldering. Het subtotaal draagt geen aantal: ruimteregels
            # tonen werkelijke m², punten komen uit toe te rekenen m². Zie #403.
            waarderingsgroep_builder.met_onderliggend(
                id="subtotaal",
                naam="Subtotaal",
                punten=float(punten_uit_m2),
            )
            for ruimte in zolders:
                deler = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                waarderingsgroep_builder.met_onderliggend(
                    id=f"{ruimte.id}__correctie_zolder_zonder_vaste_trap",
                    naam="Correctie: zolder zonder vaste trap",
                    punten=float(
                        bereken_zolder_correctie(
                            oppervlakte_totaal_na_delen,
                            toe_te_rekenen_oppervlakte(ruimte),
                            max_aftrek=Decimal("5") / Decimal(str(deler)),
                        )
                    ),
                )
            woningwaardering_groep = waarderingsgroep_builder.build()
        else:
            woningwaardering_groep = waarderingsgroep_builder.build()
            woningwaardering_groep.punten = float(utils.rond_af_op_kwart(punten_uit_m2))

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=OppervlakteVanOverigeRuimten(peildatum=date(2026, 7, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
