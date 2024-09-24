from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Redenopzegging(Enum):
    woning_geaccepteerd = Referentiedata(
        code="ACC",
        naam="Woning geaccepteerd",
    )
    """
    De overeenkomst is opgezegd in verband met het accepteren van een (andere) woning.
    """

    op_verzoek_corporatie = Referentiedata(
        code="COR",
        naam="Op verzoek corporatie",
    )
    """
    De overeenkomst is beeindigd door de woningcorporatie of vastgoedeigenaar.
    """

    inschrijfkosten_niet_betaald = Referentiedata(
        code="INB",
        naam="Inschrijfkosten niet betaald",
    )
    """
    Inschrijfkosten niet betaald
    """

    opzegging_woonconsument = Referentiedata(
        code="OPZ",
        naam="Opzegging woonconsument",
    )
    """
    De overeenkomst is opgezegd, geannuleerd of beeindigd op verzoek van de
    woonconsument.
    """

    overleden = Referentiedata(
        code="OVE",
        naam="Overleden",
    )
    """
    De contractant is overleden.
    """

    samengevoegd = Referentiedata(
        code="SAM",
        naam="Samengevoegd",
    )
    """
    De overeenkomst is samengevoegd of ontdubbeld in verband met overlap met een andere
    overeenkomst voor dezelfde contractant.
    """

    niet_verlengd = Referentiedata(
        code="VER",
        naam="Niet verlengd",
    )
    """
    De einddatum van de overeenkomst (met een optie op verlenging) is bereikt en er is
    geen bevestiging van een verlenging ontvangen.
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
