import warnings
from datetime import date
from decimal import ROUND_DOWN, Decimal
from importlib.resources import files
from itertools import chain

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
    EenhedenWozEenheid,
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


class PuntenVoorDeWozWaarde(Stelselgroep):
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
        self.stelselgroep = Woningwaarderingstelselgroep.punten_voor_de_woz_waarde
        self.pd_woz_factor = pd.read_csv(
            files("woningwaardering").joinpath(f"{LOOKUP_TABEL_FOLDER}/woz_factor.csv"),
            parse_dates=["Peildatum"],
        )
        self.pd_minimum_woz_waarde = pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/minimum_woz_waarde.csv"
            ),
            parse_dates=["Peildatum"],
        )

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
            from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
                ZelfstandigeWoonruimten,
            )

            woningwaardering_resultaat = ZelfstandigeWoonruimten(
                peildatum=self.peildatum
            ).bereken(eenheid, negeer_stelselgroep=PuntenVoorDeWozWaarde)

        if not eenheid.bouwjaar:
            warnings.warn(f"Eenheid {eenheid.id}: geen bouwjaar gevonden.", UserWarning)
            return woningwaardering_groep
        woz_eenheid = self.bepaal_woz_eenheid(eenheid)

        if woz_eenheid is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: geen WOZ-waarde gevonden", UserWarning
            )
            return woningwaardering_groep

        if woz_eenheid.vastgestelde_waarde is None:
            warnings.warn("Vastgestelde WOZ-waarde is None")
            return woningwaardering_groep

        if woz_eenheid.waardepeildatum is None:
            warnings.warn("Waardepeildatum is None")
            return woningwaardering_groep

        logger.info(
            f"Eenheid {eenheid.id}: WOZ-waarde op waardepeildatum {woz_eenheid.waardepeildatum} is {woz_eenheid.vastgestelde_waarde}"
        )

        woz_waarde = self.minimum_woz_waarde(woz_eenheid)

        if woz_waarde is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: geen minimum WOZ-waarde gevonden", UserWarning
            )
            return woningwaardering_groep

        factoren = self.pd_woz_factor[
            self.pd_woz_factor["Peildatum"]
            == pd.to_datetime(woz_eenheid.waardepeildatum)
        ].pipe(utils.dataframe_met_een_rij)

        factor_onderdeel_I = Decimal(str(factoren["Onderdeel I"].values[0]))
        factor_onderdeel_II = Decimal(str(factoren["Onderdeel II"].values[0]))

        punten_onderdeel_I = utils.rond_af(
            Decimal(woz_waarde / factor_onderdeel_I), decimalen=2
        )

        logger.info(
            f"Eenheid {eenheid.id}: Punten voor de WOZ-waarde onderdeel I is {woz_waarde} / {factor_onderdeel_I} = {punten_onderdeel_I}"
        )

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Onderdeel I"
                ),
                punten=punten_onderdeel_I,
            )
        )

        oppervlakte = self.bepaal_oppervlakte(woningwaardering_resultaat)

        if oppervlakte == 0:
            warnings.warn(
                f"Eenheid {eenheid.id}: kan geen punten voor de WOZ waarde berekenen omdat het totaal van de oppervlakte van stelselgroepen {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam} en {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam} 0 is",
                UserWarning,
            )

        punten_onderdeel_II = utils.rond_af(
            woz_waarde / oppervlakte / factor_onderdeel_II,
            decimalen=2,
        )

        logger.info(
            f"Eenheid {eenheid.id}: Punten voor de WOZ-waarde onderdeel II is {woz_waarde} / {oppervlakte} / {factor_onderdeel_II} = {punten_onderdeel_II}"
        )

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Onderdeel II"
                ),
                punten=float(punten_onderdeel_II),
            )
        )

        woningwaardering_groep = self._corrigeer_woz_punten(
            eenheid, woningwaardering_groep, woningwaardering_resultaat
        )

        punten = self._som_woz_punten(woningwaardering_groep)

        woningwaardering_groep.punten = float(utils.rond_af(punten, decimalen=0))

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.naam}"
        )

        return woningwaardering_groep

    def _corrigeer_woz_punten(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        """
        Controleert of de punten voor de stelselgroep WOZ-waarde voldoen aan de minimum punten en de maximum hoeveelheid punten.
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

        woz_punten = self._som_woz_punten(woningwaardering_groep)

        minimum_woz_punten = self._bereken_minimum_punten_nieuwbouw(
            eenheid, woningwaardering_resultaat
        )

        if (
            0.0 < woz_punten < minimum_woz_punten
            and woningwaardering_groep.woningwaarderingen is not None
        ):
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"Nieuwbouw: min. {minimum_woz_punten} punten"
                    ),
                    punten=float(minimum_woz_punten - woz_punten),
                )
            )
            return woningwaardering_groep

        # Bereken de overige punten door de punten van alle groepen op te tellen, afgerond op 0 decimalen
        overige_punten = utils.rond_af(
            sum(
                Decimal(str(groep.punten)) or Decimal("0")
                for groep in woningwaardering_resultaat.groepen or []
                if groep.punten
            ),
            0,
        )

        totaal_punten_zonder_cap = overige_punten + utils.rond_af(woz_punten, 0)
        correctie_punten = self._cap_punten(woz_punten, overige_punten)

        if (
            correctie_punten is not None
            and minimum_woz_punten == 0.0
            and woningwaardering_groep.woningwaarderingen is not None
        ):
            totaal_punten_met_cap = totaal_punten_zonder_cap + correctie_punten

            logger.debug(
                f"Eenheid {eenheid.id}: Waardering zonder cap: {totaal_punten_zonder_cap} punten. Na toepassing van cap: {totaal_punten_met_cap} punten."
            )

            # Wanneer een woning zonder die beperking een waardering heeft van meer dan
            # 186 punten en door deze beperking een waardering krijgt die lager is dan
            # 187 punten, geldt een waardering van 186 punten voor de woning.
            if totaal_punten_zonder_cap > 186 and totaal_punten_met_cap < 187:
                logger.info(
                    f"Eenheid {eenheid.id} wordt gewaardeerd met 186 punten totaal door de cap op de WOZ voor de stelselgroep {Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.naam}"
                )
                correctie_punten = 186 - totaal_punten_zonder_cap
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam="Maximering WOZ-punten tot 186 punten totaal"
                        ),
                        punten=utils.rond_af(correctie_punten, 2),
                    )
                )
            else:
                logger.info(
                    f"Eenheid {eenheid.id} wordt gewaardeerd met maximaal 33% van het totale puntenaantal van de eenheid door de cap op de WOZ voor de stelselgroep {Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.naam}"
                )
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam="Maximering WOZ-punten tot 33% van totaal"
                        ),
                        punten=utils.rond_af(correctie_punten, 2),
                    )
                )

        return woningwaardering_groep

    def _cap_punten(
        self,
        woz_punten: Decimal,
        overige_punten: Decimal,
    ) -> Decimal | None:
        """
        Berekent de cap op de WOZ. Maximaal 33% van het
        totale puntenaantal van een woning mag bepaald worden door de WOZ-waarde
        van de woning.

        Args:
            woz_punten (Decimal): Het aantal punten voor de stelselgroep WOZ-waarde.
            overige_punten (Decimal): Het totaal aantal punten van alle groepen behalve de stelselgroep WOZ-waarde.

        Returns:
            Decimal | None: De correctiepunten voor de stelselgroep WOZ-waarde.
        """
        drempel_cap_woz = Decimal("187")

        totaal_punten_zonder_cap = overige_punten + utils.rond_af(woz_punten, 0)

        if totaal_punten_zonder_cap < drempel_cap_woz:
            logger.info(
                f"Cap op op de WOZ wordt niet toegepast omdat het totaal aantal punten minder is dan {drempel_cap_woz}."
            )
            return None

        # Bereken het maximum aantal WOZ-punten dat toegestaan is
        max_woz_percentage = Decimal("33")
        overige_percentage = Decimal("100") - max_woz_percentage
        percentage_verhouding = overige_percentage / max_woz_percentage
        max_woz_punten = overige_punten / percentage_verhouding

        logger.debug(f"max_woz_punten: {max_woz_punten}")

        # Pas de cap toe op de WOZ-punten
        capped_woz_punten = min(
            Decimal(str(woz_punten)),
            max_woz_punten,
        )

        # Als de capped WOZ-punten gelijk zijn aan of groter zijn dan de oorspronkelijke
        # WOZ-punten, pas dan geen cap toe
        if capped_woz_punten >= Decimal(str(woz_punten)):
            return None
        else:
            # Indien het puntenaandeel voor de WOZ-waarde wordt beperkt op
            # ten hoogste 33%, wordt het aantal punten voor de WOZ-waarde afgerond naar
            # beneden op hele punten.
            correctiepunten = capped_woz_punten - Decimal(str(woz_punten))
            logger.debug(f"Cap punten: {correctiepunten}")
            afrondingscorrectie = min(
                (
                    utils.rond_af(capped_woz_punten, 0, rounding=ROUND_DOWN)
                    - capped_woz_punten
                ),
                Decimal(0.0),
            )
            logger.debug(f"Afronding punten: {afrondingscorrectie}")

            totaal_correctiepunten = correctiepunten + afrondingscorrectie

            return totaal_correctiepunten

    def _som_woz_punten(
        self, woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep
    ) -> Decimal:
        """
        Berekent de som van de punten voor de stelselgroep WOZ-waarde.

        Args:
            woningwaardering_groep (WoningwaarderingResultatenWoningwaarderingGroep): De woningwaardering groep voor de stelselgroep WOZ-waarde.

        Returns:
            Decimal: De som van de punten voor de stelselgroep WOZ-waarde.
        """

        return Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

    def minimum_woz_waarde(self, woz_eenheid: EenhedenWozEenheid) -> Decimal | None:
        """
        Bepaalt de minimum WOZ-waarde.

        Args:
            woz_eenheid (EenhedenWozEenheid): De WOZ-eenheid.

        Returns:
            Decimal | None: De minimum WOZ-waarde, of None indien er geen minimum vastgesteld kan worden.
        """
        if woz_eenheid.vastgestelde_waarde is None:
            warnings.warn("Vastgestelde WOZ-waarde is None")
            return None

        if woz_eenheid.waardepeildatum is None:
            warnings.warn("Waardepeildatum is None")
            return None

        vastgestelde_waarde = Decimal(str(woz_eenheid.vastgestelde_waarde))

        minimum_woz_waarde = Decimal(
            str(
                self.pd_minimum_woz_waarde[
                    self.pd_minimum_woz_waarde["Peildatum"]
                    == pd.to_datetime(woz_eenheid.waardepeildatum)
                ]
                .pipe(utils.dataframe_met_een_rij)["Minimumwaarde"]
                .values[0]
            )
        )

        if vastgestelde_waarde < minimum_woz_waarde:
            logger.info(
                f"WOZ-waarde {vastgestelde_waarde} is kleiner dan minimum {minimum_woz_waarde}, minimum wordt gebruikt"
            )
            return minimum_woz_waarde

        return vastgestelde_waarde

    def bepaal_oppervlakte(
        self,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> Decimal:
        """
        Geeft de totale oppervlakte van de stelselgroepen oppervlakte van vertrekken en oppervlakte van overige ruimten.

        Args:
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten object.

        Returns:
            Decimal: De totale oppervlakte van de stelselgroepen oppervlakte van vertrekken en oppervlakte van overige ruimten.
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
                Decimal(str(waardering.aantal))
                for waardering in chain.from_iterable(
                    groep.woningwaarderingen or []
                    for groep in oppervlakte_stelsel_groepen
                )
                if waardering.aantal is not None
            ),
            start=Decimal("0"),
        )

        return oppervlakte

    def _bereken_minimum_punten_nieuwbouw(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> Decimal:
        """
        Berekent de minimum punten voor steselgroep WOZ-waarde bij nieuwbouw of hoogniveau renovatie.

        Args:
            eenheid (EenhedenEenheid): De eenheid.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten.

        Returns:
            Decimal: De minimum punten voor stelselgroep WOZ-waarde.
        """

        minimum_punten = Decimal("0")

        bouwjaar = eenheid.bouwjaar

        hoogniveau_renovatie = PuntenVoorDeWozWaarde.hoogniveau_renovatie(
            eenheid, self.peildatum
        )
        if hoogniveau_renovatie:
            logger.info(f"Eenheid {eenheid.id}: hoogniveau renovatie geconstateerd.")

        # Indien de bouwkundige oplevering of hoogniveau renovatie van de woning heeft
        # plaatsgevonden in de jaren 2015-2019 en die woning voor de onderdelen
        # 1 t/m 10 en 12 van het woningwaarderingsstelsel minimaal 110 punten heeft
        # behaald dan worden, voor het aantal punten voor de WOZ-waarde,
        # minimaal 40 punten toegekend.
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
                    Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.code,  # 1
                    Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.code,  # 2
                    Woningwaarderingstelselgroep.verkoeling_en_verwarming.code,  # 3
                    Woningwaarderingstelselgroep.energieprestatie.code,  # 4
                    Woningwaarderingstelselgroep.keuken.code,  # 5
                    Woningwaarderingstelselgroep.sanitair.code,  # 6
                    Woningwaarderingstelselgroep.woonvoorzieningen_voor_gehandicapten.code,  # 7
                    Woningwaarderingstelselgroep.buitenruimten.code,  # 8
                    Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.code,  # 9
                    Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.code,  # 10
                    Woningwaarderingstelselgroep.bijzondere_voorzieningen.code,  # 12
                ]
            )
            logger.debug(
                f"Eenheid {eenheid.id}: punten_critische_stelselgroepen: {punten_critische_stelselgroepen}"
            )
            if punten_critische_stelselgroepen >= 110:
                minimum_punten = Decimal("40")
                logger.info(
                    f"Eenheid {eenheid.id}: minimum van 40 {Woningwaarderingstelselgroep.punten_voor_de_woz_waarde.naam}"
                )

        return minimum_punten

    def bepaal_woz_eenheid(self, eenheid: EenhedenEenheid) -> EenhedenWozEenheid | None:
        """
        bepaalt de WOZ-waarde voor de eenheid.

        Args:
            eenheid (EenhedenEenheid): de eenheid waarvoor de WOZ-waarde wordt bepaald.

        Returns:
            EenhedenWozEenheid | None: de WOZ-waarde.
        """
        woz_eenheden = sorted(
            (
                woz_eenheid
                for woz_eenheid in (eenheid.woz_eenheden or [])
                if woz_eenheid.waardepeildatum is not None
                and woz_eenheid.waardepeildatum.year in [2023, 2022]
            ),
            key=lambda x: x.waardepeildatum or date.min,
            reverse=True,
        )

        # Kies de eerste waarde uit de gesorteerde lijst
        woz_waarde = next(iter(woz_eenheden), None)

        return woz_waarde

    @staticmethod
    def hoogniveau_renovatie(eenheid: EenhedenEenheid, peildatum: date) -> bool:
        """
        Bepaalt of de eenheid een hoogniveau renovatie heeft gehad.

        Args:
            eenheid (EenhedenEenheid): De eenheid.
            peildatum (date): De peildatum van de Woningwaardering.

        Returns:
            bool: True als de eenheid een hoogniveau renovatie heeft gehad, anders False.
        """

        if not eenheid.renovatie:
            return False

        if not eenheid.renovatie.datum:
            warnings.warn(
                f"Eenheid {eenheid.id}: renovatie zonder renovatiedatum gevonden."
            )
            return False

        # De specifieke berekeningsmethodiek, die geldt voor nieuwbouwwoningen (2015-2019) (...)  is ook van toepassing
        # indien in de eerdergenoemde kalenderjaren sprake is van hoogniveau renovatie. (...) Hieruit volgt dat sprake is
        # van hoogniveau renovatie indien voor de woning een energielabel A+++ of A++++ is afgegeven (na 1 januari 2021).

        if eenheid.renovatie.datum.year < 2015:
            return False

        energieprestatie: EenhedenEnergieprestatie | None = (
            utils.energieprestatie_met_geldig_label(peildatum, eenheid)
        )

        if not energieprestatie:
            return False

        if not energieprestatie.begindatum:
            warnings.warn(
                f"Eenheid {eenheid.id}: energieprestatie zonder begindatum gevonden.",
                UserWarning,
            )
            return False

        if not energieprestatie.label:
            warnings.warn(
                f"Eenheid {eenheid.id}: energieprestatie zonder label gevonden.",
                UserWarning,
            )
            return False

        if eenheid.renovatie.datum.year <= 2019:
            if (
                energieprestatie.begindatum >= date(2021, 1, 1)
                and energieprestatie.label.naam
                and energieprestatie.label.naam in (["A+++", "A++++"])
            ):
                return True

        # Indien sprake is van verbouw in de jaren 2015-2021 dan is sprake van
        # hoogniveau renovatie als het Energie-Index van de woning lager is dan 0,4.
        if eenheid.renovatie.datum.year <= 2021:
            if not energieprestatie.waarde:
                warnings.warn(
                    f"Eenheid {eenheid.id}: energieprestatie zonder waarde (Energie-Index) gevonden bij een renovatie in de jaren 2015-2021.",
                    UserWarning,
                )
                return False
            try:
                energieprestatie_waarde = Decimal(energieprestatie.waarde)
                if energieprestatie_waarde < 0.4:
                    return True
            except ValueError:
                warnings.warn(
                    f"Eenheid {eenheid.id}: energieprestatie met een waarde (Energie-Index) dat niet kan worden omgezet in een getal ({energieprestatie.waarde}) gevonden bij een renovatie in de jaren 2015-2021"
                )
                return False

        return False


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")
    warnings.simplefilter("default", UserWarning)

    punten_voor_de_woz_waarde = PuntenVoorDeWozWaarde()
    with open(
        "tests/data/zelfstandige_woonruimten/input/20002000126.json", "r+"
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = punten_voor_de_woz_waarde.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
