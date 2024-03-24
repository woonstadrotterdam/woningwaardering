import pytest

from woningwaardering.stelsels.stelselgroep import (
    StelselgroepVersie,
    select_geldige_stelselgroepversie,
)


@pytest.mark.parametrize(
    "peildatum, stelsel, stelselgroep",
    [("01-01-2025", "zelfstandig", "oppervlakte_van_vertrekken")],
)
def test_select_geldige_stelselgroepversie(peildatum, stelsel, stelselgroep):
    geldige_stelselgroep = select_geldige_stelselgroepversie(
        peildatum=peildatum, stelsel=stelsel, stelselgroep=stelselgroep
    )
    assert isinstance(
        geldige_stelselgroep, StelselgroepVersie
    ), f"Stelselgroepversie '{geldige_stelselgroep}' is geen instance van StelselgroepVersie"
