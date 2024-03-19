from vera.referentiedata.models import Referentiedata


class Vertrouwelijkheid:
    geheim = Referentiedata(
        code="GEH",
        naam="Geheim",
    )
    """
    Informatie is alleen toegankelijk voor direct geadresseerde(n) (bv: zorggegevens en
    strafrechtelijke informatie)
    """

    intern = Referentiedata(
        code="INT",
        naam="Intern",
    )
    """
    Informatie is toegankelijk voor alle medewerkers van de organisatie (bv: intranet)
    """

    openbaar = Referentiedata(
        code="OPE",
        naam="Openbaar",
    )
    """
    Informatie mag door iedereen worden ingezien (bv: algemene informatie op de website)
    """

    vertrouwelijk = Referentiedata(
        code="VER",
        naam="Vertrouwelijk",
    )
    """
    Informatie is alleen toegankelijk voor een beperkte groep gebruikers  (bv:
    persoonsgegevens, financiële gegevens)
    """
