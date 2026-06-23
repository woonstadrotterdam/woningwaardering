import warnings
from datetime import date
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import WaarderingsgroepBouwer
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenWozEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/onzelfstandige_woonruimten/punten_voor_de_woz_waarde/lookup_tabellen"
)

DATUM_FORMAT = "%d-%m-%Y"


class PuntenVoorDeWozWaarde(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.punten_voor_de_woz_waarde  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            peildatum=peildatum,
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        waarderingsgroep_bouwer = WaarderingsgroepBouwer(
            self.stelsel, self.stelselgroep
        )
        punten = 0.0

        def _onbepaalbaar() -> WoningwaarderingResultatenWoningwaarderingGroep:
            # Bij incomplete invoer kan de WOZ-waardering niet bepaald worden. De
            # groep krijgt dan geen punten (None) en bevat geen waarderingen,
            # conform het gedrag van vóór de builder-refactor.
            groep = waarderingsgroep_bouwer.bouw()
            groep.punten = None
            return groep

        woz_eenheid = self._meest_recente_woz_eenheid(eenheid)

        if (
            woz_eenheid is None
            or woz_eenheid.waardepeildatum is None
            or woz_eenheid.vastgestelde_waarde is None
        ):
            logger.info(
                f"Eenheid {eenheid.id}: geen WOZ-waarde bekend. Laagste puntenaantal voor de WOZ-waarde wordt toegepast (10 punten)."
            )
            punten = 10.0
            waarderingsgroep_bouwer.maak_onderliggende(
                id="geen_woz_waarde_bekend",
                naam="Geen WOZ-waarde bekend",
                punten=punten,
            )
        else:
            woz_waarde = Decimal(str(woz_eenheid.vastgestelde_waarde))

            adres = eenheid.adres

            if (
                adres is None
                or not isinstance(adres, EenhedenEenheidadres)
                or (
                    (adres.postcode is None or adres.huisnummer is None)
                    and (adres.woonplaats is None or adres.woonplaats.code is None)
                )
            ):
                warnings.warn(
                    f"Eenheid {eenheid.id}: adres met woonplaatscode of postcode en huisnummer ontbreekt, COROP-gebied kan niet bepaald worden voor gemiddelde WOZ waarde",
                    UserWarning,
                )
                return _onbepaalbaar()

            puntenwaardering = waarderingsgroep_bouwer.maak_onderliggende(
                id="percentage_verschil",
                naam="Percentage verschil",
            )

            puntenwaardering.maak_onderliggende(
                id="woz_waarde",
                naam=f"WOZ-waarde op waardepeildatum {woz_eenheid.waardepeildatum.strftime(DATUM_FORMAT)}",
                aantal=woz_eenheid.vastgestelde_waarde,
                meeteenheid=Meeteenheid.euro,
            )

            gebruiksoppervlakte = (
                eenheid.adresseerbaar_object_basisregistratie.bag_gebruikers_oppervlakte
                if eenheid.adresseerbaar_object_basisregistratie
                else None
            )

            if gebruiksoppervlakte is None:
                warnings.warn(
                    f"Eenheid {eenheid.id}: geen gebruiksoppervlakte van het verblijfsobject gevonden. Dit dient gespecificeerd te worden in het attribuut 'adresseerbaar_object_basisregistratie.bag_gebruikers_oppervlakte' op de eenheid. Kan punten voor de WOZ-waarde niet bepalen.",
                    UserWarning,
                )
                puntenwaardering.verwijder()
                return _onbepaalbaar()

            puntenwaardering.maak_onderliggende(
                id="gebruiksoppervlakte",
                naam="Gebruiksoppervlakte",
                aantal=gebruiksoppervlakte,
                meeteenheid=Meeteenheid.vierkante_meter_m2,
            )

            woz_waarde_per_m2 = woz_waarde / gebruiksoppervlakte

            puntenwaardering.maak_onderliggende(
                id="woz_waarde_per_m2",
                naam="WOZ-waarde per m²",
                aantal=woz_waarde_per_m2,
            )

            woonplaats = utils.get_woonplaats(adres)

            if woonplaats is None or woonplaats.code is None:
                warnings.warn(
                    f"Eenheid {eenheid.id}: Geen woonplaats gevonden voor adres {adres}. Kan punten voor de WOZ-waarde niet bepalen.",
                    UserWarning,
                )
                puntenwaardering.verwijder()
                return _onbepaalbaar()

            corop_gebied = utils.get_corop_voor_woonplaats(woonplaats.code)

            if corop_gebied is None:
                warnings.warn(
                    f"Eenheid {eenheid.id}: Geen COROP-gebied gevonden voor woonplaats {woonplaats.naam} met woonplaatscode {woonplaats.code}. Kan punten voor de WOZ-waarde niet bepalen.",
                    UserWarning,
                )
                puntenwaardering.verwijder()
                return _onbepaalbaar()

            logger.debug(
                f"Eenheid {eenheid.id} met woonplaats {woonplaats.naam} ligt in COROP-gebied {corop_gebied['naam']}"
            )

            gemiddelde_woz_waarde_per_m2 = self._gemiddelde_woz_voor_corop_gebied(
                corop_gebied, woz_eenheid.waardepeildatum.year
            )

            if gemiddelde_woz_waarde_per_m2 is None:
                warnings.warn(
                    f"Eenheid {eenheid.id}: Geen gemiddelde WOZ-waarde gevonden voor COROP-gebied {corop_gebied}. Kan punten voor de WOZ-waarde niet bepalen.",
                    UserWarning,
                )
                puntenwaardering.verwijder()
                return _onbepaalbaar()

            logger.debug(
                f"Gemiddelde WOZ-waarde per m² voor {corop_gebied['naam']}: {gemiddelde_woz_waarde_per_m2}"
            )
            logger.debug(
                f"Eenheid {eenheid.id}: WOZ-waarde per m²: {woz_waarde_per_m2}"
            )

            puntenwaardering.maak_onderliggende(
                id="gemiddelde_woz_waarde_per_m2",
                naam=f"Gemiddelde WOZ-waarde per m² voor {corop_gebied['naam']}",
                aantal=gemiddelde_woz_waarde_per_m2,
            )

            verschil_percentage = (
                (woz_waarde_per_m2 / gemiddelde_woz_waarde_per_m2) - 1
            ) * 100

            logger.debug(
                f"Eenheid {eenheid.id}: verschil percentage WOZ-waarde per m² en gemiddelde WOZ-waarde per m² voor {corop_gebied['naam']}: {verschil_percentage}%"
            )

            if verschil_percentage > 10:
                punten = 14.0
                logger.info(
                    f"Eenheid {eenheid.id}: WOZ-waarde per m² (€{woz_waarde_per_m2:.0f}) is meer dan 10% hoger dan gemiddelde WOZ-waarde per m² (€{gemiddelde_woz_waarde_per_m2:.0f}) voor {corop_gebied['naam']}. {punten} punten voor {self.stelselgroep.naam}"
                )
            elif verschil_percentage >= -10:
                punten = 12.0
                logger.info(
                    f"Eenheid {eenheid.id}: WOZ-waarde per m² (€{woz_waarde_per_m2:.0f}) is maximaal 10% hoger of lager dan gemiddelde WOZ-waarde per m² (€{gemiddelde_woz_waarde_per_m2:.0f}) voor {corop_gebied['naam']}. {punten} punten voor {self.stelselgroep.naam}"
                )
            else:
                punten = 10.0
                logger.info(
                    f"Eenheid {eenheid.id}: WOZ-waarde per m² (€{woz_waarde_per_m2:.0f}) is meer dan 10% lager dan gemiddelde WOZ-waarde per m² (€{gemiddelde_woz_waarde_per_m2:.0f}) voor {corop_gebied['naam']}. {punten} punten voor {self.stelselgroep.naam}"
                )

            puntenwaardering.punten = punten
            puntenwaardering.aantal = float(verschil_percentage)

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()
        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _meest_recente_woz_eenheid(
        self, eenheid: EenhedenEenheid
    ) -> EenhedenWozEenheid | None:
        relevante_waardepeildatums = [
            date(self.peildatum.year - 2, 1, 1),  # T-2
            date(self.peildatum.year - 1, 1, 1),  # T-1
        ]

        woz_eenheden = [
            woz_eenheid
            for woz_eenheid in eenheid.woz_eenheden or []
            if woz_eenheid.waardepeildatum is not None
            and woz_eenheid.waardepeildatum in relevante_waardepeildatums
            and woz_eenheid.vastgestelde_waarde is not None
        ]

        if not woz_eenheden:
            datums = " of ".join(
                [
                    relevante_waardepeildatum.strftime(DATUM_FORMAT)
                    for relevante_waardepeildatum in relevante_waardepeildatums
                ]
            )
            warnings.warn(
                f"Eenheid {eenheid.id}: geen WOZ-waarde gevonden met waardepeildatum {datums}",
                UserWarning,
            )
            return None
        else:
            return max(woz_eenheden, key=lambda x: x.waardepeildatum or date.min)

    def _gemiddelde_woz_voor_corop_gebied(
        self, corop_gebied: dict[str, str], jaar: int
    ) -> Decimal | None:
        df_woz = pd.read_csv(
            str(
                files("woningwaardering")
                .joinpath(LOOKUP_TABEL_FOLDER)
                .joinpath("corop_gebied_gemiddelde_woz_waarde_per_m2.csv")
            ),
            dtype={"COROP-gebiedcode": str, str(jaar): str},
        )

        woz_mask = df_woz["COROP-gebiedcode"] == corop_gebied["code"]

        if not woz_mask.any():
            return None

        gemiddelde_woz_waarde_per_m2 = df_woz.loc[woz_mask, str(jaar)].values[0]

        return Decimal(gemiddelde_woz_waarde_per_m2)


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=PuntenVoorDeWozWaarde(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as waarderingsgroep_bouwer:
        waarderingsgroep_bouwer.waardeer(
            "tests/data/onzelfstandige_woonruimten/input/15004000185.json"
        )
