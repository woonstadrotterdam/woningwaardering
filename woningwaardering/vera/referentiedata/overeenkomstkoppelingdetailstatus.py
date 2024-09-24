from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Overeenkomstkoppelingdetailstatus(Enum):
    afgewezen_door_woningzoekende = Referentiedata(
        code="AFG",
        naam="Afgewezen door woningzoekende",
        parent=Referentiedata(
            code="AFG",
            naam="Afgewezen",
        ),
    )
    """
    Woningzoekende heeft het verzoek tot koppelen afgewezen.
    """

    bevestigingstermijn_is_verstreken = Referentiedata(
        code="BEV",
        naam="Bevestigingstermijn is verstreken",
        parent=Referentiedata(
            code="AFG",
            naam="Afgewezen",
        ),
    )
    """
    Koppeling is afgewezen omdat de bevestigingstermijn is verstreken.
    """

    geboortedatum_komt_niet_overeen = Referentiedata(
        code="GEB",
        naam="Geboortedatum komt niet overeen",
        parent=Referentiedata(
            code="AFG",
            naam="Afgewezen",
        ),
    )
    """
    Koppeling is afgewezen omdat de geboortedatum van de woningzoekende in beide
    inschrijvingen niet overeenkomt.
    """

    naamgegevens_komen_niet_overeen = Referentiedata(
        code="NAA",
        naam="Naamgegevens komen niet overeen",
        parent=Referentiedata(
            code="AFG",
            naam="Afgewezen",
        ),
    )
    """
    Koppeling is afgewezen omdat de naamgegevens van de woningzoekende in beide
    inschrijvingen niet overeenkomen.
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
