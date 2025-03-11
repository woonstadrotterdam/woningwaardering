from datetime import date, datetime
import warnings

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    EenhedenEnergieprestatie,
    EenhedenPand,
    EenhedenRuimte,
    EenhedenWozEenheid,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Energielabel,
    Pandsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
)


def get_eenheid():
    eenheid = EenhedenEenheid()
    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten

    eenheid.doelgroep = Doelgroep.zorg


    eenheid.woz_eenheden = [
        EenhedenWozEenheid(
            waardepeildatum=date(2023, 1, 1),
            vastgestelde_waarde=300000.0,
        )
    ]

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

    eenheid.ruimten = [
        EenhedenRuimte(
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.woonkamer_en_of_keuken,
            oppervlakte=60,
            bouwkundige_elementen=[
                BouwkundigElementenBouwkundigElement(
                    detail_soort=Bouwkundigelementdetailsoort.aanrecht, lengte=2150
                )
            ],
        ),
    ]

    eenheid.panden = [
        EenhedenPand(
            soort=Pandsoort.eengezinswoning,
        )
    ]

    eenheid.monumenten = []

    eenheid.bouwjaar = 1975

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
