import warnings
from datetime import date, datetime

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenPand,
    EenhedenEnergieprestatie,
    EenhedenPrijscomponent,
)
from woningwaardering.vera.referentiedata import (
    Pandsoort,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Energielabel,
    Prijscomponentdetailsoort,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel


def get_eenheid():
    eenheid = EenhedenEenheid()

    eenheid.bouwjaar = 1921

    eenheid.panden = [EenhedenPand(soort=Pandsoort.meergezinswoning)]

    eenheid.energieprestaties = [
        EenhedenEnergieprestatie(
            soort=Energieprestatiesoort.energie_index,
            status=Energieprestatiestatus.definitief,
            begindatum=date(2017, 2, 23),
            einddatum=date(2027, 2, 23),
            registratiedatum=datetime.fromisoformat("2017-02-23T09:55:37+01:00"),
            label=Energielabel.c,
            waarde="1.48",
        )
    ]

    eenheid.monumenten = []

    eenheid.prijscomponenten = [
        EenhedenPrijscomponent(
            detail_soort=Prijscomponentdetailsoort.energieprestatievergoeding
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
