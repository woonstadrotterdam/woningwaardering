from enum import Enum

from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    WoningwaarderingstelselgroepReferentiedata,
)


class GedeeldMetSoort(Enum):
    adressen = "adressen"
    onzelfstandige_woonruimten = "onzelfstandige_woonruimten"


def nest_onder(bovenliggende_id: str, criterium_id: str) -> str:
    """Nestelt een bestaande criterium-id onder een bovenliggende id.

    Het resultaat is `{bovenliggende_id}__{onderliggende onderdelen}`. Wanneer de
    onderliggende id een stelselgroep-prefix heeft (eerste `__`-segment), wordt die
    weggelaten. Anders wordt het volledige segment behouden (bijv. een categorienaam
    zonder `__`).
    """
    stelselgroep, sep, rest = criterium_id.partition("__")
    onderliggend = rest if sep else criterium_id
    return "__".join(deel for deel in (bovenliggende_id, onderliggend) if deel)


class CriteriumId:
    """Genereert criterium-id strings voor woningwaardering-output.

    Een id wordt opgebouwd uit onderdelen die met dubbele underscores (`__`)
    worden samengevoegd. De volgorde is:

    `{stelselgroep}__{gedeeld_met?}__{ruimte_id?}__{criterium?}`

    Het gedeeld-met segment (`prive` of `gedeeld_met__{n}__{soort}`) staat
    dus direct achter de stelselgroep.

    Id's kunnen hierarchisch genest worden via `bovenliggende`: wanneer een
    bovenliggende id wordt meegegeven, wordt de id opgebouwd als
    `{bovenliggende}__{eigen onderdelen}`, waarbij de eigen onderdelen de
    stelselgroep niet herhalen. Zo ontstaat een volledig pad, bijvoorbeeld een
    geneste gedeeld-met aggregaat of een detailregel onder een subgroep.
    """

    def __init__(
        self,
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
        ruimte_id: str | None = None,
        criterium: str = "",
        gedeeld_met_aantal: int | None = None,
        gedeeld_met_soort: GedeeldMetSoort | None = None,
        bovenliggende: "CriteriumId | str | None" = None,
    ):
        self.stelselgroep = stelselgroep
        self.ruimte_id = ruimte_id
        self.criterium = criterium
        self.gedeeld_met_aantal = gedeeld_met_aantal
        self.gedeeld_met_soort = gedeeld_met_soort
        self.bovenliggende = bovenliggende

    def _eigen_onderdelen(self) -> list[str]:
        """De eigen onderdelen van deze id, zonder de stelselgroep-prefix."""
        onderdelen: list[str] = []

        if self.gedeeld_met_aantal:
            if self.gedeeld_met_aantal <= 1:
                onderdelen.append("prive")
            else:
                onderdelen.extend(["gedeeld_met", str(self.gedeeld_met_aantal)])
                if self.gedeeld_met_soort:
                    onderdelen.append(self.gedeeld_met_soort.value)

        if self.ruimte_id is not None:
            onderdelen.append(self.ruimte_id)

        if self.criterium:
            onderdelen.append(self.criterium)

        return onderdelen

    def __str__(self) -> str:
        """Genereert de criterium id string."""
        if self.bovenliggende is not None:
            onderdelen = [str(self.bovenliggende), *self._eigen_onderdelen()]
        else:
            onderdelen = [self.stelselgroep.name, *self._eigen_onderdelen()]

        return "__".join(onderdelen).strip("__")
