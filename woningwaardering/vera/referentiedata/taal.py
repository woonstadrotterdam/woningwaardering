from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class TaalReferentiedata(Referentiedata):
    pass


class Taal(Referentiedatasoort):
    duits = TaalReferentiedata(
        code="DUI",
        naam="Duits",
    )

    engels = TaalReferentiedata(
        code="ENG",
        naam="Engels",
    )

    frans = TaalReferentiedata(
        code="FRA",
        naam="Frans",
    )

    nederlands = TaalReferentiedata(
        code="NLD",
        naam="Nederlands",
    )

    spaans = TaalReferentiedata(
        code="SPA",
        naam="Spaans",
    )

    turks = TaalReferentiedata(
        code="TUR",
        naam="Turks",
    )
