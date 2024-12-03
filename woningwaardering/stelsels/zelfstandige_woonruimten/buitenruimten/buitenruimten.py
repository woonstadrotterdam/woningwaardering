import re
import warnings
from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    gedeeld_met_eenheden,
)
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
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort


class Buitenruimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.buitenruimten
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
        | None = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel.value,
                stelselgroep=self.stelselgroep.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        # punten per buitenruimte
        for ruimte in eenheid.ruimten or []:
            woningwaarderingen = self._punten_voor_buitenruimte(ruimte)
            woningwaardering_groep.woningwaarderingen.extend(woningwaarderingen)

        # minimaal 2 punten bij aanwezigheid van privé buitenruimten
        # 5 aftrekpunten bij geen buitenruimten
        if (
            result := self._prive_buitenruimten_aanwezig(
                eenheid, woningwaardering_groep
            )
        ) is not None:
            woningwaardering_groep.woningwaarderingen.append(result)

        som = defaultdict(float)
        for woningwaardering in woningwaardering_groep.woningwaarderingen or []:
            if woningwaardering.criterium.bovenliggende_criterium:
                som[woningwaardering.criterium.bovenliggende_criterium.id] += (
                    woningwaardering.punten
                )

        for id, punten in som.items():
            match = re.search(r"\d+", id)
            gedeeld_met = int(match.group()) if match else 1
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"Totaal ({gedeeld_met} gedeeld met {gedeeld_met} eenheden)"
                    if gedeeld_met > 1
                    else "Totaal (privé)",
                    id=id,
                )
            )
            woningwaardering.punten = punten
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        woningwaardering_groep.punten = float(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium is not None
                and woningwaardering.criterium.bovenliggende_criterium is None
            )
        )

        # maximaal 15 punten
        maximering = self._maximering(eenheid, woningwaardering_groep)
        if maximering:
            woningwaardering_groep.woningwaarderingen.append(maximering)
            woningwaardering_groep.punten += float(Decimal(str(maximering.punten)))

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
        eenheid: EenhedenEenheid,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
    ) -> WoningwaarderingResultatenWoningwaardering | None:
        punten = Decimal(str(woningwaardering_groep.punten or "0"))
        max_punten = Decimal("15")
        if (
            punten > max_punten and woningwaardering_groep.woningwaarderingen
        ):  # maximaal 15 punten
            aftrek = max_punten - punten

            logger.info(
                f"Eenheid ({eenheid.id}): maximaal aantal punten voor {Woningwaarderingstelselgroep.buitenruimten.naam} overschreden ({punten} > {max_punten}). {aftrek} punt(en) aftrek."
            )
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Maximaal 15 punten",
                )
            )
            woningwaardering.punten = float(aftrek)
            return woningwaardering

        return None

    def _punten_voor_buitenruimte(
        self, ruimte: EenhedenRuimte
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        if classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte:
            if not ruimte.oppervlakte:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte",
                    UserWarning,
                )
                return

            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            if (
                ruimte.gedeeld_met_aantal_eenheden
                and ruimte.gedeeld_met_aantal_eenheden >= 2
            ):  # gedeelde buitenruimte
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
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een met {ruimte.gedeeld_met_aantal_eenheden} gedeelde buitenruimte met een (h, l, b) kleiner dan (2, 1.5, 1.5) en wordt daarom niet gewaardeerd."
                    )
                    return
                # Parkeerplaatsen worden alleen gewaardeerd als privé-buitenruimten
                if (
                    ruimte.detail_soort
                    and ruimte.detail_soort.code == Ruimtedetailsoort.parkeerplaats.code
                ):
                    logger.debug(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een met {ruimte.gedeeld_met_aantal_eenheden} gedeelde parkeerplaats en telt niet mee voor {Woningwaarderingstelselgroep.buitenruimten.naam}"
                    )
                    return
                logger.debug(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een met {ruimte.gedeeld_met_aantal_eenheden} gedeelde buitenruimte van {ruimte.oppervlakte}m2 en telt mee voor {Woningwaarderingstelselgroep.buitenruimten.naam}"
                )
                woningwaardering.aantal = float(
                    utils.rond_af(
                        ruimte.oppervlakte / ruimte.gedeeld_met_aantal_eenheden,
                        decimalen=2,
                    )
                )

                # Voor gemeenschappelijk buitenruimten worden 0,75 per vierkante meter toegekend, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.
                woningwaardering.punten = float(
                    utils.rond_af(
                        ruimte.oppervlakte * 0.75 / ruimte.gedeeld_met_aantal_eenheden,
                        decimalen=2,
                    )
                )
                woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                    meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                    naam=ruimte.naam,
                    bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                        id=f"{self.stelselgroep.name}_gedeeld_met_{ruimte.gedeeld_met_aantal_eenheden}_eenheden",
                    ),
                )
            else:  # privé buitenruimte
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een privé-buitenruimte van {ruimte.oppervlakte}m2 en telt mee voor {Woningwaarderingstelselgroep.buitenruimten.naam}"
                )
                woningwaardering.criterium = (
                    WoningwaarderingResultatenWoningwaarderingCriterium(
                        meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                        naam=ruimte.naam,
                        bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                            id=f"{self.stelselgroep.name}_prive",
                        ),
                    )
                )
                woningwaardering.aantal = float(
                    utils.rond_af(ruimte.oppervlakte, decimalen=2)
                )
                # Voor privé-buitenruimten worden in ieder geval 2 punten toegekend en vervolgens per vierkante meter 0,35 punt.
                # De in ieder geval 2 punten worden verderop toegevoegd.
                woningwaardering.punten = float(
                    utils.rond_af(ruimte.oppervlakte * 0.35, decimalen=2)
                )
            yield woningwaardering

    def _prive_buitenruimten_aanwezig(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
    ) -> WoningwaarderingResultatenWoningwaardering | None:
        if not any(
            classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte
            for ruimte in eenheid.ruimten or []
        ):
            logger.info(
                f"Eenheid ({eenheid.id}) heeft geen buitenruimten of loggia. Vijf minpunten voor geen buitenruimten toegepast."
            )
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Geen buitenruimten",
                )
            )
            woningwaardering.punten = -5.0
            return woningwaardering

        # 2 punten bij de aanwezigheid van privé buitenruimten
        elif woningwaardering_groep.woningwaarderingen and any(
            classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte
            and not gedeeld_met_eenheden(ruimte)
            for ruimte in eenheid.ruimten or []
        ):
            logger.info(
                f"Eenheid ({eenheid.id}): privé buitenruimten aanwezig. 2 punten worden toegekend."
            )
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Privé buitenruimten aanwezig",
                    bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                        id=f"{self.stelselgroep.name}_prive",
                    ),
                )
            )
            woningwaardering.punten = 2.0
            return woningwaardering
        return None


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Buitenruimten(),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
