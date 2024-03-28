from decimal import ROUND_HALF_UP, Decimal

from loguru import logger

from woningwaardering.stelsels import StelselgroepVersie
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


class OppervlakteVanOverigeRuimten2024(StelselgroepVersie):
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
            if (
                ruimte.soort is not None
                and ruimte.soort.code == Ruimtesoort.overige_ruimtes.code
                and ruimte.detail_soort is not None
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

                if ruimte.oppervlakte is not None and ruimte.oppervlakte < 2:
                    logger.debug(
                        f"{ruimte.naam} {ruimte.detail_soort.code} is kleiner dan 2 vierkante meter"
                    )
                    continue

                woningwaardering = WoningwaarderingResultatenWoningwaardering()

                woningwaardering.criterium = (
                    WoningwaarderingResultatenWoningwaarderingCriterium(
                        meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                        # stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
                        naam=ruimte.naam,
                    )
                )

                if ruimte.oppervlakte is not None:
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
    f = open("./input_modellen/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(f.read())
    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    print(
        oor.bereken(eenheid, woningwaardering_resultaat).model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )
