from datetime import date

from woningwaardering.stelsels.gedeelde_logica.punten_voor_de_woz_waarde import (
    meest_recente_relevante_woz_eenheid,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenWozEenheid,
)

PEILDATUM = date(2026, 7, 1)


def _woz_eenheid(
    waardepeildatum: date,
    vastgestelde_waarde: float | None,
) -> EenhedenWozEenheid:
    return EenhedenWozEenheid(
        waardepeildatum=waardepeildatum,
        vastgestelde_waarde=vastgestelde_waarde,
    )


def test_meest_recente_relevante_woz_eenheid_valt_terug_op_voorgaande():
    voorgaande = _woz_eenheid(date(2024, 1, 1), 300_000)
    eenheid = EenhedenEenheid(
        id="test",
        woz_eenheden=[
            _woz_eenheid(date(2025, 1, 1), None),
            voorgaande,
        ],
    )

    assert meest_recente_relevante_woz_eenheid(eenheid, PEILDATUM) == voorgaande


def test_meest_recente_relevante_woz_eenheid_negeert_leeg_dubbel_record():
    gevuld = _woz_eenheid(date(2025, 1, 1), 300_000)
    eenheid = EenhedenEenheid(
        id="test",
        woz_eenheden=[
            _woz_eenheid(date(2025, 1, 1), None),
            gevuld,
        ],
    )

    assert meest_recente_relevante_woz_eenheid(eenheid, PEILDATUM) == gevuld


def test_meest_recente_relevante_woz_eenheid_accepteert_alleen_eerste_januari():
    voorgaande = _woz_eenheid(date(2024, 1, 1), 300_000)
    eenheid = EenhedenEenheid(
        id="test",
        woz_eenheden=[
            _woz_eenheid(date(2025, 6, 1), 350_000),
            voorgaande,
        ],
    )

    assert meest_recente_relevante_woz_eenheid(eenheid, PEILDATUM) == voorgaande


def test_meest_recente_relevante_woz_eenheid_negeert_waarde_nul():
    voorgaande = _woz_eenheid(date(2024, 1, 1), 300_000)
    eenheid = EenhedenEenheid(
        id="test",
        woz_eenheden=[
            _woz_eenheid(date(2025, 1, 1), 0),
            voorgaande,
        ],
    )

    assert meest_recente_relevante_woz_eenheid(eenheid, PEILDATUM) == voorgaande
