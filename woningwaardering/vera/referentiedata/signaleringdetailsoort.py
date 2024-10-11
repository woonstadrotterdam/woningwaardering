from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.signaleringsoort import Signaleringsoort


class Signaleringdetailsoort(Enum):
    agressie = Referentiedata(
        code="AGS",
        naam="Agressie",
        parent=Signaleringsoort.agressie.value,
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
        parent=Signaleringsoort.huurschuld.value,
    )

    bewindvoerder = Referentiedata(
        code="BEW",
        naam="Bewindvoerder",
        parent=Signaleringsoort.huurschuld.value,
    )

    brandstichting = Referentiedata(
        code="BRA",
        naam="Brandstichting",
        parent=Signaleringsoort.agressie.value,
    )

    deurwaarder = Referentiedata(
        code="DEU",
        naam="Deurwaarder",
        parent=Signaleringsoort.huurschuld.value,
    )

    drugshandel = Referentiedata(
        code="DRU",
        naam="Drugshandel",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning.value,
    )

    geluidsoverlast = Referentiedata(
        code="GEL",
        naam="Geluidsoverlast",
        parent=Signaleringsoort.overlast.value,
    )

    hennepkwekerij = Referentiedata(
        code="HEN",
        naam="Hennepkwekerij",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning.value,
    )

    mutatieschade = Referentiedata(
        code="MUT",
        naam="Mutatieschade",
        parent=Signaleringsoort.huurschuld.value,
    )

    onderverhuur = Referentiedata(
        code="OND",
        naam="Onderverhuur",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning.value,
    )

    prostitutie = Referentiedata(
        code="PRO",
        naam="Prostitutie",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning.value,
    )

    vervuiling = Referentiedata(
        code="VER",
        naam="Vervuiling",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning.value,
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
