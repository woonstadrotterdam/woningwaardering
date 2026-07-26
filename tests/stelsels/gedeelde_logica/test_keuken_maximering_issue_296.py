"""Verificatietests voor GitHub issue #296 (ZEL keuken maximering extra voorzieningen)."""

from datetime import date

import pytest

from woningwaardering.stelsels.zelfstandige_woonruimten.keuken import Keuken
from woningwaardering.vera.bvg.generated import EenhedenEenheid


def _waardeer_keuken_punten(json_input: str) -> float:
    eenheid = EenhedenEenheid.model_validate_json(json_input)
    groep = Keuken(peildatum=date(2026, 1, 1)).waardeer(eenheid)
    assert groep.punten is not None
    return groep.punten


_KEUKEN_BASIS = """
{
  "id": "issue-296",
  "ruimten": [{
    "id": "keuken",
    "soort": {"code": "VTK", "naam": "Vertrek"},
    "detailSoort": {"code": "KEU", "naam": "Keuken"},
    "naam": "Keuken",
    "bouwkundigeElementen": {aanrechten},
    "installaties": {installaties}
  }]
}
"""


def _keuken_json(aanrecht_lengtes: list[int], aantal_koelkasten: int) -> str:
    aanrechten = ", ".join(
        f"""{{
          "id": "aanrecht_{idx}",
          "naam": "Aanrecht {idx}",
          "soort": {{"code": "KEU", "naam": "Keuken voorziening"}},
          "detailSoort": {{"code": "AAN", "naam": "Aanrecht"}},
          "lengte": {lengte}
        }}"""
        for idx, lengte in enumerate(aanrecht_lengtes, start=1)
    )
    installaties = ", ".join(
        '{"code": "IKO", "naam": "Inbouw koelkast"}' for _ in range(aantal_koelkasten)
    )
    return _KEUKEN_BASIS.replace("{aanrechten}", f"[{aanrechten}]").replace(
        "{installaties}", f"[{installaties}]"
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_296_kort_aanrecht_verhoogt_max_niet():
    assert _waardeer_keuken_punten(_keuken_json([1500, 600], 8)) == 8.0


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_296_twee_geldige_aanrechten_som_basispunten():
    assert _waardeer_keuken_punten(_keuken_json([1000, 1000], 8)) == 16.0


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_296_beleidsboek_voorbeeld_1600mm():
    eenheid_json = """{
      "id": "keuken_1600mm",
      "ruimten": [{
        "id": "keuken",
        "soort": {"code": "VTK", "naam": "Vertrek"},
        "detailSoort": {"code": "KEU", "naam": "Keuken"},
        "naam": "Keuken",
        "bouwkundigeElementen": [{
          "id": "aanrecht",
          "naam": "Aanrecht",
          "soort": {"code": "KEU", "naam": "Keuken voorziening"},
          "detailSoort": {"code": "AAN", "naam": "Aanrecht"},
          "lengte": 1600
        }],
        "installaties": [
          {"code": "IKI", "naam": "Inbouw kookplaat inductie"},
          {"code": "IAF", "naam": "Inbouw afzuiginstallatie"},
          {"code": "IOE", "naam": "Inbouw oven elektrisch"},
          {"code": "IKO", "naam": "Inbouw koelkast"}
        ]
      }]
    }"""
    assert _waardeer_keuken_punten(eenheid_json) == 8.0
