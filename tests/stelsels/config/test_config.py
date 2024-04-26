import pytest
from pydantic import ValidationError

# from woningwaardering.stelsels.config.config import Stelselconfig
from woningwaardering.stelsels.config import Stelselconfig
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


@pytest.mark.parametrize("stelsel", [Woningwaarderingstelsel.zelfstandige_woonruimten])
def test_stelselconfig(stelsel: Woningwaarderingstelsel) -> None:
    """Deze functie valideert de Stelselsconfig.yml"""
    try:
        _ = Stelselconfig.load(stelsel=stelsel)
    except ValidationError as e:
        print(e, f"Stelsel {stelsel} heeft geen valide yml config")
        raise
