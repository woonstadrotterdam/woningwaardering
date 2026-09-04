from pathlib import Path

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    waardeer_sanitair,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Installatiesoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

INPUT = (
    Path(__file__).parents[2]
    / "data/zelfstandige_woonruimten/stelselgroepen/sanitair/input/douche.json"
)


def test_waardeer_sanitair_groepeert_per_ruimte():
    with INPUT.open() as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())

    ruimte = eenheid.ruimten[0]
    waarderingsgroep_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.sanitair,
    )
    waarderingen = waardeer_sanitair(
        ruimte,
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        waarderingsgroep_builder=waarderingsgroep_builder,
    )

    ruimte_ouder_id = f"{Woningwaarderingstelselgroep.sanitair.name}__{ruimte.id}"
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
        assert not (detail.naam or "").startswith(f"{ruimte.naam} - ")


def test_waardeer_sanitair_laadt_resterende_douche_na_bad_koppeling() -> None:
    eenheid = EenhedenEenheid.model_validate(
        {
            "ruimten": [
                {
                    "id": "Space_1",
                    "soort": Ruimtesoort.vertrek,
                    "detailSoort": Ruimtedetailsoort.badkamer,
                    "naam": "Badkamer",
                    "installaties": [
                        Installatiesoort.bad,
                        Installatiesoort.douche,
                        Installatiesoort.drempelloze_inrijdouche,
                    ],
                }
            ]
        }
    )

    waarderingen = waardeer_sanitair(
        eenheid.ruimten[0],
        Woningwaarderingstelsel.onzelfstandige_woonruimten,
        waarderingsgroep_builder=WaarderingsgroepBuilder(
            Woningwaarderingstelsel.onzelfstandige_woonruimten,
            Woningwaarderingstelselgroep.sanitair,
        ),
    )

    details = {waardering.criterium_id: waardering for waardering in waarderingen}

    assert details["sanitair__Space_1__bad_en_douche"].aantal == 1
    assert details["sanitair__Space_1__bad_en_douche"].punten == 6.0
    assert "sanitair__Space_1__douche" not in details
    assert details["sanitair__Space_1__drempelloze_inrijdouche"].aantal == 1
    assert details["sanitair__Space_1__drempelloze_inrijdouche"].punten == 3.0


def test_waardeer_sanitair_trekt_expliciete_bad_en_douche_niet_af_van_resttypes() -> (
    None
):
    eenheid = EenhedenEenheid.model_validate(
        {
            "ruimten": [
                {
                    "id": "Space_1",
                    "soort": Ruimtesoort.vertrek,
                    "detailSoort": Ruimtedetailsoort.badkamer,
                    "naam": "Badkamer",
                    "installaties": [
                        Installatiesoort.bad_en_douche,
                        Installatiesoort.bad,
                        Installatiesoort.douche,
                    ],
                }
            ]
        }
    )

    waarderingen = waardeer_sanitair(
        eenheid.ruimten[0],
        Woningwaarderingstelsel.onzelfstandige_woonruimten,
        waarderingsgroep_builder=WaarderingsgroepBuilder(
            Woningwaarderingstelsel.onzelfstandige_woonruimten,
            Woningwaarderingstelselgroep.sanitair,
        ),
    )

    details = {waardering.criterium_id: waardering for waardering in waarderingen}

    assert details["sanitair__Space_1__bad_en_douche"].aantal == 2
    assert details["sanitair__Space_1__bad_en_douche"].punten == 12.0
    assert "sanitair__Space_1__bad" not in details
    assert "sanitair__Space_1__douche" not in details
