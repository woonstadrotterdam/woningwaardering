from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Tijdsbestedingdetailsoort(Enum):
    verlof_regulier = Referentiedata(
        code="VER",
        naam="Verlof (regulier)",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )
    """
    Regulier verlof
    """

    ziek = Referentiedata(
        code="ZIE",
        naam="Ziek",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )
    """
    Afwezig wegens ziekte
    """

    bijzonder_verlof = Referentiedata(
        code="BIJ",
        naam="Bijzonder verlof",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )
    """
    Bijzonder of  buitengewoon verlof. Denk bijvoorbeeld aan een examen, ondertrouw, een
    huwelijk en tandartsbezoek.
    """

    onbetaald_verlof = Referentiedata(
        code="ONB",
        naam="Onbetaald verlof",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )
    """
    Onbetaald verlof
    """

    zwangerschapsverlof = Referentiedata(
        code="ZWA",
        naam="Zwangerschapsverlof",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )
    """
    Zwangersschapsverlof of bevallingsverlof
    """

    ouderschapsverlof = Referentiedata(
        code="OUD",
        naam="Ouderschapsverlof",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )
    """
    Ouderschapsverlof
    """

    zorgverlof = Referentiedata(
        code="ZOR",
        naam="Zorgverlof",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )
    """
    Zorgverlof kortdurend of langdurend
    """

    calamiteitenverlof = Referentiedata(
        code="CAL",
        naam="Calamiteitenverlof",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )
    """
    Calamiteitenverlof of kort verzuimverlof
    """

    non_actief = Referentiedata(
        code="NON",
        naam="Non-actief",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )

    adoptieverlof = Referentiedata(
        code="ADO",
        naam="Adoptieverlof",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )
    """
    Adoptie of pleegzorgverlof
    """

    geschorst = Referentiedata(
        code="GES",
        naam="Geschorst",
        parent=Referentiedata(
            code="AFW",
            naam="Afwezig",
        ),
    )

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
