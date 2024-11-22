from .bijzondere_voorzieningen import waardeer_bijzondere_voorzieningen
from .keuken import waardeer_keuken
from .oppervlakte_van_overige_ruimten import waardeer_oppervlakte_van_overige_ruimten
from .oppervlakte_van_vertrekken import waardeer_oppervlakte_van_vertrekken
from .sanitair import waardeer_sanitair

__all__ = [
    "waardeer_bijzondere_voorzieningen",
    "waardeer_oppervlakte_van_vertrekken",
    "waardeer_oppervlakte_van_overige_ruimten",
    "waardeer_keuken",
    "waardeer_sanitair",
]
