from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidcriteriumsoortReferentiedata(Referentiedata):
    pass


class Eenheidcriteriumsoort(Referentiedatasoort):
    binding = EenheidcriteriumsoortReferentiedata(
        code="BIN",
        naam="Binding",
    )
    """
    Er is voorrang voor woningzoekenden met binding tot een bepaald gebied. Bijvoorbeeld
    regionaal voor mensen die in het regionaal samenwerkingsverband wonen en/of
    werken, lokaal voor mensen die in de gemeente wonen.
    """

    groep = EenheidcriteriumsoortReferentiedata(
        code="GRO",
        naam="Groep",
    )
    """
    Er is voorrang voor woningzoekenden die tot een bepaalde groep behoren waar geen
    binding, urgentie of indicatie van toepassing is.
    """

    indicatie = EenheidcriteriumsoortReferentiedata(
        code="IND",
        naam="Indicatie",
    )
    """
    Er is voorrang voor woningzoekenden met een (medische) indicatie.21-04-2023
    """

    urgentie = EenheidcriteriumsoortReferentiedata(
        code="URG",
        naam="Urgentie",
    )
    """
    Er is voorrang voor woningzoekenden met een urgentie.21-04-2023
    """
