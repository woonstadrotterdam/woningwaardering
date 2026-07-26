"""Tests voor toiletten in een doucheruimte.

Bron: docs/implementatietoelichtingen/onzelfstandige-woonruimten.md §2.6.1
"Toiletten die buiten toiletruimten en badkamers zijn aangebracht worden niet gewaardeerd."
"""

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    waardeer_sanitair,
)
from woningwaardering.vera.bvg.generated import EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Installatiesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def _waardeer_ruimte(
    ruimte: EenhedenRuimte,
    *,
    stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten,
):
    builder = WaarderingsgroepBuilder(stelsel, Woningwaarderingstelselgroep.sanitair)
    return waardeer_sanitair(ruimte, stelsel, waarderingsgroep_builder=builder)


def _maak_doucheruimte_met_toilet() -> EenhedenRuimte:
    return EenhedenRuimte.model_validate(
        {
            "id": "Space_doucheruimte_toilet",
            "naam": "Doucheruimte",
            "detailSoort": {"code": "DOU", "naam": "Doucheruimte"},
            "installaties": [
                {"code": "STO", "naam": "Staand Toilet"},
                {"code": "DOU", "naam": "Douche"},
                {"code": "WAS", "naam": "Wastafel"},
            ],
        }
    )


def test_toilet_in_doucheruimte_geeft_geen_keyerror():
    """Een toilet in een doucheruimte mag niet crashen met KeyError."""
    ruimte = _maak_doucheruimte_met_toilet()
    waarderingen = _waardeer_ruimte(ruimte)
    assert waarderingen


def test_toilet_in_doucheruimte_krijgt_geen_punten():
    """§2.6.1 [ONZ]: toilet buiten toiletruimte/badkamer → n.v.t."""
    ruimte = _maak_doucheruimte_met_toilet()
    waarderingen = _waardeer_ruimte(ruimte)

    toilet_waarderingen = [
        w
        for w in waarderingen
        if w.segment
        in (Installatiesoort.staand_toilet.name, Installatiesoort.hangend_toilet.name)
    ]
    assert toilet_waarderingen == []


def test_overige_sanitair_in_doucheruimte_blijft_gewaardeerd():
    """Douche en wastafel in doucheruimte blijven wel gewaardeerd."""
    ruimte = _maak_doucheruimte_met_toilet()
    waarderingen = _waardeer_ruimte(ruimte)

    segmenten = {w.segment for w in waarderingen if w.segment}
    assert Installatiesoort.douche.name in segmenten
    assert Installatiesoort.wastafel.name in segmenten


def test_toilet_in_toiletruimte_blijft_gewaardeerd():
    """Regressie: toiletruimte-toilet blijft 3 punten (staand)."""
    ruimte = EenhedenRuimte.model_validate(
        {
            "id": "Space_toiletruimte",
            "naam": "Toiletruimte",
            "detailSoort": {"code": "TOI", "naam": "Toiletruimte"},
            "installaties": [{"code": "STO", "naam": "Staand Toilet"}],
        }
    )
    waarderingen = _waardeer_ruimte(ruimte)

    toilet = next(
        w for w in waarderingen if w.segment == Installatiesoort.staand_toilet.name
    )
    assert toilet.punten == 3.0


def test_toilet_in_badkamer_blijft_gewaardeerd():
    """Regressie: badkamer-toilet blijft 2 punten (staand)."""
    ruimte = EenhedenRuimte.model_validate(
        {
            "id": "Space_badkamer",
            "naam": "Badkamer",
            "detailSoort": {"code": "BAD", "naam": "Badkamer"},
            "installaties": [{"code": "STO", "naam": "Staand Toilet"}],
        }
    )
    waarderingen = _waardeer_ruimte(ruimte)

    toilet = next(
        w for w in waarderingen if w.segment == Installatiesoort.staand_toilet.name
    )
    assert toilet.punten == 2.0
