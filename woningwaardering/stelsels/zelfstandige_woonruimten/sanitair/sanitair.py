import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    Referentiedata,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    Ruimtedetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid


class Sanitair(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            begindatum=date(2024, 7, 1),
            einddatum=date.max,
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.sanitair

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
                stelselgroep=Woningwaarderingstelselgroep.keuken.value,
            )
        )
        woningwaardering_groep.woningwaarderingen = []

        for ruimte in eenheid.ruimten or []:
            Sanitair.punten_voor_voorziening(
                woningwaardering_groep.woningwaarderingen, ruimte
            )

        totaal_punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
        )
        woningwaardering_groep.punten = float(totaal_punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def punten_voor_voorziening(
        woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering],
        ruimte: EenhedenRuimte,
    ) -> float:
        aantal_hangende_toiletten = len(
            [
                voorziening
                for voorziening in ruimte.installaties or []
                if voorziening.soort.code == Installatiesoort.hangend_toilet.code
            ]
        )
        aantal_staande_toiletten = len(
            [
                voorziening
                for voorziening in ruimte.installaties or []
                if voorziening.soort.code == Installatiesoort.staand_toilet.code
            ]
        )

        if ruimte.detail_soort.code == Ruimtedetailsoort.toiletruimte.code:
            if aantal_hangende_toiletten > 0:
                woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"{Installatiesoort.hangend_toilet.naam} (in zelfde ruimte)"
                            if aantal_hangende_toiletten > 1
                            else Installatiesoort.hangend_toilet.naam
                        ),
                        punten=utils.rond_af(
                            3.75 * aantal_hangende_toiletten, decimalen=2
                        ),
                        aantal=aantal_hangende_toiletten,
                    )
                )
            # if aantal_staande_toiletten > 0:
            #     woningwaarderingen.append(
            #         WoningwaarderingResultatenWoningwaardering(
            #             criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
            #                 naam=f"{Installatiesoort.staand_toilet.naam} (in zelfde ruimte)"
            #                 if aantal_staande_toiletten > 1
            #                 else Installatiesoort.staand_toilet.naam
            #             ),
            #             punten=utils.rond_af(

        mapping = {
            Ruimtedetailsoort.toiletruimte.value: {
                Installatiesoort.hangend_toilet.value: 3.75,
                Installatiesoort.staand_toilet.value: 3,
            },
            Ruimtedetailsoort.badruimte.value: {
                Installatiesoort.hangend_toilet.value: 2.75,
                Installatiesoort.staand_toilet.value: 2,
            },
            Ruimtedetailsoort.badkamer_met_toilet.value: {
                Installatiesoort.hangend_toilet.value: 2.75,
                Installatiesoort.staand_toilet.value: 2,
            },
        }

        # extra voorzieningen
        punten_voor_extra_voorzieningen = 0.0
        punten_per_installatie = {
            Installatiesoort.inbouw_afzuiginstallatie.value: 0.75,
            Installatiesoort.inbouw_kookplaat_inductie.value: 1.75,
            Installatiesoort.inbouw_kookplaat_keramisch.value: 1.0,
            Installatiesoort.inbouw_kookplaat_gas.value: 0.5,
            Installatiesoort.inbouw_koelkast.value: 1.0,
            Installatiesoort.inbouw_vrieskast.value: 0.75,
            Installatiesoort.inbouw_oven_elektrisch.value: 1.0,
            Installatiesoort.inbouw_oven_gas.value: 0.5,
            Installatiesoort.inbouw_magnetron.value: 1.0,
            Installatiesoort.inbouw_vaatwasmachine.value: 1.5,
            Installatiesoort.extra_keukenkastruimte_boven_het_minimum.value: 0.75,
            Installatiesoort.eenhandsmengkraan.value: 0.25,
            Installatiesoort.thermostatische_mengkraan.value: 0.5,
            Installatiesoort.kokend_waterfunctie.value: 0.5,
        }

        voorziening_counts: dict[Referentiedata, int] = {}
        # tel aantal voorzieningen per type
        for voorziening in ruimte.installaties or []:
            if voorziening in punten_per_installatie:
                voorziening_counts[voorziening] = (
                    voorziening_counts.get(voorziening, 0) + 1
                )
                punten_voor_extra_voorzieningen += punten_per_installatie[voorziening]
        # voeg punten toe voor elk type voorziening
        for voorziening, count in voorziening_counts.items():
            woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"{voorziening.naam} (in zelfde ruimte)"
                        if count > 1
                        else voorziening.naam,
                    ),
                    punten=utils.rond_af(
                        punten_per_installatie[voorziening] * count, decimalen=2
                    ),
                    aantal=count,
                )
            )

        max_punten_voorzieningen = 7 if totaal_lengte_aanrechten >= 2000 else 4
        if punten_voor_extra_voorzieningen > max_punten_voorzieningen:
            aftrek = max_punten_voorzieningen - punten_voor_extra_voorzieningen
            woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"Max. {max_punten_voorzieningen} punten voor een (open) keuken met een aanrechtlengte van {totaal_lengte_aanrechten}mm",
                    ),
                    punten=aftrek,
                )
            )
        return totaal_punten


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    keuken = Keuken()
    with open(
        "tests/data/generiek/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[keuken.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
