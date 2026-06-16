import json
from decimal import Decimal
from pathlib import Path

import pytest

from woningwaardering.stelsels.criterium_id import (
    CriteriumId,
    GedeeldMetSoort,
    weergavenaam_voor,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_stelselgroepcriterium() -> None:
    stelselgroep_id = CriteriumId.voor_stelselgroep(Woningwaarderingstelselgroep.keuken)
    assert str(stelselgroep_id) == "keuken"
    assert stelselgroep_id.bovenliggend is None


def test_onderliggendcriteriumid_pad() -> None:
    stelselgroep_id = CriteriumId.voor_stelselgroep(
        Woningwaarderingstelselgroep.verkoeling_en_verwarming
    )
    groepering = stelselgroep_id.met_onderliggend("verwarmde_vertrekken")
    onderliggend = groepering.met_onderliggend("ruimte_1")

    assert str(onderliggend) == (
        "verkoeling_en_verwarming__verwarmde_vertrekken__ruimte_1"
    )
    assert str(onderliggend).startswith(str(groepering) + "__")


def test_gedeeld_met_criterium_enkel_token() -> None:
    aggregaat = CriteriumId.voor_stelselgroep(
        Woningwaarderingstelselgroep.buitenruimten
    ).gedeeld_met_criterium(4, GedeeldMetSoort.adressen)

    assert str(aggregaat) == "buitenruimten__gedeeld_met_4_adressen"
    assert "__gedeeld_met__" not in str(aggregaat)


def test_gedeeld_met_prive() -> None:
    prive = CriteriumId.voor_stelselgroep(
        Woningwaarderingstelselgroep.buitenruimten
    ).gedeeld_met_criterium(1)

    assert str(prive) == "buitenruimten__prive"


def test_met_waardering_koppelt_bovenliggend() -> None:
    groepering = CriteriumId.voor_stelselgroep(
        Woningwaarderingstelselgroep.verkoeling_en_verwarming
    ).met_onderliggend("verwarmde_vertrekken")
    waardering = groepering.met_onderliggend("ruimte_1").met_waardering(
        "Woonkamer", punten=2.0
    )

    assert waardering.criterium is not None
    assert waardering.criterium.bovenliggende_criterium is not None
    assert waardering.criterium.bovenliggende_criterium.id == str(groepering)


def test_weergavenaam_voor_bekende_groepering() -> None:
    assert weergavenaam_voor("verwarmde_vertrekken") == "Verwarmde vertrekken"


def test_criterium_id_equality() -> None:
    a = CriteriumId.voor_stelselgroep(Woningwaarderingstelselgroep.keuken)
    b = CriteriumId.voor_stelselgroep(Woningwaarderingstelselgroep.keuken)
    assert a == b
    assert hash(a) == hash(b)


@pytest.mark.parametrize(
    ("criterium_id", "verwacht"),
    [
        ("buitenruimten__gedeeld_met_3_adressen__ruimte_1", Decimal("3")),
        (
            "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_3_adressen__ruimte_1",
            Decimal("3"),
        ),
        ("sanitair__gedeeld_met_8_onzelfstandige_woonruimten", Decimal("8")),
        ("keuken__prive__ruimte_1", Decimal("1")),
        ("keuken__ruimte_1", Decimal("1")),
        (None, Decimal("1")),
    ],
)
def test_gedeeld_met_divisor(criterium_id: str | None, verwacht: Decimal) -> None:
    from woningwaardering.stelsels import utils

    assert utils._gedeeld_met_divisor(criterium_id) == verwacht


_DATA_DIR = Path(__file__).resolve().parents[1] / "data"
_OUTPUT_FIXTURES = sorted(p for p in _DATA_DIR.rglob("*.json") if "output" in p.parts)


def _is_uitgezonderd(
    bovenliggendcriterium_id: str, onderliggendcriterium_id: str
) -> bool:
    return False


def _criteriumid_paren(node: object) -> list[tuple[str, str]]:
    paren: list[tuple[str, str]] = []
    if isinstance(node, dict):
        criterium = node.get("criterium")
        if isinstance(criterium, dict):
            onderliggend = criterium.get("id")
            bovenliggend = criterium.get("bovenliggendeCriterium")
            if (
                isinstance(bovenliggend, dict)
                and bovenliggend.get("id")
                and onderliggend
            ):
                paren.append((bovenliggend["id"], onderliggend))
        for waarde in node.values():
            paren.extend(_criteriumid_paren(waarde))
    elif isinstance(node, list):
        for waarde in node:
            paren.extend(_criteriumid_paren(waarde))
    return paren


@pytest.mark.parametrize(
    "fixture",
    _OUTPUT_FIXTURES,
    ids=[str(p.relative_to(_DATA_DIR)) for p in _OUTPUT_FIXTURES],
)
def test_onderliggendcriteriumid_begint_met_bovenliggendcriteriumid(
    fixture: Path,
) -> None:
    """Elk onderliggendcriteriumid begint met bovenliggendcriteriumid + '__'."""
    schendingen = [
        (bovenliggend, onderliggend)
        for bovenliggend, onderliggend in _criteriumid_paren(
            json.loads(fixture.read_text())
        )
        if not _is_uitgezonderd(bovenliggend, onderliggend)
        and not onderliggend.startswith(bovenliggend + "__")
    ]
    assert not schendingen, f"{fixture}: {schendingen}"
