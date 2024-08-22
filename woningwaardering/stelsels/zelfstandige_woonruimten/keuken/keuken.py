import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.utils import (
    get_bouwkundige_elementen,
)


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

        keukens = set()

        for ruimte in eenheid.ruimten or []:
            if not ruimte.detail_soort:
                warnings.warn(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detail_soort."
                )
                continue

            if ruimte.detail_soort.code not in [
                Ruimtedetailsoort.keuken.code,
                Ruimtedetailsoort.woonkamer_en_of_keuken.code,
                Ruimtedetailsoort.woonkamer.code,
                Ruimtedetailsoort.woon_en_of_slaapkamer.code,
                Ruimtedetailsoort.slaapkamer.code,
            ]:
                continue

            keukens.add(ruimte.id)

            if ruimte.bouwkundige_elementen:
                aanrechten = list(
                    get_bouwkundige_elementen(
                        ruimte, Bouwkundigelementdetailsoort.aanrecht
                    )
                )

                if any(aanrechten):
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) is een keuken met {Bouwkundigelementdetailsoort.aanrecht.naam} en komt in aanmerking voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
                    )
                elif ruimte.detail_soort.code in [
                    Ruimtedetailsoort.keuken.code,
                    Ruimtedetailsoort.woonkamer_en_of_keuken.code,
                ]:
                    warnings.warn(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) is een (open) keuken zonder aanrecht.",
                        UserWarning,
                    )
                    continue

                for element in ruimte.bouwkundige_elementen:
                    punten = self.punten_voor_voorziening(element)
                    if punten is not None:
                        logger.info(
                            f"Ruimte {ruimte.naam} ({ruimte.id}) is een keuken met een {element.naam} en krijgt daarvoor {punten} punten."
                        )

                        woningwaardering_groep.woningwaarderingen.append(
                            WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=element.naam,
                                ),
                                punten=utils.rond_af(
                                    punten,
                                    decimalen=2,
                                ),
                            )
                        )

        if not keukens:
            warnings.warn(
                f"Eenheid {eenheid.id} kan niet gewaardeerd worden op stelselgroep {Woningwaarderingstelselgroep.keuken.naam} omdat er geen keuken is gevonden.",
                UserWarning,
            )

        totaal_punten = utils.rond_af(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
            decimalen=0,
        ) * Decimal("1")
        woningwaardering_groep.punten = float(totaal_punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def punten_voor_voorziening(
        voorziening: BouwkundigElementenBouwkundigElement,
    ) -> float | None:
        # aanrecht
        if not voorziening.detail_soort or not voorziening.detail_soort.code:
            warnings.warn(
                f"Voorziening {voorziening.id} heeft geen detail_soort(code) en kan daardoor niet gewaardeerd worden.",
                UserWarning,
            )
            return None
        if voorziening.detail_soort.code == Bouwkundigelementdetailsoort.aanrecht.code:
            if not voorziening.lengte:
                warnings.warn(
                    f"{Bouwkundigelementdetailsoort.aanrecht.naam} {voorziening.id} heeft geen lengte en kan daardoor niet gewaardeerd worden.",
                    UserWarning,
                )
                return None
            if voorziening.lengte < 1000:
                return 0
            if voorziening.lengte >= 2000:
                return 7
            return 4

        # extra voorzieningen
        lookup_dict = {
            Bouwkundigelementdetailsoort.inbouw_afzuiginstallatie.code: 0.75,
            Bouwkundigelementdetailsoort.inbouw_kookplaat_inductie.code: 1.75,
            Bouwkundigelementdetailsoort.inbouw_kookplaat_keramisch.code: 1.0,
            Bouwkundigelementdetailsoort.inbouw_kookplaat_gas.code: 0.5,
            Bouwkundigelementdetailsoort.inbouw_koelkast.code: 1.0,
            Bouwkundigelementdetailsoort.inbouw_vrieskast.code: 0.75,
            Bouwkundigelementdetailsoort.inbouw_oven_elektrisch.code: 1.0,
            Bouwkundigelementdetailsoort.inbouw_oven_gas.code: 0.5,
            Bouwkundigelementdetailsoort.inbouw_magnetron.code: 1.0,
            Bouwkundigelementdetailsoort.inbouw_vaatwasmachine.code: 1.5,
            Bouwkundigelementdetailsoort.eenhandsmengkraan.code: 0.25,
            Bouwkundigelementdetailsoort.thermostatische_mengkraan.code: 0.5,
        }

        return lookup_dict.get(voorziening.detail_soort.code)


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    keuken = Keuken()
    with open("tests/data/generiek/input/37101000032.json", "r+") as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = keuken.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
