from vera.bvg.generated import Referentiedata


class Inspectierapportsoort:
    eindinspectierapport = Referentiedata(
        code="EIN",
        naam="Eindinspectierapport",
    )
    """
    Rapport naar aanleiding van een eindinspectie
    """

    reparatieinspectierapport = Referentiedata(
        code="REP",
        naam="Reparatieinspectierapport",
    )
    """
    Inspectierapport naar aanleiding van een onduidelijk reparatieverzoek
    """

    steekproefinspectierapport = Referentiedata(
        code="STE",
        naam="Steekproefinspectierapport",
    )
    """
    Inspectierapport naar aanleiding van een uitgevoerde steekproef door een
    inspecteur/opzichter.
    """

    voorinspectierapport = Referentiedata(
        code="VOO",
        naam="Voorinspectierapport",
    )
    """
    Rapport naar aanleiding van een voor- of tusseninspectie
    """
