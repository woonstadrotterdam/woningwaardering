from datetime import date, datetime
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import (
    dataframe_met_een_rij,
    energieprestatie_met_geldig_label,
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
    Energielabel,
    Energieprestatiesoort,
    Meeteenheid,
    Oppervlaktesoort,
    Prijscomponentdetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
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

    def _bereken_punten_met_label(
        self,
        eenheid: EenhedenEenheid,
        energieprestatie: EenhedenEnergieprestatie,
        energieprestatie_soort: str,
        label: str,
        woningtype: str,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium()
        )

        if (
            energieprestatie_soort
            == Energieprestatiesoort.primair_energieverbruik_woningbouw.code
            and energieprestatie.registratiedatum
            and energieprestatie.registratiedatum >= datetime(2021, 1, 1).astimezone()
        ):
            gebruiksoppervlakte_thermische_zone = next(
                (
                    float(oppervlakte.waarde)
                    for oppervlakte in eenheid.oppervlakten or []
                    if oppervlakte.soort is not None
                    and oppervlakte.soort.code
                    == Oppervlaktesoort.gebruiksoppervlakte_thermische_zone.code
                    and oppervlakte.waarde is not None
                ),
                None,
            )

            if gebruiksoppervlakte_thermische_zone is None:
                raise TypeError(
                    "voor de berekening van de energieprestatie met een nieuw energielabel dient de gebruiksoppervlakte van de thermische zone bekend te zijn"
                )
            else:
                woningwaardering.criterium.naam = label
                woningwaardering.criterium.meeteenheid = (
                    Meeteenheid.vierkante_meter_m2.value
                )
                woningwaardering.aantal = gebruiksoppervlakte_thermische_zone

                if gebruiksoppervlakte_thermische_zone < 25.0:
                    lookup_key = "oppervlakte_0-25"

                elif 25.0 <= gebruiksoppervlakte_thermische_zone < 40.0:
                    lookup_key = "oppervlakte_25-40"

                else:
                    lookup_key = "oppervlakte_40+"

        else:
            woningwaardering.criterium.naam = f"{label} (oud)"
            lookup_key = "oud"

        df = Energieprestatie2024.lookup_mapping[lookup_key].pipe(
            filter_dataframe_op_datum, datum_filter=date(2024, 1, 1)
        )

        waarderings_label: str | None = label

        energieprestatievergoeding = next(
            (
                prijscomponent
                for prijscomponent in eenheid.prijscomponenten or []
                if prijscomponent.detail_soort is not None
                and prijscomponent.detail_soort.code
                == Prijscomponentdetailsoort.energieprestatievergoeding.code
                and (
                    prijscomponent.begindatum is None
                    or prijscomponent.begindatum <= self.peildatum
                )
                and (
                    prijscomponent.einddatum is None
                    or prijscomponent.einddatum > self.peildatum
                )
            ),
            None,
        )

        if energieprestatievergoeding:
            logger.debug("Energieprestatievergoeding gevonden.")

        if energieprestatievergoeding and waarderings_label != Energielabel.b.naam:
            waarderings_label = Energielabel.b.naam
            woningwaardering.criterium.naam += f" > {waarderings_label} ivm EPV"

        filtered_df = df[(df["Label"] == waarderings_label)].pipe(dataframe_met_een_rij)

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
            filter_dataframe_op_datum, datum_filter=date(2024, 1, 1)
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
                stelselgroep=Woningwaarderingstelselgroep.energieprestatie.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        energieprestatie = energieprestatie_met_geldig_label(self.peildatum, eenheid)

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
            woningwaardering = self._bereken_punten_met_label(
                eenheid,
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
        "tests/data/zelfstandige_woonruimten/stelselgroepen/energieprestatie/input/eenheid_A++++_egw.json",
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
