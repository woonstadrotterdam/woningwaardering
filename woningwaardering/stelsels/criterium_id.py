from enum import Enum

from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    WoningwaarderingstelselgroepReferentiedata,
)


class GedeeldMetSoort(Enum):
    adressen = "adressen"
    onzelfstandige_woonruimten = "onzelfstandige_woonruimten"


class CriteriumId:
    def __init__(
        self,
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
        ruimte_id: str | None = None,
        criterium: str = "",
        gedeeld_met_aantal: int | None = None,
        gedeeld_met_soort: GedeeldMetSoort | None = None,
        is_totaal: bool = False,
    ):
        self.stelselgroep = stelselgroep
        self.ruimte_id = ruimte_id
        self.criterium = criterium
        self.gedeeld_met_aantal = gedeeld_met_aantal
        self.gedeeld_met_soort = gedeeld_met_soort
        self.is_totaal = is_totaal

    def __str__(self) -> str:
        """Genereert de criterium id string."""
        onderdelen = [self.stelselgroep.name]

        if self.ruimte_id is not None:
            onderdelen.append(self.ruimte_id)

        if self.is_totaal:
            onderdelen.append("totaal")

        if self.criterium:
            onderdelen.append(self.criterium)

        if self.gedeeld_met_aantal:
            if self.gedeeld_met_aantal <= 1:
                onderdelen.append("prive")
            else:
                onderdelen.extend(["gedeeld_met", str(self.gedeeld_met_aantal)])
                if self.gedeeld_met_soort:
                    onderdelen.append(self.gedeeld_met_soort.value)

        return "__".join(onderdelen).strip("__")
