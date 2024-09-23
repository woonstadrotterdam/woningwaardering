from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Verbijzonderingsoort(Enum):
    cluster = Referentiedata(
        code="CLS",
        naam="Cluster",
    )
    """
    Optionele verwijzing naar een cluster om een financieel feit nader te kunnen
    verbijzonderen
    """

    soort_huurdebiteur = Referentiedata(
        code="DEB",
        naam="Soort huurdebiteur",
    )
    """
    Optionele verwijzing naar een huurdebiteursoort om een financieel feit nader te
    kunnen verbijzonderen
    """

    dimensie = Referentiedata(
        code="DIM",
        naam="Dimensie",
    )
    """
    Optionele verwijzing naar een (overige) dimensiewaarde om een financieel feit nader
    te kunnen verbijzonderen. Gebruik eventueel verbijzonderingdetailsoort om de
    dimensie nader te duiden (dimensiesoort)
    """

    divisie = Referentiedata(
        code="DIV",
        naam="Divisie",
    )
    """
    Optionele verwijzing naar een divisie om een financieel feit nader te kunnen
    verbijzonderen.
    """

    kostenplaats = Referentiedata(
        code="KPL",
        naam="Kostenplaats",
    )
    """
    Optionele verwijzing naar een kostenplaats om een financieel feit nader te kunnen
    verbijzonderen. Vaak is een kostenplaats een afdeling
    """

    kostensoort = Referentiedata(
        code="KST",
        naam="Kostensoort",
    )
    """
    Optionele verwijzing naar een kostensoort om een financieel feit nader te kunnen
    verbijzonderen
    """

    soort_leverancier = Referentiedata(
        code="LEV",
        naam="Soort leverancier",
    )
    """
    Optionele verwijzing naar een leveranciersoort om een financieel feit nader te
    kunnen verbijzonderen
    """

    maatschappelijk_label = Referentiedata(
        code="MAA",
        naam="Maatschappelijk label",
    )
    """
    Optionele verwijzing naar een maatschappelijk label, of administratief eigenaar
    (DAEB/niet-DAEB) om een financieel feit nader te kunnen te kunnen verbijzonderen
    """

    medewerker = Referentiedata(
        code="MED",
        naam="Medewerker",
    )
    """
    Optionele verwijzing naar een medewerker om een financieel feit nader te kunnen
    verbijzonderen
    """

    project = Referentiedata(
        code="PRO",
        naam="Project",
    )
    """
    Optionele verwijzing naar een project om een financieel feit nader te kunnen
    verbijzonderen
    """

    vastgoedeenheid = Referentiedata(
        code="VGE",
        naam="Vastgoedeenheid",
    )
    """
    Optionele verwijzing naar een vastgoedeenheid om een financieel feit nader te kunnen
    verbijzonderen
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
