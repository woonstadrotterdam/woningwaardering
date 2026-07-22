import warnings
from datetime import date
from decimal import Decimal
from typing import Generator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    gedeeld_met_adressen,
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
        waarderingsgroep_builder = WaarderingsgroepBuilder(
            self.stelsel, self.stelselgroep
        )

        for ruimte in eenheid.ruimten or []:
            for bron in self._punten_voor_buitenruimte(ruimte):
                laag = waarderingsgroep_builder.gedeeld_met(
                    aantal_adressen=ruimte.gedeeld_met_aantal_adressen or 1,
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

        # twee 2 punten voor de aanwezigheid van privé buitenruimten
        self._prive_buitenruimten_aanwezig(waarderingsgroep_builder, eenheid)

        woningwaardering_groep = waarderingsgroep_builder.bouw()

        # maximaal 15 punten
        if self._maximering(waarderingsgroep_builder, eenheid, woningwaardering_groep):
            woningwaardering_groep = waarderingsgroep_builder.bouw()

        # rond af op kwarten
        woningwaardering_groep.punten = float(
            utils.rond_af_op_kwart(woningwaardering_groep.punten)
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _maximering(
        self,
        waarderingsgroep_builder: WaarderingsgroepBuilder,
        eenheid: EenhedenEenheid,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
    ) -> WaarderingBuilder | None:
        """Berekent de maximering voor Buitenruimten. Maximaal 15 punten toegestaan.

        Args:
            waarderingsgroep_builder (WaarderingsgroepBuilder): Builder waaraan de maximering wordt toegevoegd.
            eenheid (EenhedenEenheid): Eenheid waarvoor de maximering berekend wordt.
            woningwaardering_groep (WoningwaarderingResultatenWoningwaarderingGroep): Woningwaardering groep van buitenruimten.

        Returns:
            WaarderingBuilder | None: Maximering als er een maximering is.
        """
        punten = Decimal(str(woningwaardering_groep.punten or "0"))
        max_punten = Decimal("15")
        if punten > max_punten:
            aftrek = max_punten - punten
            logger.info(
                f"Eenheid ({eenheid.id}): maximaal aantal punten voor {self.stelselgroep.naam} overschreden ({punten} > {max_punten}). {aftrek} punt(en) aftrek."
            )
            return waarderingsgroep_builder.maak_onderliggende(
                id="maximaal_15_punten",
                naam="Maximaal 15 punten",
                punten=float(aftrek),
            )
        return None

    def _punten_voor_buitenruimte(
        self,
        ruimte: EenhedenRuimte,
    ) -> Generator[WoningwaarderingResultatenWoningwaardering, None, None]:
        """Berekent de punten voor een ruimte voor rubriek Buitenruimten.

        0.75 punten per m2 voor gedeelde buitenruimten.
        0.35 punten per m2 voor privé buitenruimten.

        Ruimte moet minimaal een afmeting hebben van 2 m x 1,5 m x 1,5 m (hoogte, lengte, breedte).
        Parkeerplaatsen worden niet meegewaardeerd als ze gedeeld zijn met andere eenheden.

        Args:
            ruimte (EenhedenRuimte): Ruimte waarvoor de punten berekend worden.

        Yields:
            WoningwaarderingResultatenWoningwaardering: Punten voor de buitenruimte.
        """
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

        if gedeeld_met_adressen(ruimte):
            # Gemeenschappelijke buitenruimten hebben een minimumafmeting van 2 m x 1,5 m, 1,5 m (hoogte, lengte, breedte)
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
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een met {ruimte.gedeeld_met_aantal_adressen} gedeelde buitenruimte met een (h, l, b) kleiner dan (2, 1.5, 1.5) en wordt daarom niet gewaardeerd."
                )
                return

        # Parkeerplaatsen worden alleen gewaardeerd als ze niet gedeeld zijn met andere eenheden
        if (
            ruimte.detail_soort
            == Ruimtedetailsoort.parkeerplaats  # parkeerplaats heeft als ruimtesoort buitenruimte
            and gedeeld_met_adressen(ruimte)
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
        # Voor privé-buitenruimten worden in ieder geval 2 punten toegekend en vervolgens per vierkante meter 0,75 punt.
        # De in ieder geval 2 punten worden verderop toegevoegd.
        if gedeeld_met_onzelfstandige_woonruimten(ruimte):
            deler = Decimal(
                (ruimte.gedeeld_met_aantal_adressen or 1)
                * (ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1)
            )
            waardering.punten = float(
                Decimal(str(ruimte.oppervlakte)) * Decimal("0.75") / deler
            )
        else:
            waardering.punten = float(
                Decimal(str(ruimte.oppervlakte))
                * Decimal("0.35")
                / Decimal(str(ruimte.gedeeld_met_aantal_adressen or 1))
            )
        yield waardering

    def _prive_buitenruimten_aanwezig(
        self,
        waarderingsgroep_builder: WaarderingsgroepBuilder,
        eenheid: EenhedenEenheid,
    ) -> WaarderingBuilder | None:
        """Kent 2 punten toe bij de aanwezigheid van privé buitenruimten.

        Args:
            waarderingsgroep_builder (WaarderingsgroepBuilder): Builder waaraan de waardering wordt toegevoegd.
            eenheid (EenhedenEenheid): Eenheid waarvoor de punten berekend worden.

        Returns:
            WaarderingBuilder | None: Woningwaardering met 2 punten als er privé buitenruimten aanwezig zijn.
        """
        # 2 punten bij de aanwezigheid van privé buitenruimten
        if next(waarderingsgroep_builder.alle_waarderingen(), None) is not None and any(
            classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte
            and not gedeeld_met_adressen(ruimte)
            and not gedeeld_met_onzelfstandige_woonruimten(ruimte)
            for ruimte in eenheid.ruimten or []
        ):
            prive_laag = waarderingsgroep_builder.gedeeld_met()
            return prive_laag.maak_onderliggende(
                id="prive_buitenruimten_aanwezig",
                naam="Privé buitenruimten aanwezig",
                punten=2.0,
            )
        return None


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Buitenruimten(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/buitenruimten/input/oprit.json"
        )
