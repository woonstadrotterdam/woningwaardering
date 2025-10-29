from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class SignaleringsoortReferentiedata(Referentiedata):
    pass


class Signaleringsoort(Referentiedatasoort):
    agressie = SignaleringsoortReferentiedata(
        code="AGR",
        naam="Agressie",
    )

    oneigenlijk_gebruik_woning = SignaleringsoortReferentiedata(
        code="ONE",
        naam="Oneigenlijk gebruik woning",
    )

    overlast = SignaleringsoortReferentiedata(
        code="OVE",
        naam="Overlast",
    )

    huurschuld = SignaleringsoortReferentiedata(
        code="SCH",
        naam="Huurschuld",
    )
