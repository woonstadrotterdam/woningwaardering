
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class SIGNALERINGDETAILSOORT:

    agressie = Referentiedata(
        code="AGS",
        naam="Agressie",
    )
    # agressie = ("AGS", "Agressie")

    ambulante_begeleiding = Referentiedata(
        code="AMB",
        naam="Ambulante begeleiding",
    )
    # ambulante_begeleiding = ("AMB", "Ambulante begeleiding")
    """
    De relatie krijgt in de eigen omgeving externe hulp om zo zelfstandig mogelijk te
    blijven functioneren.
    """

    betalingsachterstand = Referentiedata(
        code="BET",
        naam="Betalingsachterstand",
    )
    # betalingsachterstand = ("BET", "Betalingsachterstand")

    bewindvoerder = Referentiedata(
        code="BEW",
        naam="Bewindvoerder",
    )
    # bewindvoerder = ("BEW", "Bewindvoerder")

    brandstichting = Referentiedata(
        code="BRA",
        naam="Brandstichting",
    )
    # brandstichting = ("BRA", "Brandstichting")

    deurwaarder = Referentiedata(
        code="DEU",
        naam="Deurwaarder",
    )
    # deurwaarder = ("DEU", "Deurwaarder")

    drugshandel = Referentiedata(
        code="DRU",
        naam="Drugshandel",
    )
    # drugshandel = ("DRU", "Drugshandel")

    geluidsoverlast = Referentiedata(
        code="GEL",
        naam="Geluidsoverlast",
    )
    # geluidsoverlast = ("GEL", "Geluidsoverlast")

    hennepkwekerij = Referentiedata(
        code="HEN",
        naam="Hennepkwekerij",
    )
    # hennepkwekerij = ("HEN", "Hennepkwekerij")

    mutatieschade = Referentiedata(
        code="MUT",
        naam="Mutatieschade",
    )
    # mutatieschade = ("MUT", "Mutatieschade")

    onderverhuur = Referentiedata(
        code="OND",
        naam="Onderverhuur",
    )
    # onderverhuur = ("OND", "Onderverhuur")

    prostitutie = Referentiedata(
        code="PRO",
        naam="Prostitutie",
    )
    # prostitutie = ("PRO", "Prostitutie")

    vervuiling = Referentiedata(
        code="VER",
        naam="Vervuiling",
    )
    # vervuiling = ("VER", "Vervuiling")
