from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class DagdeelReferentiedata(Referentiedata):
    pass


class Dagdeel(Referentiedatasoort):
    avond = DagdeelReferentiedata(
        code="AVO",
        naam="Avond",
    )
    """
    Tussen 18 en 24 uur.
    """

    middag = DagdeelReferentiedata(
        code="MID",
        naam="Middag",
    )
    """
    Tussen 12 en 18 uur.
    """

    ochtend = DagdeelReferentiedata(
        code="OCH",
        naam="Ochtend",
    )
    """
    Tussen 8 en 12 uur.
    """
