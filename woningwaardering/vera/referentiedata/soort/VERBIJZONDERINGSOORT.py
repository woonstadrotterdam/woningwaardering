
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class VERBIJZONDERINGSOORT:

    cluster = Referentiedata(
        code="CLS",
        naam="Cluster",
    )
    # cluster = ("CLS", "Cluster")
    """
    Optionele verwijzing naar een cluster om een financieel feit nader te kunnen
    verbijzonderen
    """

    soort_huurdebiteur = Referentiedata(
        code="DEB",
        naam="Soort huurdebiteur",
    )
    # soort_huurdebiteur = ("DEB", "Soort huurdebiteur")
    """
    Optionele verwijzing naar een huurdebiteursoort om een financieel feit nader te
    kunnen verbijzonderen
    """

    dimensie = Referentiedata(
        code="DIM",
        naam="Dimensie",
    )
    # dimensie = ("DIM", "Dimensie")
    """
    Optionele verwijzing naar een (overige) dimensiewaarde om een financieel feit nader
    te kunnen verbijzonderen. Gebruik eventueel verbijzonderingdetailsoort om de
    dimensie nader te duiden (dimensiesoort)
    """

    divisie = Referentiedata(
        code="DIV",
        naam="Divisie",
    )
    # divisie = ("DIV", "Divisie")
    """
    Optionele verwijzing naar een divisie om een financieel feit nader te kunnen
    verbijzonderen.
    """

    kostenplaats = Referentiedata(
        code="KPL",
        naam="Kostenplaats",
    )
    # kostenplaats = ("KPL", "Kostenplaats")
    """
    Optionele verwijzing naar een kostenplaats om een financieel feit nader te kunnen
    verbijzonderen. Vaak is een kostenplaats een afdeling
    """

    kostensoort = Referentiedata(
        code="KST",
        naam="Kostensoort",
    )
    # kostensoort = ("KST", "Kostensoort")
    """
    Optionele verwijzing naar een kostensoort om een financieel feit nader te kunnen
    verbijzonderen
    """

    soort_leverancier = Referentiedata(
        code="LEV",
        naam="Soort leverancier",
    )
    # soort_leverancier = ("LEV", "Soort leverancier")
    """
    Optionele verwijzing naar een leveranciersoort om een financieel feit nader te
    kunnen verbijzonderen
    """

    maatschappelijk_label = Referentiedata(
        code="MAA",
        naam="Maatschappelijk label",
    )
    # maatschappelijk_label = ("MAA", "Maatschappelijk label")
    """
    Optionele verwijzing naar een maatschappelijk label, of administratief eigenaar
    (DAEB/niet-DAEB) om een financieel feit nader te kunnen te kunnen verbijzonderen
    """

    medewerker = Referentiedata(
        code="MED",
        naam="Medewerker",
    )
    # medewerker = ("MED", "Medewerker")
    """
    Optionele verwijzing naar een medewerker om een financieel feit nader te kunnen
    verbijzonderen
    """

    project = Referentiedata(
        code="PRO",
        naam="Project",
    )
    # project = ("PRO", "Project")
    """
    Optionele verwijzing naar een project om een financieel feit nader te kunnen
    verbijzonderen
    """

    vastgoedeenheid = Referentiedata(
        code="VGE",
        naam="Vastgoedeenheid",
    )
    # vastgoedeenheid = ("VGE", "Vastgoedeenheid")
    """
    Optionele verwijzing naar een vastgoedeenheid om een financieel feit nader te kunnen
    verbijzonderen
    """
