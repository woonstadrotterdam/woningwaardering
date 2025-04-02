import warnings

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    BouwkundigElementenBouwkundigElement,
)
from woningwaardering.vera.referentiedata import (
    Ruimtesoort,
    Ruimtedetailsoort,
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel


def get_eenheid():
    eenheid = EenhedenEenheid()

    eenheid.ruimten = [
        EenhedenRuimte(
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.keuken,
            oppervlakte=10,
            bouwkundige_elementen=[
                BouwkundigElementenBouwkundigElement(
                    detail_soort=Bouwkundigelementdetailsoort.aanrecht, lengte=3150
                )
            ],
        )   
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
