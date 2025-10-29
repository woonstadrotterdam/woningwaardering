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
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.installatiesoort import (
    Installatiesoort,
)


def get_eenheid():
    eenheid = EenhedenEenheid()
    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten

    eenheid.ruimten = [
        EenhedenRuimte(
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.keuken,
            oppervlakte=20,
            gedeeldMetAantalEenheden=4,
            gedeeldMetAantalOnzelfstandigeWoonruimten=4,
            bouwkundige_elementen=[
                BouwkundigElementenBouwkundigElement(
                    detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                    lengte=3001,
                )
            ],
            installaties=[
                Installatiesoort.inbouw_oven_elektrisch,
                Installatiesoort.inbouw_magnetron,
                Installatiesoort.inbouw_koelkast,
            ],
            verwarmd=True,
        ),
        EenhedenRuimte(
            soort=Ruimtesoort.overige_ruimten,
            detailSoort=Ruimtedetailsoort.toiletruimte,
            oppervlakte=2,
            gedeeldMetAantalEenheden=4,
            gedeeldMetAantalOnzelfstandigeWoonruimten=4,
            installaties=[
                Installatiesoort.hangend_toilet,
                Installatiesoort.wastafel,
            ],
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
