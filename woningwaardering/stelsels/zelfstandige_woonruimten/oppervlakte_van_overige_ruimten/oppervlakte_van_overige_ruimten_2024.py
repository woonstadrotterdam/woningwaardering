from decimal import ROUND_HALF_UP, Decimal

from loguru import logger

from woningwaardering.stelsels import Stelselgroepversie
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
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


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
                logger.warning(f"Ruimte {ruimte} heeft geen oppervlakte")
                continue
            if ruimte.detail_soort is None:
                logger.warning(f"Ruimte {ruimte} heeft geen detailsoort")
                continue
            if ruimte.detail_soort.code is None:
                logger.warning(f"Ruimte {ruimte} heeft geen detailsoortcode")
                continue

            if (
                ruimte.soort is not None
                and ruimte.soort.code == Ruimtesoort.overige_ruimtes.code
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
                    verbonden_kasten = [
                        verbonden_ruimte
                        for verbonden_ruimte in ruimte.verbonden_ruimten or []
                        if verbonden_ruimte.detail_soort is not None
                        and verbonden_ruimte.detail_soort.code
                        == Ruimtedetailsoort.kast.code
                        and verbonden_ruimte.oppervlakte is not None
                        and verbonden_ruimte.oppervlakte < Decimal("2")
                    ]

                    ruimte.oppervlakte += sum(
                        [
                            verbonden_kast.oppervlakte
                            for verbonden_kast in verbonden_kasten
                            if verbonden_kast.oppervlakte is not None
                        ]
                    )

                    if ruimte.inhoud is not None:
                        ruimte.inhoud += sum(
                            [
                                verbonden_kast.inhoud
                                for verbonden_kast in verbonden_kasten
                                if verbonden_kast.inhoud is not None
                            ]
                        )

                if ruimte.oppervlakte is not None and ruimte.oppervlakte < 2:
                    logger.debug(
                        f"{ruimte.naam} {ruimte.detail_soort.code} is kleiner dan 2 vierkante meter"
                    )
                    continue

                woningwaardering = WoningwaarderingResultatenWoningwaardering()

                woningwaardering.criterium = (
                    WoningwaarderingResultatenWoningwaarderingCriterium(
                        meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                        naam=ruimte.naam,
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
                                    Decimal(ruimte.oppervlakte).quantize(
                                        Decimal("1"), ROUND_HALF_UP
                                    )
                                    / Decimal(ruimte.gedeeld_met_aantal_eenheden)
                                ).quantize(Decimal("0.01"), ROUND_HALF_UP)
                            )
                        else:
                            logger.debug(
                                f"{ruimte.naam} {ruimte.detail_soort.code} is kleiner dan 2 vierkante meter per eenheid en komt niet in aanmerking voor een puntenwaardering onder {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
                            )
                            continue
                    else:
                        woningwaardering.aantal = float(
                            Decimal(ruimte.oppervlakte).quantize(
                                Decimal("0.01"), ROUND_HALF_UP
                            )
                        )

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = Decimal(
            sum(
                Decimal(woningwaardering.aantal)
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
        "./tests/data/input/zelfstandige_woonruimten/41164000002.json", "r+"
    ) as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())
    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    print(
        oor.bereken(eenheid, woningwaardering_resultaat).model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )
