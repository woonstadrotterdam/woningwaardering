from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class VoorzieningsoortReferentiedata(Referentiedata):
    pass


class Voorzieningsoort(Referentiedatasoort):
    tweehandsmengkraan = VoorzieningsoortReferentiedata(
        code="THM",
        naam="Tweehandsmengkraan",
    )
    """
    Een tweehandsmengkraan heeft twee aparte knoppen of grepen voor warm en koud water.
    De gebruiker mengt handmatig de gewenste temperatuur. Deze traditionele kraan
    biedt een klassieke uitstraling en nauwkeurige temperatuurregeling.
    """
