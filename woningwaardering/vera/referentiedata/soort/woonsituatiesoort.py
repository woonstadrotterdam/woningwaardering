from vera.referentiedata.models import Referentiedata


class Woonsituatiesoort:
    doorstromer = Referentiedata(
        code="DOO",
        naam="Doorstromer",
    )
    """
    Een doorstromer is een woningzoekende die een zelfstandige woning achterlaat.
    """

    starter = Referentiedata(
        code="STA",
        naam="Starter",
    )
    """
    Een woningzoekende die geen zelfstandige woning achterlaat. Bijvoorbeeld omdat deze
    nog thuis of in een onzelfstandige woning woont, of dat men gaat scheiden.
    """
