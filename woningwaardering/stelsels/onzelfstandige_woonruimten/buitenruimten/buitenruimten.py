import warnings
from datetime import date
from decimal import Decimal
from typing import Generator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    gedeeld_met_eenheden,
    gedeeld_met_onzelfstandige_woonruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class Buitenruimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.buitenruimten  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            peildatum=peildatum,
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
        | None = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        waarderingsgroep_bouwer = WaarderingsgroepBouwer(
            self.stelsel, self.stelselgroep
        )

        for ruimte in eenheid.ruimten or []:
            for bron in self._punten_voor_buitenruimte(ruimte):
                laag = waarderingsgroep_bouwer.gedeeld_met_laag(
                    aantal_eenheden=ruimte.gedeeld_met_aantal_eenheden or 1,
                    aantal_onzelfstandige_woonruimten=(
                        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                    ),
                )
                laag.maak_onderliggende(
                    id=ruimte.id or "ruimte",
                    naam=ruimte.naam or "",
                    punten=bron.punten,
                    aantal=bron.aantal,
                    meeteenheid=Meeteenheid.vierkante_meter_m2,
                )

        self._prive_buitenruimten_aanwezig(waarderingsgroep_bouwer, eenheid)

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        if self._maximering(waarderingsgroep_bouwer, eenheid, woningwaardering_groep):
            woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        woningwaardering_groep.punten = float(
            utils.rond_af_op_kwart(woningwaardering_groep.punten)
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _maximering(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        eenheid: EenhedenEenheid,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
    ) -> WaarderingBouwer | None:
        punten = Decimal(str(woningwaardering_groep.punten or "0"))
        max_punten = Decimal("15")
        if punten > max_punten:
            aftrek = max_punten - punten
            logger.info(
                f"Eenheid ({eenheid.id}): maximaal aantal punten voor {self.stelselgroep.naam} overschreden ({punten} > {max_punten}). {aftrek} punt(en) aftrek."
            )
            return waarderingsgroep_bouwer.maak_onderliggende(
                id="maximaal_15_punten",
                naam="Maximaal 15 punten",
                punten=float(aftrek),
            )
        return None

    def _punten_voor_buitenruimte(
        self,
        ruimte: EenhedenRuimte,
    ) -> Generator[WoningwaarderingResultatenWoningwaardering, None, None]:
        if classificeer_ruimte(ruimte) != Ruimtesoort.buitenruimte:
            logger.debug(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {self.stelselgroep.naam}."
            )
            return

        if not ruimte.oppervlakte:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte",
                UserWarning,
            )
            return

        if gedeeld_met_eenheden(ruimte):
            if not (ruimte.lengte and ruimte.breedte):
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een gedeelde buitenruimte, maar heeft geen lengte en/of breedte, terwijl daar wel eisen voor zijn: (h, l, b) >= (2, 1.5, 1.5).",
                    UserWarning,
                )
            if (
                (ruimte.hoogte and ruimte.hoogte < 2)
                or (ruimte.lengte and ruimte.lengte < 1.5)
                or (ruimte.breedte and ruimte.breedte < 1.5)
            ):
                logger.debug(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een met {ruimte.gedeeld_met_aantal_eenheden} gedeelde buitenruimte met een (h, l, b) kleiner dan (2, 1.5, 1.5) en wordt daarom niet gewaardeerd."
                )
                return

        if (
            ruimte.detail_soort == Ruimtedetailsoort.parkeerplaats
            and gedeeld_met_eenheden(ruimte)
        ):
            logger.debug(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een gedeelde parkeerplaats en telt daarom niet mee voor {self.stelselgroep.naam}."
            )
            return

        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) van {ruimte.oppervlakte:.2f}m2 telt mee voor {self.stelselgroep.naam}."
        )

        waardering = WoningwaarderingResultatenWoningwaardering()
        waardering.aantal = float(utils.rond_af(ruimte.oppervlakte, decimalen=2))
        if gedeeld_met_onzelfstandige_woonruimten(ruimte):
            waardering.punten = float(
                Decimal(str(ruimte.oppervlakte))
                * Decimal("0.75")
                / Decimal(str(ruimte.gedeeld_met_aantal_eenheden or 1))
                / Decimal(
                    str(ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1)
                )
            )
        else:
            waardering.punten = float(
                Decimal(str(ruimte.oppervlakte))
                * Decimal("0.35")
                / Decimal(str(ruimte.gedeeld_met_aantal_eenheden or 1))
            )
        yield waardering

    def _prive_buitenruimten_aanwezig(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        eenheid: EenhedenEenheid,
    ) -> WaarderingBouwer | None:
        if next(waarderingsgroep_bouwer.alle_waarderingen(), None) is not None and any(
            classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte
            and not gedeeld_met_eenheden(ruimte)
            and not gedeeld_met_onzelfstandige_woonruimten(ruimte)
            for ruimte in eenheid.ruimten or []
        ):
            prive_laag = waarderingsgroep_bouwer.gedeeld_met_laag(
                aantal_eenheden=1,
                aantal_onzelfstandige_woonruimten=1,
            )
            return prive_laag.maak_onderliggende(
                id="prive_buitenruimten_aanwezig",
                naam="Privé buitenruimten aanwezig",
                punten=2.0,
            )
        return None


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Buitenruimten(peildatum=date(2026, 1, 1)),
        strict=False,
        log_level="DEBUG",
    ) as waarderingsgroep_bouwer:
        waarderingsgroep_bouwer.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/buitenruimten/input/oprit.json"
        )
