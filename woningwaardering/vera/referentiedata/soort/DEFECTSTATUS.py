
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class DEFECTSTATUS:

    geinspecteerd = Referentiedata(
        code="INS",
        naam="Geinspecteerd",
    )
    # geinspecteerd = ("INS", "Geinspecteerd")

    gemeld = Referentiedata(
        code="MEL",
        naam="Gemeld",
    )
    # gemeld = ("MEL", "Gemeld")
