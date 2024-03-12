
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PUNTENMUTATIESOORT:

    intrekken_toewijzing = Referentiedata(
        code="ITO",
        naam="Intrekken toewijzing",
    )
    # intrekken_toewijzing = ("ITO", "Intrekken toewijzing")
    """
    Intrekken toewijzing van de eenheid.
    """

    puntenafbouw_situatiepunten = Referentiedata(
        code="PAS",
        naam="Puntenafbouw situatiepunten",
    )
    # puntenafbouw_situatiepunten = ("PAS", "Puntenafbouw situatiepunten")
    """
    Puntenafbouw situatiepunten
    """

    puntenafbouw_startpunten = Referentiedata(
        code="PAT",
        naam="Puntenafbouw startpunten",
    )
    # puntenafbouw_startpunten = ("PAT", "Puntenafbouw startpunten")
    """
    Puntenafbouw startpunten
    """

    puntenafbouw_zoekpunten = Referentiedata(
        code="PAZ",
        naam="Puntenafbouw zoekpunten",
    )
    # puntenafbouw_zoekpunten = ("PAZ", "Puntenafbouw zoekpunten")
    """
    Puntenafbouw zoekpunten
    """

    puntenopbouw_situatiepunten = Referentiedata(
        code="PSI",
        naam="Puntenopbouw situatiepunten",
    )
    # puntenopbouw_situatiepunten = ("PSI", "Puntenopbouw situatiepunten")
    """
    Puntenopbouw situatiepunten
    """

    puntenopbouw_startpunten = Referentiedata(
        code="PST",
        naam="Puntenopbouw startpunten",
    )
    # puntenopbouw_startpunten = ("PST", "Puntenopbouw startpunten")
    """
    Puntenopbouw startpunten
    """

    puntenopbouw_zoekpunten = Referentiedata(
        code="PZO",
        naam="Puntenopbouw zoekpunten",
    )
    # puntenopbouw_zoekpunten = ("PZO", "Puntenopbouw zoekpunten")
    """
    Puntenopbouw zoekpunten
    """

    milde_sanctie = Referentiedata(
        code="SMI",
        naam="Milde sanctie",
    )
    # milde_sanctie = ("SMI", "Milde sanctie")
    """
    Milde sanctie
    """

    no_show_sanctie = Referentiedata(
        code="SNS",
        naam="No-show sanctie",
    )
    # no_show_sanctie = ("SNS", "No-show sanctie")
    """
    No-show sanctie
    """

    zware_sanctie = Referentiedata(
        code="SZW",
        naam="Zware sanctie",
    )
    # zware_sanctie = ("SZW", "Zware sanctie")
    """
    Zware sanctie
    """

    terugdraaien_milde_sanctie = Referentiedata(
        code="TSM",
        naam="Terugdraaien milde sanctie",
    )
    # terugdraaien_milde_sanctie = ("TSM", "Terugdraaien milde sanctie")
    """
    Terugdraaien milde sanctie
    """

    terugdraaien_no_show_sanctie = Referentiedata(
        code="TSN",
        naam="Terugdraaien no-show sanctie",
    )
    # terugdraaien_no_show_sanctie = ("TSN", "Terugdraaien no-show sanctie")
    """
    Terugdraaien no-show sanctie
    """

    terugdraaien_zware_sanctie = Referentiedata(
        code="TSZ",
        naam="Terugdraaien zware sanctie",
    )
    # terugdraaien_zware_sanctie = ("TSZ", "Terugdraaien zware sanctie")
    """
    Terugdraaien zware sanctie
    """
