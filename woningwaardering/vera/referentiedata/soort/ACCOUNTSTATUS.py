
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ACCOUNTSTATUS:

    beeindigd = Referentiedata(
        code="BEE",
        naam="Beëindigd",
    )
    # beeindigd = ("BEE", "Beëindigd")
    """
    Het account is beeïndigd.
    """

    geactiveerd = Referentiedata(
        code="GEA",
        naam="Geactiveerd",
    )
    # geactiveerd = ("GEA", "Geactiveerd")
    """
    Het account is geactiveerd.
    """

    geblokkeerd = Referentiedata(
        code="GEB",
        naam="Geblokkeerd",
    )
    # geblokkeerd = ("GEB", "Geblokkeerd")
    """
    Het account is (tijdelijk) geblokkeerd. Bijvoorbeeld door onjuiste invoer
    wachtwoord.
    """

    geregistreerd = Referentiedata(
        code="GER",
        naam="Geregistreerd",
    )
    # geregistreerd = ("GER", "Geregistreerd")
    """
    Het account is aangevraagd.
    """
