from woningwaardering.vera.bvg.models import Referentiedata


class ZAAKSTATUSSOORT:
    aangemaakt = Referentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    De zaak is aangemaakt/geregistreerd maar nog niet toegewezen ter afhandeling
    """

    afgerond = Referentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    De zaak is inhoudelijk afgerond, maar nog niet definitief gesloten
    """

    geannuleerd = Referentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    """
    De afhandeling van de zaak geannuleerd
    """

    gesloten = Referentiedata(
        code="GES",
        naam="Gesloten",
    )
    """
    De zaak is afgerond en gesloten
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    De zaak is in behandeling genomen door of in behandeling gegeven aan iemand, maar er
    zijn nog geen stappen in de uitvoering gezet
    """

    in_uitvoering = Referentiedata(
        code="INU",
        naam="In uitvoering",
    )
    """
    De zaak is in uitvoering
    """
