from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class HuuropzegginghuurdersafspraakReferentiedata(Referentiedata):
    pass


class Huuropzegginghuurdersafspraak(Referentiedatasoort):
    delen_contactgegevens = HuuropzegginghuurdersafspraakReferentiedata(
        code="CON",
        naam="Delen contactgegevens",
    )
    """
    Contactgegevens mogen gedeeld worden met kandidaat huurders, zodat ze contact kunnen
    opnemen voor een bezichtiging of overname van spullen.
    """
