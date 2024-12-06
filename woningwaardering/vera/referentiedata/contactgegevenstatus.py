from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Contactgegevenstatus(Referentiedatasoort):
    aangemaakt = Referentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    Het contactgegeven is aangemaakt.
    """

    gevalideerd = Referentiedata(
        code="GEV",
        naam="Gevalideerd",
    )
    """
    Het contactgeggeven is gevalideerd via een mail, sms etc.
    """

    ongeldig = Referentiedata(
        code="ONG",
        naam="Ongeldig",
    )
    """
    Het contactgegeven is niet (meer) geldig.
    """
