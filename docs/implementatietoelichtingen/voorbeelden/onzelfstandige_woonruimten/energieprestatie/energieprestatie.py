import warnings
from datetime import date, datetime

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    EenhedenEnergieprestatie,
)
from woningwaardering.vera.referentiedata import (
    Ruimtesoort,
    Ruimtedetailsoort,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Energielabel,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel


def get_eenheid():
    eenheid = EenhedenEenheid()
    eenheid.bouwjaar = 1921
    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten

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

    eenheid.ruimten = [
        EenhedenRuimte(
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.slaapkamer,
            oppervlakte=10.0,
            gedeeld_met_aantal_onzelfstandige_woonruimten=5,
        ),
        EenhedenRuimte(
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.woonkamer,
            oppervlakte=10.0,
            gedeeld_met_aantal_onzelfstandige_woonruimten=6,
        ),
    ]

    return eenheid


def main():
    warnings.filterwarnings("ignore")
    eenheid = get_eenheid()
    woningwaardering = Woningwaardering().waardeer(eenheid)
    print(naar_tabel(woningwaardering))


if __name__ == "__main__":
    main()
