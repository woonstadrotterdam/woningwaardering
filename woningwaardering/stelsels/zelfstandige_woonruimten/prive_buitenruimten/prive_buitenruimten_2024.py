import datetime
from decimal import ROUND_HALF_UP, Decimal
from importlib.resources import files

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
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid

LOOKUP_TABEL_FOLDER = (
    "stelsels/zelfstandige_woonruimten/prive_buitenruimten/lookup_tabellen"
)


class PriveBuitenruimten2024(Stelselgroepversie):
    df_oppervlakte_punten = pd.read_csv(
        files("woningwaardering").joinpath(
            f"{LOOKUP_TABEL_FOLDER}/oppervlakte_punten.csv"
        )
    ).pipe(filter_dataframe_op_datum, datetime.date(2024, 1, 1))

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
                stelselgroep=Woningwaarderingstelselgroep.prive_buitenruimten.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        if eenheid.ruimten:
            for ruimte in eenheid.ruimten:
                # if prive-buitenruimte (tomer)
                # check of alle nodige data aanwezig is

                df = PriveBuitenruimten2024.df_oppervlakte_punten

                filtered_df = df[
                    (
                        (df["OppervlakteMin"] <= ruimte.oppervlakte)
                        | df["OppervlakteMin"].isnull()
                    )
                    & (
                        (df["OppervlakteMax"] >= ruimte.oppervlakte)
                        | df["OppervlakteMax"].isnull()
                    )
                ].pipe(dataframe_met_een_rij)

                woningwaardering = WoningwaarderingResultatenWoningwaardering()

                woningwaardering.criterium = (
                    WoningwaarderingResultatenWoningwaarderingCriterium(
                        meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                        naam=ruimte.naam,
                    )
                )

                woningwaardering.aantal = float(
                    Decimal(str(ruimte.oppervlakte)).quantize(
                        Decimal("0.01"), ROUND_HALF_UP
                    )
                )

                woningwaardering.punten = float(filtered_df["Punten"].values[0])

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

                logger.info(
                    f"Prive-buitenruimte {ruimte.id} met oppervlakte {ruimte.oppervlakte} krijgt {woningwaardering.punten} punten voor steleselgroep {Woningwaarderingstelselgroep.prive_buitenruimten.value}"
                )

        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.aantal is not None
            )
        )

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep


if __name__ == "__main__":
    logger.enable("woningwaardering")

    prive_buitenruimte = PriveBuitenruimten2024()
    with open(
        "tests/data/input/zelfstandige_woonruimten/12006000004.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = prive_buitenruimte.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = naar_tabel(woningwaardering_resultaat)

    print(tabel)
