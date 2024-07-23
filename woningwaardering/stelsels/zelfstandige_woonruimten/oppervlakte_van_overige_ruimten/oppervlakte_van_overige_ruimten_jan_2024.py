import warnings
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import Stelselgroepversie
from woningwaardering.stelsels.utils import naar_tabel, rond_af
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


class OppervlakteVanOverigeRuimtenJan2024(Stelselgroepversie):
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
                stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.value,
            ),
        )

        woningwaardering_groep.woningwaarderingen = []

        for ruimte in eenheid.ruimten or []:
            if ruimte.oppervlakte is None:
                message = f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen oppervlakte"
                warnings.warn(message, UserWarning)
                return woningwaardering_groep

            if ruimte.detail_soort is None:
                message = f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detailsoort"
                warnings.warn(message, UserWarning)
                return woningwaardering_groep

            criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

            if classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten:
                if ruimte.oppervlakte < 2:
                    logger.debug(
                        f"Ruimte {ruimte.naam} ({ruimte.id}): {ruimte.oppervlakte = }m2"
                    )
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) is kleiner dan 2 m2 en telt daarom niet mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}."
                    )
                    continue

                woningwaardering = WoningwaarderingResultatenWoningwaardering()

                gedeelde_ruimte = (
                    ruimte.gedeeld_met_aantal_eenheden
                    and ruimte.gedeeld_met_aantal_eenheden >= 2
                )

                woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                    meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                    naam=criterium_naam
                    if not gedeelde_ruimte
                    else f"{criterium_naam} (~{rond_af(ruimte.oppervlakte, decimalen=2)}m2, gedeeld met {ruimte.gedeeld_met_aantal_eenheden})",
                )

                if gedeelde_ruimte:
                    oppervlakte_per_eenheid = Decimal(
                        ruimte.oppervlakte / (ruimte.gedeeld_met_aantal_eenheden or 1)
                    )

                    if (
                        (
                            ruimte.detail_soort.code == Ruimtedetailsoort.berging.code
                            and oppervlakte_per_eenheid
                            >= 2  # Gemeenschappelijke bergingen worden gewaardeerd als overige ruimte als (...) de oppervlakte, na deling door het aantal woningen, per woning minstens 2m2 bedraagt.
                        )
                        or ruimte.detail_soort.code != Ruimtedetailsoort.berging.code
                    ):  # bij niet-bergingen staat geen specifieke eis in de regelgeving m.b.t. oppervlakte na deling door aantal woningen.
                        woningwaardering.aantal = float(
                            rond_af(
                                rond_af(ruimte.oppervlakte, decimalen=0)
                                / Decimal(str(ruimte.gedeeld_met_aantal_eenheden)),
                                decimalen=2,
                            )
                        )

                    else:
                        logger.info(
                            f"Ruimte {ruimte.naam} ({ruimte.id}) is kleiner dan 2 m2 per eenheid en komt niet in aanmerking voor een puntenwaardering onder {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
                        )
                        continue

                elif ruimte.detail_soort.code == Ruimtedetailsoort.zolder.code:
                    oppervlakte_aantal = OppervlakteVanOverigeRuimtenJan2024._oppervlakte_zolder_overige_ruimte(
                        ruimte
                    )
                    if oppervlakte_aantal > 0.0:
                        woningwaardering.aantal = oppervlakte_aantal
                    else:
                        continue

                else:
                    woningwaardering.aantal = float(
                        rond_af(ruimte.oppervlakte, decimalen=2)
                    )

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = rond_af(
            sum(
                Decimal(str(woningwaardering.aantal))
                for woningwaardering in (
                    woningwaardering_groep.woningwaarderingen or []
                )
                if woningwaardering.aantal is not None
            ),
            decimalen=0,
        ) * Decimal("0.75")

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
        )

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
            trap = heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.trap)

            if trap:
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}): trap gevonden. Telt mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
                )
                return float(rond_af(ruimte.oppervlakte, decimalen=2))

            vlizotrap = heeft_bouwkundig_element(
                ruimte, Bouwkundigelementdetailsoort.vlizotrap
            )

            if vlizotrap:
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}): vlizotrap gevonden. Telt mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
                )
                return max(
                    0.0,
                    float(
                        rond_af(
                            Decimal(
                                rond_af(ruimte.oppervlakte, decimalen=2)
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
                            ),
                            decimalen=2,
                        )
                    ),
                )

        logger.info(
            f"Ruimte {ruimte.naam} ({ruimte.id}): geen trap gevonden en telt dus niet mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
        )
        return 0.0


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    oppervlakte_van_overige_ruimten = OppervlakteVanOverigeRuimtenJan2024()
    with open(
        "tests/data/generiek/input/37101000032.json",
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
