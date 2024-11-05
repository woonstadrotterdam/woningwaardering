import warnings
from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import classificeer_ruimte
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
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.buitenruimten  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    @staticmethod
    def _maximering(
        eenheid: EenhedenEenheid,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        punten = sum(
            woningwaardering.punten
            for woningwaardering in woningwaardering_groep.woningwaarderingen or []
            if woningwaardering.punten is not None
            and woningwaardering.criterium is not None
            and woningwaardering.criterium.bovenliggende_criterium is None
        )
        max_punten = 15
        if (
            punten > max_punten and woningwaardering_groep.woningwaarderingen
        ):  # maximaal 15 punten
            aftrek = max_punten - punten

            logger.info(
                f"Eenheid {eenheid.id}: maximaal aantal punten voor buitenruimten overschreden ({punten} > {max_punten}). Een aftrek van {aftrek} punt(en) wordt toegepast."
            )
            punten += aftrek
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Maximaal 15 punten",
                )
            )
            woningwaardering.punten = float(aftrek)
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        woningwaardering_groep.punten = float(utils.rond_af_op_kwart(punten))
        return woningwaardering_groep

    @staticmethod
    def _punten_per_buitenruimte(
        ruimte: EenhedenRuimte,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        if classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte or (
            ruimte.detail_soort is not None
            and ruimte.detail_soort.code
            in [
                Ruimtedetailsoort.stalling_extern.code,
                Ruimtedetailsoort.stalling_intern.code,
            ]
        ):
            if not ruimte.oppervlakte:
                warnings.warn(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen oppervlakte",
                    UserWarning,
                )
                return
            if (
                ruimte.gedeeld_met_aantal_eenheden
                and ruimte.gedeeld_met_aantal_eenheden >= 2
            ):
                # Gemeenschappelijke buitenruimten hebben een minimumafmeting van 2 m x 1,5 m, 1,5 m (hoogte, lengte, breedte)
                if not (ruimte.lengte and ruimte.breedte):
                    warnings.warn(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) is een gedeelde buitenruimte, maar heeft geen lengte en/of breedte, terwijl daar wel eisen voor zijn: (h, l, b) >= (2, 1.5, 1.5).",
                        UserWarning,
                    )
                if (
                    (ruimte.hoogte and ruimte.hoogte < 2)
                    or (ruimte.lengte and ruimte.lengte < 1.5)
                    or (ruimte.breedte and ruimte.breedte < 1.5)
                ):
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) is een met {ruimte.gedeeld_met_aantal_eenheden} gedeelde buitenruimte met een (h, l, b) kleiner dan (2, 1.5, 1.5) en wordt daarom niet gewaardeerd."
                    )
                    return
            # Parkeerplaatsen worden alleen gewaardeerd als privé-buitenruimten
            if (
                ruimte.detail_soort
                and ruimte.detail_soort.code == Ruimtedetailsoort.parkeerplaats.code
                and (
                    ruimte.gedeeld_met_aantal_eenheden
                    and ruimte.gedeeld_met_aantal_eenheden >= 2
                )
                or (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                    and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 2
                )
            ):
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) is een gedeelde parkeerplaats en wordt daarom niet gewaardeerd voor stelselgroep {Woningwaarderingstelselgroep.buitenruimten.naam}."
                )
                return
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                naam=ruimte.naam
                if ruimte.gedeeld_met_aantal_eenheden is None
                or ruimte.gedeeld_met_aantal_eenheden < 2
                else f"{ruimte.naam} (gedeeld met {ruimte.gedeeld_met_aantal_eenheden} adressen)",
            )
            woningwaardering.aantal = float(
                utils.rond_af(ruimte.oppervlakte, decimalen=2)
            )
            # Voor privé-buitenruimten worden in ieder geval 2 punten toegekend en vervolgens per vierkante meter 0,75 punt.
            # De in ieder geval 2 punten worden verderop toegevoegd.
            if (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten > 1
            ):
                woningwaardering.punten = float(
                    Decimal(str(ruimte.oppervlakte))
                    * Decimal("0.75")
                    / Decimal(str(ruimte.gedeeld_met_aantal_eenheden or 1))
                    / Decimal(str(ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten))
                )
            else:
                woningwaardering.punten = float(
                    Decimal(str(ruimte.oppervlakte))
                    * Decimal("0.35")
                    / Decimal(str(ruimte.gedeeld_met_aantal_eenheden or 1))
                )
            yield woningwaardering

    def _saldering(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
    ) -> WoningwaarderingResultatenWoningwaardering | None:
        # 2 punten bij de aanwezigheid van privé buitenruimten
        if woningwaardering_groep.woningwaarderingen and any(
            classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte
            and (
                ruimte.gedeeld_met_aantal_eenheden is None
                or ruimte.gedeeld_met_aantal_eenheden < 2
            )
            and (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is None
                or ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten < 2
            )
            for ruimte in eenheid.ruimten or []
        ):
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Privé buitenruimten aanwezig",
                    bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                        id=f"{self.stelselgroep.name}_prive"
                    ),
                )
            )
            woningwaardering.punten = 2.0
            return woningwaardering
        return None

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
        | None = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.buitenruimten.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []
        gedeeld_met_counter: defaultdict[int, float] = defaultdict(float)
        # punten per buitenruimte
        for ruimte in eenheid.ruimten or []:
            woningwaarderingen = self._punten_per_buitenruimte(ruimte)
            for woningwaardering in woningwaarderingen:
                if woningwaardering.criterium is None:
                    continue

                if (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                    and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten > 1
                ):
                    woningwaardering.criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                        id=f"{self.stelselgroep.name}_gedeeld_met_{ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten}_onzelfstandige_woonruimten"
                    )
                    if woningwaardering.punten is not None:
                        gedeeld_met_counter[
                            ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                        ] += woningwaardering.punten
                elif (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is None
                    or ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten < 2
                ) and (
                    ruimte.gedeeld_met_aantal_eenheden is None
                    or ruimte.gedeeld_met_aantal_eenheden < 2
                ):
                    woningwaardering.criterium.bovenliggende_criterium = (
                        WoningwaarderingCriteriumSleutels(
                            id=f"{self.stelselgroep.name}_prive"
                        )
                    )
                    if woningwaardering.punten is not None:
                        gedeeld_met_counter[1] += woningwaardering.punten
                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        # minimaal 2 punten bij aanwezigheid van privé buitenruimten
        if (result := self._saldering(eenheid, woningwaardering_groep)) is not None:
            woningwaardering_groep.woningwaarderingen.append(result)
            if result.punten is not None:
                gedeeld_met_counter[1] += result.punten

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        for aantal, punten in gedeeld_met_counter.items():
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=f"Totaal (gedeeld met {aantal} onzelfstandige woonruimten)"
                if aantal > 1
                else "Totaal (privé)",
                id=f"{self.stelselgroep.name}_gedeeld_met_{aantal}_onzelfstandige_woonruimten"
                if aantal > 1
                else f"{self.stelselgroep.name}_prive",
            )
            woningwaardering.punten = punten
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        woningwaardering_groep.punten = sum(
            woningwaardering.punten
            for woningwaardering in woningwaardering_groep.woningwaarderingen or []
            if woningwaardering.punten is not None
            and woningwaardering.criterium is not None
            and woningwaardering.criterium.bovenliggende_criterium is None
        )

        # maximaal 15 punten
        woningwaardering_groep = self._maximering(eenheid, woningwaardering_groep)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.buitenruimten.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    stelselgroep = Buitenruimten()
    with open(
        "tests/data/generiek/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
