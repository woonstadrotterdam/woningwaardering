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
    Bouwkundigelementsoort,
    Bouwkundigelementdetailsoort,
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
            detail_soort=Ruimtedetailsoort.carport,
            oppervlakte=12,
            breedte=3,
            lengte=4,
            aantal=5,
            gedeeld_met_aantal_eenheden=10,
            bouwkundige_elementen=[
                BouwkundigElementenBouwkundigElement(
                    soort=Bouwkundigelementsoort.voorziening,
                    detail_soort=Bouwkundigelementdetailsoort.laadpaal,
                )
            ],
        ),
        EenhedenRuimte(
            soort=Ruimtesoort.gemeenschappelijke_ruimten_en_voorzieningen,
            detail_soort=Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
            oppervlakte=12,
            breedte=3,
            lengte=4,
            aantal=2,
            gedeeld_met_aantal_eenheden=10,
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
