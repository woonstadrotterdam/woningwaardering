from decimal import ROUND_HALF_UP, BasicContext, Decimal, setcontext
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.referentiedata.soort import (
    Meeteenheid,
    Ruimtedetailsoort,
    Woningwaarderingstelsel,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

# Set context for all calculations to avoid rounding errors
# See https://docs.python.org/3/library/decimal.html#rounding
setcontext(BasicContext)


class OppervlakteVanOverigeRuimten2024(Stelselgroep):
    @staticmethod
    def bereken(
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
                stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,
            ),
            woningwaarderingen=[],
        )

        for ruimte in eenheid.ruimten:
            if ruimte.soort == Ruimtesoort.overige_ruimtes:
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
                    print(
                        f"{ruimte.detail_soort.naam} {ruimte.detail_soort.code} komt niet in aanmerking voor een puntenwaardering onder {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
                    )
                    continue

                if ruimte.oppervlakte < 2:
                    print(
                        f"{ruimte.naam} {ruimte.detail_soort.code} is kleiner dan 2 vierkante meter"
                    )
                    continue

                woningwaardering = WoningwaarderingResultatenWoningwaardering()

                woningwaardering.criterium = (
                    WoningwaarderingResultatenWoningwaarderingCriterium(
                        Meeteenheid=Meeteenheid.vierkante_meter_m2,
                        # stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
                        naam=ruimte.naam,
                    )
                )

                woningwaardering.aantal = Decimal(ruimte.oppervlakte).quantize(
                    Decimal("0.01"), ROUND_HALF_UP
                )

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = Decimal(
            sum(
                Decimal(woningwaardering.aantal)
                for woningwaardering in woningwaardering_groep.woningwaarderingen
            )
        ).quantize(Decimal("1"), ROUND_HALF_UP) * Decimal("0.75")

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep
