import warnings
from datetime import date
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
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
    Oppervlaktesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/onzelfstandige_woonruimten/punten_voor_de_woz_waarde/lookup_tabellen"
)


class PuntenVoorDeWozWaarde(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.punten_voor_de_woz_waarde  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.value,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        if (
            eenheid.adres is None
            or eenheid.adres.postcode is None
            or eenheid.adres.huisnummer is None
        ):
            warnings.warn(
                f"Eenheid {eenheid.id}: adres, postcode of huisnummer ontbreekt, COROP-gebied kan niet bepaald worden voor gemiddelde WOZ waarde",
                UserWarning,
            )
            return woningwaardering_groep

        waardepeildatum = date(2022, 1, 1)
        woz_waarde = next(
            (
                Decimal(str(woz_eenheid.vastgestelde_waarde))
                for woz_eenheid in eenheid.woz_eenheden or []
                if woz_eenheid.waardepeildatum == waardepeildatum
                and woz_eenheid.vastgestelde_waarde is not None
            ),
            None,
        )

        if woz_waarde is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: geen WOZ-waarde gevonden met waardepeildatum {waardepeildatum}",
                UserWarning,
            )

        woningwaardering_groep.woningwaarderingen = []

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"WOZ-waarde op peildatum {waardepeildatum.strftime('%x')}"
                ),
                aantal=woz_waarde,
            )
        )

        # 11.2 Ontbreken WOZ-waarde en minimumwaarde
        # Als geen WOZ-waarde bekend is, kan als alternatief 85% van de taxatiewaarde
        # van de woning worden gebruikt volgend uit een door een Register-Taxateur
        # opgesteld (hybride)taxatierapport. De verhuurder draagt de verantwoordelijkheid
        # voor het opstellen van dit rapport. De taxatiewaarde geldt totdat een WOZ-waarde
        # is vastgesteld en vervalt voor toepassing van deze rubriek. Als de verhuurder
        # geen taxatierapport heeft aangeleverd dan geldt de minimum WOZ-waarde.
        #
        # Minimumwaarde
        # De minimum WOZ-waarde wordt ook gebruikt voor specifieke woningen van
        # specifieke verhuurders, zoals ‘containerwoningen’ die zijn bestemd voor
        # studentenhuisvesting. In die gevallen wordt een minimum WOZ-waarde gehanteerd
        # indien de WOZ-waarde lager is dan deze minimumwaarde. Deze waarde met
        # peildatum 1 januari 2023 bedraagt € 73.607. Zie de tabel hieronder voor de
        # minimumwaarde van de afgelopen jaren.
        minimum_woz_waarde = Decimal(str("71602"))

        if woz_waarde is None or woz_waarde < minimum_woz_waarde:
            logger.info(
                f"Eenheid {eenheid.id}: minimum WOZ waarde  {minimum_woz_waarde} voor waardepeildatum {waardepeildatum} wordt gebruikt"
            )
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Minimum WOZ-waarde gebruikt voor berekening"
                    ),
                    aantal=minimum_woz_waarde,
                )
            )
            woz_waarde = minimum_woz_waarde

        gebruiksoppervlakte = next(
            (
                Decimal(oppervlakte.waarde)
                for oppervlakte in eenheid.oppervlakten or []
                if oppervlakte.soort is not None
                and oppervlakte.soort.code == Oppervlaktesoort.gebruiksoppervlakte.code
                and oppervlakte.waarde is not None
            ),
            eenheid.gebruiksoppervlakte,
        )

        if gebruiksoppervlakte is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: geen gebruiksoppervlakte gevonden",
                UserWarning,
            )
            return woningwaardering_groep

        woz_waarde_per_m2 = woz_waarde / gebruiksoppervlakte

        logger.debug(f"Eenheid {eenheid.id}: WOZ-waarde per m2: {woz_waarde_per_m2}")

        woonplaats = utils.get_woonplaats(eenheid.adres)
        if woonplaats is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: Geen woonplaats gevonden voor adres {eenheid.adres}. Kan punten voor de WOZ-waarde niet bepalen.",
                UserWarning,
            )
            return woningwaardering_groep

        corop_gebied = utils.get_corop_voor_woonplaats(woonplaats["code"])

        if corop_gebied is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: Geen COROP-gebied gevonden voor woonplaats {eenheid.adres}. Kan punten voor de WOZ-waarde niet bepalen.",
                UserWarning,
            )
            return woningwaardering_groep

        logger.info(
            f"Eenheid {eenheid.id} met woonplaats {woonplaats} ligt in COROP-gebied {corop_gebied['naam']}"
        )

        df_woz = pd.read_csv(
            files("woningwaardering")
            .joinpath(LOOKUP_TABEL_FOLDER)
            .joinpath("corop_gebied_gemiddelde_woz_waarde_per_m2_2022.csv")
        )

        woz_mask = df_woz["COROP-gebiedcode"] == corop_gebied["code"]

        if not woz_mask.any():
            warnings.warn(
                f"Eenheid {eenheid.id}: Geen gemiddelde WOZ-waarde gevonden voor COROP-gebied {corop_gebied['naam']}. Kan punten voor de WOZ-waarde niet bepalen.",
                UserWarning,
            )
            return woningwaardering_groep

        gemiddelde_woz_waarde_per_m2 = df_woz.loc[
            woz_mask, "Gemiddelde WOZ-waarde per m2"
        ].values[0]

        logger.debug(
            f"Gemiddelde WOZ-waarde per m2 voor {corop_gebied['naam']}: {gemiddelde_woz_waarde_per_m2}"
        )

        verschil_percentage = (
            (woz_waarde_per_m2 / gemiddelde_woz_waarde_per_m2) - 1
        ) * 100

        punten = 0

        # De puntentoekenning is als volgt.
        if verschil_percentage > 10:
            # 14 punten wanneer de WOZ-waarde per m2 gebruiksoppervlakte meer dan 10% hoger
            # is dan de gemiddelde WOZ-waarde per m2 gebruiksoppervlakte van de woningen
            # in het COROP-gebied waarbinnen de woning is gelegen.
            punten = 14
        elif verschil_percentage >= -10:
            # 12 punten wanneer de WOZ-waarde per m2 gebruiksoppervlakte maximaal 10% hoger
            # of lager is dan de gemiddelde WOZ-waarde per m2 gebruiksoppervlakte van de
            # woningen in het COROP-gebied waarbinnen de woning is gelegen.
            punten = 12
        else:
            # 10 punten wanneer de WOZ-waarde per m2 gebruiksoppervlakte meer dan 10% lager
            # is dan de gemiddelde WOZ-waarde per m2 gebruiksoppervlakte van de woningen
            # in het COROP-gebied waarbinnen de woning is gelegen.
            punten = 10

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Gebruiksoppervlakte",
                    meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                ),
                aantal=gebruiksoppervlakte,
            )
        )

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="WOZ-waarde per m²"
                ),
                aantal=woz_waarde_per_m2,
            )
        )

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"Gemiddelde WOZ-waarde per m² voor {corop_gebied['naam']}",
                ),
                aantal=gemiddelde_woz_waarde_per_m2,
            )
        )

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Percentage verschil"
                ),
                aantal=verschil_percentage,
                punten=punten,
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.oppervlakte_onzelfstandige_woonruimte.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")
    warnings.filterwarnings("ignore", category=UserWarning)
    stelselgroep = PuntenVoorDeWozWaarde()
    with open(
        "tests/data/onzelfstandige_woonruimten/stelselgroepen/punten_voor_de_woz_waarde/input/gebruiksoppervlakten.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
