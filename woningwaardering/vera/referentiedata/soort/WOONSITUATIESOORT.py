
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class WOONSITUATIESOORT:

    doorstromer = Referentiedata(
        code="DOO",
        naam="Doorstromer",
    )
    # doorstromer = ("DOO", "Doorstromer")
    """
    Een doorstromer is een woningzoekende die een zelfstandige woning achterlaat.
    """

    starter = Referentiedata(
        code="STA",
        naam="Starter",
    )
    # starter = ("STA", "Starter")
    """
    Een woningzoekende die geen zelfstandige woning achterlaat. Bijvoorbeeld omdat deze
    nog thuis of in een onzelfstandige woning woont, of dat men gaat scheiden.
    """
