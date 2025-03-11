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
            soort=Ruimtesoort.parkeergelegenheid,
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
            soort=Ruimtesoort.parkeergelegenheid,
            detail_soort=Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt,
            oppervlakte=12,
            breedte=3,
            lengte=4,
            aantal=2,
            gedeeld_met_aantal_eenheden=10,
        ),
    ]

    print(
        eenheid.model_dump_json(
            indent=2,
            exclude_none=True,
            by_alias=True,
            exclude_defaults=True,
        )
    )

    return eenheid


def main():
    logger.enable("woningwaardering")
    warnings.filterwarnings("default")
    eenheid = get_eenheid()
    woningwaardering = Woningwaardering().waardeer(eenheid)
    print(naar_tabel(woningwaardering))


if __name__ == "__main__":
    main()
