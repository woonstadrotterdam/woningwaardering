from enum import Enum

from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaardering,
)


class GedeeldMetSoort(Enum):
    adressen = "adressen"
    onzelfstandige_woonruimten = "onzelfstandige_woonruimten"


def naam_gedeeld_met_groep(
    aantal: int,
    *,
    soort: GedeeldMetSoort | None = None,
) -> str:
    """Weergavenaam voor een gedeeld-met-groep (zonder prefix 'Totaal')."""
    if aantal <= 1:
        return "Privé"
    if soort == GedeeldMetSoort.adressen:
        return f"Gedeeld met {aantal} adressen"
    if soort == GedeeldMetSoort.onzelfstandige_woonruimten:
        return f"Gedeeld met {aantal} onzelfstandige woonruimten"
    raise ValueError(
        f"soort is verplicht bij gedeeld met aantal {aantal} (verwacht adressen of onzelfstandige_woonruimten)"
    )


def id_van_criterium(
    waardering: WoningwaarderingResultatenWoningwaardering,
) -> str:
    """Geef ``waardering.criterium.id`` of raise bij ontbrekende id."""
    if waardering.criterium is None or waardering.criterium.id is None:
        raise RuntimeError("interne fout: waardering zonder criterium-id")
    return waardering.criterium.id
