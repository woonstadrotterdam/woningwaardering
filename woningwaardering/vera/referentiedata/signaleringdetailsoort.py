from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.signaleringsoort import Signaleringsoort
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Signaleringdetailsoort(Referentiedatasoort):
    agressie = Referentiedata(
        code="AGS",
        naam="Agressie",
        parent=Signaleringsoort.agressie,
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
        parent=Signaleringsoort.huurschuld,
    )

    bewindvoerder = Referentiedata(
        code="BEW",
        naam="Bewindvoerder",
        parent=Signaleringsoort.huurschuld,
    )

    brandstichting = Referentiedata(
        code="BRA",
        naam="Brandstichting",
        parent=Signaleringsoort.agressie,
    )

    deurwaarder = Referentiedata(
        code="DEU",
        naam="Deurwaarder",
        parent=Signaleringsoort.huurschuld,
    )

    drugshandel = Referentiedata(
        code="DRU",
        naam="Drugshandel",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )

    geluidsoverlast = Referentiedata(
        code="GEL",
        naam="Geluidsoverlast",
        parent=Signaleringsoort.overlast,
    )

    hennepkwekerij = Referentiedata(
        code="HEN",
        naam="Hennepkwekerij",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )

    mutatieschade = Referentiedata(
        code="MUT",
        naam="Mutatieschade",
        parent=Signaleringsoort.huurschuld,
    )

    onderverhuur = Referentiedata(
        code="OND",
        naam="Onderverhuur",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )

    prostitutie = Referentiedata(
        code="PRO",
        naam="Prostitutie",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )

    vervuiling = Referentiedata(
        code="VER",
        naam="Vervuiling",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )
