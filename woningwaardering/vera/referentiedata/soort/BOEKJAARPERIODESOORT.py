
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BOEKJAARPERIODESOORT:

    boekjaarperiodesoort_4_weken = Referentiedata(
        code="4WE",
        naam="4-weken",
    )
    # boekjaarperiodesoort_4_weken = ("4WE", "4-weken")
    """
    Deel van een kalenderjaar met een vaste duur van 4 aaneengesloten kalenderweken.
    """

    halfjaar = Referentiedata(
        code="HLJ",
        naam="Halfjaar",
    )
    # halfjaar = ("HLJ", "Halfjaar")
    """
    Deel van een kalenderjaar met een vaste duur van 6 aaneengesloten kalendermaanden.
    """

    jaar = Referentiedata(
        code="JAR",
        naam="Jaar",
    )
    # jaar = ("JAR", "Jaar")
    """
    Periode die uitgaat van een kalenderjaar.
    """

    kwartaal = Referentiedata(
        code="KWA",
        naam="Kwartaal",
    )
    # kwartaal = ("KWA", "Kwartaal")
    """
    Deel van een kalenderjaar met een vaste duur van 3 aaneengesloten kalandermaanden.
    """

    maand = Referentiedata(
        code="MAA",
        naam="Maand",
    )
    # maand = ("MAA", "Maand")
    """
    Deel van een kalenderjaar met een vaste duur van 1 kalendermaand.
    """

    tertiaal = Referentiedata(
        code="TER",
        naam="Tertiaal",
    )
    # tertiaal = ("TER", "Tertiaal")
    """
    Deel van een kalenderjaar met een vaste duur van 4 aaneengesloten kalandermaanden.
    """

    week = Referentiedata(
        code="WEE",
        naam="Week",
    )
    # week = ("WEE", "Week")
    """
    Deel van een kalenderjaar met een vaste duur van 3 aaneengesloten kalendermaanden.
    """
