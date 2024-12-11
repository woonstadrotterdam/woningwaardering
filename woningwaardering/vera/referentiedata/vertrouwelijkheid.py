from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class VertrouwelijkheidReferentiedata(Referentiedata):
    pass


class Vertrouwelijkheid(Referentiedatasoort):
    geheim = VertrouwelijkheidReferentiedata(
        code="GEH",
        naam="Geheim",
    )
    """
    Informatie is alleen toegankelijk voor direct geadresseerde(n) (bv: zorggegevens en
    strafrechtelijke informatie)
    """

    intern = VertrouwelijkheidReferentiedata(
        code="INT",
        naam="Intern",
    )
    """
    Informatie is toegankelijk voor alle medewerkers van de organisatie (bv: intranet)
    """

    openbaar = VertrouwelijkheidReferentiedata(
        code="OPE",
        naam="Openbaar",
    )
    """
    Informatie mag door iedereen worden ingezien (bv: algemene informatie op de website)
    """

    vertrouwelijk = VertrouwelijkheidReferentiedata(
        code="VER",
        naam="Vertrouwelijk",
    )
    """
    Informatie is alleen toegankelijk voor een beperkte groep gebruikers  (bv:
    persoonsgegevens, financiële gegevens)
    """
