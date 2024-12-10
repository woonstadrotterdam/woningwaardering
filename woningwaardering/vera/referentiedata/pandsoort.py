from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PandsoortReferentiedata(Referentiedata):
    pass


class Pandsoort(Referentiedatasoort):
    eengezinswoning = PandsoortReferentiedata(
        code="EGW",
        naam="Eengezinswoning",
    )
    """
    Een eengezinswoning is een zelfstandige woning die bedoeld is om door één huishouden
    bewoond te worden.
    """

    meergezinswoning = PandsoortReferentiedata(
        code="MGW",
        naam="Meergezinswoning",
    )
    """
    Een meergezinswoning is een gebouw waarin meerdere zelfstandige wooneenheden,
    bedoeld voor bewoning door verschillende huishoudens, zijn ondergebracht.
    """
