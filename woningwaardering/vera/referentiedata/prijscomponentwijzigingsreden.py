from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PrijscomponentwijzigingsredenReferentiedata(Referentiedata):
    pass


class Prijscomponentwijzigingsreden(Referentiedatasoort):
    jaarlijkse_huuraanpassing_inkomensafhankelijk = (
        PrijscomponentwijzigingsredenReferentiedata(
            code="INK",
            naam="Jaarlijkse huuraanpassing -inkomensafhankelijk",
        )
    )
    """
    Jaarlijkse huuraanpassing - met inkomensafhankelijke huurverhoging
    """

    jaarlijkse_huuraanpassing_niet_inkomensafhankelijk = (
        PrijscomponentwijzigingsredenReferentiedata(
            code="JAA",
            naam="Jaarlijkse huuraanpassing -niet inkomensafhankelijk",
        )
    )
    """
    Jaarlijkse huuraanpassing - zonder inkomensafhankelijke huurverhoging
    """

    nieuwe_verhuring = PrijscomponentwijzigingsredenReferentiedata(
        code="MUT",
        naam="Nieuwe verhuring",
    )
    """
    Nieuwe verhuring, inclusief de eerste verhuring van een eenheid
    """

    nieuw_component = PrijscomponentwijzigingsredenReferentiedata(
        code="NIE",
        naam="Nieuw component",
    )
    """
    Nieuw prijscomponent bij een eenheid of een overeenkomst
    """

    renovatie_of_woningverbetering = PrijscomponentwijzigingsredenReferentiedata(
        code="REN",
        naam="Renovatie of woningverbetering",
    )
    """
    Huuraanpassing als gevolg van een renovatie of woningverbetering
    """
