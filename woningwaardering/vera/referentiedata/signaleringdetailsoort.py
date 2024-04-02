from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Signaleringdetailsoort(Enum):
    agressie = Referentiedata(
        code="AGS",
        naam="Agressie",
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
    )

    bewindvoerder = Referentiedata(
        code="BEW",
        naam="Bewindvoerder",
    )

    brandstichting = Referentiedata(
        code="BRA",
        naam="Brandstichting",
    )

    deurwaarder = Referentiedata(
        code="DEU",
        naam="Deurwaarder",
    )

    drugshandel = Referentiedata(
        code="DRU",
        naam="Drugshandel",
    )

    geluidsoverlast = Referentiedata(
        code="GEL",
        naam="Geluidsoverlast",
    )

    hennepkwekerij = Referentiedata(
        code="HEN",
        naam="Hennepkwekerij",
    )

    mutatieschade = Referentiedata(
        code="MUT",
        naam="Mutatieschade",
    )

    onderverhuur = Referentiedata(
        code="OND",
        naam="Onderverhuur",
    )

    prostitutie = Referentiedata(
        code="PRO",
        naam="Prostitutie",
    )

    vervuiling = Referentiedata(
        code="VER",
        naam="Vervuiling",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
