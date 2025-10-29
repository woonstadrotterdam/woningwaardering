from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ExterneincassostatusReferentiedata(Referentiedata):
    pass


class Externeincassostatus(Referentiedatasoort):
    actief = ExterneincassostatusReferentiedata(
        code="ACT",
        naam="Actief",
    )

    beeindigd = ExterneincassostatusReferentiedata(
        code="EIN",
        naam="Beëindigd",
    )

    nieuw = ExterneincassostatusReferentiedata(
        code="NIE",
        naam="Nieuw",
    )
