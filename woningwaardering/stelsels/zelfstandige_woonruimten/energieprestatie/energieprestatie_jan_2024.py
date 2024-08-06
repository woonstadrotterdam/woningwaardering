from datetime import date, datetime
from decimal import Decimal
from importlib.resources import files
import warnings

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
    Pandsoort,
    Prijscomponentdetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/zelfstandige_woonruimten/energieprestatie/lookup_tabellen"
)


class EnergieprestatieJan2024(Stelselgroepversie):
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
        pandsoortnaam: str,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium()
        )

        if not energieprestatie.soort or not energieprestatie.soort.code:
            warnings.warn(
                f"Eenheid {eenheid.id}: Energieprestatie heeft geen soort", UserWarning
            )
            return woningwaardering

        if not energieprestatie.label or not energieprestatie.label.code:
            warnings.warn(
                f"Eenheid {eenheid.id}: Energieprestatie heeft geen label", UserWarning
            )
            return woningwaardering

        if not energieprestatie.registratiedatum:
            warnings.warn(
                f"Eenheid {eenheid.id}: Energieprestatie heeft geen registratiedatum",
                UserWarning,
            )
            return woningwaardering

        label = energieprestatie.label.code

        energieprestatie_soort = energieprestatie.soort.code

        if (
            energieprestatie_soort
            == Energieprestatiesoort.primair_energieverbruik_woningbouw.code
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
                warnings.warn(
                    f"Eenheid {eenheid.id}: voor de berekening van de energieprestatie met een nieuw energielabel dient de gebruiksoppervlakte van de thermische zone bekend te zijn",
                    UserWarning,
                )
                return woningwaardering

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

        df = EnergieprestatieJan2024.lookup_mapping[lookup_key].pipe(
            filter_dataframe_op_datum, datum_filter=date(2024, 1, 1)
        )

        waarderings_label: str | None = label

        if (
            lookup_key == "oud"
            and energieprestatie.registratiedatum >= datetime(2015, 1, 1).astimezone()
        ):
            if energieprestatie.waarde is not None:
                energie_index = float(energieprestatie.waarde)

                filtered_df = df[
                    (df["Ondergrens (exclusief)"] < energie_index)
                    & (energie_index <= (df["Bovengrens (inclusief)"]))
                ].pipe(dataframe_met_een_rij)

                waarderings_label_index = filtered_df["Label"].values[0]

                if label != waarderings_label_index:
                    woningwaardering.criterium.naam += (
                        f" > {waarderings_label_index} obv Energie-index"
                    )
                    waarderings_label = waarderings_label_index

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
            logger.info(f"Eenheid {eenheid.id}: energieprestatievergoeding gevonden.")

        if energieprestatievergoeding and waarderings_label != Energielabel.b.naam:
            waarderings_label = Energielabel.b.naam
            woningwaardering.criterium.naam += f" > {waarderings_label} ivm EPV"

        filtered_df = df[(df["Label"] == waarderings_label)].pipe(dataframe_met_een_rij)

        woningwaardering.punten = float(filtered_df[pandsoortnaam].values[0])

        return woningwaardering

    @staticmethod
    def _bereken_punten_met_bouwjaar(
        eenheid: EenhedenEenheid,
        pandsoortnaam: str,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        criterium_naam = f"Bouwjaar {eenheid.bouwjaar}"

        df = EnergieprestatieJan2024.lookup_mapping["bouwjaar"].pipe(
            filter_dataframe_op_datum, datum_filter=date(2024, 1, 1)
        )
        filtered_df = df[
            ((df["BouwjaarMin"] <= eenheid.bouwjaar) | df["BouwjaarMin"].isnull())
            & ((df["BouwjaarMax"] >= eenheid.bouwjaar) | df["BouwjaarMax"].isnull())
        ].pipe(dataframe_met_een_rij)

        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(naam=criterium_naam)
        )
        woningwaardering.punten = float(filtered_df[pandsoortnaam].values[0])

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

        pandsoort = (
            Pandsoort.meergezinswoning
            if any(
                pand.soort == Pandsoort.meergezinswoning.value
                for pand in eenheid.panden or []
            )
            else Pandsoort.eengezinswoning
            if any(
                pand.soort == Pandsoort.eengezinswoning.value
                for pand in eenheid.panden or []
            )
            else None
        )

        if not pandsoort or not pandsoort.naam:
            warnings.warn(
                f"Eenheid {eenheid.id} heeft geen pandsoort {Pandsoort.eengezinswoning.naam} of {Pandsoort.meergezinswoning.naam} en komt daarom niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}",
                UserWarning,
            )
            return woningwaardering_groep

        if not (energieprestatie or eenheid.bouwjaar):
            warnings.warn(
                f"Eenheid {eenheid.id} heeft geen energieprestatie of bouwjaar en komt daarom niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}",
                UserWarning,
            )
            return woningwaardering_groep

        woningwaardering = WoningwaarderingResultatenWoningwaardering()

        if energieprestatie:
            woningwaardering = self._bereken_punten_met_label(
                eenheid,
                energieprestatie,
                pandsoort.naam,
                woningwaardering,
            )

        elif eenheid.bouwjaar and not energieprestatie:
            woningwaardering = EnergieprestatieJan2024._bereken_punten_met_bouwjaar(
                eenheid, pandsoort.naam, woningwaardering
            )

        if woningwaardering.criterium:
            logger.info(
                f"Eenheid {eenheid.id} krijgt {woningwaardering.punten} punten voor {woningwaardering.criterium.naam}."
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

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    energieprestatie = EnergieprestatieJan2024()
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
