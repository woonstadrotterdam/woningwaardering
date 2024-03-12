
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class RENTESOORT:

    variabel = Referentiedata(
        code="VAR",
        naam="Variabel",
    )
    # variabel = ("VAR", "Variabel")

    vast = Referentiedata(
        code="VST",
        naam="Vast",
    )
    # vast = ("VST", "Vast")
