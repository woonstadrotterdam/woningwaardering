from woningwaardering.vera.bvg.generated import Referentiedata


class Inkomensbron:
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
