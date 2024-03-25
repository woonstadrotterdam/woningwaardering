from datetime import datetime
import pytest

from woningwaardering.stelsels.utils import is_geldig


@pytest.mark.parametrize(
    "begindatum,einddatum,peildatum,expected",
    [
        ("01-01-2020", "31-12-2020", "01-01-2020", True),  # Peildatum is begindatum
        ("01-01-2020", "31-12-2020", "31-12-2020", True),  # Peildatum is einddatum
        (
            "01-01-2020",
            "31-12-2020",
            "15-06-2020",
            True,
        ),  # Peildatum tussen begindatum en einddatum
        (
            "01-01-2020",
            "31-12-2020",
            "31-12-2019",
            False,
        ),  # Peildatum voor begindatum
        ("01-01-2020", "31-12-2020", "01-01-2021", False),  # Peildatum na einddatum
    ],
)
def test_is_geldig(begindatum, einddatum, peildatum, expected):
    assert (
        is_geldig(
            datetime.strptime(begindatum, "%d-%m-%Y").date(),
            datetime.strptime(einddatum, "%d-%m-%Y").date(),
            datetime.strptime(peildatum, "%d-%m-%Y").date(),
        )
        == expected
    )
