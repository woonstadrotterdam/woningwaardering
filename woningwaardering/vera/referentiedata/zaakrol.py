from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Zaakrol(Enum):
    adviseur = Referentiedata(
        code="ADV",
        naam="Adviseur",
    )

    behandelaar = Referentiedata(
        code="BEH",
        naam="Behandelaar",
    )
    """
    De medewerker die de zaak in behandeling heeft
    """

    beklaagde = Referentiedata(
        code="BEK",
        naam="Beklaagde",
    )
    """
    De betrokkene binnen de zaak waarover geklaagd wordt bij een (sociale) klacht
    """

    belanghebbende = Referentiedata(
        code="BEL",
        naam="Belanghebbende",
    )

    beslisser = Referentiedata(
        code="BES",
        naam="Beslisser",
    )

    initiator = Referentiedata(
        code="INI",
        naam="Initiator",
    )

    klantcontacter = Referentiedata(
        code="KLA",
        naam="Klantcontacter",
    )

    klager = Referentiedata(
        code="KLG",
        naam="Klager",
    )
    """
    De betrokkene binnen de zaak die een klacht heeft ingediend
    """

    melder = Referentiedata(
        code="MEL",
        naam="Melder",
    )
    """
    De melder van de zaak
    """

    overige_betrokkene = Referentiedata(
        code="OVE",
        naam="Overige betrokkene",
    )
    """
    Overige betrokkene binnen de zaak zoals instanties als bijvoorbeeld politie,
    gemeente, sociale dienst, etc.
    """

    zaakcoordinator = Referentiedata(
        code="ZAA",
        naam="Zaakcoördinator",
    )

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
