import warnings
from collections import Counter
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
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
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    Ruimtedetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.utils import get_bouwkundige_elementen


class Keuken(Stelselgroep):
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
        self.stelselgroep = Woningwaarderingstelselgroep.keuken

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

        keukens = [
            ruimte for ruimte in eenheid.ruimten or [] if Keuken.is_keuken(ruimte)
        ]

        woningwaardering_groep.woningwaarderingen = [
            woningwaardering
            for ruimte in keukens
            for woningwaardering in Keuken.genereer_woningwaarderingen(
                ruimte, self.stelselgroep
            )
        ]

        if not keukens:
            warnings.warn(
                f"Eenheid {eenheid.id} kan niet gewaardeerd worden op stelselgroep {Woningwaarderingstelselgroep.keuken.naam} omdat er geen keuken is gevonden.",
                UserWarning,
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
    def is_keuken(ruimte: EenhedenRuimte) -> bool:
        aanrecht_aantal = len(
            [
                aanrecht
                for aanrecht in get_bouwkundige_elementen(
                    ruimte, Bouwkundigelementdetailsoort.aanrecht
                )
                if aanrecht.lengte and aanrecht.lengte >= 1000
            ]
        )

        if not ruimte.detail_soort or not ruimte.detail_soort.code:
            warnings.warn(
                f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detail_soort(code) en daardoor kan niet gecontroleerd of het een keuken is.",
                UserWarning,
            )
            return False

        if ruimte.detail_soort.code in [
            Ruimtedetailsoort.keuken.code,
            Ruimtedetailsoort.woonkamer_en_of_keuken.code,
        ]:
            if aanrecht_aantal == 0:
                warnings.warn(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) is een keuken, maar heeft geen aanrecht (of geen aanrecht met een lengte >=1000mm) en mag daardoor niet gewaardeerd worden voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}.",
                    UserWarning,
                )
                return False  # ruimte is een keuken maar heeft geen valide aanrecht en mag dus niet als keuken gewaardeerd worden
            return True  # ruimte is een keuken met een valide aanrecht
        if ruimte.detail_soort.code not in [
            Ruimtedetailsoort.woonkamer.code,
            Ruimtedetailsoort.woon_en_of_slaapkamer.code,
            Ruimtedetailsoort.slaapkamer.code,
        ]:
            return False  # ruimte is geen ruimte dat een keuken zou kunnen zijn met een aanrecht erin

        if (
            aanrecht_aantal == 0
        ):  # ruimte is geen keuken want heeft geen valide aanrecht
            return False

        return True  # ruimte is een impliciete keuken vanwege een valide aanrecht

    @staticmethod
    def genereer_woningwaarderingen(
        ruimte: EenhedenRuimte,
        stelselgroep: Woningwaarderingstelselgroep,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        if not Keuken.is_keuken(ruimte):
            logger.debug(
                f"Ruimte {ruimte.naam} ({ruimte.id}) is geen keuken en wordt daarom niet gewaardeerd voor stelselgroep {stelselgroep.naam}"
            )
            return 0
        totaal_punten = 0.0
        totaal_lengte_aanrechten = 0.0
        # deze loop is voor de lengte van de aanrechten
        for element in ruimte.bouwkundige_elementen or []:
            if not element.detail_soort or not element.detail_soort.code:
                warnings.warn(
                    f"Bouwkundig element {element.id} heeft geen detail_soort.code en kan daardoor niet gewaardeerd worden.",
                    UserWarning,
                )
                continue
            if element.detail_soort.code == Bouwkundigelementdetailsoort.aanrecht.code:
                if not element.lengte:
                    warnings.warn(
                        f"{Bouwkundigelementdetailsoort.aanrecht.naam} {element.id} heeft geen lengte en kan daardoor niet gewaardeerd worden.",
                        UserWarning,
                    )
                    continue
                if element.lengte < 1000:
                    aanrecht_punten = 0
                    totaal_lengte_aanrechten += element.lengte
                elif element.lengte >= 2000:
                    aanrecht_punten = 7
                    totaal_lengte_aanrechten += element.lengte
                else:
                    aanrecht_punten = 4
                    totaal_lengte_aanrechten += element.lengte
                totaal_punten += aanrecht_punten
                yield (
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"{ruimte.naam} - Lengte {element.naam.lower() if element.naam else 'aanrecht'}",
                            meeteenheid=Meeteenheid.millimeter.value,
                        ),
                        punten=aanrecht_punten,
                        aantal=element.lengte,
                    )
                )
        # extra voorzieningen
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

        voorziening_counts = Counter(
            voorziening
            for voorziening in ruimte.installaties or []
            if voorziening in punten_per_installatie
        )
        punten_voor_extra_voorzieningen = sum(
            punten_per_installatie[voorziening] * count
            for voorziening, count in voorziening_counts.items()
        )

        for voorziening, count in voorziening_counts.items():
            yield (
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
            yield (
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"Max. {max_punten_voorzieningen} punten voor een (open) keuken met een aanrechtlengte van {totaal_lengte_aanrechten}mm",
                    ),
                    punten=aftrek,
                )
            )


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
