import warnings

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_rapport
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Eenheidmonument,
    Woningwaarderingstelsel,
)


def get_eenheid():
    eenheid = EenhedenEenheid()

    # Geef aan dat het om een gemeentelijk monument gaat
    eenheid.monumenten = [Eenheidmonument.gemeentelijk_monument]

    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten

    return eenheid


def main():
    logger.enable("woningwaardering")
    warnings.filterwarnings("default")
    eenheid = get_eenheid()
    woningwaardering = Woningwaardering().waardeer(eenheid)
    print(naar_rapport(woningwaardering))


if __name__ == "__main__":
    main()
