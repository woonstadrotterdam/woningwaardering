from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Clustersoort(Enum):
    buurt = Referentiedata(
        code="BUU",
        naam="Buurt",
    )
    """
    Cluster van eenheden die samen een buurt vormen, anders dan de officiële CBS-buurt
    """

    financieel = Referentiedata(
        code="FIN",
        naam="Financieel",
    )

    markt = Referentiedata(
        code="MAR",
        naam="Markt",
    )

    onderhoud = Referentiedata(
        code="OND",
        naam="Onderhoud",
    )

    project = Referentiedata(
        code="PRO",
        naam="Project",
    )

    rayon = Referentiedata(
        code="RAY",
        naam="Rayon",
    )
    """
    Cluster van eenheden die samen een niet-officieel geografisch gebied, of
    organisatorische eenheid, vormen
    """

    servicekosten = Referentiedata(
        code="SER",
        naam="Servicekosten",
    )
    """
    Cluster van eenheden t.b.v. afrekening servicekosten
    """

    verbruikskosten = Referentiedata(
        code="STO",
        naam="Verbruikskosten",
    )
    """
    Cluster van eenheden t.b.v. afrekening verbruik van water, elektriciteit, gas,
    warmte.
    """

    strategisch = Referentiedata(
        code="STR",
        naam="Strategisch",
    )

    vereniging_van_eigenaars = Referentiedata(
        code="VVE",
        naam="Vereniging van Eigenaars",
    )

    wijk = Referentiedata(
        code="WIJ",
        naam="Wijk",
    )
    """
    Cluster van eenheden die samen een wijk vormen, anders dan de officiële CBS-wijk
    """

    waardering = Referentiedata(
        code="WRD",
        naam="Waardering",
    )
    """
    Cluster van eenheden dat wordt gewaardeerd conform de uitgangspunten van het
    Handboek Marktwaarde Verhuurde Staat (MVS).
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
