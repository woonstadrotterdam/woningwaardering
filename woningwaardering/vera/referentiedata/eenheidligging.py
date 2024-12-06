from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Eenheidligging(Referentiedatasoort):
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
