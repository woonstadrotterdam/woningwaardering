from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class VerantwoordingregimeReferentiedata(Referentiedata):
    pass


class Verantwoordingregime(Referentiedatasoort):
    administratieve_scheiding = VerantwoordingregimeReferentiedata(
        code="ADM",
        naam="Administratieve scheiding",
    )
    """
    De DAEB- en niet-DAEB activiteiten van de coporatie worden administratief van elkaar
    gescheiden
    """

    hybride = VerantwoordingregimeReferentiedata(
        code="HYB",
        naam="Hybride",
    )
    """
    Een scheiding is hybride indien er bezit wordt overgeheveld van de TI naar een
    dochtervennootschap, terwijl ook niet-DAEB bezit achterblijft in de TI.
    """

    juridische_scheiding = VerantwoordingregimeReferentiedata(
        code="JUR",
        naam="Juridische scheiding",
    )
    """
    De DAEB- en niet-DAEB activiteiten van de corporatie zijn in aparte juridische
    entiteiten ondergebracht, elk met een eigen financiële administratie
    """

    verlicht_regime = VerantwoordingregimeReferentiedata(
        code="VER",
        naam="Verlicht regime",
    )
    """
    De corporatie voldoet aan de voorwaarden waaronder geen gescheiden administraties
    voor DAEB- en niet-DAEB activiteiten gevoerd hoeven te worden.
    """
