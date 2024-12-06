from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Boekjaarstatus(Referentiedatasoort):
    gesloten = Referentiedata(
        code="GES",
        naam="Gesloten",
    )

    huidig = Referentiedata(
        code="HUD",
        naam="Huidig",
    )

    open = Referentiedata(
        code="OPN",
        naam="Open",
    )

    vorig = Referentiedata(
        code="VRG",
        naam="Vorig",
    )
