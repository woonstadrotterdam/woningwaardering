from pydantic import ValidationError

from woningwaardering.stelsels.config.stelselsconfig import StelselsConfig


def test_stelselconfig() -> None:
    """
    This function valdiates the Stelselsconfig.yml
    """
    try:
        _ = StelselsConfig.load()
    except ValidationError as e:
        print(e)
        raise
