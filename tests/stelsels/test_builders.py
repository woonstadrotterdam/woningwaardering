from decimal import Decimal

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def test_stelselgroeptotaal_volgt_uit_onafgeronde_punten():
    """Het stelselgroeptotaal is het kwartpunt van de onafgeronde som, niet van de vastgelegde rijen.

    Bewust rekenkundig randgeval (geen realistische woonruimte): zeven
    waarderingen van 0,0178 punt. Onafgerond is de som 0,1246, wat afrondt op
    kwartpunt 0,00. De rijen worden in de output vastgelegd op 0,02; wie die
    afgeronde rijen zou sommeren komt op 0,14 en daarmee op kwartpunt 0,25.
    Deze test legt vast dat het totaal uit de onafgeronde builder-punten volgt
    en de waardering Afronding op kwartpunten het verschil met de vastgelegde
    rijen sluit.
    """
    waarderingsgroep_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.buitenruimten,
    )
    for nummer in range(7):
        waarderingsgroep_builder.met_onderliggend(
            id=f"waardering_{nummer}",
            naam=f"Waardering {nummer}",
            punten=Decimal("0.0178"),
        )

    groep = waarderingsgroep_builder.build()

    assert groep.punten == 0.0, (
        "Het stelselgroeptotaal moet het kwartpunt van de onafgeronde som zijn "
        "(0,1246 -> 0,00), niet dat van de op twee decimalen vastgelegde rijen "
        "(7 x 0,02 = 0,14 -> 0,25)"
    )

    waarderingen = groep.woningwaarderingen or []
    afronding = [
        waardering
        for waardering in waarderingen
        if waardering.criterium is not None
        and waardering.criterium.naam == "Afronding op kwartpunten"
    ]
    assert len(afronding) == 1
    assert afronding[0].punten == -0.14

    som_rijen = sum(
        Decimal(str(waardering.punten))
        for waardering in waarderingen
        if waardering.punten is not None
    )
    assert som_rijen == Decimal(str(groep.punten))
