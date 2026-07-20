from typing import NamedTuple

from woningwaardering.vera.referentiedata import RuimtesoortReferentiedata


class GedeeldMet(NamedTuple):
    """Groeperingssleutel voor ruimten die met dezelfde aantallen worden gedeeld.

    Gebruik dit type als dict-sleutel (bijvoorbeeld bij oppervlaktegroepen).
    Heb je een ruimte in scope, gebruik dan de ruimte-attributen rechtstreeks.
    """

    aantal_adressen: int = 1
    aantal_onzelfstandige_woonruimten: int = 1


GedeeldeRuimtegroepsleutel = tuple[GedeeldMet, RuimtesoortReferentiedata]
