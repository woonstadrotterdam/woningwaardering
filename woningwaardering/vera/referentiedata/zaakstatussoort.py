from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ZaakstatussoortReferentiedata(Referentiedata):
    pass


class Zaakstatussoort(Referentiedatasoort):
    aangemaakt = ZaakstatussoortReferentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    De zaak is aangemaakt/geregistreerd maar nog niet toegewezen ter afhandeling
    """

    afgerond = ZaakstatussoortReferentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    De zaak is inhoudelijk afgerond, maar nog niet definitief gesloten
    """

    geannuleerd = ZaakstatussoortReferentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    """
    De afhandeling van de zaak geannuleerd
    """

    gesloten = ZaakstatussoortReferentiedata(
        code="GES",
        naam="Gesloten",
    )
    """
    De zaak is afgerond en gesloten
    """

    in_behandeling = ZaakstatussoortReferentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    De zaak is in behandeling genomen door of in behandeling gegeven aan iemand, maar er
    zijn nog geen stappen in de uitvoering gezet
    """

    in_uitvoering = ZaakstatussoortReferentiedata(
        code="INU",
        naam="In uitvoering",
    )
    """
    De zaak is in uitvoering
    """
