"""Tests voor de minimumafmeting van gemeenschappelijke buitenruimten."""

import pytest

from woningwaardering.stelsels.gedeelde_logica.buitenruimten import (
    voldoet_aan_minimumafmeting_gemeenschappelijke_buitenruimte,
)
from woningwaardering.vera.bvg.generated import EenhedenRuimte


@pytest.mark.parametrize(
    ("hoogte", "lengte", "breedte", "verwacht"),
    [
        (None, None, None, True),
        (2000, 1500, 1500, True),
        (2000, None, None, True),
        (None, 1500, None, True),
        (None, None, 1500, True),
        (1999, None, None, False),
        (None, 1499, None, False),
        (None, None, 1499, False),
        (0, None, None, False),
        (None, 0, None, False),
        (None, None, 0, False),
        (2000, 1500, 1499, False),
        (1999, 1500, 1500, False),
        (2000, 1499, 1500, False),
    ],
)
def test_voldoet_aan_minimumafmeting_gemeenschappelijke_buitenruimte(
    hoogte: float | None,
    lengte: float | None,
    breedte: float | None,
    verwacht: bool,
) -> None:
    ruimte = EenhedenRuimte(hoogte=hoogte, lengte=lengte, breedte=breedte)
    assert (
        voldoet_aan_minimumafmeting_gemeenschappelijke_buitenruimte(ruimte) is verwacht
    )
