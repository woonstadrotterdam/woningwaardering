import datetime
from decimal import Decimal
from importlib.resources import files

from loguru import logger
import pandas as pd

from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import (
    dataframe_met_een_rij,
    filter_dataframe_op_datum,
    naar_tabel,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import classificeer_ruimte
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
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort

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
            woningwaardering = WoningwaarderingResultatenWoningwaardering()

            buitenruimten = [
                ruimte
                for ruimte in eenheid.ruimten
                if classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte
            ]

            if buitenruimten:
                logger.debug(
                    f"{len(buitenruimten)} buitenruimt(en) gevonden in eenheid {eenheid.id}"
                )
                for ruimte in buitenruimten:
                    # TODO: vera modellen ondersteunen dit nog niet
                    # if PriveBuitenruimten2024._buitenruimte_heeft_geldige_afmetingen(ruimte):
                    #     logger.debug(
                    #         f"Prive-buitenruimte {ruimte.id} met oppervlakte {ruimte.oppervlakte} gevonden in eenheid {eenheid.id}"
                    #     )

                    if (
                        ruimte.code == Ruimtedetailsoort.carport.code
                        or ruimte.code
                        == Ruimtedetailsoort.open_parkergarage_niet_specifieke_plek.code
                        or ruimte.code
                        == Ruimtedetailsoort.open_parkeergarage_specifieke_plek.code
                    ):
                        woningwaardering = PriveBuitenruimten2024._bereken_carport(
                            ruimte, woningwaardering
                        )

                    if (
                        ruimte.code
                        == Ruimtedetailsoort.parkeergarage_niet_specifieke_plek.code
                    ):
                        woningwaardering = PriveBuitenruimten2024._bereken_parkeergarage_niet_specifieke_plek(
                            ruimte, woningwaardering
                        )

                    if (
                        ruimte.code
                        == Ruimtedetailsoort.gemeenschappelijke_parkeerruimte_niet_specifieke_plek.code
                    ):
                        woningwaardering = PriveBuitenruimten2024._bereken_gemeenschappelijke_parkeerruimte_niet_specifieke_plek(
                            ruimte, woningwaardering
                        )

                    if (
                        ruimte.code
                        == Ruimtedetailsoort.gemeenschappelijke_parkeerruimte_specifieke_plek.code
                    ):
                        woningwaardering = PriveBuitenruimten2024._bereken_gemeenschappelijke_parkeerruimte_specifieke_plek(
                            ruimte, woningwaardering
                        )

                    else:
                        woningwaardering = PriveBuitenruimten2024._bereken_buitenruimte(
                            ruimte, woningwaardering
                        )

                    logger.info(
                        f"{ruimte.id} {ruimte.naam} krijgt {woningwaardering.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.prive_buitenruimten.naam}"
                    )

                    woningwaardering_groep.woningwaarderingen.append(woningwaardering)
            else:
                # punten aftrek wanneer er geen enkele buitenruimte is
                woningwaardering.criterium = (
                    WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Geen buitenruimte"
                    )
                )
                woningwaardering.punten = -5.0

                logger.warning(
                    f"Geen buitenruimte gevonden in eenheid {eenheid.id}: 5 punten in mindering gebracht voor stelselgroep {Woningwaarderingstelselgroep.prive_buitenruimten.naam}"
                )

        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep

    # @staticmethod
    # def _buitenruimte_heeft_geldige_grootte(ruimte) -> bool:
    #     if ruimte.diepte > 1.5 and ruimte.breedte > 1.5 and ruimte.hoogte > 1.50:
    #         return True
    #     return False

    @staticmethod
    def _bereken_punten_met_oppervlakte(oppervlakte: float) -> float:
        filtered_df = PriveBuitenruimten2024.df_oppervlakte_punten[
            (
                (
                    PriveBuitenruimten2024.df_oppervlakte_punten["OppervlakteMin"]
                    <= oppervlakte
                )
                | PriveBuitenruimten2024.df_oppervlakte_punten[
                    "OppervlakteMin"
                ].isnull()
            )
            & (
                (
                    PriveBuitenruimten2024.df_oppervlakte_punten["OppervlakteMax"]
                    >= oppervlakte
                )
                | PriveBuitenruimten2024.df_oppervlakte_punten[
                    "OppervlakteMax"
                ].isnull()
            )
        ].pipe(dataframe_met_een_rij)

        return float(filtered_df["Punten"].values[0])

    @staticmethod
    def _bereken_carport(
        ruimte: EenhedenRuimte,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=f"{ruimte.naam} (max 2 punten)",
            )
        )
        woningwaardering.punten = 2.0

        return woningwaardering

    @staticmethod
    def _bereken_parkeergarage_niet_specifieke_plek(
        ruimte: EenhedenRuimte,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        FIXED_OPPERVLAKTE = 12.0
        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                naam=f"{ruimte.naam} (vaste oppervlakte {FIXED_OPPERVLAKTE}m2)",
            )
        )
        woningwaardering.aantal = ruimte.oppervlakte
        woningwaardering.punten = (
            PriveBuitenruimten2024._bereken_punten_met_oppervlakte(FIXED_OPPERVLAKTE)
        )

        return woningwaardering

    @staticmethod
    def _bereken_gemeenschappelijke_parkeerruimte_niet_specifieke_plek(
        ruimte: EenhedenRuimte,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        oppervlakte = float(
            Decimal(str(ruimte.oppervlakte))
            / Decimal(str(ruimte.gedeeld_met_aantal_eenheden))
        )

        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=f"{ruimte.naam} (max 15 punten)",
                meeteenheid=Meeteenheid.vierkante_meter_m2.value,
            )
        )
        woningwaardering.aantal = oppervlakte

        oppervlakte_punten = PriveBuitenruimten2024._bereken_punten_met_oppervlakte(
            oppervlakte
        )
        punten = min(oppervlakte_punten, 15.0)
        woningwaardering.punten = punten

        return woningwaardering

    @staticmethod
    def _bereken_gemeenschappelijke_parkeerruimte_specifieke_plek(
        ruimte: EenhedenRuimte,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=f"{ruimte.naam} (max 2 punten)",
            )
        )
        woningwaardering.punten = 2.0
        return woningwaardering

    @staticmethod
    def _bereken_buitenruimte(
        ruimte: EenhedenRuimte,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                naam=ruimte.naam,
            )
        )
        woningwaardering.aantal = ruimte.oppervlakte
        if ruimte.oppervlakte:
            woningwaardering.punten = (
                PriveBuitenruimten2024._bereken_punten_met_oppervlakte(
                    ruimte.oppervlakte
                )
            )
        return woningwaardering


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
