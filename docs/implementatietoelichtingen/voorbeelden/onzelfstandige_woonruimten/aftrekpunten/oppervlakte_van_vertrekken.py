import warnings

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_rapport
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
)


def get_eenheid():
    eenheid = EenhedenEenheid()
    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten

    eenheid.ruimten = [
        EenhedenRuimte(
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.woonkamer,
            oppervlakte=6,
            gedeeldMetAantalOnzelfstandigeWoonruimten=2,
        )
    ]

    return eenheid


def main():
    logger.enable("woningwaardering")
    warnings.filterwarnings("default")
    eenheid = get_eenheid()
    woningwaardering = Woningwaardering().waardeer(eenheid)
    print(naar_rapport(woningwaardering))


if __name__ == "__main__":
    main()
