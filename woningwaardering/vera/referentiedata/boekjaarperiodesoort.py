from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BoekjaarperiodesoortReferentiedata(Referentiedata):
    pass


class Boekjaarperiodesoort(Referentiedatasoort):
    boekjaarperiodesoort_4_weken = BoekjaarperiodesoortReferentiedata(
        code="4WE",
        naam="4-weken",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 4 aaneengesloten kalenderweken.
    """

    halfjaar = BoekjaarperiodesoortReferentiedata(
        code="HLJ",
        naam="Halfjaar",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 6 aaneengesloten kalendermaanden.
    """

    jaar = BoekjaarperiodesoortReferentiedata(
        code="JAR",
        naam="Jaar",
    )
    """
    Periode die uitgaat van een kalenderjaar.
    """

    kwartaal = BoekjaarperiodesoortReferentiedata(
        code="KWA",
        naam="Kwartaal",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 3 aaneengesloten kalandermaanden.
    """

    maand = BoekjaarperiodesoortReferentiedata(
        code="MAA",
        naam="Maand",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 1 kalendermaand.
    """

    tertiaal = BoekjaarperiodesoortReferentiedata(
        code="TER",
        naam="Tertiaal",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 4 aaneengesloten kalandermaanden.
    """

    week = BoekjaarperiodesoortReferentiedata(
        code="WEE",
        naam="Week",
    )
    """
    Deel van een kalenderjaar met een vaste duur van 3 aaneengesloten kalendermaanden.
    """
