from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PrijsaanpassingsoortReferentiedata(Referentiedata):
    pass


class Prijsaanpassingsoort(Referentiedatasoort):
    korting = PrijsaanpassingsoortReferentiedata(
        code="KOR",
        naam="Korting",
    )

    toeslag = PrijsaanpassingsoortReferentiedata(
        code="TOE",
        naam="Toeslag",
    )
