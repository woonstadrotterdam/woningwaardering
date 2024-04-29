from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Conditiescore(Enum):
    uitstekende_conditie = Referentiedata(
        code="1",
        naam="Uitstekende conditie",
    )
    """
    Incidenteel geringe gebreken. (Conditiescore 1 van NEN 2767)
    """

    goede_conditie = Referentiedata(
        code="2",
        naam="Goede conditie",
    )
    """
    Incidenteel beginnende veroudering. (Conditiescore 2 van NEN 2767)
    """

    redelijke_conditie = Referentiedata(
        code="3",
        naam="Redelijke conditie",
    )
    """
    Plaatselijk zichtbare veroudering Functievervulling van bouw- en installatiedelen
    niet in gevaar. (Conditiescore 3 van NEN 2767)
    """

    matige_conditie = Referentiedata(
        code="4",
        naam="Matige conditie",
    )
    """
    Functievervulling van bouw- en installatiedelen incidenteel in gevaar.
    (Conditiescore 4 van NEN 2767)
    """

    slechte_conditie = Referentiedata(
        code="5",
        naam="Slechte conditie",
    )
    """
    De veroudering is onomkeerbaar. (Conditiescore 5 van NEN 2767)
    """

    zeer_slechte_conditie = Referentiedata(
        code="6",
        naam="Zeer slechte conditie",
    )
    """
    Technisch rijp voor sloop. (Conditiescore 6 van NEN 2767)
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
