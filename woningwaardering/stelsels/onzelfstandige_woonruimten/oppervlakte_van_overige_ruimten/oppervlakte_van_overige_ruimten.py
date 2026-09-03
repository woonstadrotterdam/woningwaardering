from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.gedeelde_logica import (
    bereken_oppervlakte_punten,
    bereken_zolder_correctie,
    is_zolder_zonder_vaste_trap,
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    gedeeld_met_adressen,
    toe_te_rekenen_oppervlakte,
)
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
        waarderingsgroep_builder = WaarderingsgroepBuilder(
            self.stelsel, self.stelselgroep
        )

        # Ruimten gedeeld met meerdere adressen worden gewaardeerd volgens Rubriek
        # "gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
        overige_ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not gedeeld_met_adressen(ruimte)
            and classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
        ]

        zolders = [
            ruimte for ruimte in overige_ruimten if is_zolder_zonder_vaste_trap(ruimte)
        ]

        # Bij een vlizotrap hangen de gedeeld-met-lagen onder het Subtotaal, zodat de
        # ruimteregels bij het subtotaal horen. Correcties staan op hetzelfde
        # niveau als het subtotaal. Punten op het subtotaal volgen ná de saldering.
        parent: WaarderingsgroepBuilder | WaarderingBuilder = waarderingsgroep_builder
        subtotaal: WaarderingBuilder | None = None
        if zolders:
            # 2.2.2.3 Zolderruimte zonder vaste trap
            # De maximumaftrek van 5 punten is van de zolder en wordt gedeeld. De zolder
            # blijft in de saldering. Het subtotaal draagt geen aantal: ruimteregels
            # tonen werkelijke m², punten komen uit toe te rekenen m². Zie #403.
            subtotaal = waarderingsgroep_builder.met_onderliggend(
                id="subtotaal",
                naam="Subtotaal",
            )
            parent = subtotaal

        # Eerst per ruimte delen, daarna salderen, daarna éénmaal afronden op hele m²
        # (#391). Punten staan op de stelselgroep, niet op de gedeeld-met-laag (#393).
        oppervlakte_totaal_na_delen = Decimal("0")
        for ruimte in overige_ruimten:
            oppervlakte_totaal_na_delen += toe_te_rekenen_oppervlakte(ruimte)
            deler = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            waardeer_oppervlakte_van_overige_ruimte(
                ruimte,
                waarderingsgroep_builder=parent.gedeeld_met(
                    aantal_onzelfstandige_woonruimten=deler,
                ),
            )

        punten_uit_m2 = bereken_oppervlakte_punten(
            oppervlakte_totaal_na_delen, Decimal("0.75")
        )
        if subtotaal is not None:
            subtotaal.punten = float(punten_uit_m2)

        # maak_zolder_correctie_waardering is hier niet bruikbaar: die helper gaat
        # uit van ongedeelde zolder-m² tegen een ongedeeld totaal en een vaste
        # maximumaftrek van 5 punten. Daarom wordt bereken_zolder_correctie hier
        # met toe te rekenen m² en een gedeelde maximumaftrek aangeroepen.
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
        if subtotaal is None:
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
