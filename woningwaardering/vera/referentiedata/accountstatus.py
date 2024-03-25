from woningwaardering.vera.bvg.generated import Referentiedata


class Accountstatus:
    beeindigd = Referentiedata(
        code="BEE",
        naam="Beëindigd",
    )
    """
    Het account is beeïndigd.
    """

    geactiveerd = Referentiedata(
        code="GEA",
        naam="Geactiveerd",
    )
    """
    Het account is geactiveerd.
    """

    geblokkeerd = Referentiedata(
        code="GEB",
        naam="Geblokkeerd",
    )
    """
    Het account is (tijdelijk) geblokkeerd. Bijvoorbeeld door onjuiste invoer
    wachtwoord.
    """

    geregistreerd = Referentiedata(
        code="GER",
        naam="Geregistreerd",
    )
    """
    Het account is aangevraagd.
    """
