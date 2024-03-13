from woningwaardering.vera.bvg.models import Referentiedata


class DEFECTSTATUS:
    geinspecteerd = Referentiedata(
        code="INS",
        naam="Geinspecteerd",
    )

    gemeld = Referentiedata(
        code="MEL",
        naam="Gemeld",
    )
