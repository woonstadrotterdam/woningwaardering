from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Taal(Referentiedatasoort):
    duits = Referentiedata(
        code="DUI",
        naam="Duits",
    )

    engels = Referentiedata(
        code="ENG",
        naam="Engels",
    )

    frans = Referentiedata(
        code="FRA",
        naam="Frans",
    )

    nederlands = Referentiedata(
        code="NLD",
        naam="Nederlands",
    )

    spaans = Referentiedata(
        code="SPA",
        naam="Spaans",
    )

    turks = Referentiedata(
        code="TUR",
        naam="Turks",
    )
