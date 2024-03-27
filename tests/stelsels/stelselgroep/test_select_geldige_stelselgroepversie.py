from datetime import date
import pytest

from woningwaardering.stelsels.stelselgroep import (
    Stelselgroep,
    StelselgroepVersie,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


@pytest.mark.parametrize(
    "peildatum, stelsel, stelselgroep",
    [
        (
            date(2025, 1, 1),
            Woningwaarderingstelsel.zelfstandige_woonruimten,
            Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
        )
    ],
)
def test_select_geldige_stelselgroepversie(peildatum, stelsel, stelselgroep):
    geldige_stelselgroep = Stelselgroep.select_geldige_stelselgroepversie(
        peildatum=peildatum, stelsel=stelsel, stelselgroep=stelselgroep
    )
    assert isinstance(
        geldige_stelselgroep, StelselgroepVersie
    ), f"Stelselgroepversie '{geldige_stelselgroep}' is geen instance van StelselgroepVersie, {type(geldige_stelselgroep)}"
