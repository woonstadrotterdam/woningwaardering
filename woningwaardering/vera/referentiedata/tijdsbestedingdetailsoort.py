from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.tijdsbestedingsoort import (
    Tijdsbestedingsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class TijdsbestedingdetailsoortReferentiedata(Referentiedata):
    pass


class Tijdsbestedingdetailsoort(Referentiedatasoort):
    verlof_regulier = TijdsbestedingdetailsoortReferentiedata(
        code="VER",
        naam="Verlof (regulier)",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Regulier verlof
    """

    ziek = TijdsbestedingdetailsoortReferentiedata(
        code="ZIE",
        naam="Ziek",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Afwezig wegens ziekte
    """

    bijzonder_verlof = TijdsbestedingdetailsoortReferentiedata(
        code="BIJ",
        naam="Bijzonder verlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Bijzonder of  buitengewoon verlof. Denk bijvoorbeeld aan een examen, ondertrouw, een
    huwelijk en tandartsbezoek.
    """

    onbetaald_verlof = TijdsbestedingdetailsoortReferentiedata(
        code="ONB",
        naam="Onbetaald verlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Onbetaald verlof
    """

    zwangerschapsverlof = TijdsbestedingdetailsoortReferentiedata(
        code="ZWA",
        naam="Zwangerschapsverlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Zwangersschapsverlof of bevallingsverlof
    """

    ouderschapsverlof = TijdsbestedingdetailsoortReferentiedata(
        code="OUD",
        naam="Ouderschapsverlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Ouderschapsverlof
    """

    zorgverlof = TijdsbestedingdetailsoortReferentiedata(
        code="ZOR",
        naam="Zorgverlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Zorgverlof kortdurend of langdurend
    """

    calamiteitenverlof = TijdsbestedingdetailsoortReferentiedata(
        code="CAL",
        naam="Calamiteitenverlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Calamiteitenverlof of kort verzuimverlof
    """

    non_actief = TijdsbestedingdetailsoortReferentiedata(
        code="NON",
        naam="Non-actief",
        parent=Tijdsbestedingsoort.afwezig,
    )

    adoptieverlof = TijdsbestedingdetailsoortReferentiedata(
        code="ADO",
        naam="Adoptieverlof",
        parent=Tijdsbestedingsoort.afwezig,
    )
    """
    Adoptie of pleegzorgverlof
    """

    geschorst = TijdsbestedingdetailsoortReferentiedata(
        code="GES",
        naam="Geschorst",
        parent=Tijdsbestedingsoort.afwezig,
    )
