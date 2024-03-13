from woningwaardering.vera.bvg.models import Referentiedata


class MACHTIGINGSOORT:
    doorlopend = Referentiedata(
        code="DOO",
        naam="Doorlopend",
    )

    eenmalig = Referentiedata(
        code="EEN",
        naam="Eenmalig",
    )
