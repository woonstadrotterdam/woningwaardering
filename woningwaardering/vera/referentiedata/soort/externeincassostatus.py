from vera.bvg.generated import Referentiedata


class Externeincassostatus:
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
