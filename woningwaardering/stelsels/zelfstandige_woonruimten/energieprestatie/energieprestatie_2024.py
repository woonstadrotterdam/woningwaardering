import datetime
from loguru import logger
import pandas as pd

from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import lees_csv_als_dataframe, naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
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

LOOKUP_TABEL_FOLDER = "woningwaardering/stelsels/zelfstandige_woonruimten/energieprestatie/lookup_tabellen"


class Energieprestatie2024(Stelselgroepversie):
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
                stelselgroep=Woningwaarderingstelselgroep.energieprestatie.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        # TODO:
        # oppervlakte? waar kom die vandaan?
        # eengezins of meergezinswoning?
        oppervlakte = 20

        energieprestatie = (
            Energieprestatie2024._krijg_energieprestatie_met_geldig_label(eenheid)
        )

        if not (energieprestatie or eenheid.bouwjaar):
            logger.debug(
                f"Eenheid {eenheid.id} heeft geen geldig energielabel en geen bouwjaar en komt daarom niet in aanmerking voor {Woningwaarderingstelselgroep.energieprestatie.naam}"
            )
            return woningwaardering_groep

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=eenheid.id
                )
            )
        )

        if energieprestatie:
            df = Energieprestatie2024._laad_energieprestatie_lookup(
                energieprestatie, oppervlakte
            )
            print(energieprestatie)
            df_punten_nieuw_energielabel = df[
                (df["Label"] == energieprestatie.label.naam)
            ]
            print(df_punten_nieuw_energielabel)
            punten = df_punten_nieuw_energielabel["Eengezinswoning"].values[0]

            woningwaardering_groep.punten = float(punten)
            return woningwaardering_groep

        if eenheid.bouwjaar:
            df = Energieprestatie2024._laad_energieprestatie_lookup()
            filtered_df = df[
                ((df["BouwjaarMin"] <= eenheid.bouwjaar) | df["BouwjaarMin"].isnull())
                & ((df["BouwjaarMax"] >= eenheid.bouwjaar) | df["BouwjaarMax"].isnull())
            ]

            Energieprestatie2024._dataframe_heeft_een_rij(filtered_df)

            punten = filtered_df["Eengezinswoning"].values[0]
            woningwaardering_groep.punten = float(punten)
            return woningwaardering_groep

    @staticmethod
    def _krijg_energieprestatie_met_geldig_label(
        eenheid: EenhedenEenheid,
    ) -> EenhedenEnergieprestatie | None:
        if eenheid.energieprestaties is not None:
            # loop door energieprestatie en return de eerste geldige energieprestatie met label
            for energieprestatie in eenheid.energieprestaties:
                if (
                    (
                        energieprestatie.begindatum is not None
                        and energieprestatie.einddatum is not None
                        and energieprestatie.label is not None
                        and energieprestatie.registratiedatum is not None
                    )
                    and (
                        energieprestatie.begindatum
                        < datetime.date.today()
                        < energieprestatie.einddatum
                    )
                    and (
                        energieprestatie.registratiedatum
                        > (datetime.date.today() - datetime.timedelta(weeks=520))
                    )
                ):
                    logger.debug("Eenergieprestatie met geldig label gevonden")
                    return energieprestatie
        return None

    @staticmethod
    def _laad_energieprestatie_lookup(
        energieprestatie: datetime.date = None, oppervlakte: float = None
    ) -> pd.DataFrame:
        lookup_tabel = "bouwjaar_punten.csv"
        if energieprestatie and oppervlakte:
            if energieprestatie.begindatum >= datetime.date(2021, 1, 1):
                if oppervlakte < 25.0:
                    lookup_tabel = "nieuw_0-25m2_energielabel_punten.csv"
                elif 25.0 <= oppervlakte < 40.0:
                    lookup_tabel = "nieuw_25-40m2_energielabel_punten.csv"
                else:
                    lookup_tabel = "nieuw_40m2+_energielabel_punten.csv"
            else:
                lookup_tabel = "oud_energielabel_punten.csv"

        logger.debug(f"Laad lookup tabel {lookup_tabel}")

        # peildatum? -> selecteer alleen de geldige records voor die peildatum dan moet deze functie een nivea hoger
        df = lees_csv_als_dataframe(f"{LOOKUP_TABEL_FOLDER}/{lookup_tabel}")
        return df

    @staticmethod
    def _dataframe_heeft_een_rij(df: pd.DataFrame) -> None:
        # TODO: nagaan of we error willen raisen of loggen.
        if df.empty:
            logger.error("Geen resultaat gevonden in de bouwjaar_punten lookup tabel.")
            raise ValueError
        if len(df) > 1:
            logger.error(
                "Meerdere resultaten gevonden in de bouwjaar_punten lookup tabel."
            )
            raise ValueError


if __name__ == "__main__":
    logger.enable("woningwaardering")

    energieprestatie = Energieprestatie2024()
    with open(
        "tests/data/input/zelfstandige_woonruimten/12006000004.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = energieprestatie.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = naar_tabel(woningwaardering_resultaat)

    print(tabel)
