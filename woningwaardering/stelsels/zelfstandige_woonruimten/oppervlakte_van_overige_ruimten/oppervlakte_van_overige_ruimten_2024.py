from decimal import ROUND_HALF_UP, Decimal

from loguru import logger

from woningwaardering.stelsels import Stelselgroepversie, utils
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import (
    vertrek_telt_als_vertrek,
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


def _oppervlakte_zolder_overige_ruimte(ruimte: EenhedenRuimte) -> float:
    """
    Berekent de oppervlakte voor een zolder van een overige ruimte op basis van een EenhedenRuimte object.

    Args:
        ruimte (EenhedenRuimte): Het EenhedenRuimte object dat een zolder type is.

    Returns:
        float: De berekende oppervlakte voor de zolder.
    """
    if ruimte.detail_soort is not None and ruimte.oppervlakte is not None:
        trap = [
            element.detail_soort
            for element in ruimte.bouwkundige_elementen or []
            if element.detail_soort
            and element.detail_soort.code == Bouwkundigelementdetailsoort.trap.code
        ]

        if trap:
            logger.debug(
                f"Trap gevonden in {ruimte.naam} ({ruimte.id}): telt mee voor oppervlakte van overige ruimten"
            )
            return float(
                Decimal(str(ruimte.oppervlakte)).quantize(
                    Decimal("0.01"), ROUND_HALF_UP
                )
            )

        vlizotrap = [
            element.detail_soort
            for element in ruimte.bouwkundige_elementen or []
            if element.detail_soort
            and element.detail_soort.code == Bouwkundigelementdetailsoort.vlizotrap.code
        ]

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
        f"Geen trap gevonden in {ruimte.naam} ({ruimte.id}): telt niet mee voor oppervlakte van overige ruimten"
    )
    return 0.0


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
                logger.warning(f"Ruimte {ruimte.id} heeft geen oppervlakte")
                continue
            if ruimte.detail_soort is None:
                logger.warning(f"Ruimte {ruimte.id} heeft geen detailsoort")
                continue
            if ruimte.detail_soort.code is None:
                logger.warning(f"Ruimte {ruimte.id} heeft geen detailsoortcode")
                continue

            if ruimte.soort is not None and (
                ruimte.soort.code == Ruimtesoort.overige_ruimtes.code
                or not vertrek_telt_als_vertrek(ruimte)
            ):
                if ruimte.detail_soort.code not in [
                    Ruimtedetailsoort.bijkeuken.code,
                    Ruimtedetailsoort.berging.code,
                    Ruimtedetailsoort.wasruimte.code,
                    Ruimtedetailsoort.garage.code,
                    Ruimtedetailsoort.zolder.code,
                    Ruimtedetailsoort.kelder.code,
                    Ruimtedetailsoort.parkeerplaats.code,
                    # Deze vertrekken kunnen als overige ruimte tellen
                    # wanneer ze niet aan bepaalde voorwaarden voldoen:
                    Ruimtedetailsoort.woonkamer.code,
                    Ruimtedetailsoort.woon_en_of_slaapkamer.code,
                    Ruimtedetailsoort.woonkamer_en_of_keuken.code,
                    Ruimtedetailsoort.keuken.code,
                    Ruimtedetailsoort.overig_vertrek.code,
                    Ruimtedetailsoort.badkamer.code,
                    Ruimtedetailsoort.badkamer_en_of_toilet.code,
                    Ruimtedetailsoort.doucheruimte.code,
                    Ruimtedetailsoort.zolder.code,
                    Ruimtedetailsoort.slaapkamer.code,
                ]:
                    logger.debug(
                        f"{ruimte.detail_soort.naam} {ruimte.detail_soort.code} komt niet in aanmerking voor een puntenwaardering onder {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
                    )
                    continue

                criterium_naam = ruimte.naam

                # Van vaste kasten (kleiner dan 2m²) wordt de netto oppervlakte bepaald
                # en bij de oppervlakte van het betreffende vertrek opgeteld.
                # Een kast, (kleiner dan 2m²) waarvan de deur uitkomt op een
                # verkeersruimte, wordt niet gewaardeerd
                if ruimte.detail_soort.code not in [
                    Ruimtedetailsoort.hal.code,
                    Ruimtedetailsoort.overloop.code,
                    Ruimtedetailsoort.entree.code,
                    Ruimtedetailsoort.gang.code,
                ]:
                    ruimte_kasten = [
                        verbonden_ruimte
                        for verbonden_ruimte in ruimte.verbonden_ruimten or []
                        if verbonden_ruimte.detail_soort is not None
                        and verbonden_ruimte.detail_soort.code
                        == Ruimtedetailsoort.kast.code
                        and verbonden_ruimte.oppervlakte is not None
                        and verbonden_ruimte.oppervlakte < 2.0
                    ]

                    aantal_ruimte_kasten = len(ruimte_kasten)

                    if aantal_ruimte_kasten > 0:
                        ruimte.oppervlakte += sum(
                            [
                                ruimte_kast.oppervlakte
                                for ruimte_kast in ruimte_kasten
                                if ruimte_kast.oppervlakte is not None
                            ]
                        )

                        if ruimte.inhoud is not None:
                            ruimte.inhoud += sum(
                                [
                                    ruimte_kast.inhoud
                                    for ruimte_kast in ruimte_kasten
                                    if ruimte_kast.inhoud is not None
                                ]
                            )

                        logger.debug(
                            f"De netto oppervlakte van {aantal_ruimte_kasten} verbonden {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'} is opgeteld bij {ruimte.naam}"
                        )

                        criterium_naam = f"{ruimte.naam} + {aantal_ruimte_kasten} {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'}"

                if ruimte.oppervlakte is not None and ruimte.oppervlakte < 2:
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

                if ruimte.oppervlakte is not None:
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
                        oppervlakte_aantal = _oppervlakte_zolder_overige_ruimte(ruimte)
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

                logger.debug(
                    f"Oppervlakte voor {ruimte.naam} van {ruimte.oppervlakte} is afgerond naar {woningwaardering.aantal}"
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


if __name__ == "__main__":
    oor = OppervlakteVanOverigeRuimten2024()
    with open(
        "tests/data/input/zelfstandige_woonruimten/85651000021.json",
        "r+",
    ) as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())

    woningwaardering_resultaat = oor.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
