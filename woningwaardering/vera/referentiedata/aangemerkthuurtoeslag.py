from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AangemerkthuurtoeslagReferentiedata(Referentiedata):
    pass


class Aangemerkthuurtoeslag(Referentiedatasoort):
    aangemerkt = AangemerkthuurtoeslagReferentiedata(
        code="AAN",
        naam="Aangemerkt",
    )
    """
    De eenheid is aangemerkt voor huurtoeslag.
    """

    niet_aangemerkt = AangemerkthuurtoeslagReferentiedata(
        code="NIE",
        naam="Niet aangemerkt",
    )
    """
    De eenheid is niet aangemerkt voor huurtoeslag.
    """

    onbekend = AangemerkthuurtoeslagReferentiedata(
        code="ONB",
        naam="Onbekend",
    )
    """
    Het is niet bekend of de eenheid is aangemerkt voor huurtoeslag.
    """
