
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class CONDITIESCORE:

    uitstekende_conditie = Referentiedata(
        code="1",
        naam="Uitstekende conditie",
    )
    # uitstekende_conditie = ("1", "Uitstekende conditie")
    """
    Incidenteel geringe gebreken. (Conditiescore 1 van NEN 2767)
    """

    goede_conditie = Referentiedata(
        code="2",
        naam="Goede conditie",
    )
    # goede_conditie = ("2", "Goede conditie")
    """
    Incidenteel beginnende veroudering. (Conditiescore 2 van NEN 2767)
    """

    redelijke_conditie = Referentiedata(
        code="3",
        naam="Redelijke conditie",
    )
    # redelijke_conditie = ("3", "Redelijke conditie")
    """
    Plaatselijk zichtbare veroudering Functievervulling van bouw- en installatiedelen
    niet in gevaar. (Conditiescore 3 van NEN 2767)
    """

    matige_conditie = Referentiedata(
        code="4",
        naam="Matige conditie",
    )
    # matige_conditie = ("4", "Matige conditie")
    """
    Functievervulling van bouw- en installatiedelen incidenteel in gevaar.
    (Conditiescore 4 van NEN 2767)
    """

    slechte_conditie = Referentiedata(
        code="5",
        naam="Slechte conditie",
    )
    # slechte_conditie = ("5", "Slechte conditie")
    """
    De veroudering is onomkeerbaar. (Conditiescore 5 van NEN 2767)
    """

    zeer_slechte_conditie = Referentiedata(
        code="6",
        naam="Zeer slechte conditie",
    )
    # zeer_slechte_conditie = ("6", "Zeer slechte conditie")
    """
    Technisch rijp voor sloop. (Conditiescore 6 van NEN 2767)
    """
