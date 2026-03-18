from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class MonitorlogregelsoortReferentiedata(Referentiedata):
    pass


class Monitorlogregelsoort(Referentiedatasoort):
    fout = MonitorlogregelsoortReferentiedata(
        code="FOU",
        naam="Fout",
    )
    """
    De severity of de monitorlogregelsoort is een fout.
    """

    informatie = MonitorlogregelsoortReferentiedata(
        code="INF",
        naam="Informatie",
    )
    """
    De severity of de monitorlogregelsoort is informatie.
    """

    waarschuwing = MonitorlogregelsoortReferentiedata(
        code="WAA",
        naam="Waarschuwing",
    )
    """
    De severity of de monitorlogregelsoort is een waarschuwing.
    """
