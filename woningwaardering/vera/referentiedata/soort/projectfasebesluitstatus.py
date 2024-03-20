from woningwaardering.vera.bvg.generated import Referentiedata


class Projectfasebesluitstatus:
    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Projectfasebesluit (-versie) is afgewezen
    """

    aangeboden_ter_goedkeuring = Referentiedata(
        code="ATG",
        naam="Aangeboden ter goedkeuring",
    )
    """
    Projectfasebesluit wacht op goedkeuring, is in behandeling
    """

    concept = Referentiedata(
        code="CON",
        naam="Concept",
    )
    """
    Projectfasebesluit(-versie) in concept
    """

    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    """
    Projectfasebesluit definitief maar nog niet ter goedkeuring aangeboden
    """

    goedgekeurd = Referentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    """
    Projectfasebesluit is formeel goedgekeurd
    """
