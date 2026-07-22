import warnings
from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Iterator

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
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
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
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.buitenruimten
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

        totaal_criteria: dict[WaarderingBuilder, int] = {}

        # punten per buitenruimte
        for ruimte in eenheid.ruimten or []:
            for _ in self._punten_voor_buitenruimte(
                waarderingsgroep_builder, ruimte, totaal_criteria
            ):
                pass

        # minimaal 2 punten bij aanwezigheid van privé buitenruimten
        # 5 aftrekpunten bij geen buitenruimten
        self._prive_buitenruimten_aanwezig(waarderingsgroep_builder, eenheid)

        som_aantal: dict[WaarderingBuilder, Decimal] = defaultdict(lambda: Decimal("0"))
        for waardering in waarderingsgroep_builder.alle_waarderingen():
            gedeeld_met = waardering.bovenliggende
            if isinstance(gedeeld_met, WaarderingBuilder):
                som_aantal[gedeeld_met] += Decimal(str(waardering.aantal or "0"))

        for gedeeld_met, aantal_som in som_aantal.items():
            gedeeld_met_aantal = totaal_criteria[gedeeld_met]
            factor = Decimal("0.35") if gedeeld_met_aantal == 1 else Decimal("0.75")
            m2_afgerond = utils.rond_af(aantal_som, decimalen=0)
            punten_uit_m2 = m2_afgerond * factor / gedeeld_met_aantal
            gedeeld_met.punten = float(punten_uit_m2)
            gedeeld_met.aantal = float(m2_afgerond)
            gedeeld_met.meeteenheid = Meeteenheid.vierkante_meter_m2

        # maximaal 15 punten
        self._maximering(waarderingsgroep_builder, eenheid)

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
    ) -> None:
        waarderingen = list(waarderingsgroep_builder.alle_waarderingen())
        punten = Decimal(
            str(
                sum(
                    Decimal(str(waardering.punten))
                    for waardering in waarderingen
                    if waardering.punten is not None
                )
            )
        )
        max_punten = Decimal("15")
        if punten > max_punten and waarderingen:  # maximaal 15 punten
            aftrek = max_punten - punten

            logger.info(
                f"Eenheid ({eenheid.id}): maximaal aantal punten voor {Woningwaarderingstelselgroep.buitenruimten.naam} overschreden ({punten} > {max_punten}). {aftrek} punt(en) aftrek."
            )
            waarderingsgroep_builder.met_onderliggend(
                id="maximering",
                naam="Maximaal 15 punten",
                punten=float(aftrek),
            )

    def _punten_voor_buitenruimte(
        self,
        waarderingsgroep_builder: WaarderingsgroepBuilder,
        ruimte: EenhedenRuimte,
        totaal_criteria: dict[WaarderingBuilder, int],
    ) -> Iterator[WaarderingBuilder]:
        if classificeer_ruimte(ruimte) != Ruimtesoort.buitenruimte:
            logger.debug(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.buitenruimten.naam}."
            )
            return

        if not ruimte.oppervlakte:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte",
                UserWarning,
            )
            return

        aantal_adressen = ruimte.gedeeld_met_aantal_adressen or 1
        if aantal_adressen >= 2:  # gedeelde buitenruimte
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
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een met {aantal_adressen} gedeelde buitenruimte met een (h, l, b) kleiner dan (2, 1.5, 1.5) en wordt daarom niet gewaardeerd."
                )
                return
            # Parkeerplaatsen worden alleen gewaardeerd als privé-buitenruimten
            if ruimte.detail_soort == Ruimtedetailsoort.parkeerplaats:
                logger.debug(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een met {aantal_adressen} gedeelde parkeerplaats en telt niet mee voor {Woningwaarderingstelselgroep.buitenruimten.naam}"
                )
                return
            logger.debug(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een met {aantal_adressen} gedeelde buitenruimte van {ruimte.oppervlakte}m2 en telt mee voor {Woningwaarderingstelselgroep.buitenruimten.naam}"
            )
            gedeeld_met = waarderingsgroep_builder.gedeeld_met(
                aantal_adressen=aantal_adressen,
            )
        else:
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een privé-buitenruimte van {ruimte.oppervlakte}m2 en telt mee voor {Woningwaarderingstelselgroep.buitenruimten.naam}"
            )
            gedeeld_met = waarderingsgroep_builder.gedeeld_met()

        totaal_criteria[gedeeld_met] = aantal_adressen

        waardering = gedeeld_met.met_onderliggend(
            id=ruimte.id or "ruimte",
            naam=ruimte.naam or "",
            meeteenheid=Meeteenheid.vierkante_meter_m2,
        )
        waardering.aantal = float(utils.rond_af(ruimte.oppervlakte, decimalen=2))
        yield waardering

    def _prive_buitenruimten_aanwezig(
        self,
        waarderingsgroep_builder: WaarderingsgroepBuilder,
        eenheid: EenhedenEenheid,
    ) -> None:
        if not any(
            classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte
            for ruimte in eenheid.ruimten or []
        ):
            logger.info(
                f"Eenheid ({eenheid.id}) heeft geen buitenruimten of loggia. Vijf minpunten voor geen buitenruimten toegepast."
            )
            waarderingsgroep_builder.met_onderliggend(
                id="geen_buitenruimten",
                naam="Geen buitenruimten",
                punten=-5.0,
            )
            return

        if any(waarderingsgroep_builder.alle_waarderingen()) and any(
            classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte
            and not gedeeld_met_adressen(ruimte)
            for ruimte in eenheid.ruimten or []
        ):
            logger.info(
                f"Eenheid ({eenheid.id}): privé buitenruimten aanwezig. 2 punten worden toegekend."
            )
            waarderingsgroep_builder.met_onderliggend(
                id="prive_buitenruimten_aanwezig",
                naam="Privé buitenruimten aanwezig",
                punten=2.0,
            )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Buitenruimten(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
