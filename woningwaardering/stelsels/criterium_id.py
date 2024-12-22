from enum import Enum

from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    WoningwaarderingstelselgroepReferentiedata,
)


class GedeeldMetSoort(Enum):
    adressen = "adressen"
    onzelfstandige_woonruimten = "onzelfstandige_woonruimten"


class CriteriumId:
    """Genereert een criterium id met het format:"""

    def __init__(
        self,
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
        ruimte_id: str | None = "totaal",
        criterium: str = "",
        gedeeld_met_aantal: int | None = None,
        gedeeld_met_soort: GedeeldMetSoort | None = None,
    ):
        self.stelselgroep = stelselgroep
        self.ruimte_id = ruimte_id
        self.criterium = criterium
        self.gedeeld_met_aantal = gedeeld_met_aantal
        self.gedeeld_met_soort = gedeeld_met_soort

    def __str__(self) -> str:
        """Genereert de criterium id string."""
        onderdelen = [self.stelselgroep.name]

        # Voeg ruimte_id toe als deze bestaat, anders een lege string
        onderdelen.append(self.ruimte_id or "")

        # Controleer of criterium bestaat en voeg deze toe
        if self.criterium:
            onderdelen.append(self.criterium)

        # Voeg gedeeld met aantal en soort toe
        if self.gedeeld_met_aantal:
            if self.gedeeld_met_aantal <= 1:
                onderdelen.append("prive")
            else:
                onderdelen.extend(["gedeeld_met", str(self.gedeeld_met_aantal)])
                if self.gedeeld_met_soort:
                    onderdelen.append(self.gedeeld_met_soort.value)

        # Combineer alle onderdelen met dubbele underscores
        return "__".join(onderdelen).strip("__")
