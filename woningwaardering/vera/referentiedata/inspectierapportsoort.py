from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Inspectierapportsoort(Enum):
    eindinspectierapport = Referentiedata(
        code="EIN",
        naam="Eindinspectierapport",
    )
    """
    Rapport naar aanleiding van een eindinspectie
    """

    reparatieinspectierapport = Referentiedata(
        code="REP",
        naam="Reparatieinspectierapport",
    )
    """
    Inspectierapport naar aanleiding van een onduidelijk reparatieverzoek
    """

    steekproefinspectierapport = Referentiedata(
        code="STE",
        naam="Steekproefinspectierapport",
    )
    """
    Inspectierapport naar aanleiding van een uitgevoerde steekproef door een
    inspecteur/opzichter.
    """

    voorinspectierapport = Referentiedata(
        code="VOO",
        naam="Voorinspectierapport",
    )
    """
    Rapport naar aanleiding van een voor- of tusseninspectie
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
