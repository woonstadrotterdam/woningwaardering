import warnings
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
import requests

from woningwaardering.stelsels.utils import (
    PDOK_LOCATIESERVER_ENDPOINT,
    get_woonplaats,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheidadres, EenhedenWoonplaats

REQUESTS_GET = "woningwaardering.stelsels.utils.requests.get"


def _locatieserver_response(*documenten: dict[str, Any]) -> MagicMock:
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "response": {"numFound": len(documenten), "docs": list(documenten)}
    }
    mock_response.raise_for_status = MagicMock()
    return mock_response


def _document(
    woonplaatscode: str = "3295",
    woonplaatsnaam: str = "Utrecht",
    postcode: str = "3511AD",
    huisnummer: int = 100,
    **overig: str,
) -> dict[str, Any]:
    return {
        "woonplaatscode": woonplaatscode,
        "woonplaatsnaam": woonplaatsnaam,
        "postcode": postcode,
        "huisnummer": huisnummer,
        **overig,
    }


def test_get_woonplaats_gebruikt_opgegeven_code_zonder_locatieserver():
    adres = EenhedenEenheidadres(
        postcode="3511AD",
        huisnummer="100",
        woonplaats=EenhedenWoonplaats(code="3295", naam="Utrecht"),
    )

    with patch(REQUESTS_GET) as mock_get:
        woonplaats = get_woonplaats(adres)

    assert woonplaats == adres.woonplaats
    mock_get.assert_not_called()


def test_get_woonplaats_verrijkt_woonplaats_via_locatieserver():
    adres = EenhedenEenheidadres(postcode="3511 AD", huisnummer="100")
    mock_response = _locatieserver_response(_document())

    with patch(REQUESTS_GET, return_value=mock_response) as mock_get:
        woonplaats = get_woonplaats(adres)

    assert woonplaats == EenhedenWoonplaats(code="3295", naam="Utrecht")
    assert adres.woonplaats is None
    mock_get.assert_called_once()
    assert mock_get.call_args.args == (PDOK_LOCATIESERVER_ENDPOINT,)
    params = mock_get.call_args.kwargs["params"]
    assert params["q"] == 'postcode:"3511AD" AND huisnummer:100'
    assert params["fq"] == ["type:adres", "-huisletter:*", "-huisnummertoevoeging:*"]


def test_get_woonplaats_kiest_exact_adres_uit_meerdere_documenten():
    adres = EenhedenEenheidadres(postcode="3511AD", huisnummer="100", huisletter="B")
    mock_response = _locatieserver_response(
        _document("0001", "Elders"),
        _document("0001", "Elders", huisletter="A"),
        _document(huisletter="B"),
        _document("0001", "Elders", huisletter="B", huisnummertoevoeging="1"),
        _document("0001", "Elders", huisnummer=102, huisletter="B"),
    )

    with patch(REQUESTS_GET, return_value=mock_response):
        woonplaats = get_woonplaats(adres)

    assert woonplaats == EenhedenWoonplaats(code="3295", naam="Utrecht")


def test_get_woonplaats_geeft_geen_woonplaats_zonder_resultaat():
    adres = EenhedenEenheidadres(postcode="9999ZZ", huisnummer="1")

    with patch(REQUESTS_GET, return_value=_locatieserver_response()):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            woonplaats = get_woonplaats(adres)

    assert woonplaats is None


def test_get_woonplaats_geeft_geen_woonplaats_bij_afwijkende_naam():
    adres = EenhedenEenheidadres(
        postcode="3511AD",
        huisnummer="100",
        woonplaats=EenhedenWoonplaats(naam="Rotterdam"),
    )

    with patch(REQUESTS_GET, return_value=_locatieserver_response(_document())):
        with pytest.warns(UserWarning, match="Kan geen woonplaats bepalen"):
            woonplaats = get_woonplaats(adres)

    assert woonplaats is None


def test_get_woonplaats_geen_waarschuwing_bij_overeenkomende_naam():
    adres = EenhedenEenheidadres(
        postcode="3511AD",
        huisnummer="100",
        woonplaats=EenhedenWoonplaats(naam="UTRECHT"),
    )
    mock_response = _locatieserver_response(_document())

    with patch(REQUESTS_GET, return_value=mock_response):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            woonplaats = get_woonplaats(adres)

    assert woonplaats == EenhedenWoonplaats(code="3295", naam="Utrecht")


def test_get_woonplaats_waarschuwt_bij_netwerkfout():
    adres = EenhedenEenheidadres(postcode="3511AD", huisnummer="100")
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("503")

    with patch(REQUESTS_GET, return_value=mock_response):
        with pytest.warns(UserWarning, match="Fout bij het ophalen van woonplaatsdata"):
            woonplaats = get_woonplaats(adres)

    assert woonplaats is None
