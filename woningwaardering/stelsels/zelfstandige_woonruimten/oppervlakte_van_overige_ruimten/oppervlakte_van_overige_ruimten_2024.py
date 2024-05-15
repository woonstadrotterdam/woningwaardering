from decimal import ROUND_HALF_UP, Decimal

from loguru import logger

from woningwaardering.stelsels import Stelselgroepversie
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import (
    classificeer_ruimte,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
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
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element


class OppervlakteVanOverigeRuimten2024(Stelselgroepversie):
    @staticmethod
    def bereken(
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.value,
            ),
        )

        woningwaardering_groep.woningwaarderingen = []

        for ruimte in eenheid.ruimten or []:
            if ruimte.oppervlakte is None:
                error_msg = f"ruimte {ruimte.id} heeft geen oppervlakte"
                raise TypeError(error_msg)
            if ruimte.detail_soort is None:
                error_msg = f"ruimte {ruimte.id} heeft geen detailsoort"
                raise TypeError(error_msg)

            criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

            if classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimtes:
                if ruimte.oppervlakte < 2:
                    logger.debug(
                        f"{ruimte.naam} {ruimte.detail_soort.code} is kleiner dan 2 vierkante meter"
                    )
                    continue

                woningwaardering = WoningwaarderingResultatenWoningwaardering()

                woningwaardering.criterium = (
                    WoningwaarderingResultatenWoningwaarderingCriterium(
                        meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                        naam=criterium_naam,
                    )
                )

                if (
                    ruimte.gedeeld_met_aantal_eenheden is not None
                    and ruimte.gedeeld_met_aantal_eenheden > 1
                    and ruimte.detail_soort.code == Ruimtedetailsoort.berging.code
                ):
                    oppervlakte_per_eenheid = Decimal(
                        ruimte.oppervlakte / ruimte.gedeeld_met_aantal_eenheden
                    )

                    if oppervlakte_per_eenheid >= 2:
                        woningwaardering.aantal = float(
                            (
                                Decimal(str(ruimte.oppervlakte)).quantize(
                                    Decimal("1"), ROUND_HALF_UP
                                )
                                / Decimal(str(ruimte.gedeeld_met_aantal_eenheden))
                            ).quantize(Decimal("0.01"), ROUND_HALF_UP)
                        )
                    else:
                        logger.debug(
                            f"{ruimte.naam} {ruimte.detail_soort.code} is kleiner dan 2 vierkante meter per eenheid en komt niet in aanmerking voor een puntenwaardering onder {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
                        )
                        continue

                elif ruimte.detail_soort.code == Ruimtedetailsoort.zolder.code:
                    oppervlakte_aantal = OppervlakteVanOverigeRuimten2024._oppervlakte_zolder_overige_ruimte(
                        ruimte
                    )
                    if oppervlakte_aantal > 0.0:
                        woningwaardering.aantal = oppervlakte_aantal
                    else:
                        continue

                else:
                    woningwaardering.aantal = float(
                        Decimal(str(ruimte.oppervlakte)).quantize(
                            Decimal("0.01"), ROUND_HALF_UP
                        )
                    )

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.aantal))
                for woningwaardering in (
                    woningwaardering_groep.woningwaarderingen or []
                )
                if woningwaardering.aantal is not None
            )
        ).quantize(Decimal("1"), ROUND_HALF_UP) * Decimal("0.75")

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep

    @staticmethod
    def _oppervlakte_zolder_overige_ruimte(ruimte: EenhedenRuimte) -> float:
        """
        Berekent de oppervlakte voor een zolder van een overige ruimte op basis van een EenhedenRuimte object.

        Args:
            ruimte (EenhedenRuimte): Het EenhedenRuimte object dat een zolder type is.

        Returns:
            float: De berekende oppervlakte voor de zolder.
        """
        if ruimte.detail_soort is not None and ruimte.oppervlakte is not None:
            trap = heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.trap.code
            )

            if trap:
                logger.debug(
                    f"Trap gevonden in {ruimte.naam} ({ruimte.id}): telt mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
                )
                return float(
                    Decimal(str(ruimte.oppervlakte)).quantize(
                        Decimal("0.01"), ROUND_HALF_UP
                    )
                )

            vlizotrap = heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.vlizotrap.code
            )

            if vlizotrap:
                logger.debug(
                    f"Vlizotrap gevonden in {ruimte.naam} ({ruimte.id}): telt mee voor oppervlakte van overige ruimten"
                )
                return max(
                    0.0,
                    float(
                        Decimal(
                            Decimal(str(ruimte.oppervlakte)).quantize(
                                Decimal("0.01"), ROUND_HALF_UP
                            )
                            # Min 5 punten omdat de ruimte niet bereikt kan worden met een
                            # vaste trap.
                            # Let op, hier wordt de oppervlakte gecorrigeerd met de
                            # hoeveelheid punten per vierkante meter. Onze keuze is om hier
                            # al de vijf punten in mindering te brengen. Het beleidsboek
                            # geeft aan dat de punten in mindering gebracht moeten worden
                            # op de punten berekend voor deze ruimte, maar ook dat punten
                            # pas berekend moeten worden wanneer de totale oppervlakte
                            # bekend is en afegerond is.
                            # Door de afronding komt deze berekening niet helemaal juist
                            # uit, maar dit is de benadering waar wij nu voor kiezen.
                            - Decimal("5") / Decimal("0.75")
                        ).quantize(Decimal("0.01"), ROUND_HALF_UP)
                    ),
                )

        logger.warning(
            f"Geen trap gevonden in {ruimte.naam} ({ruimte.id}): telt niet mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
        )
        return 0.0


if __name__ == "__main__":
    logger.enable("woningwaardering")

    oppervlakte_van_overige_ruimten = OppervlakteVanOverigeRuimten2024()
    with open(
        "tests/data/input/zelfstandige_woonruimten/85651000021.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = oppervlakte_van_overige_ruimten.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = naar_tabel(woningwaardering_resultaat)

    print(tabel)
