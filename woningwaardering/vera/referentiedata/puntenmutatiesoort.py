from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PuntenmutatiesoortReferentiedata(Referentiedata):
    pass


class Puntenmutatiesoort(Referentiedatasoort):
    intrekken_toewijzing = PuntenmutatiesoortReferentiedata(
        code="ITO",
        naam="Intrekken toewijzing",
    )
    """
    Intrekken toewijzing van de eenheid.
    """

    puntenafbouw_situatiepunten = PuntenmutatiesoortReferentiedata(
        code="PAS",
        naam="Puntenafbouw situatiepunten",
    )
    """
    Puntenafbouw situatiepunten
    """

    puntenafbouw_startpunten = PuntenmutatiesoortReferentiedata(
        code="PAT",
        naam="Puntenafbouw startpunten",
    )
    """
    Puntenafbouw startpunten
    """

    puntenafbouw_zoekpunten = PuntenmutatiesoortReferentiedata(
        code="PAZ",
        naam="Puntenafbouw zoekpunten",
    )
    """
    Puntenafbouw zoekpunten
    """

    puntenopbouw_situatiepunten = PuntenmutatiesoortReferentiedata(
        code="PSI",
        naam="Puntenopbouw situatiepunten",
    )
    """
    Puntenopbouw situatiepunten
    """

    puntenopbouw_startpunten = PuntenmutatiesoortReferentiedata(
        code="PST",
        naam="Puntenopbouw startpunten",
    )
    """
    Puntenopbouw startpunten
    """

    puntenopbouw_zoekpunten = PuntenmutatiesoortReferentiedata(
        code="PZO",
        naam="Puntenopbouw zoekpunten",
    )
    """
    Puntenopbouw zoekpunten
    """

    milde_sanctie = PuntenmutatiesoortReferentiedata(
        code="SMI",
        naam="Milde sanctie",
    )
    """
    Milde sanctie
    """

    no_show_sanctie = PuntenmutatiesoortReferentiedata(
        code="SNS",
        naam="No-show sanctie",
    )
    """
    No-show sanctie
    """

    zware_sanctie = PuntenmutatiesoortReferentiedata(
        code="SZW",
        naam="Zware sanctie",
    )
    """
    Zware sanctie
    """

    terugdraaien_milde_sanctie = PuntenmutatiesoortReferentiedata(
        code="TSM",
        naam="Terugdraaien milde sanctie",
    )
    """
    Terugdraaien milde sanctie
    """

    terugdraaien_no_show_sanctie = PuntenmutatiesoortReferentiedata(
        code="TSN",
        naam="Terugdraaien no-show sanctie",
    )
    """
    Terugdraaien no-show sanctie
    """

    terugdraaien_zware_sanctie = PuntenmutatiesoortReferentiedata(
        code="TSZ",
        naam="Terugdraaien zware sanctie",
    )
    """
    Terugdraaien zware sanctie
    """
