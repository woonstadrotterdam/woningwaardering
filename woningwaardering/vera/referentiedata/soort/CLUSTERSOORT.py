
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class CLUSTERSOORT:

    buurt = Referentiedata(
        code="BUU",
        naam="Buurt",
    )
    # buurt = ("BUU", "Buurt")
    """
    Cluster van eenheden die samen een buurt vormen, anders dan de officiële CBS-buurt
    """

    financieel = Referentiedata(
        code="FIN",
        naam="Financieel",
    )
    # financieel = ("FIN", "Financieel")

    markt = Referentiedata(
        code="MAR",
        naam="Markt",
    )
    # markt = ("MAR", "Markt")

    onderhoud = Referentiedata(
        code="OND",
        naam="Onderhoud",
    )
    # onderhoud = ("OND", "Onderhoud")

    project = Referentiedata(
        code="PRO",
        naam="Project",
    )
    # project = ("PRO", "Project")

    rayon = Referentiedata(
        code="RAY",
        naam="Rayon",
    )
    # rayon = ("RAY", "Rayon")
    """
    Cluster van eenheden die samen een niet-officieel geografisch gebied, of
    organisatorische eenheid, vormen
    """

    servicekosten = Referentiedata(
        code="SER",
        naam="Servicekosten",
    )
    # servicekosten = ("SER", "Servicekosten")
    """
    Cluster van eenheden t.b.v. afrekening servicekosten
    """

    verbruikskosten = Referentiedata(
        code="STO",
        naam="Verbruikskosten",
    )
    # verbruikskosten = ("STO", "Verbruikskosten")
    """
    Cluster van eenheden t.b.v. afrekening verbruik van water, elektriciteit, gas,
    warmte.
    """

    strategisch = Referentiedata(
        code="STR",
        naam="Strategisch",
    )
    # strategisch = ("STR", "Strategisch")

    vereniging_van_eigenaars = Referentiedata(
        code="VVE",
        naam="Vereniging van Eigenaars",
    )
    # vereniging_van_eigenaars = ("VVE", "Vereniging van Eigenaars")

    wijk = Referentiedata(
        code="WIJ",
        naam="Wijk",
    )
    # wijk = ("WIJ", "Wijk")
    """
    Cluster van eenheden die samen een wijk vormen, anders dan de officiële CBS-wijk
    """

    waardering = Referentiedata(
        code="WRD",
        naam="Waardering",
    )
    # waardering = ("WRD", "Waardering")
    """
    Cluster van eenheden dat wordt gewaardeerd conform de uitgangspunten van het
    Handboek Marktwaarde Verhuurde Staat (MVS).
    """
