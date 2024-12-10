from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AdressoortReferentiedata(Referentiedata):
    pass


class Adressoort(Referentiedatasoort):
    buitenlands_adres = AdressoortReferentiedata(
        code="BUI",
        naam="Buitenlands adres",
    )
    """
    Een buitenlands adres.
    """

    eenheid_adres = AdressoortReferentiedata(
        code="EEN",
        naam="Eenheid adres",
    )
    """
    De adresgegevens van een eenheid, ook wel woonadres
    """

    postadres = AdressoortReferentiedata(
        code="POS",
        naam="Postadres",
    )
    """
    Het postadres
    """
