from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidstatus(Enum):
    administratief = Referentiedata(
        code="ADM",
        naam="Administratief",
    )
    """
    De eenheid wordt geëxploiteerd door een particulier of andere vastgoedbeheerder. De
    daadwerkelijke status van de eenheid is onbekend in de administratie van de
    corporatie
    """

    leegstand = Referentiedata(
        code="LEE",
        naam="Leegstand",
    )
    """
    De eenheid is in exploitatie, maar niet verhuurd. Aansluitende verhuur is niet
    mogelijk omdat nog geen nieuwe huurder is gevonden of omdat de woning nog niet
    gereed is voor verhuur
    """

    in_ontwikkeling = Referentiedata(
        code="ONT",
        naam="In ontwikkeling",
    )
    """
    De eenheid is (nog) niet in exploitatie omdat deze in ontwikkeling is. Gebruik
    eventueel een detailstatus om aan te geven in welke fase van het
    ontwikkelingsproces de eenheid zich bevindt
    """

    uit_exploitatie = Referentiedata(
        code="UIT",
        naam="Uit exploitatie",
    )
    """
    De eenheid is niet (meer) in exploitatie bij de corporatie. Gebruik in combinatie
    met Uit Exploitatiereden om te verantwoorden met welke reden de eenheid uit
    exploitatie is.
    """

    verhuurd = Referentiedata(
        code="VEH",
        naam="Verhuurd",
    )
    """
    De eenheid is verhuurd voor bepaalde of onbepaalde duur
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
