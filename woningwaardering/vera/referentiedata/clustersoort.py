from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ClustersoortReferentiedata(Referentiedata):
    pass


class Clustersoort(Referentiedatasoort):
    buurt = ClustersoortReferentiedata(
        code="BUU",
        naam="Buurt",
    )
    """
    Cluster van eenheden die samen een buurt vormen, anders dan de officiële CBS-buurt
    """

    financieel = ClustersoortReferentiedata(
        code="FIN",
        naam="Financieel",
    )

    markt = ClustersoortReferentiedata(
        code="MAR",
        naam="Markt",
    )

    onderhoud = ClustersoortReferentiedata(
        code="OND",
        naam="Onderhoud",
    )

    project = ClustersoortReferentiedata(
        code="PRO",
        naam="Project",
    )

    rayon = ClustersoortReferentiedata(
        code="RAY",
        naam="Rayon",
    )
    """
    Cluster van eenheden die samen een niet-officieel geografisch gebied, of
    organisatorische eenheid, vormen
    """

    servicekosten = ClustersoortReferentiedata(
        code="SER",
        naam="Servicekosten",
    )
    """
    Cluster van eenheden t.b.v. afrekening servicekosten
    """

    verbruikskosten = ClustersoortReferentiedata(
        code="STO",
        naam="Verbruikskosten",
    )
    """
    Cluster van eenheden t.b.v. afrekening verbruik van water, elektriciteit, gas,
    warmte.
    """

    strategisch = ClustersoortReferentiedata(
        code="STR",
        naam="Strategisch",
    )

    vereniging_van_eigenaars = ClustersoortReferentiedata(
        code="VVE",
        naam="Vereniging van Eigenaars",
    )

    wijk = ClustersoortReferentiedata(
        code="WIJ",
        naam="Wijk",
    )
    """
    Cluster van eenheden die samen een wijk vormen, anders dan de officiële CBS-wijk
    """

    waardering = ClustersoortReferentiedata(
        code="WRD",
        naam="Waardering",
    )
    """
    Cluster van eenheden dat wordt gewaardeerd conform de uitgangspunten van het
    Handboek Marktwaarde Verhuurde Staat (MVS).
    """
