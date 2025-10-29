from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class GebeurtenissoortReferentiedata(Referentiedata):
    pass


class Gebeurtenissoort(Referentiedatasoort):
    begin_situatiepunten = GebeurtenissoortReferentiedata(
        code="BSI",
        naam="Begin situatiepunten",
    )
    """
    Begin situatiepunten
    """

    begin_startpunten = GebeurtenissoortReferentiedata(
        code="BST",
        naam="Begin startpunten",
    )
    """
    Begin startpunten
    """

    gewijzigde_inschrijving = GebeurtenissoortReferentiedata(
        code="GEW",
        naam="Gewijzigde inschrijving",
    )
    """
    Gewijzigde inschrijving
    """

    gewijzigde_startpunten = GebeurtenissoortReferentiedata(
        code="GSA",
        naam="Gewijzigde startpunten",
    )
    """
    Gewijzigde startpunten
    """

    gewijzigde_situatiepunten = GebeurtenissoortReferentiedata(
        code="GSI",
        naam="Gewijzigde situatiepunten",
    )
    """
    Gewijzigde situatiepunten
    """

    intrekken_no_show = GebeurtenissoortReferentiedata(
        code="INS",
        naam="Intrekken no-show",
    )
    """
    Intrekken gebeurtenis niet aanwezig op bevestigde bezichtiging (No-show)
    """

    intrekken_reactie = GebeurtenissoortReferentiedata(
        code="IRE",
        naam="Intrekken reactie",
    )
    """
    Intrekken reactie met puntenopbouw
    """

    intrekken_toewijzing = GebeurtenissoortReferentiedata(
        code="ITO",
        naam="Intrekken toewijzing",
    )
    """
    Intrekken toewijzing van de eenheid.
    """

    intrekken_weigering_als_hoogste_acceptant = GebeurtenissoortReferentiedata(
        code="IWH",
        naam="Intrekken weigering als hoogste acceptant",
    )
    """
    Intrekken weigering als hoogste acceptant
    """

    intrekken_weigering_niet_als_hoogste_acceptant = GebeurtenissoortReferentiedata(
        code="IWN",
        naam="Intrekken weigering niet als hoogste acceptant",
    )
    """
    Intrekken weigering niet als hoogste acceptant
    """

    nieuwe_inschrijving = GebeurtenissoortReferentiedata(
        code="NIE",
        naam="Nieuwe inschrijving",
    )
    """
    Nieuwe inschrijving
    """

    no_show = GebeurtenissoortReferentiedata(
        code="NOS",
        naam="No-show",
    )
    """
    Niet aanwezig op bevestigde bezichtiging
    """

    reactie = GebeurtenissoortReferentiedata(
        code="REA",
        naam="Reactie",
    )
    """
    Reactie met puntenopbouw
    """

    toewijzing = GebeurtenissoortReferentiedata(
        code="TOE",
        naam="Toewijzing",
    )
    """
    Toewijzing
    """

    weigering_als_hoogste_acceptant = GebeurtenissoortReferentiedata(
        code="WEI",
        naam="Weigering als hoogste acceptant",
    )
    """
    Weigering als hoogste acceptant
    """

    weigering_niet_als_hoogste_acceptant = GebeurtenissoortReferentiedata(
        code="WEN",
        naam="Weigering niet als hoogste acceptant",
    )
    """
    Weigering niet als hoogste acceptant
    """
