from woningwaardering.vera.bvg.models import Referentiedata


class PROJECTSTATUS:
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    """
    Het project is actief, en bevindt zich in een van de projectfasen
    """

    afgerond = Referentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    Het project is afgerond, en bevindt zich niet meer in een van de projectfasen
    """
