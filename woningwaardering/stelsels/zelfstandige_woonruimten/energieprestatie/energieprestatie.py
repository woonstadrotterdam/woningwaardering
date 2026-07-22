import warnings
from datetime import date
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.gedeelde_logica.energieprestatie import (
    get_energieprestatievergoeding,
    monument_correctie,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Energielabel,
    Energieprestatiesoort,
    Pandsoort,
    PandsoortReferentiedata,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/zelfstandige_woonruimten/energieprestatie/lookup_tabellen"
)


class Energieprestatie(Stelselgroep):
    lookup_mapping = {
        "energieprestatievergoeding": pd.read_csv(
            str(
                files("woningwaardering").joinpath(
                    f"{LOOKUP_TABEL_FOLDER}/energieprestatievergoeding.csv"
                )
            )
        ),
        "label_ei": pd.read_csv(
            str(
                files("woningwaardering").joinpath(
                    f"{LOOKUP_TABEL_FOLDER}/label_en_energie-index.csv"
                )
            )
        ),
        "bouwjaar": pd.read_csv(
            str(
                files("woningwaardering").joinpath(
                    f"{LOOKUP_TABEL_FOLDER}/bouwjaar.csv"
                )
            )
        ),
    }

    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.energieprestatie
        super().__init__(
            peildatum=peildatum,
        )

    def _bereken_punten_met_label(
        self,
        eenheid: EenhedenEenheid,
        energieprestatie: EenhedenEnergieprestatie,
        pandsoort: PandsoortReferentiedata,
        waarderingsgroep_builder: WaarderingsgroepBuilder,
    ) -> WaarderingBuilder | None:
        """
        Berekent de punten voor Energieprestatie op basis van het energielabel.

        Args:
            eenheid (EenhedenEenheid): Eenheid
            energieprestatie (EenhedenEnergieprestatie): Energieprestatie van de eenheid
            pandsoort (PandsoortReferentiedata): Pandsoort van het pand
            waarderingsgroep_builder (WaarderingsgroepBuilder): Builder voor deze stelselgroep

        Returns:
            WaarderingBuilder | None: De waardering met aangepaste criteriumnaam en punten,
            of None als vereiste energieprestatiegegevens ontbreken.

        Raises:
            ValueError: Als de lookup-tabel geen unieke match oplevert voor label of energie-index.
        """
        if (
            not energieprestatie.soort
            or not energieprestatie.label
            or not energieprestatie.label.code
            or not energieprestatie.begindatum
        ):
            warnings.warn(
                f"Eenheid ({eenheid.id}): energieprestatie mist vereiste gegevens "
                f"(soort, label, label.code of begindatum) en kan daarom niet "
                f"worden gewaardeerd onder stelselgroep {self.stelselgroep.naam}.",
                UserWarning,
            )
            return None

        label = getattr(
            Energielabel, energieprestatie.label.code.lower(), energieprestatie.label
        ).naam
        woningwaardering = waarderingsgroep_builder.met_onderliggend(
            id="label", naam=label
        )

        lookup_key = "label_ei"

        df = Energieprestatie.lookup_mapping[lookup_key]

        waarderings_label: str | None = label

        if (
            lookup_key == "label_ei"
            and energieprestatie.begindatum >= date(2015, 1, 1)
            and energieprestatie.begindatum < date(2021, 1, 1)
            and energieprestatie.soort == Energieprestatiesoort.energie_index
        ):
            if energieprestatie.waarde is not None:
                logger.info(
                    f"Eenheid ({eenheid.id}): {Woningwaarderingstelselgroep.energieprestatie.naam} wordt gewaardeerd op basis van energie-index."
                )

                energie_index = float(energieprestatie.waarde)
                filtered_df = df[
                    (df["Ondergrens (exclusief)"] < energie_index)
                    & (energie_index <= (df["Bovengrens (inclusief)"]))
                ]
                if len(filtered_df) != 1:
                    raise ValueError(
                        f"Eenheid ({eenheid.id}): lookup-table gefaald voor energie-index {energie_index}."
                    )

                waarderings_label_index = str(filtered_df["Label"].values[0])

                # wanneer de energie-index afwijkt van het label, geef voorkeur aan energie-index want de index is in deze tijd afgegeven
                if label != waarderings_label_index:
                    woningwaardering.naam += (
                        f" -> {waarderings_label_index} (Energie-index)"
                    )
                    waarderings_label = waarderings_label_index
                else:
                    woningwaardering.naam += " (Energie-index)"

        filtered_df = df[(df["Label"] == waarderings_label)]
        if len(filtered_df) != 1:
            raise ValueError(
                f"Eenheid ({eenheid.id}): lookup-table gefaald voor label {waarderings_label} voor {self.stelselgroep.naam}."
            )

        woningwaardering.punten = float(filtered_df[pandsoort.naam].values[0])
        return woningwaardering

    def _bereken_punten_met_bouwjaar(
        self,
        eenheid: EenhedenEenheid,
        pandsoort: PandsoortReferentiedata,
        waarderingsgroep_builder: WaarderingsgroepBuilder,
    ) -> WaarderingBuilder:
        """
        Berekent de punten voor Energieprestatie op basis van het bouwjaar.

        Args:
            eenheid (EenhedenEenheid): Eenheid
            pandsoort (PandsoortReferentiedata): Pandsoort
            waarderingsgroep_builder (WaarderingsgroepBuilder): Builder voor deze stelselgroep

        Returns:
            WaarderingBuilder: De waardering met aangepaste criteriumnaam en punten.

        Raises:
            ValueError: Als er iets onverwachts fout gaat bij het gebruiken van een lookup-tabel.
        """

        logger.info(
            f"Eenheid ({eenheid.id}): punten voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam} worden berekend op basis van bouwjaar."
        )

        criterium_naam = f"Bouwjaar {eenheid.bouwjaar}"

        df = Energieprestatie.lookup_mapping["bouwjaar"]
        filtered_df = df[
            ((df["BouwjaarMin"] <= eenheid.bouwjaar) | df["BouwjaarMin"].isnull())
            & ((df["BouwjaarMax"] >= eenheid.bouwjaar) | df["BouwjaarMax"].isnull())
        ]
        if len(filtered_df) != 1:
            raise ValueError(
                f"Eenheid ({eenheid.id}): lookup-table gefaald voor bouwjaar {eenheid.bouwjaar} voor {self.stelselgroep.naam}."
            )

        woningwaardering = waarderingsgroep_builder.met_onderliggend(
            id="bouwjaar",
            naam=criterium_naam,
            punten=float(filtered_df[pandsoort.naam].values[0]),
        )

        return woningwaardering

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        waarderingsgroep_builder = WaarderingsgroepBuilder(
            self.stelsel, self.stelselgroep
        )

        energieprestatie = utils.energieprestatie_met_geldig_label(
            self.peildatum, eenheid
        )

        if eenheid.monumenten is None:
            warnings.warn(
                f"Eenheid ({eenheid.id}): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
                UserWarning,
            )
            eenheid = utils.update_eenheid_monumenten(eenheid)

        pandsoort = (
            Pandsoort.meergezinswoning
            if any(
                pand.soort == Pandsoort.meergezinswoning
                for pand in eenheid.panden or []
            )
            else Pandsoort.eengezinswoning
            if any(
                pand.soort == Pandsoort.eengezinswoning for pand in eenheid.panden or []
            )
            else None
        )

        if pandsoort and not pandsoort.naam:
            warnings.warn(
                f"Eenheid ({eenheid.id}) heeft een geldige pandsoort, maar de naam is niet gespecificeerd. Voeg {Pandsoort.eengezinswoning.naam} of {Pandsoort.meergezinswoning.naam} toe aan de naam van het 'pandsoort'-attribuut.",
                UserWarning,
            )
            return waarderingsgroep_builder.build()

        if not pandsoort:
            warnings.warn(
                f"Eenheid ({eenheid.id}) heeft geen pandsoort {Pandsoort.eengezinswoning.naam} of {Pandsoort.meergezinswoning.naam} en komt daarom niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}.",
                UserWarning,
            )
            return waarderingsgroep_builder.build()

        if not (energieprestatie or eenheid.bouwjaar):
            warnings.warn(
                f"Eenheid ({eenheid.id}) heeft geen bruikbare energieprestatie of bouwjaar en komt daarom niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}.",
                UserWarning,
            )
            return waarderingsgroep_builder.build()

        energieprestatievergoeding = get_energieprestatievergoeding(
            self.peildatum, eenheid
        )

        woningwaardering: WaarderingBuilder | None
        if energieprestatievergoeding:
            logger.info(f"Eenheid ({eenheid.id}): energieprestatievergoeding gevonden.")
            woningwaardering = waarderingsgroep_builder.met_onderliggend(
                id="energieprestatievergoeding",
                naam=f"Energieprestatievergoeding {pandsoort.naam}",
                punten=float(
                    Energieprestatie.lookup_mapping["energieprestatievergoeding"][
                        pandsoort.naam
                    ].values[0]
                ),
            )

        elif energieprestatie:
            woningwaardering = self._bereken_punten_met_label(
                eenheid,
                energieprestatie,
                pandsoort,
                waarderingsgroep_builder,
            )

        elif eenheid.bouwjaar and not energieprestatie:
            woningwaardering = self._bereken_punten_met_bouwjaar(
                eenheid, pandsoort, waarderingsgroep_builder
            )
        else:
            woningwaardering = waarderingsgroep_builder.met_onderliggend(
                id="onbekend", naam=""
            )

        # Voor rijks-, provinciale en gemeentelijke monumenten geldt dat de waardering voor energieprestatie minimaal 0 punten is.
        if woningwaardering is not None:
            monument_correctie(
                eenheid,
                woningwaardering,
                waarderingsgroep_builder=waarderingsgroep_builder,
            )

        woningwaardering_groep = waarderingsgroep_builder.build()

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}."
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Energieprestatie(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
