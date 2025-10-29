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
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
)


def get_eenheid():
    eenheid = EenhedenEenheid()

    eenheid.ruimten = [
        EenhedenRuimte(
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.keuken,
            oppervlakte=10,
            bouwkundige_elementen=[
                BouwkundigElementenBouwkundigElement(
                    detail_soort=Bouwkundigelementdetailsoort.aanrecht, lengte=3000
                )
            ],
            installaties=[
                Installatiesoort.eenhandsmengkraan,
                Installatiesoort.inbouw_kookplaat_inductie,
                Installatiesoort.inbouw_koelkast,
                Installatiesoort.inbouw_vaatwasmachine,
            ],
        )
    ]

    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten

    return eenheid


def main():
    logger.enable("woningwaardering")
    warnings.filterwarnings("default")
    eenheid = get_eenheid()
    woningwaardering = Woningwaardering().waardeer(eenheid)
    print(naar_tabel(woningwaardering))


if __name__ == "__main__":
    main()
