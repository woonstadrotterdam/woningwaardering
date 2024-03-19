from vera.bvg.generated import Referentiedata


class Communicatierichting:
    inkomend = Referentiedata(
        code="INK",
        naam="Inkomend",
    )

    uitgaand = Referentiedata(
        code="UIT",
        naam="Uitgaand",
    )
