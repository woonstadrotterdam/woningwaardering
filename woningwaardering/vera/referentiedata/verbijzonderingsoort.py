from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class VerbijzonderingsoortReferentiedata(Referentiedata):
    pass


class Verbijzonderingsoort(Referentiedatasoort):
    cluster = VerbijzonderingsoortReferentiedata(
        code="CLS",
        naam="Cluster",
    )
    """
    Optionele verwijzing naar een cluster om een financieel feit nader te kunnen
    verbijzonderen
    """

    soort_huurdebiteur = VerbijzonderingsoortReferentiedata(
        code="DEB",
        naam="Soort huurdebiteur",
    )
    """
    Optionele verwijzing naar een huurdebiteursoort om een financieel feit nader te
    kunnen verbijzonderen
    """

    dimensie = VerbijzonderingsoortReferentiedata(
        code="DIM",
        naam="Dimensie",
    )
    """
    Optionele verwijzing naar een (overige) dimensiewaarde om een financieel feit nader
    te kunnen verbijzonderen. Gebruik eventueel verbijzonderingdetailsoort om de
    dimensie nader te duiden (dimensiesoort)
    """

    divisie = VerbijzonderingsoortReferentiedata(
        code="DIV",
        naam="Divisie",
    )
    """
    Optionele verwijzing naar een divisie om een financieel feit nader te kunnen
    verbijzonderen.
    """

    kostenplaats = VerbijzonderingsoortReferentiedata(
        code="KPL",
        naam="Kostenplaats",
    )
    """
    Optionele verwijzing naar een kostenplaats om een financieel feit nader te kunnen
    verbijzonderen. Vaak is een kostenplaats een afdeling
    """

    kostensoort = VerbijzonderingsoortReferentiedata(
        code="KST",
        naam="Kostensoort",
    )
    """
    Optionele verwijzing naar een kostensoort om een financieel feit nader te kunnen
    verbijzonderen
    """

    soort_leverancier = VerbijzonderingsoortReferentiedata(
        code="LEV",
        naam="Soort leverancier",
    )
    """
    Optionele verwijzing naar een leveranciersoort om een financieel feit nader te
    kunnen verbijzonderen
    """

    maatschappelijk_label = VerbijzonderingsoortReferentiedata(
        code="MAA",
        naam="Maatschappelijk label",
    )
    """
    Optionele verwijzing naar een maatschappelijk label, of administratief eigenaar
    (DAEB/niet-DAEB) om een financieel feit nader te kunnen te kunnen verbijzonderen
    """

    medewerker = VerbijzonderingsoortReferentiedata(
        code="MED",
        naam="Medewerker",
    )
    """
    Optionele verwijzing naar een medewerker om een financieel feit nader te kunnen
    verbijzonderen
    """

    project = VerbijzonderingsoortReferentiedata(
        code="PRO",
        naam="Project",
    )
    """
    Optionele verwijzing naar een project om een financieel feit nader te kunnen
    verbijzonderen
    """

    vastgoedeenheid = VerbijzonderingsoortReferentiedata(
        code="VGE",
        naam="Vastgoedeenheid",
    )
    """
    Optionele verwijzing naar een vastgoedeenheid om een financieel feit nader te kunnen
    verbijzonderen
    """
