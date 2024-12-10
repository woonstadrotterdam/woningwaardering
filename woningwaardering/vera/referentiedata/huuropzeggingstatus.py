from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class HuuropzeggingstatusReferentiedata(Referentiedata):
    pass


class Huuropzeggingstatus(Referentiedatasoort):
    aangemaakt = HuuropzeggingstatusReferentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    De huuropzegging (c.q. het verzoek tot huuropzegging) is geregistreerd, maar nog
    niet in behandeling genomen.
    """

    afgewezen = HuuropzeggingstatusReferentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    De huuropzegging voldoet niet aan de voorwaarden en is afgewezen.
    """

    geannuleerd = HuuropzeggingstatusReferentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    """
    De huuropzegging is geannuleerd, voordat de beoordeling heeft plaatsgevonden.
    """

    goedgekeurd = HuuropzeggingstatusReferentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    """
    De huuropzegging voldoet aan de voorwaarden en is goedgekeurd.
    """

    in_behandeling = HuuropzeggingstatusReferentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    De huuropzegging is geregistreerd en in behandeling genomen, maar nog niet
    beoordeeld.
    """
