from enum import Enum

from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingCriterium,
)


class CriteriumSleutels(Enum):
    """The enum name must be equal to the id of the criterion."""

    verwarmde_overige_en_verkeersruimten = (
        WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Verwarmde overige- en verkeersruimten",
            id="verwarmde_overige_en_verkeersruimten",
        )
    )
    verkoelde_en_verwarmde_vertrekken = (
        WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Verkoelde en verwarmde vertrekken",
            id="verkoelde_en_verwarmde_vertrekken",
        )
    )
    open_keuken = WoningwaarderingResultatenWoningwaarderingCriterium(
        naam="Open keuken",
        id="open_keuken",
    )
    verwarmde_vertrekken = WoningwaarderingResultatenWoningwaarderingCriterium(
        naam="Verwarmde vertrekken",
        id="verwarmde_vertrekken",
    )


# Example usage:
# x = "verwarmde_overige_en_verkeersruimten"
# enum_value = CriteriumSleutelsVerkoelingEnVerwarming[x]
