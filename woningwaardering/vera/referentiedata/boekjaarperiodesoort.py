from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Boekjaarperiodesoort(Enum):
    boekjaarperiodesoort_4_weken = Referentiedata(
        code="4WE",
        naam="4-weken",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 4 aaneengesloten kalenderweken.
    """

    halfjaar = Referentiedata(
        code="HLJ",
        naam="Halfjaar",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 6 aaneengesloten kalendermaanden.
    """

    jaar = Referentiedata(
        code="JAR",
        naam="Jaar",
    )
    """
    Periode die uitgaat van een kalenderjaar.
    """

    kwartaal = Referentiedata(
        code="KWA",
        naam="Kwartaal",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 3 aaneengesloten kalandermaanden.
    """

    maand = Referentiedata(
        code="MAA",
        naam="Maand",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 1 kalendermaand.
    """

    tertiaal = Referentiedata(
        code="TER",
        naam="Tertiaal",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 4 aaneengesloten kalandermaanden.
    """

    week = Referentiedata(
        code="WEE",
        naam="Week",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 3 aaneengesloten kalendermaanden.
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
