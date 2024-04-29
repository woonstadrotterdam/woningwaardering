from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Afspraakstatus(Enum):
    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    De afspraak is nog niet gepland, maar wel aangevraagd. Daarbij kan eventueel een
    voorkeur bloktijd zijn opgegeven.
    """

    afgerond = Referentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    De afspraak heeft plaatsgevonden.
    """

    geannuleerd = Referentiedata(
        code="ANN",
        naam="Geannuleerd",
    )
    """
    De afspraak is geannuleerd.
    """

    gepland = Referentiedata(
        code="GEP",
        naam="Gepland",
    )
    """
    De afspraak is gepland. Hierbij zal doorgaans ook een medewerker zijn toegewezen.
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
