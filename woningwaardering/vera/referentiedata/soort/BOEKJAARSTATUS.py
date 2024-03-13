from woningwaardering.vera.bvg.models import Referentiedata


class BOEKJAARSTATUS:
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
