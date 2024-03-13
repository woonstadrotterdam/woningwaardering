from woningwaardering.vera.bvg.models import Referentiedata


class ADRESSOORT:
    buitenlands_adres = Referentiedata(
        code="BUI",
        naam="Buitenlands adres",
    )
    """
    Een buitenlands adres
    """

    eenheid_adres = Referentiedata(
        code="EEN",
        naam="Eenheid adres",
    )
    """
    De adresgegevens van een eenheid, ook wel woonadres
    """

    postadres = Referentiedata(
        code="POS",
        naam="Postadres",
    )
    """
    Het postadres
    """
