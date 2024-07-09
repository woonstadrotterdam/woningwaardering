from datetime import date
from decimal import ROUND_HALF_UP, Decimal
from importlib.resources import files
from itertools import chain

import pandas as pd
from loguru import logger

from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import (
    energieprestatie_met_geldig_label,
    filter_dataframe_op_datum,
    naar_tabel,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.punten_voor_de_woz_waarde.punten_voor_de_woz_waarde import (
    PuntenVoorDeWozWaarde,
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

LOOKUP_TABEL_FOLDER = (
    "stelsels/zelfstandige_woonruimten/punten_voor_de_woz_waarde/lookup_tabellen"
)


class PuntenVoorDeWozWaardeJan2024(Stelselgroepversie):
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
                stelselgroep=Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        if not woningwaardering_resultaat or not woningwaardering_resultaat.groepen:
            logger.warning(
                "Geen woningwaardering resultaat gevonden: Woningwaarderingresultaat wordt aangemaakt"
            )
            woningwaardering_resultaat = self._bereken_woningwaarderingresultaat(
                eenheid
            )

        if not eenheid.bouwjaar:
            raise ValueError(f"Geen bouwjaar gevonden voor eenheid {eenheid.id}")

        woz_waarde = self.bepaal_woz_waarde(eenheid)

        if woz_waarde is None:
            woz_waarde = 0
            logger.warning("Geen WOZ-waarde gevonden")

        woz_waarde = self.minimum_woz_waarde(woz_waarde)

        df_woz_factor = pd.read_csv(
            files("woningwaardering").joinpath(f"{LOOKUP_TABEL_FOLDER}/woz_factor.csv")
        ).pipe(filter_dataframe_op_datum, self.peildatum)

        factor_onderdeel_I = df_woz_factor["Onderdeel I"].item()

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Onderdeel I"
                ),
                punten=float(
                    Decimal(woz_waarde / factor_onderdeel_I).quantize(
                        Decimal(".01"), rounding=ROUND_HALF_UP
                    )
                ),
            )
        )

        oppervlakte = self.bepaal_oppervlakte(woningwaardering_resultaat)

        if oppervlakte == 0:
            raise ValueError(
                f"Kan geen punten voor de WOZ waarde berekenen omdat het totaal van de oppervlakte van stelselgroepen {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam} en {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam} 0 is"
            )

        factor_onderdeel_II = df_woz_factor["Onderdeel II"].astype(float).item()

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Onderdeel II"
                ),
                punten=float(
                    Decimal(woz_waarde / oppervlakte / factor_onderdeel_II).quantize(
                        Decimal(".01"), rounding=ROUND_HALF_UP
                    )
                ),
            )
        )

        woningwaardering_groep = self._corrigeer_woz_punten(
            eenheid, woningwaardering_groep, woningwaardering_resultaat
        )

        punten = self._som_woz_punten(woningwaardering_groep)
        woningwaardering_groep.punten = float(
            Decimal(str(punten)).quantize(Decimal("1"), ROUND_HALF_UP)
        )

        logger.info(
            f"Stelselgroep {Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.naam} krijgt {woningwaardering_groep.punten} punten"
        )

        return woningwaardering_groep

    def _corrigeer_woz_punten(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        """
        Controleert of de punten voor de stelselgroep WOZ-waarde voldoen aan de minumum punten en de maximum hoeveelheid punten.
        Een correctie vindt plaats wanneer:
            - Een nieuwbouwwoning niet het minimum aantal punten heeft.
            - De punten voor WOZ-waarde meer dan 33.33% van het totaal aantal punten bedraagt en geen nieuwbouwwoning is.

        Args:
            eenheid (EenhedenEenheid): De eenheid.
            woningwaardering_groep (WoningwaarderingResultatenWoningwaarderingGroep): De woningwaardering groep.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten.

        Returns:
            WoningwaarderingResultatenWoningwaarderingGroep: De woningwaardering groep met eventuele correcties.
        """

        huidige_punten = self._som_woz_punten(woningwaardering_groep)

        minimum_punten = self._bereken_minimum_punten_nieuwbouw(
            eenheid, woningwaardering_resultaat
        )

        if (
            0.0 < huidige_punten < minimum_punten
            and woningwaardering_groep.woningwaarderingen is not None
        ):
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"Nieuwbouw: min. {minimum_punten} punten"
                    ),
                    punten=minimum_punten - huidige_punten,
                )
            )
            return woningwaardering_groep

        correctie_punten = self._cap_punten(huidige_punten, woningwaardering_resultaat)

        if (
            correctie_punten < 0.0
            and minimum_punten == 0.0
            and woningwaardering_groep.woningwaarderingen is not None
        ):
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Max. 33% van totaal"
                    ),
                    punten=correctie_punten,
                )
            )
            return woningwaardering_groep

        return woningwaardering_groep

    def _cap_punten(
        self,
        punten: float,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> float:
        """
        Berekent de capping voor de stelselgroep WOZ-waarde. De punten voor WOZ mag maximaal 33.33% van het totaal aantal punten.

        Args:
            punten (float): Het aantal punten voor de stelselgroep WOZ-waarde.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten.

        Returns:
            float: De correctiepunten voor de stelselgroep WOZ-waarde.
        """

        totaal_punten = sum(
            Decimal(str(groep.punten)) or Decimal("0")
            for groep in woningwaardering_resultaat.groepen or []
            if groep.punten
        ) + Decimal(str(punten))

        cap_punten = (totaal_punten / Decimal("3")).quantize(
            Decimal(".01"), rounding=ROUND_HALF_UP
        )

        # cap niet wanneer punten onder de cap grens zitten of totaal punten lager is dan 142
        if cap_punten >= Decimal(str(punten)) or totaal_punten < Decimal("142"):
            return 0.0

        else:
            return float(cap_punten - Decimal(str(punten)))

    def _som_woz_punten(
        self, woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep
    ) -> float:
        """
        Berekent de som van de punten voor de stelselgroep WOZ-waarde.

        Args:
            woningwaardering_groep (WoningwaarderingResultatenWoningwaarderingGroep): De woningwaardering groep voor de stelselgroep WOZ-waarde.

        Returns:
            float: De som van de punten voor de stelselgroep WOZ-waarde.
        """

        return float(
            Decimal(
                sum(
                    Decimal(str(woningwaardering.punten))
                    for woningwaardering in woningwaardering_groep.woningwaarderingen
                    or []
                    if woningwaardering.punten is not None
                )
            )
        )

    def minimum_woz_waarde(self, woz_waarde: float) -> float:
        """
        Bepaalt de minimum WOZ-waarde.

        Args:
            woz_waarde (float): De WOZ-waarde.

        Returns:
            float: De minimum WOZ-waarde.
        """
        df_minimum_woz_waarde = pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/minimum_woz_waarde.csv"
            )
        ).pipe(filter_dataframe_op_datum, self.peildatum)

        minimum_woz_waarde = df_minimum_woz_waarde["Minimumwaarde"].astype(float).item()

        if woz_waarde < minimum_woz_waarde:
            logger.info(
                f"WOZ-waarde {woz_waarde} is kleiner dan minimum {minimum_woz_waarde}, minimum wordt gebruikt"
            )
            woz_waarde = minimum_woz_waarde
        return woz_waarde

    def bepaal_oppervlakte(
        self,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> float:
        """
        Geeft de totale oppervlakte van de stelselgroepen oppervlakte van vertrekken en oppervlakte van overige ruimten.

        Args:
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten object.

        Returns:
            float: De totale oppervlakte van de stelselgroepen oppervlakte van vertrekken en oppervlakte van overige ruimten.
        """
        oppervlakte_stelsel_groepen = [
            groep
            for groep in (woningwaardering_resultaat.groepen or [])
            if (
                groep.criterium_groep is not None
                and groep.criterium_groep.stelselgroep is not None
                and groep.criterium_groep.stelselgroep.code
                in [
                    Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.code,
                    Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.code,
                ]
            )
        ]

        oppervlakte = sum(
            (
                waardering.aantal
                for waardering in chain.from_iterable(
                    groep.woningwaarderingen or []
                    for groep in oppervlakte_stelsel_groepen
                )
                if waardering.aantal is not None
            ),
            start=0.0,
        )

        return oppervlakte

    def _bereken_minimum_punten_nieuwbouw(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> float:
        """
        Berekent de minimum punten voor steselgroep WOZ-waarde bij nieuwbouw of hoogniveau renovatie.

        Args:
            eenheid (EenhedenEenheid): De eenheid.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten.

        Returns:
            float: De minimum punten voor stelselgroep WOZ-waarde.
        """

        minimum_punten = 0.0

        bouwjaar = eenheid.bouwjaar

        hoogniveau_renovatie = PuntenVoorDeWozWaardeJan2024.hoogniveau_renovatie(
            eenheid, self.peildatum
        )
        if hoogniveau_renovatie:
            logger.debug("Hoogniveau renovatie geconstateerd.")

        if (bouwjaar and 2015 <= bouwjaar <= 2019) or hoogniveau_renovatie:
            punten_critische_stelselgroepen = sum(
                groep.punten or 0.0
                for groep in woningwaardering_resultaat.groepen or []
                if groep.punten
                and groep.criterium_groep
                and groep.criterium_groep.stelselgroep
                and groep.criterium_groep.stelselgroep.code
                and groep.criterium_groep.stelselgroep.code
                in [
                    Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.code,
                    Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.code,
                    Woningwaarderingstelselgroep.verwarming.code,
                    Woningwaarderingstelselgroep.energieprestatie.code,
                    Woningwaarderingstelselgroep.keuken.code,
                    Woningwaarderingstelselgroep.sanitair.code,
                    Woningwaarderingstelselgroep.woonvoorzieningen_voor_gehandicapten.code,
                    Woningwaarderingstelselgroep.prive_buitenruimten.code,
                    Woningwaarderingstelselgroep.bijzondere_voorzieningen.code,  # Zorgwoning
                ]
            )

            if punten_critische_stelselgroepen >= 110:
                minimum_punten = 40
                logger.info(
                    f"Minimum van 40 {Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.naam}"
                )

        return minimum_punten

    def bepaal_woz_waarde(self, eenheid: EenhedenEenheid) -> float | None:
        """
        bepaalt de WOZ-waarde voor de eenheid.

        Args:
            eenheid (EenhedenEenheid): de eenheid waarvoor de WOZ-waarde wordt bepaald.

        Returns:
            float | None: de WOZ-waarde.
        """
        woz_waardepeildatum = date(self.peildatum.year - 1, 1, 1)

        woz_waarde = next(
            (
                woz_eenheid.vastgestelde_waarde
                for woz_eenheid in eenheid.woz_eenheden or []
                if woz_eenheid.waardepeildatum == woz_waardepeildatum
            ),
            None,
        )

        return woz_waarde

    def _bereken_woningwaarderingresultaat(
        self, eenheid: EenhedenEenheid
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """
        Berekent de woningwaardering resultaten voor de eenheid voor alle stelselgroepen behalve stelselgroep WOZ-waarde.

        Args:
            eenheid (EenhedenEenheid): de eenheid waarvoor de woningwaardering wordt berekend.

        Returns:
            WoningwaarderingResultatenWoningwaarderingResultaat: de woningwaardering resultaten.
        """

        woningwaardering_resultaat = (
            WoningwaarderingResultatenWoningwaarderingResultaat()
        )
        woningwaardering_resultaat.stelsel = (
            Woningwaarderingstelsel.zelfstandige_woonruimten.value
        )
        woningwaardering_resultaat.groepen = []

        geldige_stelselgroepen = Stelsel.select_geldige_stelselgroepen(
            self.peildatum, Woningwaarderingstelsel.zelfstandige_woonruimten
        )

        woz_stelselgroep = PuntenVoorDeWozWaarde().stelselgroep

        for stelselgroep in geldige_stelselgroepen:
            if stelselgroep.stelselgroep == woz_stelselgroep:
                continue

            woningwaardering_groep = stelselgroep.bereken(
                eenheid, woningwaardering_resultaat
            )
            woningwaardering_resultaat.groepen.append(woningwaardering_groep)

        return woningwaardering_resultaat

    @staticmethod
    def hoogniveau_renovatie(eenheid: EenhedenEenheid, peildatum: date) -> bool:
        """
        Bepaalt of de eenheid een hoogniveau renovatie heeft gehad.

        Args:
            eenheid (EenhedenEenheid): De eenheid.
            peildatum (date): De peildatum van de Woningwaardering.

        Returns:
            bool: True als de eenheid een hoogniveau renovatie heeft gehad, anders False.

        Raises:
            ValueError: Bij ontbrekende informatie die tot een onjuiste beoordeling kan leiden.
        """

        if not eenheid.renovatie:
            return False

        if not eenheid.renovatie.datum:
            raise ValueError("Een renovatie zonder renovatiedatum gevonden")

        # De specifieke berekeningsmethodiek, die geldt voor nieuwbouwwoningen (2015-2019) (...)  is ook van toepassing
        # indien in de eerdergenoemde kalenderjaren sprake is van hoogniveau renovatie. (...) Hieruit volgt dat sprake is
        # van hoogniveau renovatie indien voor de woning een energielabel A+++ of A++++ is afgegeven (na 1 januari 2021).

        if eenheid.renovatie.datum.year < 2015:
            return False

        energieprestatie: EenhedenEnergieprestatie | None = (
            energieprestatie_met_geldig_label(peildatum, eenheid)
        )

        if not energieprestatie:
            return False

        if not energieprestatie.begindatum:
            raise ValueError("Een energieprestatie zonder begindatum gevonden")

        if not energieprestatie.label:
            raise ValueError("Een energieprestatie zonder label gevonden")

        if eenheid.renovatie.datum.year <= 2019:
            if (
                energieprestatie.begindatum >= date(2021, 1, 1)
                and energieprestatie.label.naam
                and energieprestatie.label.naam in (["A+++", "A++++"])
            ):
                return True

        # Indien sprake is van verbouw in de jaren 2015-2021 dan is sprake van hoogniveau renovatie als het Energie-Index van de woning lager is dan 0,4.
        if eenheid.renovatie.datum.year <= 2021:
            if not energieprestatie.waarde:
                raise ValueError(
                    "Een energieprestatie zonder waarde (Energie-Index) gevonden bij een eenheid met een renovatie in de jaren 2015-2021"
                )
            try:
                energieprestatie_waarde = float(energieprestatie.waarde)
            except ValueError:
                raise ValueError(
                    f"Een energieprestatie met een waarde (Energie-Index) gevonden bij een eenheid met een renovatie in de jaren 2015-2021 dat niet kan worden omgezet in een getal: {energieprestatie.waarde}"
                )
            if energieprestatie_waarde < 0.4:
                return True

        return False


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    woz = PuntenVoorDeWozWaardeJan2024()
    with open(
        "tests/data/zelfstandige_woonruimten/stelselgroepen/punten_voor_de_woz_waade/input/hoogniveau_renovatie_waarde.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = woz.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = naar_tabel(woningwaardering_resultaat)

    print(tabel)
