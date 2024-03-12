
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class INSPECTIERAPPORTSOORT:

    eindinspectierapport = Referentiedata(
        code="EIN",
        naam="Eindinspectierapport",
    )
    # eindinspectierapport = ("EIN", "Eindinspectierapport")
    """
    Rapport naar aanleiding van een eindinspectie
    """

    reparatieinspectierapport = Referentiedata(
        code="REP",
        naam="Reparatieinspectierapport",
    )
    # reparatieinspectierapport = ("REP", "Reparatieinspectierapport")
    """
    Inspectierapport naar aanleiding van een onduidelijk reparatieverzoek
    """

    steekproefinspectierapport = Referentiedata(
        code="STE",
        naam="Steekproefinspectierapport",
    )
    # steekproefinspectierapport = ("STE", "Steekproefinspectierapport")
    """
    Inspectierapport naar aanleiding van een uitgevoerde steekproef door een
    inspecteur/opzichter.
    """

    voorinspectierapport = Referentiedata(
        code="VOO",
        naam="Voorinspectierapport",
    )
    # voorinspectierapport = ("VOO", "Voorinspectierapport")
    """
    Rapport naar aanleiding van een voor- of tusseninspectie
    """
