from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Puntenmutatiesoort(Referentiedatasoort):
    intrekken_toewijzing = Referentiedata(
        code="ITO",
        naam="Intrekken toewijzing",
    )
    """
    Intrekken toewijzing van de eenheid.
    """

    puntenafbouw_situatiepunten = Referentiedata(
        code="PAS",
        naam="Puntenafbouw situatiepunten",
    )
    """
    Puntenafbouw situatiepunten
    """

    puntenafbouw_startpunten = Referentiedata(
        code="PAT",
        naam="Puntenafbouw startpunten",
    )
    """
    Puntenafbouw startpunten
    """

    puntenafbouw_zoekpunten = Referentiedata(
        code="PAZ",
        naam="Puntenafbouw zoekpunten",
    )
    """
    Puntenafbouw zoekpunten
    """

    puntenopbouw_situatiepunten = Referentiedata(
        code="PSI",
        naam="Puntenopbouw situatiepunten",
    )
    """
    Puntenopbouw situatiepunten
    """

    puntenopbouw_startpunten = Referentiedata(
        code="PST",
        naam="Puntenopbouw startpunten",
    )
    """
    Puntenopbouw startpunten
    """

    puntenopbouw_zoekpunten = Referentiedata(
        code="PZO",
        naam="Puntenopbouw zoekpunten",
    )
    """
    Puntenopbouw zoekpunten
    """

    milde_sanctie = Referentiedata(
        code="SMI",
        naam="Milde sanctie",
    )
    """
    Milde sanctie
    """

    no_show_sanctie = Referentiedata(
        code="SNS",
        naam="No-show sanctie",
    )
    """
    No-show sanctie
    """

    zware_sanctie = Referentiedata(
        code="SZW",
        naam="Zware sanctie",
    )
    """
    Zware sanctie
    """

    terugdraaien_milde_sanctie = Referentiedata(
        code="TSM",
        naam="Terugdraaien milde sanctie",
    )
    """
    Terugdraaien milde sanctie
    """

    terugdraaien_no_show_sanctie = Referentiedata(
        code="TSN",
        naam="Terugdraaien no-show sanctie",
    )
    """
    Terugdraaien no-show sanctie
    """

    terugdraaien_zware_sanctie = Referentiedata(
        code="TSZ",
        naam="Terugdraaien zware sanctie",
    )
    """
    Terugdraaien zware sanctie
    """
