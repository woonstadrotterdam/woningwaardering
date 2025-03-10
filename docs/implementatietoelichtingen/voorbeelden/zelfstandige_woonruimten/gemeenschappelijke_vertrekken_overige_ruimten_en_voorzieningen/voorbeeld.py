import warnings

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    Woningwaarderingstelsel,
    Ruimtesoort,
    Ruimtedetailsoort,
)


def get_eenheid():
    eenheid = EenhedenEenheid()
    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
    eenheid.ruimten = [
        EenhedenRuimte(
            naam="Ruimte A",
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.keuken,
            oppervlakte=20,
            gedeeld_met_aantal_eenheden=4,
            verwarmd=True,
            bouwkundige_elementen=[
                BouwkundigElementenBouwkundigElement(
                    detail_soort=Bouwkundigelementdetailsoort.aanrecht, lengte=3150
                )
            ],
            installaties=[
                Installatiesoort.inbouw_kookplaat_inductie,
                Installatiesoort.eenhandsmengkraan,
                Installatiesoort.inbouw_koelkast,
            ]
        ),
        EenhedenRuimte(
            naam="Ruimte B",
            soort=Ruimtesoort.overige_ruimten,
            detail_soort=Ruimtedetailsoort.toiletruimte,
            oppervlakte=2,
            gedeeld_met_aantal_eenheden=4,
            verwarmd=False,
            installaties=[
                Installatiesoort.hangend_toilet,
                Installatiesoort.wastafel,
            ]
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
