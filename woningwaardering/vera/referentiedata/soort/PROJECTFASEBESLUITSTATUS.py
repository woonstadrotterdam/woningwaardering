
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PROJECTFASEBESLUITSTATUS:

    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    # afgewezen = ("AFG", "Afgewezen")
    """
    Projectfasebesluit (-versie) is afgewezen
    """

    aangeboden_ter_goedkeuring = Referentiedata(
        code="ATG",
        naam="Aangeboden ter goedkeuring",
    )
    # aangeboden_ter_goedkeuring = ("ATG", "Aangeboden ter goedkeuring")
    """
    Projectfasebesluit wacht op goedkeuring, is in behandeling
    """

    concept = Referentiedata(
        code="CON",
        naam="Concept",
    )
    # concept = ("CON", "Concept")
    """
    Projectfasebesluit(-versie) in concept
    """

    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    # definitief = ("DEF", "Definitief")
    """
    Projectfasebesluit definitief maar nog niet ter goedkeuring aangeboden
    """

    goedgekeurd = Referentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    # goedgekeurd = ("GOE", "Goedgekeurd")
    """
    Projectfasebesluit is formeel goedgekeurd
    """
