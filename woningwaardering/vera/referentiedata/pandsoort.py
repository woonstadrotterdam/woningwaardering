from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Pandsoort(Referentiedatasoort):
    eengezinswoning = Referentiedata(
        code="EGW",
        naam="Eengezinswoning",
    )
    """
    Een eengezinswoning is een zelfstandige woning die bedoeld is om door één huishouden
    bewoond te worden.
    """

    meergezinswoning = Referentiedata(
        code="MGW",
        naam="Meergezinswoning",
    )
    """
    Een meergezinswoning is een gebouw waarin meerdere zelfstandige wooneenheden,
    bedoeld voor bewoning door verschillende huishoudens, zijn ondergebracht.
    """
