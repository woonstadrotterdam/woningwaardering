from vera.referentiedata.models import Referentiedata


class Communicatierichting:
    inkomend = Referentiedata(
        code="INK",
        naam="Inkomend",
    )

    uitgaand = Referentiedata(
        code="UIT",
        naam="Uitgaand",
    )
