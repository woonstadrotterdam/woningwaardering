import warnings
from collections import defaultdict
from datetime import date
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.gedeelde_logica.energieprestatie import (
    get_energieprestatievergoeding,
    monument_correctie,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Energielabel,
    Energieprestatiesoort,
    Meeteenheid,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/onzelfstandige_woonruimten/energieprestatie/lookup_tabellen"
)


class Energieprestatie(Stelselgroep):
    lookup_mapping = {
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
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.energieprestatie  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            peildatum=peildatum,
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        waarderingsgroep_bouwer = WaarderingsgroepBouwer(
            self.stelsel, self.stelselgroep
        )

        if not eenheid.ruimten:
            warnings.warn(f"Eenheid ({eenheid.id}): geen ruimten gevonden")
            return waarderingsgroep_bouwer.bouw()

        if eenheid.monumenten is None:
            warnings.warn(
                f"Eenheid ({eenheid.id}): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
                UserWarning,
            )
            eenheid = utils.update_eenheid_monumenten(eenheid)

        oppervlakte_van_vertrekken = self._oppervlakte_vertrekken(eenheid)

        energieprestatievergoeding = get_energieprestatievergoeding(
            self.peildatum, eenheid
        )

        energieprestatie = utils.energieprestatie_met_geldig_label(
            self.peildatum, eenheid
        )

        if energieprestatievergoeding:
            logger.info(f"Eenheid ({eenheid.id}): energieprestatievergoeding gevonden.")
            woningwaardering = waarderingsgroep_bouwer.maak_onderliggende(
                id="energieprestatievergoeding",
                naam="Energieprestatievergoeding",
                meeteenheid=Meeteenheid.vierkante_meter_m2,
            )
            woningwaardering.aantal = float(
                utils.rond_af(oppervlakte_van_vertrekken, decimalen=2)
            )
            woningwaardering.punten = float(
                utils.rond_af(
                    Decimal("0.5") * Decimal(str(oppervlakte_van_vertrekken)),
                    decimalen=2,
                )
            )

        elif energieprestatie:
            woningwaardering = self._bereken_punten_met_label(
                waarderingsgroep_bouwer,
                eenheid,
                oppervlakte_van_vertrekken,
                energieprestatie,
            )

        elif eenheid.bouwjaar:
            woningwaardering = self._bereken_punten_met_bouwjaar(
                waarderingsgroep_bouwer, eenheid, oppervlakte_van_vertrekken
            )
        else:
            woningwaardering = waarderingsgroep_bouwer.maak_onderliggende(
                id="onbekend", naam=""
            )

        monument_correctie(
            eenheid, woningwaardering, waarderingsgroep_bouwer=waarderingsgroep_bouwer
        )

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()
        woningwaardering_groep.punten = float(
            utils.rond_af_op_kwart(Decimal(str(woningwaardering_groep.punten or 0)))
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    def _bereken_punten_met_label(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        eenheid: EenhedenEenheid,
        oppervlakte: float,
        energieprestatie: EenhedenEnergieprestatie,
    ) -> WaarderingBouwer:
        if (
            not energieprestatie.soort
            or not energieprestatie.label
            or not energieprestatie.label.code
            or not energieprestatie.begindatum
        ):
            return waarderingsgroep_bouwer.maak_onderliggende(id="label", naam="")

        label = getattr(
            Energielabel, energieprestatie.label.code.lower(), energieprestatie.label
        ).naam
        criterium_naam = f"{label}"
        df = Energieprestatie.lookup_mapping["label_ei"]

        waarderings_label = label

        if (
            energieprestatie.begindatum >= date(2015, 1, 1)
            and energieprestatie.begindatum < date(2021, 1, 1)
            and energieprestatie.soort == Energieprestatiesoort.energie_index
        ):
            if energieprestatie.waarde is not None:
                energie_index = float(energieprestatie.waarde)

                filtered_df = df[
                    (df["Ondergrens (exclusief)"] < energie_index)
                    & (energie_index <= (df["Bovengrens (inclusief)"]))
                ]
                if len(filtered_df) != 1:
                    raise ValueError(
                        f"Eenheid ({eenheid.id}): lookup-table gefaald voor energie-index {energie_index} voor {self.stelselgroep.naam}."
                    )

                waarderings_label_index = filtered_df["Label"].values[0]

                # wanneer de energie-index afwijkt van het label, geef voorkeur aan energie-index want de index is in deze tijd afgegeven
                if label != waarderings_label_index:
                    criterium_naam += f" -> {waarderings_label_index} (Energie-index)"
                    waarderings_label = waarderings_label_index
                else:
                    criterium_naam += " (Energie-index)"

        filtered_df = df[(df["Label"] == waarderings_label)]
        if len(filtered_df) != 1:
            raise ValueError(
                f"Eenheid ({eenheid.id}): lookup-table gefaald voor label {waarderings_label} voor {self.stelselgroep.naam}."
            )

        punten_per_m2 = filtered_df["PuntenPerM2"].values[0]

        woningwaardering = waarderingsgroep_bouwer.maak_onderliggende(
            id="label",
            naam=criterium_naam,
            meeteenheid=Meeteenheid.vierkante_meter_m2,
        )
        woningwaardering.aantal = float(utils.rond_af(oppervlakte, decimalen=2))
        woningwaardering.punten = float(
            utils.rond_af(
                Decimal(str(punten_per_m2)) * Decimal(str(oppervlakte)), decimalen=2
            )
        )

        logger.info(
            f"Eenheid ({eenheid.id}): krijgt {woningwaardering.punten} punten op basis van label {label} voor {self.stelselgroep.naam}."
        )

        return woningwaardering

    def _bereken_punten_met_bouwjaar(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        eenheid: EenhedenEenheid,
        oppervlakte: float,
    ) -> WaarderingBouwer:
        """
        Berekent de punten voor Energieprestatie op basis van het bouwjaar.

        Args:
            waarderingsgroep_bouwer (WaarderingsgroepBouwer): Bouwer voor deze stelselgroep
            eenheid (EenhedenEenheid): Eenheid
            oppervlakte (float): Oppervlakte

        Returns:
            WaarderingBouwer: De waardering met aangepaste criteriumnaam en punten.

        Raises:
            ValueError: Als er iets onverwachts fout gaat bij het gebruiken van een lookup-tabel.
        """
        criterium_naam = f"Bouwjaar {eenheid.bouwjaar}"

        df = Energieprestatie.lookup_mapping["bouwjaar"]
        filtered_df = df[
            (df["BouwjaarMin"] <= eenheid.bouwjaar)
            & ((df["BouwjaarMax"] >= eenheid.bouwjaar) | df["BouwjaarMax"].isnull())
        ]
        if len(filtered_df) != 1:
            raise ValueError(
                f"Eenheid ({eenheid.id}): lookup-table gefaald voor bouwjaar {eenheid.bouwjaar} voor {self.stelselgroep.naam}."
            )

        punten_per_m2 = filtered_df["PuntenPerM2"].values[0]

        woningwaardering = waarderingsgroep_bouwer.maak_onderliggende(
            id="bouwjaar",
            naam=criterium_naam,
            meeteenheid=Meeteenheid.vierkante_meter_m2,
        )
        woningwaardering.aantal = float(utils.rond_af(oppervlakte, decimalen=2))
        woningwaardering.punten = float(
            utils.rond_af(
                Decimal(str(punten_per_m2)) * Decimal(str(oppervlakte)), decimalen=2
            )
        )

        logger.info(
            f"Eenheid ({eenheid.id}): krijgt {woningwaardering.punten} punten op basis van bouwjaar {eenheid.bouwjaar} voor {self.stelselgroep.naam}."
        )

        return woningwaardering

    def _oppervlakte_vertrekken(self, eenheid: EenhedenEenheid) -> float:
        """
        Berekent de oppervlakte van de vertrekken in de eenheid.

        Args:
            eenheid (EenhedenEenheid): Eenheid

        Returns:
            float: Oppervlakte van de vertrekken.
        """
        oppervlakte_gedeeld_met_counter: defaultdict[int, Decimal] = defaultdict(
            Decimal
        )

        for ruimte in eenheid.ruimten or []:
            if ruimte.oppervlakte is None:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte.",
                    UserWarning,
                )
                continue

            if classificeer_ruimte(ruimte) == Ruimtesoort.vertrek:
                oppervlakte_gedeeld_met_counter[
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                ] += utils.rond_af(
                    Decimal(str(ruimte.oppervlakte)), decimalen=2
                )  # beleidsboek geeft expliciet aan dat moet worden afgerond op 2 decimalen

        return float(
            sum(
                utils.rond_af(
                    # op hele m2 afronden per categorie (aantal gedeeld met)
                    (utils.rond_af(oppervlakte, decimalen=0) / Decimal(str(aantal))),
                    decimalen=2,
                )
                for aantal, oppervlakte in oppervlakte_gedeeld_met_counter.items()
            )
        )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Energieprestatie(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
