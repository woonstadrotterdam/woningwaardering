from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Gebeurtenissoort(Enum):
    begin_situatiepunten = Referentiedata(
        code="BSI",
        naam="Begin situatiepunten",
    )
    """
    Begin situatiepunten
    """

    begin_startpunten = Referentiedata(
        code="BST",
        naam="Begin startpunten",
    )
    """
    Begin startpunten
    """

    gewijzigde_inschrijving = Referentiedata(
        code="GEW",
        naam="Gewijzigde inschrijving",
    )
    """
    Gewijzigde inschrijving
    """

    gewijzigde_startpunten = Referentiedata(
        code="GSA",
        naam="Gewijzigde startpunten",
    )
    """
    Gewijzigde startpunten
    """

    gewijzigde_situatiepunten = Referentiedata(
        code="GSI",
        naam="Gewijzigde situatiepunten",
    )
    """
    Gewijzigde situatiepunten
    """

    intrekken_no_show = Referentiedata(
        code="INS",
        naam="Intrekken no-show",
    )
    """
    Intrekken gebeurtenis niet aanwezig op bevestigde bezichtiging (No-show)
    """

    intrekken_reactie = Referentiedata(
        code="IRE",
        naam="Intrekken reactie",
    )
    """
    Intrekken reactie met puntenopbouw
    """

    intrekken_toewijzing = Referentiedata(
        code="ITO",
        naam="Intrekken toewijzing",
    )
    """
    Intrekken toewijzing van de eenheid.
    """

    intrekken_weigering_als_hoogste_acceptant = Referentiedata(
        code="IWH",
        naam="Intrekken weigering als hoogste acceptant",
    )
    """
    Intrekken weigering als hoogste acceptant
    """

    intrekken_weigering_niet_als_hoogste_acceptant = Referentiedata(
        code="IWN",
        naam="Intrekken weigering niet als hoogste acceptant",
    )
    """
    Intrekken weigering niet als hoogste acceptant
    """

    nieuwe_inschrijving = Referentiedata(
        code="NIE",
        naam="Nieuwe inschrijving",
    )
    """
    Nieuwe inschrijving
    """

    no_show = Referentiedata(
        code="NOS",
        naam="No-show",
    )
    """
    Niet aanwezig op bevestigde bezichtiging
    """

    reactie = Referentiedata(
        code="REA",
        naam="Reactie",
    )
    """
    Reactie met puntenopbouw
    """

    toewijzing = Referentiedata(
        code="TOE",
        naam="Toewijzing",
    )
    """
    Toewijzing
    """

    weigering_als_hoogste_acceptant = Referentiedata(
        code="WEI",
        naam="Weigering als hoogste acceptant",
    )
    """
    Weigering als hoogste acceptant
    """

    weigering_niet_als_hoogste_acceptant = Referentiedata(
        code="WEN",
        naam="Weigering niet als hoogste acceptant",
    )
    """
    Weigering niet als hoogste acceptant
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
