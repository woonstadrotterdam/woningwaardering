
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class OVEREENKOMSTKOPPELINGDETAILSTATUS:

    afgewezen_door_woningzoekende = Referentiedata(
        code="AFG",
        naam="Afgewezen door woningzoekende",
    )
    # afgewezen_door_woningzoekende = ("AFG", "Afgewezen door woningzoekende")
    """
    Woningzoekende heeft het verzoek tot koppelen afgewezen.
    """

    bevestigingstermijn_is_verstreken = Referentiedata(
        code="BEV",
        naam="Bevestigingstermijn is verstreken",
    )
    # bevestigingstermijn_is_verstreken = ("BEV", "Bevestigingstermijn is verstreken")
    """
    Koppeling is afgewezen omdat de bevestigingstermijn is verstreken.
    """

    geboortedatum_komt_niet_overeen = Referentiedata(
        code="GEB",
        naam="Geboortedatum komt niet overeen",
    )
    # geboortedatum_komt_niet_overeen = ("GEB", "Geboortedatum komt niet overeen")
    """
    Koppeling is afgewezen omdat de geboortedatum van de woningzoekende in beide
    inschrijvingen niet overeenkomt.
    """

    naamgegevens_komen_niet_overeen = Referentiedata(
        code="NAA",
        naam="Naamgegevens komen niet overeen",
    )
    # naamgegevens_komen_niet_overeen = ("NAA", "Naamgegevens komen niet overeen")
    """
    Koppeling is afgewezen omdat de naamgegevens van de woningzoekende in beide
    inschrijvingen niet overeenkomen.
    """
