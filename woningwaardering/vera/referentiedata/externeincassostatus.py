from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Externeincassostatus(Referentiedatasoort):
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )

    beeindigd = Referentiedata(
        code="EIN",
        naam="Beëindigd",
    )

    nieuw = Referentiedata(
        code="NIE",
        naam="Nieuw",
    )
