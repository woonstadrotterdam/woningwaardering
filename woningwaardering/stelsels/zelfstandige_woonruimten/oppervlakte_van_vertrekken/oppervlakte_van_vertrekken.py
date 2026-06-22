from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_oppervlakte_van_vertrek,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.woningwaardering_groep import WoningwaarderingGroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
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
        super().__init__(
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_vertrekken

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

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        for ruimte in ruimten:
            for bron in waardeer_oppervlakte_van_vertrek(ruimte):
                if bron.criterium is None:
                    continue
                onderliggend_id = utils.criteriumid_onder_stelselgroep(
                    bron.criterium.id, self.stelselgroep.name
                )
                if onderliggend_id is None:
                    if bron.criterium.id == self.stelselgroep.name:
                        onderliggend_id = ruimte.id or "ruimte"
                    else:
                        continue
                elif onderliggend_id == "":
                    onderliggend_id = ruimte.id or "ruimte"
                woningwaardering_groep.met_onderliggend(
                    onderliggend_id,
                    naam=bron.criterium.naam,
                    aantal=bron.aantal,
                    meeteenheid=bron.criterium.meeteenheid,
                )

        punten = utils.rond_af_op_kwart(
            utils.rond_af(
                sum(
                    Decimal(str(woningwaardering.aantal))
                    for woningwaardering in woningwaardering_groep.woningwaarderingen
                    or []
                    if woningwaardering.aantal is not None
                ),
                decimalen=0,
            )
            * Decimal("1")
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=OppervlakteVanVertrekken(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
