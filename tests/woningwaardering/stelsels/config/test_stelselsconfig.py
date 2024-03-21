import pytest
from pydantic import ValidationError

from woningwaardering.stelsels import Config


@pytest.mark.parametrize("stelsel", ["zelfstandig"])
def test_stelselconfig(stelsel: str) -> None:
    """
    This function valdiates the Stelselsconfig.yml
    """
    try:
        _ = Config.load(stelsel=stelsel)
    except ValidationError as e:
        print(e, f"Stelsel {stelsel} does not have a valid yml config")
        raise
