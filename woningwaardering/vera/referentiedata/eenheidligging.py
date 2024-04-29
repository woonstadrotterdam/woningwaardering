from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidligging(Enum):
    buiten_bebouwde_kom = Referentiedata(
        code="BBK",
        naam="Buiten bebouwde kom",
    )

    beschutte_ligging = Referentiedata(
        code="BES",
        naam="Beschutte ligging",
    )

    in_bosrijke_omgeving = Referentiedata(
        code="BOS",
        naam="In bosrijke omgeving",
    )

    aan_bosrand = Referentiedata(
        code="BRA",
        naam="Aan bosrand",
    )

    in_centrum = Referentiedata(
        code="CEN",
        naam="In centrum",
    )

    aan_drukke_weg = Referentiedata(
        code="DRU",
        naam="Aan drukke weg",
    )

    landelijk_gelegen = Referentiedata(
        code="LAN",
        naam="Landelijk gelegen",
    )

    open_ligging = Referentiedata(
        code="OPE",
        naam="Open ligging",
    )

    aan_park = Referentiedata(
        code="PAR",
        naam="Aan park",
    )

    aan_rustige_weg = Referentiedata(
        code="RUS",
        naam="Aan rustige weg",
    )

    aan_vaarwater = Referentiedata(
        code="VAA",
        naam="Aan vaarwater",
    )

    vrij_uitzicht = Referentiedata(
        code="VRI",
        naam="Vrij uitzicht",
    )

    aan_water = Referentiedata(
        code="WAT",
        naam="Aan water",
    )

    in_woonwijk = Referentiedata(
        code="WOO",
        naam="In woonwijk",
    )

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
