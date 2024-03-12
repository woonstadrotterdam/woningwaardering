
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class VOORRANGSOORT:

    binding = Referentiedata(
        code="BIN",
        naam="Binding",
    )
    # binding = ("BIN", "Binding")
    """
    Er is voorrang voor woningzoekenden met binding tot een bepaald gebied. Bijvoorbeeld
    regionaal voor mensen die in het regionaal samenwerkingsverband wonen en/of werken,
    lokaal voor mensen die in de gemeente wonen.
    """

    groep = Referentiedata(
        code="GRO",
        naam="Groep",
    )
    # groep = ("GRO", "Groep")
    """
    Er is voorrang voor woningzoekenden die tot een bepaalde groep behoren waar geen
    binding, urgentie of indicatie van toepassing is.
    """

    indicatie = Referentiedata(
        code="IND",
        naam="Indicatie",
    )
    # indicatie = ("IND", "Indicatie")
    """
    Er is voorrang voor woningzoekenden met een (medische) indicatie.
    """

    urgentie = Referentiedata(
        code="URG",
        naam="Urgentie",
    )
    # urgentie = ("URG", "Urgentie")
    """
    Er is voorrang voor woningzoekenden met een urgentie.
    """
