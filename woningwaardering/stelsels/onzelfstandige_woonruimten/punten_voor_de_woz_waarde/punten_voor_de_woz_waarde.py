import warnings
from datetime import date
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenWozEenheid,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
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
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaarderingen = list[WoningwaarderingResultatenWoningwaardering]()

        # 2.11.1 Waarderingsmethode WOZ-waarde
        # De WOZ-waarde de woning kan voor de woningwaardering op twee manieren worden vastgesteld. Deze manieren zijn als volgt:
        # 1. Op basis van de laatst vastgestelde WOZ-waarde: dit is de standaardregel; of
        # 2. Op basis van 85% van de taxatiewaarde van de woonruimte: wanneer er geen relevante WOZ-waarde voor de woonruimte bekend is.
        # Wanneer er geen enkele WOZ-waarde of taxatiewaarde bekend is voor het adres van de woning, dan wordt het laagste puntenaantal voor de WOZ-waarde toegepast (10 punten).

        woz_eenheid = self._meest_recente_woz_eenheid(eenheid)

        if (
            woz_eenheid is None
            or woz_eenheid.waardepeildatum is None
            or woz_eenheid.vastgestelde_waarde is None
        ):
            logger.info(
                f"Eenheid {eenheid.id}: geen WOZ-waarde bekend. Laagste puntenaantal voor de WOZ-waarde wordt toegepast (10 punten)."
            )
            punten = 10
            woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Geen WOZ-waarde bekend",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="geen_woz_waarde_bekend",
                            )
                        ),
                    ),
                    punten=punten,
                )
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
                return woningwaardering_groep

            puntenwaardering_sleutel = WoningwaarderingCriteriumSleutels(
                id=str(
                    CriteriumId(
                        stelselgroep=self.stelselgroep,
                        criterium="percentage_verschil",
                        is_totaal=True,
                    )
                )
            )

            woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"WOZ-waarde op waardepeildatum {woz_eenheid.waardepeildatum.strftime(DATUM_FORMAT)}",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="woz_waarde",
                            )
                        ),
                        bovenliggende_criterium=puntenwaardering_sleutel,
                    ),
                    aantal=woz_eenheid.vastgestelde_waarde,
                )
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
                return woningwaardering_groep

            woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Gebruiksoppervlakte",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="gebruiksoppervlakte",
                            )
                        ),
                        meeteenheid=Meeteenheid.vierkante_meter_m2,
                        bovenliggende_criterium=puntenwaardering_sleutel,
                    ),
                    aantal=gebruiksoppervlakte,
                )
            )

            woz_waarde_per_m2 = woz_waarde / gebruiksoppervlakte

            woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="WOZ-waarde per m²",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="woz_waarde_per_m2",
                            )
                        ),
                        bovenliggende_criterium=puntenwaardering_sleutel,
                    ),
                    aantal=woz_waarde_per_m2,
                )
            )

            woonplaats = utils.get_woonplaats(adres)

            if woonplaats is None or woonplaats.code is None:
                warnings.warn(
                    f"Eenheid {eenheid.id}: Geen woonplaats gevonden voor adres {adres}. Kan punten voor de WOZ-waarde niet bepalen.",
                    UserWarning,
                )
                return woningwaardering_groep

            corop_gebied = utils.get_corop_voor_woonplaats(woonplaats.code)

            if corop_gebied is None:
                warnings.warn(
                    f"Eenheid {eenheid.id}: Geen COROP-gebied gevonden voor woonplaats {woonplaats.naam} met woonplaatscode {woonplaats.code}. Kan punten voor de WOZ-waarde niet bepalen.",
                    UserWarning,
                )
                return woningwaardering_groep

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
                return woningwaardering_groep

            logger.debug(
                f"Gemiddelde WOZ-waarde per m² voor {corop_gebied['naam']}: {gemiddelde_woz_waarde_per_m2}"
            )
            logger.debug(
                f"Eenheid {eenheid.id}: WOZ-waarde per m²: {woz_waarde_per_m2}"
            )

            woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"Gemiddelde WOZ-waarde per m² voor {corop_gebied['naam']}",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="gemiddelde_woz_waarde_per_m2",
                            )
                        ),
                        bovenliggende_criterium=puntenwaardering_sleutel,
                    ),
                    aantal=gemiddelde_woz_waarde_per_m2,
                )
            )

            verschil_percentage = (
                (woz_waarde_per_m2 / gemiddelde_woz_waarde_per_m2) - 1
            ) * 100

            logger.debug(
                f"Eenheid {eenheid.id}: verschil percentage WOZ-waarde per m² en gemiddelde WOZ-waarde per m² voor {corop_gebied['naam']}: {verschil_percentage}%"
            )

            punten = 0

            # De puntentoekenning is als volgt.
            if verschil_percentage > 10:
                # 14 punten wanneer de WOZ-waarde per m² gebruiksoppervlakte meer dan 10% hoger
                # is dan de gemiddelde WOZ-waarde per m² gebruiksoppervlakte van de woningen
                # in het COROP-gebied waarbinnen de woning is gelegen.
                punten = 14
                logger.info(
                    f"Eenheid {eenheid.id}: WOZ-waarde per m² (€{woz_waarde_per_m2:.0f}) is meer dan 10% hoger dan gemiddelde WOZ-waarde per m² (€{gemiddelde_woz_waarde_per_m2:.0f}) voor {corop_gebied['naam']}. {punten} punten voor {self.stelselgroep.naam}"
                )
            elif verschil_percentage >= -10:
                # 12 punten wanneer de WOZ-waarde per m² gebruiksoppervlakte maximaal 10% hoger
                # of lager is dan de gemiddelde WOZ-waarde per m² gebruiksoppervlakte van de
                # woningen in het COROP-gebied waarbinnen de woning is gelegen.
                punten = 12
                logger.info(
                    f"Eenheid {eenheid.id}: WOZ-waarde per m² (€{woz_waarde_per_m2:.0f}) is maximaal 10% hoger of lager dan gemiddelde WOZ-waarde per m² (€{gemiddelde_woz_waarde_per_m2:.0f}) voor {corop_gebied['naam']}. {punten} punten voor {self.stelselgroep.naam}"
                )
            else:
                # 10 punten wanneer de WOZ-waarde per m² gebruiksoppervlakte meer dan 10% lager
                # is dan de gemiddelde WOZ-waarde per m² gebruiksoppervlakte van de woningen
                # in het COROP-gebied waarbinnen de woning is gelegen.
                punten = 10
                logger.info(
                    f"Eenheid {eenheid.id}: WOZ-waarde per m² (€{woz_waarde_per_m2:.0f}) is meer dan 10% lager dan gemiddelde WOZ-waarde per m² (€{gemiddelde_woz_waarde_per_m2:.0f}) voor {corop_gebied['naam']}. {punten} punten voor {self.stelselgroep.naam}"
                )

            woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Percentage verschil",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="percentage_verschil",
                                is_totaal=True,
                            )
                        ),
                    ),
                    aantal=verschil_percentage,
                    punten=punten,
                )
            )

        woningwaardering_groep.woningwaarderingen = woningwaarderingen
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
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
