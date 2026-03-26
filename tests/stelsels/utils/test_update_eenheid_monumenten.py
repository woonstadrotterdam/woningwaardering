from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from unittest.mock import AsyncMock, patch

import pandas as pd
import pytest

from woningwaardering.stelsels.utils import update_eenheid_monumenten
from woningwaardering.vera.referentiedata.eenheidmonument import Eenheidmonument


@dataclass
class _AdresseerbaarObjectBasisregistratie:
    bag_identificatie: str | None


@dataclass
class _Eenheid:
    id: str
    adresseerbaar_object_basisregistratie: _AdresseerbaarObjectBasisregistratie | None
    monumenten: list[Any] | None = None


def test_monumenten_vera_output_contract():
    monumenten = pytest.importorskip("monumenten")
    MonumentenClient = monumenten.MonumentenClient

    client = MonumentenClient.__new__(MonumentenClient)

    row_rijksmonument = pd.Series(
        {
            "rijksmonument": True,
            "rijksmonument_bron": ["RCE"],
            "rijksbeschermd_gezicht": False,
            "gemeentelijk_monument": False,
        }
    )
    result = client._naar_referentiedata(row_rijksmonument)
    assert result == [
        {
            "code": Eenheidmonument.rijksmonument.code,
            "naam": Eenheidmonument.rijksmonument.naam,
            "bron": ["RCE"],
        }
    ]

    row_rijksbeschermd_stadsgezicht = pd.Series(
        {
            "rijksmonument": False,
            "rijksmonument_bron": None,
            "rijksbeschermd_gezicht": True,
            "gemeentelijk_monument": False,
        }
    )
    result = client._naar_referentiedata(row_rijksbeschermd_stadsgezicht)
    assert result == [
        {
            "code": Eenheidmonument.rijksbeschermd_stadsgezicht.code,
            "naam": Eenheidmonument.rijksbeschermd_stadsgezicht.naam,
        }
    ]

    row_gemeentelijk_monument = pd.Series(
        {
            "rijksmonument": False,
            "rijksmonument_bron": None,
            "rijksbeschermd_gezicht": False,
            "gemeentelijk_monument": True,
        }
    )
    result = client._naar_referentiedata(row_gemeentelijk_monument)
    assert result == [
        {
            "code": Eenheidmonument.gemeentelijk_monument.code,
            "naam": Eenheidmonument.gemeentelijk_monument.naam,
        }
    ]


def _run_update_with_vera_output(
    vera_output: dict[str, list[dict[str, Any]]],
) -> _Eenheid:
    pytest.importorskip("monumenten")

    bag_id = "0599010000360091"
    mocked_instance = AsyncMock()
    mocked_instance.process_from_list = AsyncMock(return_value=vera_output)

    mocked_cm = AsyncMock()
    mocked_cm.__aenter__.return_value = mocked_instance
    mocked_cm.__aexit__.return_value = False

    with patch("monumenten.MonumentenClient", return_value=mocked_cm):
        eenheid = _Eenheid(
            id="eenheid-1",
            adresseerbaar_object_basisregistratie=_AdresseerbaarObjectBasisregistratie(
                bag_identificatie=bag_id
            ),
            monumenten=None,
        )

        result = update_eenheid_monumenten(eenheid)  # type: ignore[arg-type]
    return result


def test_update_eenheid_monumenten_rijksmonument_rce_bron():
    bag_id = "0599010000360091"
    result = _run_update_with_vera_output(
        {
            bag_id: [
                {"code": "RIJ", "naam": "Rijksmonument", "bron": ["RCE"]},
                {"code": "SGR", "naam": "Rijksbeschermd stadsgezicht"},
                {"code": "GEM", "naam": "Gemeentelijk monument"},
            ]
        }
    )

    assert result.monumenten is not None
    assert sorted(m.code for m in result.monumenten) == ["GEM", "RIJ", "SGR"]
    assert {m.naam for m in result.monumenten} == {
        "Gemeentelijk monument",
        "Rijksbeschermd stadsgezicht",
        "Rijksmonument",
    }


def test_update_eenheid_monumenten_rijksmonument_kadaster_only_bron():
    bag_id = "0599010000360091"
    result = _run_update_with_vera_output(
        {
            bag_id: [
                {"code": "RIJ", "naam": "Rijksmonument", "bron": ["Kadaster"]},
                {"code": "SGR", "naam": "Rijksbeschermd stadsgezicht"},
                {"code": "GEM", "naam": "Gemeentelijk monument"},
            ]
        }
    )

    assert result.monumenten is not None
    assert sorted(m.code for m in result.monumenten) == ["GEM", "SGR"]
    assert {m.naam for m in result.monumenten} == {
        "Gemeentelijk monument",
        "Rijksbeschermd stadsgezicht",
    }
