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
    """Weergavenaam voor een groeperingscriterium op basis van criteriumid_toevoeging."""
    return WEERGAVENAMEN.get(
        criteriumid_toevoeging,
        criteriumid_toevoeging.replace("_", " ").capitalize(),
    )


def laatste_criteriumid_toevoeging(criteriumid: str) -> str:
    """Laatste segment van een criteriumid (na de laatste scheiding `__`)."""
    return criteriumid.rsplit("__", 1)[-1]


class CriteriumId:
    """Bouwt criteriumids als pad van bovenliggendcriteriumids.

    Eenheidsmodel: elk output-element is een criterium met een criteriumid;
    punten en aantal zijn optioneel.

    Padregel:
        onderliggendcriteriumid == bovenliggendcriteriumid + "__" + criteriumid_toevoeging

    Gedeeld-met aggregaten gebruiken één criteriumid_toevoeging, bijvoorbeeld
    ``gedeeld_met_4_adressen`` (enkele underscores binnen het segment).
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
        """Stelselgroepcriterium (de wortel): geen bovenliggendcriterium."""
        return cls(path=stelselgroep.name)

    def met_onderliggend(self, criteriumid_toevoeging: str | None) -> CriteriumId:
        """Onderliggendcriterium: str(self) + '__' + criteriumid_toevoeging."""
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
        """Onderliggend gedeeld-met-criterium: 'prive' of 'gedeeld_met_N_soort'."""
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
        return self._bovenliggend

    def naar_criterium_sleutels(self) -> WoningwaarderingCriteriumSleutels:
        return WoningwaarderingCriteriumSleutels(id=str(self))

    def met_criterium(
        self,
        naam: str | None,
        *,
        meeteenheid: Referentiedata | None = None,
    ) -> WoningwaarderingResultatenWoningwaarderingCriterium:
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
