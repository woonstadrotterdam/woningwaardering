from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BedrijfsoortReferentiedata(Referentiedata):
    pass


class Bedrijfsoort(Referentiedatasoort):
    bouwbedrijf = BedrijfsoortReferentiedata(
        code="BOU",
        naam="Bouwbedrijf",
    )
    """
    Financieel bedrijf dat zich bezighoudt met bouwactiviteiten.
    """

    monumenten = BedrijfsoortReferentiedata(
        code="MON",
        naam="Monumenten",
    )
    """
    Financieel bedrijf dat zich bezighoudt met beheeractiviteiten van panden met een
    monumenten status.
    """

    onderhoudsbedrijf = BedrijfsoortReferentiedata(
        code="OND",
        naam="Onderhoudsbedrijf",
    )
    """
    Financieel bedrijf dat zich bezighoudt met onderhoudsactiviteiten.
    """

    projectontwikkeling = BedrijfsoortReferentiedata(
        code="PRO",
        naam="Projectontwikkeling",
    )
    """
    Financieel bedrijf dat zich bezighoudt met projectontwikkeling.
    """

    servicebedrijf = BedrijfsoortReferentiedata(
        code="SER",
        naam="Servicebedrijf",
    )
    """
    Financieel bedrijf dat zich bezighoudt met het verlenen van diensten.
    """

    toegelaten_instelling = BedrijfsoortReferentiedata(
        code="TI",
        naam="Toegelaten instelling",
    )
    """
    Financieel bedrijf dat door de Autoriteit woningcorporaties (Aw) is toegelaten als
    toegelaten instelling volgens de Woningwet.
    """

    vereniging_van_eigenaren = BedrijfsoortReferentiedata(
        code="VVE",
        naam="Vereniging van Eigenaren",
    )
    """
    Vereniging van Eigenaren van een cluster van eenheden binnen het bezit van een
    corporatie, die is opgericht nadat een corporatie een of meer eenheden binnen de
    cluster heeft verkocht.
    """

    wijkontwikkelingsmaatschappij = BedrijfsoortReferentiedata(
        code="WOM",
        naam="Wijkontwikkelingsmaatschappij",
    )
    """
    Financieel bedrijf die de regie van projectontwikkeling, uitvoering en beheer van
    woningen in een wijk op zich neemt, omdat de complexiteit van een gebied te
    groot is voor één partij (bijvoorbeeld een woningcorporatie).
    """

    woonwagenzaken = BedrijfsoortReferentiedata(
        code="WWA",
        naam="Woonwagenzaken",
    )
    """
    Financieel bedrijf dat zich bezighoudt met beheeractiviteiten van woonwagens en
    standplaatsen.
    """
