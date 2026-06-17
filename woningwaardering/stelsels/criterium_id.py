from __future__ import annotations

from decimal import Decimal
from enum import Enum

from woningwaardering.vera.bvg.generated import (
    Referentiedata,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    WoningwaarderingstelselgroepReferentiedata,
)


class GedeeldMetSoort(Enum):
    adressen = "adressen"
    onzelfstandige_woonruimten = "onzelfstandige_woonruimten"


WEERGAVENAMEN: dict[str, str] = {
    "aanbelfunctie_met_video_en_audioverbinding": (
        "Aanbelfunctie met video- en audioverbinding"
    ),
    "aanwezig": "Aanwezig",
    "bouwjaar": "Bouwjaar",
    "correctie_monument": "Correctie monument",
    "correctie_zolder_zonder_vaste_trap": "Correctie: zolder zonder vaste trap",
    "energieprestatievergoeding": "Energieprestatievergoeding",
    "factor_I": "Factor I",
    "factor_II": "Factor II",
    "gebruiksoppervlakte": "Gebruiksoppervlakte",
    "gemeentelijk_of_provinciaal_monument": "Gemeentelijk of provinciaal monument",
    "geen_buitenruimten": "Geen buitenruimten",
    "geen_woz_waarde_bekend": "Geen WOZ-waarde bekend",
    "gemiddelde_woz_waarde_per_m2": "Gemiddelde WOZ-waarde per m²",
    "label": "Label",
    "laadpalen": "Laadpalen",
    "max_aantal_extra_punten": "Max aantal extra punten",
    "max_aantal_punten": "Max aantal punten",
    "maximaal_15_punten": "Maximaal 15 punten",
    "maximering": "Maximering",
    "maximering_extra_voorzieningen": "Maximering extra voorzieningen",
    "maximering_punten_voorzieningen": "Maximering punten voorzieningen",
    "maximering_woz_punten": "Maximering WOZ-punten",
    "minimum_woz_waarde": "Minimum WOZ-waarde",
    "nieuwbouw": "Nieuwbouw",
    "nieuwbouw_minimum_punten": "Nieuwbouw minimum punten",
    "onderdeel_I": "Onderdeel I",
    "onderdeel_II": "Onderdeel II",
    "open_keuken": "Open keuken",
    "oppervlakte_vertrekken_en_overige_ruimten": (
        "Oppervlakte vertrekken en overige ruimten"
    ),
    "percentage_verschil": "Percentage verschil",
    "rijksbeschermd_stads_of_dorpsgezicht": "Rijksbeschermd stads- of dorpsgezicht",
    "rijksmonument": "Rijksmonument",
    "subtotaal": "Subtotaal",
    "verkoelde_en_verwarmde_vertrekken": "Verkoelde en verwarmde vertrekken",
    "verwarmde_vertrekken": "Verwarmde vertrekken",
    "woz_waarde": "WOZ-waarde",
    "woz_waarde_per_m2": "WOZ-waarde per m²",
    "zorgwoning": "Zorgwoning",
    "zorgwoning_puntenverhoging": "Zorgwoning puntenverhoging",
}


def weergavenaam_voor(criteriumid_toevoeging: str) -> str:
    """Zet een criteriumid-toevoeging om naar een leesbare weergavenaam.

    Outputcriteria hebben machine-id's (bijv. ``verwarmde_vertrekken``); voor
    tabellen en JSON moet de ``naam`` leesbaar zijn. Bekende toevoegingen staan
    in ``WEERGAVENAMEN``; onbekende worden afgeleid met spaties en hoofdletter.

    Args:
        criteriumid_toevoeging (str): Toevoeging aan het criteriumid (bijv. groeperingsdeel).

    Returns:
        str: Weergavenaam voor het criterium.

    Example:
        >>> weergavenaam_voor("verwarmde_vertrekken")
        'Verwarmde vertrekken'
    """
    return WEERGAVENAMEN.get(
        criteriumid_toevoeging,
        criteriumid_toevoeging.replace("_", " ").capitalize(),
    )


def laatste_criteriumid_toevoeging(criteriumid: str) -> str:
    """Geeft de laatste ``criteriumid_toevoeging`` van een criteriumid.

    Bij geneste paden is vaak alleen de laatste toevoeging relevant (installatiesoort,
    groeperingsdeel). Scheiding is ``__`` tussen criteria, ``_`` binnen één toevoeging.

    Args:
        criteriumid (str): Volledig criteriumid.

    Returns:
        str: ``criteriumid_toevoeging`` na de laatste ``__``.

    Example:
        >>> laatste_criteriumid_toevoeging(
        ...     "keuken__gedeeld_met_2_adressen__Space_1__lengte_aanrecht"
        ... )
        'lengte_aanrecht'
    """
    return criteriumid.rsplit("__", 1)[-1]


class CriteriumId:
    """Bouwt criteriumids als pad van bovenliggendcriteriumids.

    Eenheidsmodel: elk output-element is een criterium met een criteriumid;
    punten en aantal zijn optioneel.

    Padregel:
        onderliggendcriteriumid == bovenliggendcriteriumid + "__" + criteriumid_toevoeging

    Gedeeld-met-criteria gebruiken één criteriumid_toevoeging, bijvoorbeeld
    ``gedeeld_met_4_adressen`` (enkele underscores binnen de ``criteriumid_toevoeging``).
    """

    __slots__ = ("_bovenliggend", "path")

    def __init__(
        self,
        path: str,
        *,
        bovenliggend: CriteriumId | None = None,
    ) -> None:
        self.path = path
        self._bovenliggend = bovenliggend

    @classmethod
    def voor_stelselgroep(
        cls, stelselgroep: WoningwaarderingstelselgroepReferentiedata
    ) -> CriteriumId:
        """Maakt het stelselgroepcriterium: de bovenste laag van elk criteriumid-pad.

        Elke stelselgroep-output begint bij de VERA-stelselgroepnaam. Dit is het
        startpunt om onderliggende criteria (gedeeld-met, geneste stelselgroepen,
        ruimten) consistent te nesten.

        Args:
            stelselgroep (WoningwaarderingstelselgroepReferentiedata): VERA-referentiedata van de stelselgroep.

        Returns:
            CriteriumId: Stelselgroepcriterium-id zonder bovenliggend criterium.

        Example:
            >>> from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep
            >>> str(CriteriumId.voor_stelselgroep(Woningwaarderingstelselgroep.keuken))
            'keuken'
        """
        return cls(path=stelselgroep.name)

    def met_onderliggend(self, criteriumid_toevoeging: str | None) -> CriteriumId:
        """Voegt een onderliggend criterium toe aan het pad.

        De padregel ``onderliggend == bovenliggend + "__" + toevoeging`` geldt
        overal in de package; deze methode voorkomt handmatig concateneren en
        houdt ``bovenliggend`` in sync voor ``bovenliggendeCriterium``.

        Args:
            criteriumid_toevoeging (str | None): Toevoeging onder dit criterium; ``None`` geeft een kopie.

        Returns:
            CriteriumId: Nieuw onderliggend criterium.

        Example:
            >>> from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep
            >>> stelselgroep_id = CriteriumId.voor_stelselgroep(Woningwaarderingstelselgroep.keuken)
            >>> str(stelselgroep_id.met_onderliggend("gedeeld_met_4_adressen"))
            'keuken__gedeeld_met_4_adressen'
        """
        if criteriumid_toevoeging is None:
            return CriteriumId(path=self.path, bovenliggend=self.bovenliggend)
        return CriteriumId(
            path=f"{self.path}__{criteriumid_toevoeging}",
            bovenliggend=self,
        )

    def gedeeld_met_criterium(
        self,
        aantal: int | None,
        soort: GedeeldMetSoort | None = None,
    ) -> CriteriumId:
        """Maakt een gedeeld-met-criterium onder dit criterium.

        Gedeelde ruimten krijgen een vast patroon in het id: ``prive`` bij aantal
        ≤ 1, anders ``gedeeld_met_{n}_{soort}``. Eén methode dekt privé- en
        gedeeld-met-takken.

        Args:
            aantal (int | None): Aantal adressen of onzelfstandige woonruimten.
            soort (GedeeldMetSoort | None): Verplicht bij aantal > 1 (adressen of onzelfstandige_woonruimten).

        Returns:
            CriteriumId: Onderliggend gedeeld-met-criterium.

        Raises:
            ValueError: Als ``aantal`` ``None`` is.

        Example:
            >>> from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep
            >>> sg = CriteriumId.voor_stelselgroep(Woningwaarderingstelselgroep.sanitair)
            >>> str(sg.gedeeld_met_criterium(8, GedeeldMetSoort.onzelfstandige_woonruimten))
            'sanitair__gedeeld_met_8_onzelfstandige_woonruimten'
        """
        if aantal is None:
            raise ValueError("aantal is vereist voor gedeeld_met_criterium")
        if aantal <= 1:
            return self.met_onderliggend("prive")
        deel = f"gedeeld_met_{aantal}"
        if soort is not None:
            deel += f"_{soort.value}"
        return self.met_onderliggend(deel)

    @property
    def bovenliggend(self) -> CriteriumId | None:
        """Direct bovenliggend criterium in het pad, of ``None`` bij het stelselgroepcriterium.

        Nodig om ``bovenliggendeCriterium`` in VERA-output te vullen en om bij
        herschrijven van ids de juiste bovenliggende laag te behouden.

        Example:
            >>> from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep
            >>> kind = CriteriumId.voor_stelselgroep(
            ...     Woningwaarderingstelselgroep.keuken
            ... ).met_onderliggend("prive")
            >>> kind.bovenliggend is not None
            True
        """
        return self._bovenliggend

    def naar_criterium_sleutels(self) -> WoningwaarderingCriteriumSleutels:
        """Zet dit id om naar een VERA ``WoningwaarderingCriteriumSleutels``.

        Output gebruikt dit type voor het veld ``bovenliggendeCriterium``; deze
        helper voorkomt herhaaldelijk ``WoningwaarderingCriteriumSleutels(id=...)``.

        Returns:
            WoningwaarderingCriteriumSleutels: Verwijzing met ``id=str(self)``.

        Example:
            >>> criterium_sleutels = CriteriumId(path="keuken__prive").naar_criterium_sleutels()
            >>> criterium_sleutels.id
            'keuken__prive'
        """
        return WoningwaarderingCriteriumSleutels(id=str(self))

    def met_criterium(
        self,
        naam: str | None,
        *,
        meeteenheid: Referentiedata | None = None,
    ) -> WoningwaarderingResultatenWoningwaarderingCriterium:
        """Bouwt een VERA-criteriumobject met id, naam en optioneel bovenliggend.

        Veel outputregels zijn structuur (naam, meeteenheid) zonder punten; deze
        methode koppelt het pad automatisch aan ``bovenliggendeCriterium``.

        Args:
            naam (str | None): Weergavenaam in output.
            meeteenheid (Referentiedata | None): Optionele VERA-meeteenheid.

        Returns:
            WoningwaarderingResultatenWoningwaarderingCriterium: Criterium klaar voor een waardering.

        Example:
            >>> from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep
            >>> c = CriteriumId.voor_stelselgroep(
            ...     Woningwaarderingstelselgroep.keuken
            ... ).met_onderliggend("gedeeld_met_2_adressen")
            >>> c.met_criterium("Gedeeld met 2 adressen").id
            'keuken__gedeeld_met_2_adressen'
        """
        criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
            id=str(self),
            naam=naam,
            meeteenheid=meeteenheid,
        )
        if self.bovenliggend is not None:
            criterium.bovenliggende_criterium = (
                self.bovenliggend.naar_criterium_sleutels()
            )
        return criterium

    def met_waardering(
        self,
        naam: str | None,
        *,
        punten: float | Decimal | None = None,
        aantal: float | None = None,
        meeteenheid: Referentiedata | None = None,
    ) -> WoningwaarderingResultatenWoningwaardering:
        """Bouwt een volledige waardering (criterium + optionele punten/aantal).

        Combineert ``met_criterium`` met punten en aantal in één stap voor
        eenvoudige stelselgroep-regels zonder aparte objectbouw.

        Args:
            naam (str | None): Weergavenaam in output.
            punten (float | Decimal | None): Punten voor de waardering.
            aantal (float | None): Optionele hoeveelheid.
            meeteenheid (Referentiedata | None): Optionele VERA-meeteenheid.

        Returns:
            WoningwaarderingResultatenWoningwaardering: Waardering met ingevuld criterium.

        Example:
            >>> from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep
            >>> w = CriteriumId.voor_stelselgroep(
            ...     Woningwaarderingstelselgroep.keuken
            ... ).met_onderliggend("ruimte_1").met_waardering("Woonkamer", punten=12.0)
            >>> w.punten
            12.0
        """
        return WoningwaarderingResultatenWoningwaardering(
            criterium=self.met_criterium(naam, meeteenheid=meeteenheid),
            punten=float(punten) if punten is not None else None,
            aantal=aantal,
        )

    def __str__(self) -> str:
        return self.path

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CriteriumId):
            return NotImplemented
        return self.path == other.path

    def __hash__(self) -> int:
        return hash(self.path)
