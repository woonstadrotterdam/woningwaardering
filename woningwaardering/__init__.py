from woningwaardering._woningwaardering import Woningwaardering
from woningwaardering.stelsels.onzelfstandige_woonruimten.onzelfstandige_woonruimten import (
    OnzelfstandigeWoonruimten,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)

from ._setup import initialize

initialize()

__all__ = [
    "OnzelfstandigeWoonruimten",
    "ZelfstandigeWoonruimten",
    "Woningwaardering",
]
