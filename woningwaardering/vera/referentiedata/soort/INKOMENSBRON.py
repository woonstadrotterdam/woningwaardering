from woningwaardering.vera.bvg.models import Referentiedata


class INKOMENSBRON:
    anders = Referentiedata(
        code="AND",
        naam="Anders",
    )

    arbeid = Referentiedata(
        code="ARB",
        naam="Arbeid",
    )

    sociale_uitkering = Referentiedata(
        code="SOC",
        naam="Sociale uitkering",
    )

    studiefinanciering = Referentiedata(
        code="STU",
        naam="Studiefinanciering",
    )
