from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class WoonsituatiesoortReferentiedata(Referentiedata):
    pass


class Woonsituatiesoort(Referentiedatasoort):
    doorstromer = WoonsituatiesoortReferentiedata(
        code="DOO",
        naam="Doorstromer",
    )
    """
    Een doorstromer is een woningzoekende die een zelfstandige woning achterlaat.
    """

    starter = WoonsituatiesoortReferentiedata(
        code="STA",
        naam="Starter",
    )
    """
    Een woningzoekende die geen zelfstandige woning achterlaat. Bijvoorbeeld omdat deze
    nog thuis of in een onzelfstandige woning woont, of dat men gaat scheiden.
    """
