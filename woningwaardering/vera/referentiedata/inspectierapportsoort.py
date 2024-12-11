from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InspectierapportsoortReferentiedata(Referentiedata):
    pass


class Inspectierapportsoort(Referentiedatasoort):
    eindinspectierapport = InspectierapportsoortReferentiedata(
        code="EIN",
        naam="Eindinspectierapport",
    )
    """
    Rapport naar aanleiding van een eindinspectie
    """

    reparatieinspectierapport = InspectierapportsoortReferentiedata(
        code="REP",
        naam="Reparatieinspectierapport",
    )
    """
    Inspectierapport naar aanleiding van een onduidelijk reparatieverzoek
    """

    steekproefinspectierapport = InspectierapportsoortReferentiedata(
        code="STE",
        naam="Steekproefinspectierapport",
    )
    """
    Inspectierapport naar aanleiding van een uitgevoerde steekproef door een
    inspecteur/opzichter.
    """

    voorinspectierapport = InspectierapportsoortReferentiedata(
        code="VOO",
        naam="Voorinspectierapport",
    )
    """
    Rapport naar aanleiding van een voor- of tusseninspectie
    """
