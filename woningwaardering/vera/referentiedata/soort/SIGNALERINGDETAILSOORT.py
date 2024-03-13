from woningwaardering.vera.bvg.models import Referentiedata


class SIGNALERINGDETAILSOORT:
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
