
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ADRESSOORT:

    buitenlands_adres = Referentiedata(
        code="BUI",
        naam="Buitenlands adres",
    )
    # buitenlands_adres = ("BUI", "Buitenlands adres")
    """
    Een buitenlands adres
    """

    eenheid_adres = Referentiedata(
        code="EEN",
        naam="Eenheid adres",
    )
    # eenheid_adres = ("EEN", "Eenheid adres")
    """
    De adresgegevens van een eenheid, ook wel woonadres
    """

    postadres = Referentiedata(
        code="POS",
        naam="Postadres",
    )
    # postadres = ("POS", "Postadres")
    """
    Het postadres
    """
