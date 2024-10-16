from enum import Enum

from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingCriterium,
)


class CriteriumSleutels(Enum):
    """De naam van de enum moet gelijk zijn aan het id van de criterium."""

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
