from vera.referentiedata.models import Referentiedata


class Defectstatus:
    geinspecteerd = Referentiedata(
        code="INS",
        naam="Geinspecteerd",
    )

    gemeld = Referentiedata(
        code="MEL",
        naam="Gemeld",
    )
