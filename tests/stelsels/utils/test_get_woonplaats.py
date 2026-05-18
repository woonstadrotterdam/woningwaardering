import warnings
from unittest.mock import MagicMock, patch

import pytest

from woningwaardering.stelsels.utils import get_woonplaats
from woningwaardering.vera.bvg.generated import EenhedenEenheidadres, EenhedenWoonplaats


def test_get_woonplaats_gebruikt_opgegeven_code_zonder_kadaster():
    adres = EenhedenEenheidadres(
        postcode="3511AD",
        huisnummer="100",
        woonplaats=EenhedenWoonplaats(code="3295", naam="Utrecht"),
    )

    with patch("woningwaardering.stelsels.utils.requests.post") as mock_post:
        woonplaats = get_woonplaats(adres)

    assert woonplaats == adres.woonplaats
    mock_post.assert_not_called()


def test_get_woonplaats_verrijkt_woonplaats_via_kadaster():
    adres = EenhedenEenheidadres(postcode="3511AD", huisnummer="100")
    mock_response = MagicMock()
    mock_response.json.return_value = [{"identificatie": "3295", "naam": "Utrecht"}]
    mock_response.raise_for_status = MagicMock()

    with patch(
        "woningwaardering.stelsels.utils.requests.post", return_value=mock_response
    ):
        woonplaats = get_woonplaats(adres)

    assert woonplaats == EenhedenWoonplaats(code="3295", naam="Utrecht")
    assert adres.woonplaats is None


def test_get_woonplaats_geeft_geen_woonplaats_bij_afwijkende_naam():
    adres = EenhedenEenheidadres(
        postcode="1013GS",
        huisnummer="22",
        woonplaats=EenhedenWoonplaats(naam="Rotterdam"),
    )
    mock_response = MagicMock()
    mock_response.json.return_value = [{"identificatie": "3594", "naam": "Amsterdam"}]
    mock_response.raise_for_status = MagicMock()

    with patch(
        "woningwaardering.stelsels.utils.requests.post", return_value=mock_response
    ):
        with pytest.warns(UserWarning, match="Kan geen woonplaats bepalen"):
            woonplaats = get_woonplaats(adres)

    assert woonplaats is None


def test_get_woonplaats_geen_waarschuwing_bij_overeenkomende_naam():
    adres = EenhedenEenheidadres(
        postcode="3511AD",
        huisnummer="100",
        woonplaats=EenhedenWoonplaats(naam="UTRECHT"),
    )
    mock_response = MagicMock()
    mock_response.json.return_value = [{"identificatie": "3295", "naam": "Utrecht"}]
    mock_response.raise_for_status = MagicMock()

    with patch(
        "woningwaardering.stelsels.utils.requests.post", return_value=mock_response
    ):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            woonplaats = get_woonplaats(adres)

    assert woonplaats == EenhedenWoonplaats(code="3295", naam="Utrecht")
