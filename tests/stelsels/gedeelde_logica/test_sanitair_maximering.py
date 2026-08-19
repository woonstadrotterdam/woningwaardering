from decimal import Decimal
from pathlib import Path

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    maximeer_wastafels,
    waardeer_sanitair,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

INPUT = (
    Path(__file__).parents[2]
    / "data/onzelfstandige_woonruimten/stelselgroepen/sanitair/input/maximering_wastafels_8_onz_gunstigste_ruimte.json"
)


def _maximeringsregels_per_ruimte(
    ruimte_waarderingen: list,
) -> dict[str, list[str]]:
    per_ruimte: dict[str, list[str]] = {}
    for ruimte, ruimte_criterium, waarderingen in ruimte_waarderingen:
        maximeringen = [
            waardering.naam or ""
            for waardering in waarderingen
            if waardering.bovenliggende is ruimte_criterium
            and (waardering.naam or "").startswith("Max")
        ]
        per_ruimte[ruimte.id] = maximeringen
    return per_ruimte


def test_maximeer_wastafels_stelt_precies_een_uitzonderingsruimte_vrij():
    with INPUT.open() as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())

    waarderingsgroep_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.onzelfstandige_woonruimten,
        Woningwaarderingstelselgroep.sanitair,
    )

    ruimte_waarderingen = []
    for ruimte in eenheid.ruimten or []:
        gedeeld_met = waarderingsgroep_builder.gedeeld_met(
            aantal_onzelfstandige_woonruimten=(
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            ),
        )
        waarderingen = waardeer_sanitair(
            ruimte,
            Woningwaarderingstelsel.onzelfstandige_woonruimten,
            waarderingsgroep_builder=gedeeld_met,
            deler=1,
        )
        if not waarderingen:
            continue
        ruimte_waarderingen.append((ruimte, waarderingen[0], waarderingen))

    maximeer_wastafels(
        ruimte_waarderingen,
        deler=lambda ruimte: Decimal(
            ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
        ),
    )

    maximeringen = _maximeringsregels_per_ruimte(ruimte_waarderingen)
    vrijgestelde_ruimten = [
        ruimte_id for ruimte_id, regels in maximeringen.items() if not regels
    ]
    gemaximeerde_ruimten = [
        ruimte_id for ruimte_id, regels in maximeringen.items() if regels
    ]

    assert vrijgestelde_ruimten == ["bergruimte_meerpersoons"]
    assert gemaximeerde_ruimten == ["woonkamer_wastafels"]
    assert maximeringen["woonkamer_wastafels"] == ["Maximering voor Wastafel"]
