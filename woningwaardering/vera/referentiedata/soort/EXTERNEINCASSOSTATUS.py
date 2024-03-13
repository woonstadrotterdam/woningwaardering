from woningwaardering.vera.bvg.models import Referentiedata


class EXTERNEINCASSOSTATUS:
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
