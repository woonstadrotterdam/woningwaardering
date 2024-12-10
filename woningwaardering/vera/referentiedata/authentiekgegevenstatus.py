from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AuthentiekgegevenstatusReferentiedata(Referentiedata):
    pass


class Authentiekgegevenstatus(Referentiedatasoort):
    gevalideerd = AuthentiekgegevenstatusReferentiedata(
        code="GEV",
        naam="Gevalideerd",
    )
    """
    Gegevens zijn gevalideerd door de bron.
    """

    vervallen = AuthentiekgegevenstatusReferentiedata(
        code="VER",
        naam="Vervallen",
    )
    """
    Gegevens zijn vervallen doordat deze zijn verlopen.
    """
