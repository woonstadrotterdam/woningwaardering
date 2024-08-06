import warnings
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import naar_tabel, rond_af
from woningwaardering.vera.bvg.generated import (
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
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.utils import get_bouwkundige_elementen


class KeukenJan2024(Stelselgroepversie):
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

            gedeelde_ruimte = (
                ruimte.gedeeld_met_aantal_eenheden
                and ruimte.gedeeld_met_aantal_eenheden >= 2
            )
            keukens.add(ruimte.id)

            aanrechten = list(
                get_bouwkundige_elementen(ruimte, Bouwkundigelementdetailsoort.aanrecht)
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

            for aanrecht in aanrechten:
                if not aanrecht.lengte:
                    warnings.warn(
                        f"{Bouwkundigelementdetailsoort.aanrecht.naam} {aanrecht.id} in ruimte {ruimte.id} heeft geen lengte en kan daardoor niet gewaardeerd worden.",
                        UserWarning,
                    )

                if aanrecht.lengte:
                    if aanrecht.lengte < 1000:
                        punten = 0.0
                    elif aanrecht.lengte >= 2000:
                        punten = 7.0
                    else:
                        punten = 4.0

                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) is een keuken met een aanrecht met lengte {aanrecht.lengte} millimeter en krijgt {punten} punten."
                    )

                    woningwaardering_groep.woningwaarderingen.append(
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam="Lengte aanrecht"
                                if not gedeelde_ruimte
                                else f"Lengte aanrecht (gedeeld met {ruimte.gedeeld_met_aantal_eenheden})",
                                meeteenheid=Meeteenheid.millimeter.value,
                            ),
                            aantal=aanrecht.lengte,
                            punten=rond_af(
                                punten / (ruimte.gedeeld_met_aantal_eenheden or 1),
                                decimalen=2,
                            ),
                        )
                    )

        if not keukens:
            warnings.warn(
                f"Eenheid {eenheid.id} kan niet gewaardeerd worden op stelselgroep {Woningwaarderingstelselgroep.keuken.naam} omdat er geen keuken is gevonden.",
                UserWarning,
            )

        totaal_punten = rond_af(
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


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    keukenJan2024 = KeukenJan2024()
    with open(
        "tests/data/zelfstandige_woonruimten/stelselgroepen/keuken/input/keuken_zonder_aanrecht.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

        woningwaardering_resultaat = keukenJan2024.bereken(eenheid)

        print(
            woningwaardering_resultaat.model_dump_json(
                by_alias=True, indent=2, exclude_none=True
            )
        )

        tabel = naar_tabel(woningwaardering_resultaat)

        print(tabel)
