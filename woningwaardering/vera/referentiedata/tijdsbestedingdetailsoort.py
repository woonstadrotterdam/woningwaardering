from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.tijdsbestedingsoort import Tijdsbestedingsoort


class Tijdsbestedingdetailsoort(Enum):
    verlof_regulier = Referentiedata(
        code="VER",
        naam="Verlof (regulier)",
        parent=Tijdsbestedingsoort.afwezig.value,
    )
    """
    Regulier verlof
    """

    ziek = Referentiedata(
        code="ZIE",
        naam="Ziek",
        parent=Tijdsbestedingsoort.afwezig.value,
    )
    """
    Afwezig wegens ziekte
    """

    bijzonder_verlof = Referentiedata(
        code="BIJ",
        naam="Bijzonder verlof",
        parent=Tijdsbestedingsoort.afwezig.value,
    )
    """
    Bijzonder of  buitengewoon verlof. Denk bijvoorbeeld aan een examen, ondertrouw, een
    huwelijk en tandartsbezoek.
    """

    onbetaald_verlof = Referentiedata(
        code="ONB",
        naam="Onbetaald verlof",
        parent=Tijdsbestedingsoort.afwezig.value,
    )
    """
    Onbetaald verlof
    """

    zwangerschapsverlof = Referentiedata(
        code="ZWA",
        naam="Zwangerschapsverlof",
        parent=Tijdsbestedingsoort.afwezig.value,
    )
    """
    Zwangersschapsverlof of bevallingsverlof
    """

    ouderschapsverlof = Referentiedata(
        code="OUD",
        naam="Ouderschapsverlof",
        parent=Tijdsbestedingsoort.afwezig.value,
    )
    """
    Ouderschapsverlof
    """

    zorgverlof = Referentiedata(
        code="ZOR",
        naam="Zorgverlof",
        parent=Tijdsbestedingsoort.afwezig.value,
    )
    """
    Zorgverlof kortdurend of langdurend
    """

    calamiteitenverlof = Referentiedata(
        code="CAL",
        naam="Calamiteitenverlof",
        parent=Tijdsbestedingsoort.afwezig.value,
    )
    """
    Calamiteitenverlof of kort verzuimverlof
    """

    non_actief = Referentiedata(
        code="NON",
        naam="Non-actief",
        parent=Tijdsbestedingsoort.afwezig.value,
    )

    adoptieverlof = Referentiedata(
        code="ADO",
        naam="Adoptieverlof",
        parent=Tijdsbestedingsoort.afwezig.value,
    )
    """
    Adoptie of pleegzorgverlof
    """

    geschorst = Referentiedata(
        code="GES",
        naam="Geschorst",
        parent=Tijdsbestedingsoort.afwezig.value,
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
