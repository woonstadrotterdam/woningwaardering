import pytest

from woningwaardering.bereken import select_geldige_stelsels
from woningwaardering.stelsels.stelsel import Stelsel


@pytest.mark.parametrize("peildatum", ["01-01-2025"])
def test_select_geldige_stelsels(peildatum):
    geldige_stelsels = select_geldige_stelsels(peildatum=peildatum)
    assert len(geldige_stelsels) == 1, "Aantal geldige stelsels is niet correct."
    for stelsel in geldige_stelsels:
        assert isinstance(
            stelsel, Stelsel
        ), f"Stelsel '{stelsel}' is geen instance van Stelsel"
