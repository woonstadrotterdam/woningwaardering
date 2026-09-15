from decimal import Decimal

import pytest

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def test_stelselgroeptotaal_volgt_uit_onafgeronde_punten():
    """Het stelselgroeptotaal is de som van de onafgeronde punten, afgerond op een kwart punt, niet die van de op twee decimaal afgeronde vastgelegde waarderingen.

    Bewust rekenkundig randgeval (geen realistische woonruimte): zeven
    waarderingen van 0,0178 punt. Onafgerond is de som 0,1246, wat afrondt op
    een kwart punt tot 0,00. De rijen worden in de output vastgelegd op 0,02; wie die
    afgeronde rijen zou sommeren komt op 0,14 en daarmee op een kwart punt tot 0,25.
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
        "Het stelselgroeptotaal moet de som van de onafgeronde punten zijn, "
        "afgerond op een kwart punt (0,1246 -> 0,00), niet die van de op twee "
        "decimalen vastgelegde rijen (7 x 0,02 = 0,14 -> 0,25)"
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


@pytest.mark.parametrize(
    "ruimte_id, naam, verwacht_segment",
    [
        ("0e6e6d1e", "Slaapkamer 2", "0e6e6d1e"),
        (None, "Slaapkamer 2", "slaapkamer_2"),
        (None, "", "onbekend"),
    ],
)
def test_id_segment_valt_terug_van_id_op_naam_op_onbekend(
    ruimte_id: str | None, naam: str, verwacht_segment: str
) -> None:
    waarderingsgroep_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
    )

    waardering = waarderingsgroep_builder.met_onderliggend(
        id=ruimte_id, naam=naam, aantal=12.0
    )

    assert waardering.segment == verwacht_segment


def test_subgroepen_met_dezelfde_naam_en_zonder_id_zijn_één_subgroep() -> None:
    """Waarderingen voor dezelfde subgroep komen onder één kop, ook als die subgroep geen id heeft."""
    waarderingsgroep_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.keuken,
    )

    keuken = waarderingsgroep_builder.met_subgroep(id=None, naam="Keuken")

    assert keuken is waarderingsgroep_builder.met_subgroep(id=None, naam="Keuken")
