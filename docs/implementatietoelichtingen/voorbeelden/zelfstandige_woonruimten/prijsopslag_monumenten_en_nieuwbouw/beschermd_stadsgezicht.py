import warnings

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Eenheidmonument
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel

def get_eenheid():
    eenheid = EenhedenEenheid()

    eenheid.bouwjaar = 1952

    eenheid.monumenten = [
        Eenheidmonument.rijksbeschermd_stadsgezicht
    ]

    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten

    return eenheid

def main():
    logger.enable("woningwaardering")
    warnings.filterwarnings("default")
    eenheid = get_eenheid()
    woningwaardering = Woningwaardering().waardeer(eenheid)
    print(naar_tabel(woningwaardering))

if __name__ == "__main__":
    main() 