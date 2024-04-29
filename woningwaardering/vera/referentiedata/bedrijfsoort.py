from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Bedrijfsoort(Enum):
    bouwbedrijf = Referentiedata(
        code="BOU",
        naam="Bouwbedrijf",
    )
    """
    Financieel bedrijf dat zich bezighoudt met bouwactiviteiten.
    """

    monumenten = Referentiedata(
        code="MON",
        naam="Monumenten",
    )
    """
    Financieel bedrijf dat zich bezighoudt met beheeractiviteiten van panden met een
    monumenten status.
    """

    onderhoudsbedrijf = Referentiedata(
        code="OND",
        naam="Onderhoudsbedrijf",
    )
    """
    Financieel bedrijf dat zich bezighoudt met onderhoudsactiviteiten.
    """

    projectontwikkeling = Referentiedata(
        code="PRO",
        naam="Projectontwikkeling",
    )
    """
    Financieel bedrijf dat zich bezighoudt met projectontwikkeling.
    """

    servicebedrijf = Referentiedata(
        code="SER",
        naam="Servicebedrijf",
    )
    """
    Financieel bedrijf dat zich bezighoudt met het verlenen van diensten.
    """

    toegelaten_instelling = Referentiedata(
        code="TI",
        naam="Toegelaten instelling",
    )
    """
    Financieel bedrijf dat door de Autoriteit woningcorporaties (Aw) is toegelaten als
    toegelaten instelling volgens de Woningwet.
    """

    vereniging_van_eigenaren = Referentiedata(
        code="VVE",
        naam="Vereniging van Eigenaren",
    )
    """
    Vereniging van Eigenaren van een cluster van eenheden binnen het bezit van een
    corporatie, die is opgericht nadat een corporatie een of meer eenheden binnen de
    cluster heeft verkocht.
    """

    wijkontwikkelingsmaatschappij = Referentiedata(
        code="WOM",
        naam="Wijkontwikkelingsmaatschappij",
    )
    """
    Financieel bedrijf die de regie van projectontwikkeling, uitvoering en beheer van
    woningen in een wijk op zich neemt, omdat de complexiteit van een gebied te
    groot is voor één partij (bijvoorbeeld een woningcorporatie).
    """

    woonwagenzaken = Referentiedata(
        code="WWA",
        naam="Woonwagenzaken",
    )
    """
    Financieel bedrijf dat zich bezighoudt met beheeractiviteiten van woonwagens en
    standplaatsen.
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
