
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PRIJSCOMPONENTWIJZIGINGSREDEN:

    jaarlijkse_huuraanpassing_inkomensafhankelijk = Referentiedata(
        code="INK",
        naam="Jaarlijkse huuraanpassing -inkomensafhankelijk",
    )
    # jaarlijkse_huuraanpassing_inkomensafhankelijk = ("INK", "Jaarlijkse huuraanpassing -inkomensafhankelijk")
    """
    Jaarlijkse huuraanpassing - met inkomensafhankelijke huurverhoging
    """

    jaarlijkse_huuraanpassing_niet_inkomensafhankelijk = Referentiedata(
        code="JAA",
        naam="Jaarlijkse huuraanpassing -niet inkomensafhankelijk",
    )
    # jaarlijkse_huuraanpassing_niet_inkomensafhankelijk = ("JAA", "Jaarlijkse huuraanpassing -niet inkomensafhankelijk")
    """
    Jaarlijkse huuraanpassing - zonder inkomensafhankelijke huurverhoging
    """

    nieuwe_verhuring = Referentiedata(
        code="MUT",
        naam="Nieuwe verhuring",
    )
    # nieuwe_verhuring = ("MUT", "Nieuwe verhuring")
    """
    Nieuwe verhuring, inclusief de eerste verhuring van een eenheid
    """

    nieuw_component = Referentiedata(
        code="NIE",
        naam="Nieuw component",
    )
    # nieuw_component = ("NIE", "Nieuw component")
    """
    Nieuw prijscomponent bij een eenheid of een overeenkomst
    """

    renovatie_of_woningverbetering = Referentiedata(
        code="REN",
        naam="Renovatie of woningverbetering",
    )
    # renovatie_of_woningverbetering = ("REN", "Renovatie of woningverbetering")
    """
    Huuraanpassing als gevolg van een renovatie of woningverbetering
    """
