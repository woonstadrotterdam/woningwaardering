from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OvereenkomstversturenstatusReferentiedata(Referentiedata):
    pass


class Overeenkomstversturenstatus(Referentiedatasoort):
    afgeleverd = OvereenkomstversturenstatusReferentiedata(
        code="AFL",
        naam="Afgeleverd",
    )
    """
    De overeenkomst is technisch succesvol afgeleverd, bijvoorbeeld via e-mail of
    portaal.
    """

    geannuleerd = OvereenkomstversturenstatusReferentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    """
    De verzending is geannuleerd, bijvoorbeeld omdat de overeenkomst is aangepast of
    ingetrokken.
    """

    mislukt = OvereenkomstversturenstatusReferentiedata(
        code="MIS",
        naam="Mislukt",
    )
    """
    Het versturen is mislukt, bijvoorbeeld door een technische fout of ontbrekende
    gegevens.
    """

    niet_verstuurd = OvereenkomstversturenstatusReferentiedata(
        code="NVT",
        naam="Niet verstuurd",
    )
    """
    De overeenkomst is nog niet verstuurd. Dit is de initiële status.
    """

    verstuurd = OvereenkomstversturenstatusReferentiedata(
        code="VER",
        naam="Verstuurd",
    )
    """
    De overeenkomst is succesvol verstuurd naar de betrokkene(n).
    """
