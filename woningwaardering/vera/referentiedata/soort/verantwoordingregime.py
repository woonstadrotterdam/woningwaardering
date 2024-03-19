from vera.referentiedata.models import Referentiedata


class Verantwoordingregime:
    administratieve_scheiding = Referentiedata(
        code="ADM",
        naam="Administratieve scheiding",
    )
    """
    De DAEB- en niet-DAEB activiteiten van de coporatie worden administratief van elkaar
    gescheiden
    """

    hybride = Referentiedata(
        code="HYB",
        naam="Hybride",
    )
    """
    Een scheiding is hybride indien er bezit wordt overgeheveld van de TI naar een
    dochtervennootschap, terwijl ook niet-DAEB bezit achterblijft in de TI.
    """

    juridische_scheiding = Referentiedata(
        code="JUR",
        naam="Juridische scheiding",
    )
    """
    De DAEB- en niet-DAEB activiteiten van de corporatie zijn in aparte juridische
    entiteiten ondergebracht, elk met een eigen financiële administratie
    """

    verlicht_regime = Referentiedata(
        code="VER",
        naam="Verlicht regime",
    )
    """
    De corporatie voldoet aan de voorwaarden waaronder geen gescheiden administraties
    voor DAEB- en niet-DAEB activiteiten gevoerd hoeven te worden.
    """
