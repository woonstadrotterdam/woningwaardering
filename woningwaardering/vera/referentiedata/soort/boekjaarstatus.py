from vera.bvg.generated import Referentiedata


class Boekjaarstatus:
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
