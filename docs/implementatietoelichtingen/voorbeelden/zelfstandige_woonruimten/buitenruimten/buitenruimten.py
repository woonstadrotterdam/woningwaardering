import warnings

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Ruimtesoort,
    Ruimtedetailsoort,
)


def get_eenheid():
    eenheid = EenhedenEenheid()
    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten

    eenheid.ruimten = [
        EenhedenRuimte(
            soort=Ruimtesoort.buitenruimte,
            detail_soort=Ruimtedetailsoort.achtertuin,
            oppervlakte=50,
        ),
        EenhedenRuimte(
            soort=Ruimtesoort.buitenruimte,
            detail_soort=Ruimtedetailsoort.dakterras,
            oppervlakte=25,
            breedte=5,
            lengte=5,
            gedeeld_met_aantal_eenheden=2,
        ),
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
