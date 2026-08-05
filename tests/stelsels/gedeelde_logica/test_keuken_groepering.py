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


def test_waardeer_keuken_gebruikt_subtotaal_bij_meerdere_aanrechten():
    with INPUT.open() as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())

    ruimte = eenheid.ruimten[0]
    extra_aanrecht = ruimte.bouwkundige_elementen[0].model_copy(deep=True)
    extra_aanrecht.id = "aanrecht_extra"
    extra_aanrecht.lengte = 900
    ruimte.bouwkundige_elementen.append(extra_aanrecht)

    waarderingsgroep_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.keuken,
    )
    waarderingen = waardeer_keuken(
        ruimte,
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        waarderingsgroep_builder=waarderingsgroep_builder,
    )

    subtotaal = next(w for w in waarderingen if w.segment == "subtotaal")
    details = [w for w in waarderingen if w.segment.startswith("lengte_aanrecht_")]

    assert subtotaal.naam == "Totale aanrechtlengte"
    assert subtotaal.aantal == 1900
    assert subtotaal.punten == 4
    assert len(details) == 2
    assert all(detail.punten is None for detail in details)
    assert all(detail.bovenliggende_id == subtotaal.criterium_id for detail in details)
