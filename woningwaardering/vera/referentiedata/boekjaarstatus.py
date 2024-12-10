from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BoekjaarstatusReferentiedata(Referentiedata):
    pass


class Boekjaarstatus(Referentiedatasoort):
    gesloten = BoekjaarstatusReferentiedata(
        code="GES",
        naam="Gesloten",
    )

    huidig = BoekjaarstatusReferentiedata(
        code="HUD",
        naam="Huidig",
    )

    open = BoekjaarstatusReferentiedata(
        code="OPN",
        naam="Open",
    )

    vorig = BoekjaarstatusReferentiedata(
        code="VRG",
        naam="Vorig",
    )
