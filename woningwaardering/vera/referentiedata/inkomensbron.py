from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InkomensbronReferentiedata(Referentiedata):
    pass


class Inkomensbron(Referentiedatasoort):
    anders = InkomensbronReferentiedata(
        code="AND",
        naam="Anders",
    )

    arbeid = InkomensbronReferentiedata(
        code="ARB",
        naam="Arbeid",
    )

    sociale_uitkering = InkomensbronReferentiedata(
        code="SOC",
        naam="Sociale uitkering",
    )

    studiefinanciering = InkomensbronReferentiedata(
        code="STU",
        naam="Studiefinanciering",
    )
