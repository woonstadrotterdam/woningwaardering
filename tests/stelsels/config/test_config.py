import pytest
from pydantic import ValidationError

# from woningwaardering.stelsels.config.config import Stelselconfig
from woningwaardering.stelsels.config import Stelselconfig
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


@pytest.mark.parametrize("stelsel", [Woningwaarderingstelsel.zelfstandige_woonruimten])
def test_stelselconfig(stelsel: Woningwaarderingstelsel) -> None:
    """This function valdiates the Stelselsconfig.yml"""
    try:
        _ = Stelselconfig.load(stelsel=stelsel)
    except ValidationError as e:
        print(e, f"Stelsel {stelsel} does not have a valid yml config")
        raise
