from datetime import date
import pytest

from woningwaardering.stelsels.stelselgroep import (
    Stelselgroep,
    StelselgroepVersie,
)


@pytest.mark.parametrize(
    "peildatum, stelsel, stelselgroep",
    [(date(2025, 1, 1), "zelfstandig", "oppervlakte_van_vertrekken")],
)
def test_select_geldige_stelselgroepversie(peildatum, stelsel, stelselgroep):
    geldige_stelselgroep = Stelselgroep.select_geldige_stelselgroepversie(
        peildatum=peildatum, stelsel=stelsel, stelselgroep=stelselgroep
    )
    assert isinstance(
        geldige_stelselgroep, StelselgroepVersie
    ), f"Stelselgroepversie '{geldige_stelselgroep}' is geen instance van StelselgroepVersie"
