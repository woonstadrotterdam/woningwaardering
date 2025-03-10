import warnings
from datetime import date, datetime

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Ruimtesoort,
    Ruimtedetailsoort,
    Installatiesoort,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel


def get_eenheid():
    eenheid = EenhedenEenheid()

    eenheid.ruimten = [
        EenhedenRuimte(
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.badkamer,
            oppervlakte=10,
            installaties=[
                Installatiesoort.bad,
                Installatiesoort.douche,
                Installatiesoort.hangend_toilet,
            ],
        )
    ]

    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten

    print(
        eenheid.model_dump_json(
            indent=2, exclude_none=True, by_alias=True, exclude_defaults=True
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
