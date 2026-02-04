from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BewakingsstatusReferentiedata(Referentiedata):
    pass


class Bewakingsstatus(Referentiedatasoort):
    in_incasso = BewakingsstatusReferentiedata(
        code="INC",
        naam="In incasso",
    )
    """
    De overeenkomst is in behandeling bij een incassobureau.
    """

    normale_bewaking = BewakingsstatusReferentiedata(
        code="NOR",
        naam="Normale bewaking",
    )
    """
    Er is sprake van standaard bewaking en opvolging binnen het reguliere incassoproces
    """

    on_hold = BewakingsstatusReferentiedata(
        code="ONH",
        naam="On hold",
    )
    """
    De bewaking is tijdelijk gepauzeerd, bijvoorbeeld bij bezwaar of tijdelijk uitstel
    """
