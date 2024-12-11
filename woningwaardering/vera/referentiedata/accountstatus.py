from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AccountstatusReferentiedata(Referentiedata):
    pass


class Accountstatus(Referentiedatasoort):
    beeindigd = AccountstatusReferentiedata(
        code="BEE",
        naam="Beëindigd",
    )
    """
    Het account is beeïndigd.
    """

    geactiveerd = AccountstatusReferentiedata(
        code="GEA",
        naam="Geactiveerd",
    )
    """
    Het account is geactiveerd.
    """

    geblokkeerd = AccountstatusReferentiedata(
        code="GEB",
        naam="Geblokkeerd",
    )
    """
    Het account is (tijdelijk) geblokkeerd. Bijvoorbeeld door onjuiste invoer
    wachtwoord.
    """

    geregistreerd = AccountstatusReferentiedata(
        code="GER",
        naam="Geregistreerd",
    )
    """
    Het account is aangevraagd.
    """
