import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
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

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.buitenruimten.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        buitenruimten_aanwezig = False
        prive_buitenruimten_aanwezig = False
        for ruimte in eenheid.ruimten or []:
            if classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte:
                buitenruimten_aanwezig = True
                if not ruimte.oppervlakte:
                    warnings.warn(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen oppervlakte",
                        UserWarning,
                    )
                    continue

                woningwaardering = WoningwaarderingResultatenWoningwaardering()
                if (
                    ruimte.gedeeld_met_aantal_eenheden
                    and ruimte.gedeeld_met_aantal_eenheden >= 2
                ):  # gedeelde buitenruimte
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
                        continue
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) is een met {ruimte.gedeeld_met_aantal_eenheden} gedeelde buitenruimte met oppervlakte {ruimte.oppervlakte}m2 en wordt gewaardeerd onder stelselgroep {Woningwaarderingstelselgroep.buitenruimten.naam}."
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
                            ruimte.oppervlakte
                            * 0.75
                            / ruimte.gedeeld_met_aantal_eenheden,
                            decimalen=2,
                        )
                    )
                    woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                        meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                        naam=f"{ruimte.naam} (gedeeld met {ruimte.gedeeld_met_aantal_eenheden})",
                    )
                else:  # privé buitenruimte
                    prive_buitenruimten_aanwezig = True
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) is een privé-buitenruimte met oppervlakte {ruimte.oppervlakte}m2 en wordt gewaardeerd onder stelselgroep {Woningwaarderingstelselgroep.buitenruimten.naam}."
                    )
                    woningwaardering.criterium = (
                        WoningwaarderingResultatenWoningwaarderingCriterium(
                            meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                            naam=f"{ruimte.naam} (privé)",
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

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        if not buitenruimten_aanwezig:
            logger.info(
                f"Eenheid {eenheid.id} heeft geen buitenruimten of loggia. Vijf minpunten voor geen buitenruimten toegepast."
            )
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Geen buitenruimten",
                )
            )
            woningwaardering.punten = -5.0
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        # 2 punten bij de aanwezigheid van privé buitenruimten
        elif prive_buitenruimten_aanwezig:
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Privé buitenruimten aanwezig",
                )
            )
            woningwaardering.punten = 2.0
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
        )
        max_punten = 15
        if punten > max_punten:  # maximaal 15 punten
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

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.buitenruimten.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    buitenruimten = Buitenruimten(peildatum=date.fromisoformat("2024-07-01"))

    with open(
        "tests/data/zelfstandige_woonruimten/stelselgroepen/buitenruimten/input/te_kleine_buitenruimtes.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[buitenruimten.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
