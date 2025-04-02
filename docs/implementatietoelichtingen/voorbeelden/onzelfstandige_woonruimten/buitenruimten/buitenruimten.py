import warnings

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
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
            soort=Ruimtesoort.buitenruimte,
            detail_soort=Ruimtedetailsoort.achtertuin,
            oppervlakte=1,
            breedte=0.5,
            lengte=2,
        ),
        EenhedenRuimte(
            soort=Ruimtesoort.buitenruimte,
            detail_soort=Ruimtedetailsoort.balkon,
            oppervlakte=4.5,
            breedte=1.5,
            lengte=3,
            gedeeld_met_aantal_onzelfstandige_woonruimten=4,
        ),
        EenhedenRuimte(
            soort=Ruimtesoort.buitenruimte,
            detail_soort=Ruimtedetailsoort.dakterras,
            oppervlakte=52,
            breedte=6.5,
            lengte=8,
            gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            gedeeld_met_aantal_eenheden=5,
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
