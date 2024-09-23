from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Prijscomponentwijzigingsreden(Enum):
    jaarlijkse_huuraanpassing_inkomensafhankelijk = Referentiedata(
        code="INK",
        naam="Jaarlijkse huuraanpassing -inkomensafhankelijk",
    )
    """
    Jaarlijkse huuraanpassing - met inkomensafhankelijke huurverhoging
    """

    jaarlijkse_huuraanpassing_niet_inkomensafhankelijk = Referentiedata(
        code="JAA",
        naam="Jaarlijkse huuraanpassing -niet inkomensafhankelijk",
    )
    """
    Jaarlijkse huuraanpassing - zonder inkomensafhankelijke huurverhoging
    """

    nieuwe_verhuring = Referentiedata(
        code="MUT",
        naam="Nieuwe verhuring",
    )
    """
    Nieuwe verhuring, inclusief de eerste verhuring van een eenheid
    """

    nieuw_component = Referentiedata(
        code="NIE",
        naam="Nieuw component",
    )
    """
    Nieuw prijscomponent bij een eenheid of een overeenkomst
    """

    renovatie_of_woningverbetering = Referentiedata(
        code="REN",
        naam="Renovatie of woningverbetering",
    )
    """
    Huuraanpassing als gevolg van een renovatie of woningverbetering
    """

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
