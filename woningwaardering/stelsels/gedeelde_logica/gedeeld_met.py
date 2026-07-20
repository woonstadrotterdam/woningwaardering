from typing import NamedTuple


class GedeeldMet(NamedTuple):
    """Groeperingssleutel voor ruimten die met dezelfde aantallen worden gedeeld.

    Gebruik dit type als dict-sleutel (bijvoorbeeld bij oppervlaktegroepen).
    """

    aantal_adressen: int = 1
    aantal_onzelfstandige_woonruimten: int = 1
