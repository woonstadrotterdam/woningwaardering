
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class VERTROUWELIJKHEID:

    geheim = Referentiedata(
        code="GEH",
        naam="Geheim",
    )
    # geheim = ("GEH", "Geheim")
    """
    Informatie is alleen toegankelijk voor direct geadresseerde(n) (bv: zorggegevens en
    strafrechtelijke informatie)
    """

    intern = Referentiedata(
        code="INT",
        naam="Intern",
    )
    # intern = ("INT", "Intern")
    """
    Informatie is toegankelijk voor alle medewerkers van de organisatie (bv: intranet)
    """

    openbaar = Referentiedata(
        code="OPE",
        naam="Openbaar",
    )
    # openbaar = ("OPE", "Openbaar")
    """
    Informatie mag door iedereen worden ingezien (bv: algemene informatie op de website)
    """

    vertrouwelijk = Referentiedata(
        code="VER",
        naam="Vertrouwelijk",
    )
    # vertrouwelijk = ("VER", "Vertrouwelijk")
    """
    Informatie is alleen toegankelijk voor een beperkte groep gebruikers (bv:
    persoonsgegevens, financiële gegevens)
    """
