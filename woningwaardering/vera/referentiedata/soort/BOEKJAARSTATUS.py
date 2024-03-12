
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BOEKJAARSTATUS:

    gesloten = Referentiedata(
        code="GES",
        naam="Gesloten",
    )
    # gesloten = ("GES", "Gesloten")

    huidig = Referentiedata(
        code="HUD",
        naam="Huidig",
    )
    # huidig = ("HUD", "Huidig")

    open = Referentiedata(
        code="OPN",
        naam="Open",
    )
    # open = ("OPN", "Open")

    vorig = Referentiedata(
        code="VRG",
        naam="Vorig",
    )
    # vorig = ("VRG", "Vorig")
