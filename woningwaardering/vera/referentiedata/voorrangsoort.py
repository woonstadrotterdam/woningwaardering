from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class VoorrangsoortReferentiedata(Referentiedata):
    pass


class Voorrangsoort(Referentiedatasoort):
    binding = VoorrangsoortReferentiedata(
        code="BIN",
        naam="Binding",
    )
    """
    Er is voorrang voor woningzoekenden met binding tot een bepaald gebied. Bijvoorbeeld
    regionaal voor mensen die in het regionaal samenwerkingsverband wonen en/of
    werken, lokaal voor mensen die in de gemeente wonen.
    """

    groep = VoorrangsoortReferentiedata(
        code="GRO",
        naam="Groep",
    )
    """
    Er is voorrang voor woningzoekenden die tot een bepaalde groep behoren waar geen
    binding, urgentie of indicatie van toepassing is.
    """

    indicatie = VoorrangsoortReferentiedata(
        code="IND",
        naam="Indicatie",
    )
    """
    Er is voorrang voor woningzoekenden met een (medische) indicatie.
    """

    urgentie = VoorrangsoortReferentiedata(
        code="URG",
        naam="Urgentie",
    )
    """
    Er is voorrang voor woningzoekenden met een urgentie.
    """
