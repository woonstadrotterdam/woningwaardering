import pytest

from woningwaardering.stelsels.stelsel import select_geldige_stelselgroepversies
from woningwaardering.stelsels.stelselgroep import StelselgroepVersie


@pytest.mark.parametrize(
    "peildatum, stelsel, aantal_geldige_stelselgroepversies",
    [("01-01-2025", "zelfstandig", 2)],
)
def test_select_geldige_stelselgroepversies(
    peildatum, stelsel, aantal_geldige_stelselgroepversies
):
    geldigige_stelselgroepversies = select_geldige_stelselgroepversies(
        peildatum=peildatum, stelsel=stelsel
    )
    assert (
        len(geldigige_stelselgroepversies) == aantal_geldige_stelselgroepversies
    ), "Aantal geldige stelselgroepen is niet correct."
    for stelselgroep in geldigige_stelselgroepversies:
        assert isinstance(
            stelselgroep, StelselgroepVersie
        ), f"Stelselgroepversie '{stelselgroep}' is geen instance van StelselgroepVersie"
