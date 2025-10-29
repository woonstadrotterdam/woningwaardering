from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class CommunicatievoorkeursoortReferentiedata(Referentiedata):
    pass


class Communicatievoorkeursoort(Referentiedatasoort):
    klantcontact = CommunicatievoorkeursoortReferentiedata(
        code="KLA",
        naam="Klantcontact",
    )
    """
    Direct contact voor ondersteuning, vragen, of klachten
    """

    nieuwsbrief = CommunicatievoorkeursoortReferentiedata(
        code="NIE",
        naam="Nieuwsbrief",
    )
    """
    Periodieke updates over projecten, evenementen, en relevante informatie voor
    huurders
    """

    kennisgeving = CommunicatievoorkeursoortReferentiedata(
        code="KEN",
        naam="Kennisgeving",
    )
    """
    Informereren over onderhoudswerkzaamheden, aankondiging storingen,
    beleidswijzigingen, etc.
    """

    formele_communicatie = CommunicatievoorkeursoortReferentiedata(
        code="FOR",
        naam="Formele communicatie",
    )
    """
    Officiële documenten zoals facturen, huurovereenkomsten, serviceovereenkomsten,
    betalingsherrinneringen, informatie over huurverhogingen
    """

    overige_communicatie = CommunicatievoorkeursoortReferentiedata(
        code="OVE",
        naam="Overige communicatie",
    )
