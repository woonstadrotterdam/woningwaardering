from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InspectierapportstatusReferentiedata(Referentiedata):
    pass


class Inspectierapportstatus(Referentiedatasoort):
    concept = InspectierapportstatusReferentiedata(
        code="CON",
        naam="Concept",
    )

    definitief = InspectierapportstatusReferentiedata(
        code="DEF",
        naam="Definitief",
    )

    getekend = InspectierapportstatusReferentiedata(
        code="GET",
        naam="Getekend",
    )

    ter_review = InspectierapportstatusReferentiedata(
        code="REV",
        naam="Ter review",
    )

    vervallen = InspectierapportstatusReferentiedata(
        code="VAL",
        naam="Vervallen",
    )
