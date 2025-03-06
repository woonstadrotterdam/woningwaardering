import warnings
from datetime import date, datetime

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
    EenhedenPand,
    EenhedenRuimte,
    BouwkundigElementenBouwkundigElement,
    EenhedenWozEenheid
)
from woningwaardering.vera.referentiedata import (
    Energieprestatiesoort,
    Energieprestatiestatus,
    Energielabel,
    Pandsoort,
    Ruimtesoort,
    Ruimtedetailsoort,
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel

def get_eenheid():
    eenheid = EenhedenEenheid()

    eenheid.bouwjaar = 2024
    eenheid.begin_bouwdatum = date(2024, 6, 1)
    eenheid.in_exploitatiedatum = date(2024, 9, 1)

    eenheid.monumenten = []

    eenheid.energieprestaties = [EenhedenEnergieprestatie(
        soort=Energieprestatiesoort.primair_energieverbruik_woningbouw,
        status=Energieprestatiestatus.definitief,
        begindatum=date(2022, 2, 23),
        einddatum=date(2032, 2, 23),
        registratiedatum=datetime.fromisoformat("2022-02-23T09:55:37+01:00"),
        label=Energielabel.ap4,
    )]

    eenheid.ruimten = [
        EenhedenRuimte(
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.keuken,
            oppervlakte=10,
            bouwkundige_elementen=[
                BouwkundigElementenBouwkundigElement(
                    detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                    lengte=3000
                )
            ]
        )
    ]

    eenheid.panden = [
        EenhedenPand(
            soort=Pandsoort.eengezinswoning,
        )
    ]

    eenheid.woz_eenheden = [
        EenhedenWozEenheid(
            vastgestelde_waarde=270000,
            waardepeildatum=date(2024, 1, 1),
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