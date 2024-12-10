from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class SignaleringstatusReferentiedata(Referentiedata):
    pass


class Signaleringstatus(Referentiedatasoort):
    actief = SignaleringstatusReferentiedata(
        code="ACT",
        naam="Actief",
    )

    passief = SignaleringstatusReferentiedata(
        code="PAS",
        naam="Passief",
    )

    vervallen = SignaleringstatusReferentiedata(
        code="VER",
        naam="Vervallen",
    )
