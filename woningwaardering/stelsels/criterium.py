from enum import Enum


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


def maximering_naam(
    *, gedeeld: bool, met_puntental: str, gedeelde_naam: str = "Maximering"
) -> str:
    """Naam voor een maximering: zonder puntental zodra de waardering gedeeld wordt."""
    return gedeelde_naam if gedeeld else met_puntental
