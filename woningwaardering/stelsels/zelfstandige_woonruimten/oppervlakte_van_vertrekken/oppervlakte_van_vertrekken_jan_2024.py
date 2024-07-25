from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import naar_tabel, rond_af
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import (
    classificeer_ruimte,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort
from woningwaardering.vera.utils import badruimte_met_toilet


class OppervlakteVanVertrekkenJan2024(Stelselgroepversie):
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
                stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        for ruimte in eenheid.ruimten or []:
            criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

            # Indien een toilet in een badruimte of doucheruimte is geplaatst, wordt de oppervlakte van die ruimte met 1m2 verminderd.
            if badruimte_met_toilet(ruimte):
                ruimte.oppervlakte = float(
                    Decimal(str(ruimte.oppervlakte)) - Decimal("1")
                )
                criterium_naam += " (1m2 verminderd ivm toilet)"
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}): toilet gevonden. 1m2 in mindering gebracht van de oppervlakte van de ruimte."
                )

            if classificeer_ruimte(ruimte) == Ruimtesoort.vertrek:
                woningwaardering = WoningwaarderingResultatenWoningwaardering()

                if (
                    not ruimte.gedeeld_met_aantal_eenheden
                    or ruimte.gedeeld_met_aantal_eenheden <= 1
                ):
                    woningwaardering.criterium = (
                        WoningwaarderingResultatenWoningwaarderingCriterium(
                            meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                            naam=criterium_naam,
                        )
                    )

                    woningwaardering.aantal = float(
                        rond_af(ruimte.oppervlakte, decimalen=2)
                    )

                elif (
                    ruimte.gedeeld_met_aantal_eenheden
                    and ruimte.gedeeld_met_aantal_eenheden >= 2
                ):
                    woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                        meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                        naam=f"{criterium_naam} (~{rond_af(ruimte.oppervlakte, decimalen=2)}m2, gedeeld met {ruimte.gedeeld_met_aantal_eenheden})",
                    )

                    woningwaardering.aantal = float(
                        rond_af(
                            rond_af(ruimte.oppervlakte, decimalen=2)
                            / ruimte.gedeeld_met_aantal_eenheden,
                            decimalen=2,
                        )
                    )

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = rond_af(
            sum(
                Decimal(str(woningwaardering.aantal))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.aantal is not None
            ),
            decimalen=0,
        ) * Decimal("1")

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    oppervlakteVanVertrekkenJan2024 = OppervlakteVanVertrekkenJan2024()
    with open(
        "tests/data/zelfstandige_woonruimten/input/12006000004.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

        woningwaardering_resultaat = oppervlakteVanVertrekkenJan2024.bereken(eenheid)

        print(
            woningwaardering_resultaat.model_dump_json(
                by_alias=True, indent=2, exclude_none=True
            )
        )

        tabel = naar_tabel(woningwaardering_resultaat)

        print(tabel)
