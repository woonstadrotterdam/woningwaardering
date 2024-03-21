from pydantic import ValidationError

from woningwaardering.stelsels.config.stelselsconfig import Stelselsconfig


def test_stelselconfig() -> None:
    """
    This function valdiates the Stelselsconfig.yml
    """
    try:
        _ = Stelselsconfig.load()
    except ValidationError as e:
        print(e)
        raise
