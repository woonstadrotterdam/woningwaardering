from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ProjectfasebesluitstatusReferentiedata(Referentiedata):
    pass


class Projectfasebesluitstatus(Referentiedatasoort):
    afgewezen = ProjectfasebesluitstatusReferentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Projectfasebesluit (-versie) is afgewezen
    """

    aangeboden_ter_goedkeuring = ProjectfasebesluitstatusReferentiedata(
        code="ATG",
        naam="Aangeboden ter goedkeuring",
    )
    """
    Projectfasebesluit wacht op goedkeuring, is in behandeling
    """

    concept = ProjectfasebesluitstatusReferentiedata(
        code="CON",
        naam="Concept",
    )
    """
    Projectfasebesluit(-versie) in concept
    """

    definitief = ProjectfasebesluitstatusReferentiedata(
        code="DEF",
        naam="Definitief",
    )
    """
    Projectfasebesluit definitief maar nog niet ter goedkeuring aangeboden
    """

    goedgekeurd = ProjectfasebesluitstatusReferentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    """
    Projectfasebesluit is formeel goedgekeurd
    """
