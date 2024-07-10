import datetime
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import (
    dataframe_met_een_rij,
    filter_dataframe_op_datum,
    naar_tabel,
    round_half_up,
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
                stelselgroep=Woningwaarderingstelselgroep.prive_buitenruimten.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        buitenruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte
        ]

        if buitenruimten:
            logger.debug(
                f"{len(buitenruimten)} buitenruimt(en) gevonden in eenheid {eenheid.id}"
            )

            for buitenruimte in buitenruimten:
                if (
                    buitenruimte.soort
                    and buitenruimte.soort.code
                    == Ruimtesoort.gemeenschappelijke_ruimten_en_voorzieningen.code
                    and (
                        buitenruimte.gedeeld_met_aantal_eenheden is None
                        or buitenruimte.gedeeld_met_aantal_eenheden < 2
                    )
                ):
                    raise ValueError(
                        f"{buitenruimte.naam} {buitenruimte.id} is een gemeenschappelijke ruimte en moet gedeeld worden met minimaal 2 eenheden, maar gedeeldMetAantalEenheden={buitenruimte.gedeeld_met_aantal_eenheden}"
                    )
                if buitenruimte.detail_soort is None:
                    raise ValueError(
                        f"Prive-buitenruimte {buitenruimte.naam} {buitenruimte.id} heeft geen detailsoort"
                    )
                if not PriveBuitenruimten2024._buitenruimte_heeft_geldige_afmetingen(
                    buitenruimte
                ):
                    logger.debug(
                        f"Prive-buitenruimte {buitenruimte.naam} {buitenruimte.id} komt niet in aanmerking voor waardering onder {Woningwaarderingstelselgroep.prive_buitenruimten.naam}"
                    )
                    continue

                woningwaardering = WoningwaarderingResultatenWoningwaardering()

                if buitenruimte.detail_soort.code in [
                    Ruimtedetailsoort.carport.code,
                ]:
                    woningwaardering = PriveBuitenruimten2024._bereken_carport(
                        buitenruimte, woningwaardering
                    )
                else:
                    woningwaardering = PriveBuitenruimten2024._bereken_buitenruimte(
                        buitenruimte, woningwaardering
                    )

                logger.info(
                    f"{buitenruimte.id} {buitenruimte.naam} wordt voor {woningwaardering.aantal} m2 meegerekend voor stelselgroep {Woningwaarderingstelselgroep.prive_buitenruimten.naam}"
                )

                # corrigeer buitenruimte voor wanneer deze gedeeld wordt met andere eenheden
                woningwaardering = (
                    PriveBuitenruimten2024._bereken_gedeelde_buitenruimte(
                        buitenruimte, woningwaardering
                    )
                )

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        else:
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Geen buitenruimte"
                )
            )
            # Punten aftrek wanneer er geen enkele buitenruimte is
            woningwaardering.punten = -5.0

            logger.warning(
                f"Geen buitenruimte gevonden in eenheid {eenheid.id}: 5 punten in mindering gebracht voor stelselgroep {Woningwaarderingstelselgroep.prive_buitenruimten.naam}"
            )

            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = float(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        aantal = float(
            sum(
                Decimal(str(woningwaardering.aantal))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.aantal is not None
            )
        )

        if aantal > 0:
            punten += PriveBuitenruimten2024._bereken_punten_met_oppervlakte(aantal)

        woningwaardering_groep.punten = float(punten)

        logger.info(
            (
                f"Eenheid {eenheid.id} wordt gewaardeerd met "
                f"{woningwaardering_groep.punten} punten "
                f"voor stelselgroep "
                f"{Woningwaarderingstelselgroep.prive_buitenruimten.naam}"
            )
        )
        return woningwaardering_groep

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
    def _buitenruimte_heeft_geldige_afmetingen(ruimte: EenhedenRuimte) -> bool:
        missende_attributen = [
            attr for attr in ["lengte", "breedte"] if getattr(ruimte, attr) is None
        ]

        if missende_attributen:
            error_message = (
                f"Ruimte {ruimte.naam} {ruimte.id} heeft geen "
                + " en ".join(missende_attributen)
            )
            raise ValueError(error_message)
        return (
            (ruimte.lengte or 0) >= 1.5
            and (ruimte.breedte or 0) >= 1.5
            # Hoogte mag None zijn, bijvoorbeeld bij een tuin
            # waarvan de vrije hoogte oneindig is
            and (ruimte.hoogte is None or ruimte.hoogte >= 1.5)
        )

    @staticmethod
    def _bereken_carport(
        ruimte: EenhedenRuimte,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=f"{ruimte.naam}",
            )
        )
        woningwaardering.punten = 2.0

        return woningwaardering

    @staticmethod
    def _bereken_gedeelde_buitenruimte(
        ruimte: EenhedenRuimte,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        gedeeld_met_aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
        if gedeeld_met_aantal_eenheden >= 2:
            # eigenlijk moet oppervlakte niet gedeeld worden door het aantal eenheden, maar de punten.
            # i.v.m. complexiteit daarvan is er voor gekozen om toch de oppervlakte te delen omdat in de meeste gevallen
            # dit een redelijke benadering is.
            oppervlakte = float(
                Decimal(str(ruimte.oppervlakte))
                / Decimal(str(gedeeld_met_aantal_eenheden))
            )

            woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=f"{ruimte.naam} (~{round_half_up(ruimte.oppervlakte, precision=2)}m2, gedeeld met {gedeeld_met_aantal_eenheden})",
                meeteenheid=Meeteenheid.vierkante_meter_m2.value,
            )

            woningwaardering.aantal = round_half_up(
                oppervlakte, precision=2, type_=float
            )

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
        woningwaardering.aantal = round_half_up(
            ruimte.oppervlakte, precision=2, type_=float
        )

        return woningwaardering


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    prive_buitenruimte = PriveBuitenruimten2024()
    with open(
        "tests/data/zelfstandige_woonruimten/input/37101000032.json",
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
