from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Kwaliteitsmetingverzoeksoort(Enum):
    algemene_dienstverlening = Referentiedata(
        code="ALG",
        naam="Algemene dienstverlening",
    )
    """
    Kwaliteitsmetingverzoek betreffende algemene dienstverlening
    """

    nieuwe_huurders = Referentiedata(
        code="HUN",
        naam="Nieuwe huurders",
    )
    """
    Kwaliteitsmetingverzoek betreffende nieuwe huurders
    """

    vertrokken_huurders = Referentiedata(
        code="HUV",
        naam="Vertrokken huurders",
    )
    """
    Kwaliteitsmetingverzoek betreffende vertrokken huurders
    """

    onderhoud = Referentiedata(
        code="OND",
        naam="Onderhoud",
    )
    """
    Kwaliteitsmetingverzoek betreffende onderhoud
    """

    overig = Referentiedata(
        code="OVR",
        naam="Overig",
    )
    """
    Kwaliteitsmetingverzoek betreffende overige onderwerpen
    """

    reparaties = Referentiedata(
        code="REP",
        naam="Reparaties",
    )
    """
    Kwaliteitsmetingverzoek betreffende reparaties
    """

    woonomgeving = Referentiedata(
        code="WOO",
        naam="Woonomgeving",
    )
    """
    Kwaliteitsmetingverzoek betreffende woonomgeving
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
