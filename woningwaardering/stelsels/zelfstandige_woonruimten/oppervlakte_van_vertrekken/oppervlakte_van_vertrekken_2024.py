from decimal import ROUND_HALF_UP, Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import (
    vertrek_telt_als_vertrek,
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
    Ruimtedetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import badruimte_met_toilet


class OppervlakteVanVertrekken2024(Stelselgroepversie):
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
                stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        for ruimte in eenheid.ruimten or []:
            logger.debug(f"Processsing ruimte: {ruimte.id}")
            if ruimte.oppervlakte is None:
                error_msg = f"Ruimte {ruimte.id} heeft geen oppervlakte"
                logger.error(error_msg)
                raise TypeError(error_msg)
            if ruimte.detail_soort is None:
                error_msg = f"Ruimte {ruimte.id} heeft geen detailsoort"
                logger.error(error_msg)
                raise TypeError(error_msg)
            if ruimte.detail_soort.code is None:
                error_msg = f"Ruimte {ruimte.id} heeft geen detailsoortcode"
                logger.error(error_msg)
                raise TypeError(error_msg)

            criterium_naam = ruimte.naam

            # Indien een toilet in een badruimte of doucheruimte is geplaatst, wordt de oppervlakte van die ruimte met 1m2 verminderd.
            if badruimte_met_toilet(ruimte):
                ruimte.oppervlakte = float(
                    Decimal(str(ruimte.oppervlakte)) - Decimal("1")
                )
                logger.debug(
                    "Toilet in badkamer gevonden. 1m2 in mindering gebracht van de oppervlakte van de ruimte."
                )

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
                    ruimte.oppervlakte += float(
                        sum(
                            [
                                Decimal(ruimte_kast.oppervlakte)
                                for ruimte_kast in ruimte_kasten
                                if ruimte_kast.oppervlakte is not None
                            ]
                        )
                    )

                    if ruimte.inhoud is not None:
                        ruimte.inhoud += float(
                            sum(
                                [
                                    Decimal(ruimte_kast.inhoud)
                                    for ruimte_kast in ruimte_kasten
                                    if ruimte_kast.inhoud is not None
                                ]
                            )
                        )

                    logger.debug(
                        f"De netto oppervlakte van {aantal_ruimte_kasten} verbonden {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'} is opgeteld bij {ruimte.naam}"
                    )

                    criterium_naam = f"{ruimte.naam} + {aantal_ruimte_kasten} {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'}"

            if not vertrek_telt_als_vertrek(ruimte):
                continue

            woningwaardering = WoningwaarderingResultatenWoningwaardering()

            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                    naam=criterium_naam,
                )
            )

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
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.aantal is not None
            )
        ).quantize(Decimal("1"), ROUND_HALF_UP) * Decimal("1")

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep


if __name__ == "__main__":
    f = open(
        "tests/data/input/zelfstandige_woonruimten/12006000004.json",
        "r+",
    )
    eenheid = EenhedenEenheid.model_validate_json(f.read())

    woningwaardering_resultaat = OppervlakteVanVertrekken2024.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
