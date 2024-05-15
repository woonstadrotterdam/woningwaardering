import datetime
from importlib.resources import files
from dateutil.relativedelta import relativedelta
from decimal import Decimal
from loguru import logger
import pandas as pd

from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import (
    dataframe_met_een_rij,
    filter_dataframe_op_datum,
    naar_tabel,
)
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
from woningwaardering.vera.referentiedata.energielabel import Energielabel
from woningwaardering.vera.referentiedata.energieprestatiesoort import (
    Energieprestatiesoort,
)
from woningwaardering.vera.referentiedata.energieprestatiestatus import (
    Energieprestatiestatus,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/zelfstandige_woonruimten/energieprestatie/lookup_tabellen"
)


class Energieprestatie2024(Stelselgroepversie):
    lookup_mapping = {
        "oppervlakte_0-25": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/oppervlakte_0-25m2_energielabel_punten.csv"
            )
        ),
        "oppervlakte_25-40": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/oppervlakte_25-40m2_energielabel_punten.csv"
            )
        ),
        "oppervlakte_40+": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/oppervlakte_40m2+_energielabel_punten.csv"
            )
        ),
        "oud": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/oud_energielabel_punten.csv"
            )
        ),
        "bouwjaar": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/bouwjaar_punten.csv"
            )
        ),
    }

    @staticmethod
    def _energieprestatie_met_geldig_label(
        eenheid: EenhedenEenheid,
    ) -> EenhedenEnergieprestatie | None:
        """
        Returnt de eerste geldige energieprestatie met een energielabel van een eenheid.

        Args:
            eenheid (EenhedenEenheid): De eenheid met mogelijke energieprestaties.

        Returns:
            EenhedenEnergieprestatie | None: De eerste geldige energieprestatie met een energielabel en None Wanneer er geen geldige energieprestatie met label is gevonden.
        """
        if eenheid.energieprestaties is not None:
            for energieprestatie in eenheid.energieprestaties:
                if (
                    energieprestatie.registratiedatum
                    and energieprestatie.soort
                    and energieprestatie.soort.code
                    and energieprestatie.status
                    and energieprestatie.status.code
                    and energieprestatie.begindatum
                    and energieprestatie.einddatum
                    and energieprestatie.label
                    and (
                        energieprestatie.soort.code
                        == Energieprestatiesoort.energie_index.code
                        or energieprestatie.soort.code
                        == Energieprestatiesoort.primair_energieverbruik_woningbouw.code
                        or energieprestatie.soort.code
                        == Energieprestatiesoort.voorlopig_energielabel.code  # Een voorloopig energie_label kan ook als status definitief zijn, want dit is het soort energie label gemeten met de meetmethode van voor 2015.
                    )
                    and (
                        energieprestatie.begindatum
                        < datetime.date.today()
                        < energieprestatie.einddatum
                        and energieprestatie.status.code
                        == Energieprestatiestatus.definitief.code
                    )
                    and (
                        # Check of de registratie niet ouder is dan 10 jaar
                        energieprestatie.registratiedatum
                        > (
                            (datetime.datetime.now()).astimezone()
                            - relativedelta(years=10)
                        )
                    )
                ):
                    logger.debug("Energieprestatie met geldig label gevonden")
                    return energieprestatie

        logger.debug("Geen geldige energieprestatie met label gevonden")
        return None

    @staticmethod
    def _bereken_punten_met_label(
        energieprestatie: EenhedenEnergieprestatie,
        energieprestatie_soort: str,
        label: str,
        woningtype: str,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        if energieprestatie.energieprestatievergoeding is None:
            raise TypeError(
                "voor de berekening van de energieprestatie dient aangegeven te worden of er sprake is van een energieprestatievergoeding"
            )
        if (
            energieprestatie_soort
            == Energieprestatiesoort.primair_energieverbruik_woningbouw.code
            and energieprestatie.registratiedatum
            and energieprestatie.registratiedatum
            >= datetime.datetime(2021, 1, 1).astimezone()
        ):
            if energieprestatie.gebruiksoppervlakte_thermische_zone is None:
                raise TypeError(
                    "voor de berekening van de energieprestatie met een nieuw energielabel dient de gebruiksoppervlakte van de thermische zone bekend te zijn"
                )
            else:
                criterium_naam = f"{label} + {energieprestatie.gebruiksoppervlakte_thermische_zone}m2"

                if energieprestatie.gebruiksoppervlakte_thermische_zone < 25.0:
                    lookup_key = "oppervlakte_0-25"

                elif (
                    25.0 <= energieprestatie.gebruiksoppervlakte_thermische_zone < 40.0
                ):
                    lookup_key = "oppervlakte_25-40"

                else:
                    lookup_key = "oppervlakte_40+"

        else:
            criterium_naam = f"{label} (oud)"
            lookup_key = "oud"

        df = Energieprestatie2024.lookup_mapping[lookup_key].pipe(
            filter_dataframe_op_datum, datum_filter=datetime.date(2024, 1, 1)
        )

        waarderings_label: str | None = label

        if energieprestatie.energieprestatievergoeding:
            logger.debug("Energieprestatievergoeding gevonden.")

        if (
            energieprestatie.energieprestatievergoeding
            and waarderings_label != Energielabel.b.naam
        ):
            waarderings_label = Energielabel.b.naam
            criterium_naam += f" > {waarderings_label} ivm EPV"

        filtered_df = df[(df["Label"] == waarderings_label)].pipe(dataframe_met_een_rij)

        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(naam=criterium_naam)
        )
        woningwaardering.punten = float(filtered_df[woningtype].values[0])

        return woningwaardering

    @staticmethod
    def _bereken_punten_met_bouwjaar(
        eenheid: EenhedenEenheid,
        woningtype: str,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        criterium_naam = f"Bouwjaar {eenheid.bouwjaar}"

        df = Energieprestatie2024.lookup_mapping["bouwjaar"].pipe(
            filter_dataframe_op_datum, datum_filter=datetime.date(2024, 1, 1)
        )
        filtered_df = df[
            ((df["BouwjaarMin"] <= eenheid.bouwjaar) | df["BouwjaarMin"].isnull())
            & ((df["BouwjaarMax"] >= eenheid.bouwjaar) | df["BouwjaarMax"].isnull())
        ].pipe(dataframe_met_een_rij)

        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(naam=criterium_naam)
        )
        woningwaardering.punten = float(filtered_df[woningtype].values[0])

        return woningwaardering

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

        energieprestatie = Energieprestatie2024._energieprestatie_met_geldig_label(
            eenheid
        )

        if not (
            eenheid.woningtype
            and eenheid.woningtype.naam
            and (energieprestatie or eenheid.bouwjaar)
        ):
            logger.warning(
                f"Eenheid {eenheid.id} heeft geen woningtype en/of geldig energielabel en/of bouwjaar en komt daarom niet in aanmerking voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}"
            )
            return woningwaardering_groep

        woningwaardering = WoningwaarderingResultatenWoningwaardering()

        if (
            energieprestatie
            and energieprestatie.label
            and energieprestatie.label.naam
            and energieprestatie.soort
            and energieprestatie.soort.code
        ):
            woningwaardering = Energieprestatie2024._bereken_punten_met_label(
                energieprestatie,
                energieprestatie.soort.code,
                energieprestatie.label.naam,
                eenheid.woningtype.naam,
                woningwaardering,
            )

        elif eenheid.bouwjaar and not energieprestatie:
            woningwaardering = Energieprestatie2024._bereken_punten_met_bouwjaar(
                eenheid, eenheid.woningtype.naam, woningwaardering
            )

        if woningwaardering.criterium:
            logger.debug(
                f"Eenheid {eenheid.id} met {woningwaardering.criterium.naam} krijgt {woningwaardering.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}."
            )

        woningwaardering_groep.woningwaarderingen.append(woningwaardering)
        punten_totaal = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in (
                    woningwaardering_groep.woningwaarderingen or []
                )
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten_totaal)
        return woningwaardering_groep


if __name__ == "__main__":
    logger.enable("woningwaardering")

    energieprestatie = Energieprestatie2024()
    with open(
        "tests/stelsels/zelfstandige_woonruimten/energieprestatie/data/input/eenheid_A++++_egw.json",
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
