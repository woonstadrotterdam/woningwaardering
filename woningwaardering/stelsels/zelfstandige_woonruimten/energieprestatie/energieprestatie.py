import warnings
from datetime import date, datetime
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
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
from woningwaardering.vera.referentiedata.eenheidmonument import Eenheidmonument
from woningwaardering.vera.referentiedata.energieprestatiesoort import (
    Energieprestatiesoort,
)
from woningwaardering.vera.referentiedata.oppervlaktesoort import Oppervlaktesoort
from woningwaardering.vera.referentiedata.pandsoort import Pandsoort
from woningwaardering.vera.referentiedata.prijscomponentdetailsoort import (
    Prijscomponentdetailsoort,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/zelfstandige_woonruimten/energieprestatie/lookup_tabellen"
)


class Energieprestatie(Stelselgroep):
    lookup_mapping = {
        "overgangsrecht_0-25": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/overgangsrecht_0-25m2.csv"
            )
        ),
        "overgangsrecht_25-40": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/overgangsrecht_25-40m2.csv"
            )
        ),
        "energieprestatievergoeding": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/energieprestatievergoeding.csv"
            )
        ),
        "oud_en_nieuw": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/oud_en_nieuw.csv"
            )
        ),
        "bouwjaar": pd.read_csv(
            files("woningwaardering").joinpath(f"{LOOKUP_TABEL_FOLDER}/bouwjaar.csv")
        ),
    }

    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            begindatum=date(2024, 7, 1),
            einddatum=date.max,
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.energieprestatie

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

        if (
            not energieprestatie.soort
            or not energieprestatie.soort.code
            or not energieprestatie.label
            or not energieprestatie.label.code
            or not energieprestatie.registratiedatum
        ):
            return woningwaardering

        label = energieprestatie.label.code
        woningwaardering.criterium.naam = f"{label}"
        energieprestatie_soort = energieprestatie.soort.code
        lookup_key = "oud_en_nieuw"

        if (
            energieprestatie_soort
            == Energieprestatiesoort.primair_energieverbruik_woningbouw.code
            and energieprestatie.registratiedatum >= datetime(2021, 1, 1).astimezone()
            and energieprestatie.registratiedatum < datetime(2024, 7, 1).astimezone()
            and self.peildatum
            < date(2025, 1, 1)  # Overgangsrecht kleine woningen < 40 m2 vervalt in 2025
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

            woningwaardering.criterium.naam = label

            woningwaardering.aantal = gebruiksoppervlakte_thermische_zone

            if gebruiksoppervlakte_thermische_zone < 25.0:
                logger.info(
                    f"Eenheid {eenheid.id} heeft een gebruiksoppervlakte thermische zone van {gebruiksoppervlakte_thermische_zone} m2: wordt gewaardeerd volgens het 'Overgangsrecht kleine woningen < 25 m2.'"
                )
                lookup_key = "overgangsrecht_0-25"
                woningwaardering.criterium.naam += " <25m2"

            elif 25.0 <= gebruiksoppervlakte_thermische_zone < 40.0:
                logger.info(
                    f"Eenheid {eenheid.id} heeft een gebruiksoppervlakte thermische zone van {gebruiksoppervlakte_thermische_zone} m2: wordt gewaardeerd volgens het 'Overgangsrecht kleine woningen ≥ 25m2 en < 40 m2.'"
                )
                lookup_key = "overgangsrecht_25-40"
                woningwaardering.criterium.naam += " 25-40m2"

            else:
                logger.info(
                    f"Eenheid {eenheid.id} heeft een gebruiksoppervlakte thermische zone van {gebruiksoppervlakte_thermische_zone} m2: wordt gewaardeerd volgens de puntentelling van 'Oud en Nieuw' energielabel."
                )

        df = Energieprestatie.lookup_mapping[lookup_key]

        waarderings_label: str | None = label

        if (
            lookup_key == "oud_en_nieuw"
            and energieprestatie.registratiedatum >= datetime(2015, 1, 1).astimezone()
            and energieprestatie.registratiedatum < datetime(2021, 1, 1).astimezone()
            and energieprestatie.soort.code == Energieprestatiesoort.energie_index.code
        ):
            if energieprestatie.waarde is not None:
                logger.info(
                    f"Eenheid {eenheid.id}: waardeer {Woningwaarderingstelselgroep.energieprestatie.naam} op basis van energie-index."
                )

                energie_index = float(energieprestatie.waarde)

                filtered_df = df[
                    (df["Ondergrens (exclusief)"] < energie_index)
                    & (energie_index <= (df["Bovengrens (inclusief)"]))
                ].pipe(utils.dataframe_met_een_rij)

                waarderings_label_index = filtered_df["Label"].values[0]

                # wanneer de energie-index afwijkt van het label, geef voorkeur aan energie-index want de index is in deze tijd afgegeven
                if label != waarderings_label_index:
                    woningwaardering.criterium.naam += (
                        f" -> {waarderings_label_index} (Energie-index)"
                    )
                    waarderings_label = waarderings_label_index
                else:
                    woningwaardering.criterium.naam += " (Energie-index)"

        filtered_df = df[(df["Label"] == waarderings_label)].pipe(
            utils.dataframe_met_een_rij
        )

        woningwaardering.punten = float(filtered_df[pandsoortnaam].values[0])

        return woningwaardering

    @staticmethod
    def _bereken_punten_met_bouwjaar(
        eenheid: EenhedenEenheid,
        pandsoortnaam: str,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        logger.info(
            f"Eenheid {eenheid.id}: punten voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam} worden berekend op basis van bouwjaar."
        )

        criterium_naam = f"Bouwjaar {eenheid.bouwjaar}"

        df = Energieprestatie.lookup_mapping["bouwjaar"]
        filtered_df = df[
            ((df["BouwjaarMin"] <= eenheid.bouwjaar) | df["BouwjaarMin"].isnull())
            & ((df["BouwjaarMax"] >= eenheid.bouwjaar) | df["BouwjaarMax"].isnull())
        ].pipe(utils.dataframe_met_een_rij)

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

        energieprestatie = utils.energieprestatie_met_geldig_label(
            self.peildatum, eenheid
        )

        if eenheid.monumenten is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
                UserWarning,
            )
            eenheid = utils.update_eenheid_monumenten(eenheid)

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
                f"Eenheid {eenheid.id} heeft geen pandsoort {Pandsoort.eengezinswoning.naam} of {Pandsoort.meergezinswoning.naam} en komt daarom niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}.",
                UserWarning,
            )
            return woningwaardering_groep

        if not (energieprestatie or eenheid.bouwjaar):
            warnings.warn(
                f"Eenheid {eenheid.id} heeft geen energieprestatie of bouwjaar en komt daarom niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}.",
                UserWarning,
            )
            return woningwaardering_groep

        woningwaardering = WoningwaarderingResultatenWoningwaardering()

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
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"EPV {pandsoort.naam}"
                )
            )
            woningwaardering.punten = float(
                Energieprestatie.lookup_mapping["energieprestatievergoeding"][
                    pandsoort.naam
                ].values[0]
            )

        elif energieprestatie:
            woningwaardering = self._bereken_punten_met_label(
                eenheid,
                energieprestatie,
                pandsoort.naam,
                woningwaardering,
            )

        elif eenheid.bouwjaar and not energieprestatie:
            woningwaardering = Energieprestatie._bereken_punten_met_bouwjaar(
                eenheid, pandsoort.naam, woningwaardering
            )

        woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        # Voor rijks-, provinciale en gemeentelijke monumenten geldt dat de waardering voor energieprestatie minimaal 0 punten is.
        if (
            eenheid.monumenten
            and any(
                monument.code
                in [
                    Eenheidmonument.rijksmonument.code,
                    Eenheidmonument.gemeentelijk_monument.code,
                    Eenheidmonument.provinciaal_monument.code,
                ]
                for monument in eenheid.monumenten or []
            )
            and woningwaardering.punten
            and woningwaardering.punten < 0.0
        ):
            logger.info(
                f"Eenheid {eenheid.id} is een monument: waardering voor {Woningwaarderingstelselgroep.energieprestatie.naam} is minimaal 0 punten."
            )
            woningwaardering_correctie_monument = (
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Correctie monument"
                    ),
                    punten=woningwaardering.punten * -1.0,
                )
            )

            woningwaardering_groep.woningwaarderingen.append(
                woningwaardering_correctie_monument
            )

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
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}."
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")
    warnings.simplefilter("default")
    energieprestatie = Energieprestatie(peildatum=date(2024, 7, 1))
    with open(
        "tests/data/generiek/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = energieprestatie.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
