
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class GEBEURTENISSOORT:

    begin_situatiepunten = Referentiedata(
        code="BSI",
        naam="Begin situatiepunten",
    )
    # begin_situatiepunten = ("BSI", "Begin situatiepunten")
    """
    Begin situatiepunten
    """

    begin_startpunten = Referentiedata(
        code="BST",
        naam="Begin startpunten",
    )
    # begin_startpunten = ("BST", "Begin startpunten")
    """
    Begin startpunten
    """

    gewijzigde_inschrijving = Referentiedata(
        code="GEW",
        naam="Gewijzigde inschrijving",
    )
    # gewijzigde_inschrijving = ("GEW", "Gewijzigde inschrijving")
    """
    Gewijzigde inschrijving
    """

    gewijzigde_startpunten = Referentiedata(
        code="GSA",
        naam="Gewijzigde startpunten",
    )
    # gewijzigde_startpunten = ("GSA", "Gewijzigde startpunten")
    """
    Gewijzigde startpunten
    """

    gewijzigde_situatiepunten = Referentiedata(
        code="GSI",
        naam="Gewijzigde situatiepunten",
    )
    # gewijzigde_situatiepunten = ("GSI", "Gewijzigde situatiepunten")
    """
    Gewijzigde situatiepunten
    """

    intrekken_no_show = Referentiedata(
        code="INS",
        naam="Intrekken no-show",
    )
    # intrekken_no_show = ("INS", "Intrekken no-show")
    """
    Intrekken gebeurtenis niet aanwezig op bevestigde bezichtiging (No-show)
    """

    intrekken_reactie = Referentiedata(
        code="IRE",
        naam="Intrekken reactie",
    )
    # intrekken_reactie = ("IRE", "Intrekken reactie")
    """
    Intrekken reactie met puntenopbouw
    """

    intrekken_toewijzing = Referentiedata(
        code="ITO",
        naam="Intrekken toewijzing",
    )
    # intrekken_toewijzing = ("ITO", "Intrekken toewijzing")
    """
    Intrekken toewijzing van de eenheid.
    """

    intrekken_weigering_als_hoogste_acceptant = Referentiedata(
        code="IWH",
        naam="Intrekken weigering als hoogste acceptant",
    )
    # intrekken_weigering_als_hoogste_acceptant = ("IWH", "Intrekken weigering als hoogste acceptant")
    """
    Intrekken weigering als hoogste acceptant
    """

    intrekken_weigering_niet_als_hoogste_acceptant = Referentiedata(
        code="IWN",
        naam="Intrekken weigering niet als hoogste acceptant",
    )
    # intrekken_weigering_niet_als_hoogste_acceptant = ("IWN", "Intrekken weigering niet als hoogste acceptant")
    """
    Intrekken weigering niet als hoogste acceptant
    """

    nieuwe_inschrijving = Referentiedata(
        code="NIE",
        naam="Nieuwe inschrijving",
    )
    # nieuwe_inschrijving = ("NIE", "Nieuwe inschrijving")
    """
    Nieuwe inschrijving
    """

    no_show = Referentiedata(
        code="NOS",
        naam="No-show",
    )
    # no_show = ("NOS", "No-show")
    """
    Niet aanwezig op bevestigde bezichtiging
    """

    reactie = Referentiedata(
        code="REA",
        naam="Reactie",
    )
    # reactie = ("REA", "Reactie")
    """
    Reactie met puntenopbouw
    """

    toewijzing = Referentiedata(
        code="TOE",
        naam="Toewijzing",
    )
    # toewijzing = ("TOE", "Toewijzing")
    """
    Toewijzing
    """

    weigering_als_hoogste_acceptant = Referentiedata(
        code="WEI",
        naam="Weigering als hoogste acceptant",
    )
    # weigering_als_hoogste_acceptant = ("WEI", "Weigering als hoogste acceptant")
    """
    Weigering als hoogste acceptant
    """

    weigering_niet_als_hoogste_acceptant = Referentiedata(
        code="WEN",
        naam="Weigering niet als hoogste acceptant",
    )
    # weigering_niet_als_hoogste_acceptant = ("WEN", "Weigering niet als hoogste acceptant")
    """
    Weigering niet als hoogste acceptant
    """
