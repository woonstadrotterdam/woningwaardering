from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Communicatievoorkeursoort(Referentiedatasoort):
    klantcontact = Referentiedata(
        code="KLA",
        naam="Klantcontact",
    )
    """
    Direct contact voor ondersteuning, vragen, of klachten
    """

    nieuwsbrief = Referentiedata(
        code="NIE",
        naam="Nieuwsbrief",
    )
    """
    Periodieke updates over projecten, evenementen, en relevante informatie voor
    huurders
    """

    kennisgeving = Referentiedata(
        code="KEN",
        naam="Kennisgeving",
    )
    """
    Informereren over onderhoudswerkzaamheden, aankondiging storingen,
    beleidswijzigingen, etc.
    """

    formele_communicatie = Referentiedata(
        code="FOR",
        naam="Formele communicatie",
    )
    """
    Officiële documenten zoals facturen, huurovereenkomsten, serviceovereenkomsten,
    betalingsherrinneringen, informatie over huurverhogingen
    """

    overige_communicatie = Referentiedata(
        code="OVE",
        naam="Overige communicatie",
    )
