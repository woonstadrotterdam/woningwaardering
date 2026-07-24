import warnings

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_rapport
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Doelgroep,
    Woningwaarderingstelsel,
)


def get_eenheid():
    eenheid = EenhedenEenheid()
    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten

    eenheid.doelgroep = Doelgroep.zorg

    return eenheid


def main():
    logger.enable("woningwaardering")
    warnings.filterwarnings("default")
    eenheid = get_eenheid()
    woningwaardering = Woningwaardering().waardeer(eenheid)
    print(naar_rapport(woningwaardering))


if __name__ == "__main__":
    main()
