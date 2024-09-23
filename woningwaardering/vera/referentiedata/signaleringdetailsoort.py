from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Signaleringdetailsoort(Enum):
    agressie = Referentiedata(
        code="AGS",
        naam="Agressie",
        parent=Referentiedata(
            code="AGR",
            naam="Agressie",
        ),
    )

    ambulante_begeleiding = Referentiedata(
        code="AMB",
        naam="Ambulante begeleiding",
    )
    """
    De relatie krijgt in de eigen omgeving externe hulp om zo zelfstandig mogelijk te
    blijven functioneren.
    """

    betalingsachterstand = Referentiedata(
        code="BET",
        naam="Betalingsachterstand",
        parent=Referentiedata(
            code="SCH",
            naam="Huurschuld",
        ),
    )

    bewindvoerder = Referentiedata(
        code="BEW",
        naam="Bewindvoerder",
        parent=Referentiedata(
            code="SCH",
            naam="Huurschuld",
        ),
    )

    brandstichting = Referentiedata(
        code="BRA",
        naam="Brandstichting",
        parent=Referentiedata(
            code="AGR",
            naam="Agressie",
        ),
    )

    deurwaarder = Referentiedata(
        code="DEU",
        naam="Deurwaarder",
        parent=Referentiedata(
            code="SCH",
            naam="Huurschuld",
        ),
    )

    drugshandel = Referentiedata(
        code="DRU",
        naam="Drugshandel",
        parent=Referentiedata(
            code="ONE",
            naam="Oneigenlijk gebruik woning",
        ),
    )

    geluidsoverlast = Referentiedata(
        code="GEL",
        naam="Geluidsoverlast",
        parent=Referentiedata(
            code="OVE",
            naam="Overlast",
        ),
    )

    hennepkwekerij = Referentiedata(
        code="HEN",
        naam="Hennepkwekerij",
        parent=Referentiedata(
            code="ONE",
            naam="Oneigenlijk gebruik woning",
        ),
    )

    mutatieschade = Referentiedata(
        code="MUT",
        naam="Mutatieschade",
        parent=Referentiedata(
            code="SCH",
            naam="Huurschuld",
        ),
    )

    onderverhuur = Referentiedata(
        code="OND",
        naam="Onderverhuur",
        parent=Referentiedata(
            code="ONE",
            naam="Oneigenlijk gebruik woning",
        ),
    )

    prostitutie = Referentiedata(
        code="PRO",
        naam="Prostitutie",
        parent=Referentiedata(
            code="ONE",
            naam="Oneigenlijk gebruik woning",
        ),
    )

    vervuiling = Referentiedata(
        code="VER",
        naam="Vervuiling",
        parent=Referentiedata(
            code="ONE",
            naam="Oneigenlijk gebruik woning",
        ),
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
