from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidliggingReferentiedata(Referentiedata):
    pass


class Eenheidligging(Referentiedatasoort):
    buiten_bebouwde_kom = EenheidliggingReferentiedata(
        code="BBK",
        naam="Buiten bebouwde kom",
    )

    beschutte_ligging = EenheidliggingReferentiedata(
        code="BES",
        naam="Beschutte ligging",
    )

    in_bosrijke_omgeving = EenheidliggingReferentiedata(
        code="BOS",
        naam="In bosrijke omgeving",
    )

    aan_bosrand = EenheidliggingReferentiedata(
        code="BRA",
        naam="Aan bosrand",
    )

    in_centrum = EenheidliggingReferentiedata(
        code="CEN",
        naam="In centrum",
    )

    aan_drukke_weg = EenheidliggingReferentiedata(
        code="DRU",
        naam="Aan drukke weg",
    )

    landelijk_gelegen = EenheidliggingReferentiedata(
        code="LAN",
        naam="Landelijk gelegen",
    )

    open_ligging = EenheidliggingReferentiedata(
        code="OPE",
        naam="Open ligging",
    )

    aan_park = EenheidliggingReferentiedata(
        code="PAR",
        naam="Aan park",
    )

    aan_rustige_weg = EenheidliggingReferentiedata(
        code="RUS",
        naam="Aan rustige weg",
    )

    aan_vaarwater = EenheidliggingReferentiedata(
        code="VAA",
        naam="Aan vaarwater",
    )

    vrij_uitzicht = EenheidliggingReferentiedata(
        code="VRI",
        naam="Vrij uitzicht",
    )

    aan_water = EenheidliggingReferentiedata(
        code="WAT",
        naam="Aan water",
    )

    in_woonwijk = EenheidliggingReferentiedata(
        code="WOO",
        naam="In woonwijk",
    )
