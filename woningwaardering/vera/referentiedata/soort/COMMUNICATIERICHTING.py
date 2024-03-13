from woningwaardering.vera.bvg.models import Referentiedata


class COMMUNICATIERICHTING:
    inkomend = Referentiedata(
        code="INK",
        naam="Inkomend",
    )

    uitgaand = Referentiedata(
        code="UIT",
        naam="Uitgaand",
    )
