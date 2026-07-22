from pathlib import Path

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.keuken.keuken import waardeer_keuken
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

INPUT = (
    Path(__file__).parents[2]
    / "data/zelfstandige_woonruimten/stelselgroepen/keuken/input/aanrecht_1.json"
)


def test_waardeer_keuken_groepeert_per_ruimte():
    with INPUT.open() as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())

    ruimte = eenheid.ruimten[0]
    waarderingsgroep_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.keuken,
    )
    waarderingen = waardeer_keuken(
        ruimte,
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        waarderingsgroep_builder=waarderingsgroep_builder,
    )

    ruimte_ouder_id = f"{Woningwaarderingstelselgroep.keuken.name}__{ruimte.id}"
    ouders = [w for w in waarderingen if w.criterium_id == ruimte_ouder_id]
    details = [w for w in waarderingen if w not in ouders]

    assert len(ouders) == 1
    assert ouders[0].punten is None
    assert ouders[0].naam == ruimte.naam
    assert ouders[0].bovenliggende_id is None

    assert len(details) >= 1
    for detail in details:
        assert detail.bovenliggende_id == ruimte_ouder_id
        assert detail.punten is not None
        assert ruimte.naam not in (detail.naam or "")
