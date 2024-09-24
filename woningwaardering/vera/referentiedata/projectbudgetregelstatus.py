from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Projectbudgetregelstatus(Enum):
    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    Projectbudgetregel betreft aangevraagd, maar nog niet goedgekeurd budget of
    prognosebedrag
    """

    bijgesteld = Referentiedata(
        code="BIJ",
        naam="Bijgesteld",
    )
    """
    Projectbudgetregel betreft bijgesteld, maar nog niet aangevraagd budget of
    prognosebedrag
    """

    goedgekeurd = Referentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    """
    Projectbudgetregel betreft goedgekeurd, maar nog niet vrijgegeven budget of
    prognosebedrag
    """

    vrijgegeven = Referentiedata(
        code="VRI",
        naam="Vrijgegeven",
    )
    """
    Projectbudgetregel betreft vrijgegeven budget
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
