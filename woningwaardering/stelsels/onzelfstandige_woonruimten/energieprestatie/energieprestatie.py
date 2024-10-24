import warnings
from collections import defaultdict
from datetime import date, datetime
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import classificeer_ruimte
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
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.prijscomponentdetailsoort import (
    Prijscomponentdetailsoort,
)
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort

LOOKUP_TABEL_FOLDER = (
    "stelsels/onzelfstandige_woonruimten/energieprestatie/lookup_tabellen"
)


class Energieprestatie(Stelselgroep):
    lookup_mapping = {
        "label_ei": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/label_en_energie-index.csv"
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
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.energieprestatie  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def _bereken_punten_met_label(
        self,
        eenheid: EenhedenEenheid,
        oppervlakte: float,
        energieprestatie: EenhedenEnergieprestatie,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        if (
            not energieprestatie.soort
            or not energieprestatie.soort.code
            or not energieprestatie.label
            or not energieprestatie.label.code
            or not energieprestatie.registratiedatum
        ):
            return woningwaardering

        label = energieprestatie.label.code
        criterium_naam = f"{label}"
        df = Energieprestatie.lookup_mapping["label_ei"]

        waarderings_label = label

        if (
            energieprestatie.registratiedatum >= datetime(2015, 1, 1).astimezone()
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
                    criterium_naam += f" -> {waarderings_label_index} (Energie-index)"
                    waarderings_label = waarderings_label_index
                else:
                    criterium_naam += " (Energie-index)"

        punten_per_m2 = (
            df[(df["Label"] == waarderings_label)]
            .pipe(utils.dataframe_met_een_rij)["PuntenPerM2"]
            .values[0]
        )

        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=criterium_naam,
                meeteenheid=Meeteenheid.vierkante_meter_m2.value,
            )
        )

        woningwaardering.aantal = float(utils.rond_af(oppervlakte, decimalen=2))
        woningwaardering.punten = float(
            utils.rond_af(
                Decimal(str(punten_per_m2)) * Decimal(str(oppervlakte)), decimalen=2
            )
        )

        return woningwaardering

    def _bereken_punten_met_bouwjaar(
        self,
        eenheid: EenhedenEenheid,
        oppervlakte: float,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        logger.info(
            f"Eenheid {eenheid.id}: punten voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam} worden berekend op basis van bouwjaar."
        )

        criterium_naam = f"Bouwjaar {eenheid.bouwjaar}"

        df = Energieprestatie.lookup_mapping["bouwjaar"]
        punten_per_m2 = (
            df[
                ((df["BouwjaarMin"] <= eenheid.bouwjaar) | df["BouwjaarMin"].isnull())
                & ((df["BouwjaarMax"] >= eenheid.bouwjaar) | df["BouwjaarMax"].isnull())
            ]
            .pipe(utils.dataframe_met_een_rij)["PuntenPerM2"]
            .values[0]
        )

        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=criterium_naam,
                meeteenheid=Meeteenheid.vierkante_meter_m2.value,
            )
        )

        woningwaardering.aantal = float(utils.rond_af(oppervlakte, decimalen=2))
        woningwaardering.punten = float(
            utils.rond_af(
                Decimal(str(punten_per_m2)) * Decimal(str(oppervlakte)), decimalen=2
            )
        )

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
                stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.energieprestatie.value,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        if eenheid.ruimten is None:
            raise ValueError(f"Eenheid {eenheid.id}: ruimten is None")

        oppervlakte_gedeeld_met_counter: dict[int, float] = defaultdict(int)

        for ruimte in eenheid.ruimten:
            if ruimte.oppervlakte is None:
                warnings.warn(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen oppervlakte.",
                    UserWarning,
                )
                continue

            if classificeer_ruimte(ruimte) == Ruimtesoort.vertrek:
                oppervlakte_gedeeld_met_counter[
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                ] += float(utils.rond_af(ruimte.oppervlakte, decimalen=2))

        oppervlakte_van_vertrekken: float = sum(
            float(
                utils.rond_af(
                    (utils.rond_af(oppervlakte, decimalen=0) / Decimal(str((aantal)))),
                    decimalen=2,
                )
            )
            for aantal, oppervlakte in oppervlakte_gedeeld_met_counter.items()
        )

        if eenheid.monumenten is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
                UserWarning,
            )
            eenheid = utils.update_eenheid_monumenten(eenheid)

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

        energieprestatie = utils.energieprestatie_met_geldig_label(
            self.peildatum, eenheid
        )

        if energieprestatievergoeding:
            logger.info(f"Eenheid {eenheid.id}: energieprestatievergoeding gevonden.")
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="EPV",
                    meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                )
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
                eenheid,
                oppervlakte_van_vertrekken,
                energieprestatie,
                woningwaardering,
            )

        elif eenheid.bouwjaar and not energieprestatie:
            woningwaardering = self._bereken_punten_met_bouwjaar(
                eenheid, oppervlakte_van_vertrekken, woningwaardering
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
            utils.rond_af_op_kwart(
                sum(
                    Decimal(str(woningwaardering.punten))
                    for woningwaardering in (
                        woningwaardering_groep.woningwaarderingen or []
                    )
                    if woningwaardering.punten is not None
                )
            )
        )

        woningwaardering_groep.punten = float(punten_totaal)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}."
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    stelselgroep = Energieprestatie()
    with open(
        "tests/data/onzelfstandige_woonruimten/stelselgroepen/energieprestatie/input/monument_geen_correctie.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
