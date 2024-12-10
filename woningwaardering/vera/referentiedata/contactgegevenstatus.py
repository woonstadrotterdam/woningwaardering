from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ContactgegevenstatusReferentiedata(Referentiedata):
    pass


class Contactgegevenstatus(Referentiedatasoort):
    aangemaakt = ContactgegevenstatusReferentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    Het contactgegeven is aangemaakt.
    """

    gevalideerd = ContactgegevenstatusReferentiedata(
        code="GEV",
        naam="Gevalideerd",
    )
    """
    Het contactgeggeven is gevalideerd via een mail, sms etc.
    """

    ongeldig = ContactgegevenstatusReferentiedata(
        code="ONG",
        naam="Ongeldig",
    )
    """
    Het contactgegeven is niet (meer) geldig.
    """
