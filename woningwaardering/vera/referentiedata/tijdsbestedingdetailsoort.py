from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.tijdsbestedingsoort import Tijdsbestedingsoort
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Tijdsbestedingdetailsoort(Referentiedatasoort):
    verlof_regulier = Referentiedata(
        code="VER",
        naam="Verlof (regulier)",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Regulier verlof
    """

    ziek = Referentiedata(
        code="ZIE",
        naam="Ziek",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Afwezig wegens ziekte
    """

    bijzonder_verlof = Referentiedata(
        code="BIJ",
        naam="Bijzonder verlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Bijzonder of  buitengewoon verlof. Denk bijvoorbeeld aan een examen, ondertrouw, een
    huwelijk en tandartsbezoek.
    """

    onbetaald_verlof = Referentiedata(
        code="ONB",
        naam="Onbetaald verlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Onbetaald verlof
    """

    zwangerschapsverlof = Referentiedata(
        code="ZWA",
        naam="Zwangerschapsverlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Zwangersschapsverlof of bevallingsverlof
    """

    ouderschapsverlof = Referentiedata(
        code="OUD",
        naam="Ouderschapsverlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Ouderschapsverlof
    """

    zorgverlof = Referentiedata(
        code="ZOR",
        naam="Zorgverlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Zorgverlof kortdurend of langdurend
    """

    calamiteitenverlof = Referentiedata(
        code="CAL",
        naam="Calamiteitenverlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Calamiteitenverlof of kort verzuimverlof
    """

    non_actief = Referentiedata(
        code="NON",
        naam="Non-actief",
        parent=Tijdsbestedingsoort.afwezig,
    )

    adoptieverlof = Referentiedata(
        code="ADO",
        naam="Adoptieverlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Adoptie of pleegzorgverlof
    """

    geschorst = Referentiedata(
        code="GES",
        naam="Geschorst",
        parent=Tijdsbestedingsoort.afwezig,
    )
