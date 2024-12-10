from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ProjectstatusReferentiedata(Referentiedata):
    pass


class Projectstatus(Referentiedatasoort):
    actief = ProjectstatusReferentiedata(
        code="ACT",
        naam="Actief",
    )
    """
    Het project is actief, en bevindt zich in een van de projectfasen
    """

    afgerond = ProjectstatusReferentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    Het project is afgerond, en bevindt zich niet meer in een van de projectfasen
    """
