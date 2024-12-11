from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.signaleringsoort import (
    Signaleringsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class SignaleringdetailsoortReferentiedata(Referentiedata):
    pass


class Signaleringdetailsoort(Referentiedatasoort):
    agressie = SignaleringdetailsoortReferentiedata(
        code="AGS",
        naam="Agressie",
        parent=Signaleringsoort.agressie,
    )

    ambulante_begeleiding = SignaleringdetailsoortReferentiedata(
        code="AMB",
        naam="Ambulante begeleiding",
    )
    """
    De relatie krijgt in de eigen omgeving externe hulp om zo zelfstandig mogelijk te
    blijven functioneren.
    """

    betalingsachterstand = SignaleringdetailsoortReferentiedata(
        code="BET",
        naam="Betalingsachterstand",
        parent=Signaleringsoort.huurschuld,
    )

    bewindvoerder = SignaleringdetailsoortReferentiedata(
        code="BEW",
        naam="Bewindvoerder",
        parent=Signaleringsoort.huurschuld,
    )

    brandstichting = SignaleringdetailsoortReferentiedata(
        code="BRA",
        naam="Brandstichting",
        parent=Signaleringsoort.agressie,
    )

    deurwaarder = SignaleringdetailsoortReferentiedata(
        code="DEU",
        naam="Deurwaarder",
        parent=Signaleringsoort.huurschuld,
    )

    drugshandel = SignaleringdetailsoortReferentiedata(
        code="DRU",
        naam="Drugshandel",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )

    geluidsoverlast = SignaleringdetailsoortReferentiedata(
        code="GEL",
        naam="Geluidsoverlast",
        parent=Signaleringsoort.overlast,
    )

    hennepkwekerij = SignaleringdetailsoortReferentiedata(
        code="HEN",
        naam="Hennepkwekerij",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )

    mutatieschade = SignaleringdetailsoortReferentiedata(
        code="MUT",
        naam="Mutatieschade",
        parent=Signaleringsoort.huurschuld,
    )

    onderverhuur = SignaleringdetailsoortReferentiedata(
        code="OND",
        naam="Onderverhuur",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )

    prostitutie = SignaleringdetailsoortReferentiedata(
        code="PRO",
        naam="Prostitutie",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )

    vervuiling = SignaleringdetailsoortReferentiedata(
        code="VER",
        naam="Vervuiling",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )
