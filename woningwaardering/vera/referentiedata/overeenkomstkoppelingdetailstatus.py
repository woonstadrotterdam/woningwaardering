from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.overeenkomstkoppelingstatus import (
    Overeenkomstkoppelingstatus,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Overeenkomstkoppelingdetailstatus(Referentiedatasoort):
    afgewezen_door_woningzoekende = Referentiedata(
        code="AFG",
        naam="Afgewezen door woningzoekende",
        parent=Overeenkomstkoppelingstatus.afgewezen,
    )
    """
    Woningzoekende heeft het verzoek tot koppelen afgewezen.
    """

    bevestigingstermijn_is_verstreken = Referentiedata(
        code="BEV",
        naam="Bevestigingstermijn is verstreken",
        parent=Overeenkomstkoppelingstatus.afgewezen,
    )
    """
    Koppeling is afgewezen omdat de bevestigingstermijn is verstreken.
    """

    geboortedatum_komt_niet_overeen = Referentiedata(
        code="GEB",
        naam="Geboortedatum komt niet overeen",
        parent=Overeenkomstkoppelingstatus.afgewezen,
    )
    """
    Koppeling is afgewezen omdat de geboortedatum van de woningzoekende in beide
    inschrijvingen niet overeenkomt.
    """

    naamgegevens_komen_niet_overeen = Referentiedata(
        code="NAA",
        naam="Naamgegevens komen niet overeen",
        parent=Overeenkomstkoppelingstatus.afgewezen,
    )
    """
    Koppeling is afgewezen omdat de naamgegevens van de woningzoekende in beide
    inschrijvingen niet overeenkomen.
    """
