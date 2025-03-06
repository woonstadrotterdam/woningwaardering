import warnings
from datetime import date

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
    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten

    eenheid.datum_afsluiten_huurovereenkomst = date(2024, 7, 1)

    eenheid.monumenten = [
        Eenheidmonument.rijksmonument
    ]

    return eenheid

def main():
    logger.enable("woningwaardering")
    warnings.filterwarnings("default")
    eenheid = get_eenheid()
    woningwaardering = Woningwaardering().waardeer(eenheid)
    print(naar_tabel(woningwaardering))

if __name__ == "__main__":
    main() 
