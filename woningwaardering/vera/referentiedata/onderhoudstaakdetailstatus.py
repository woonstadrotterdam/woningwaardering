from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.onderhoudstaakstatus import (
    Onderhoudstaakstatus,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OnderhoudstaakdetailstatusReferentiedata(Referentiedata):
    pass


class Onderhoudstaakdetailstatus(Referentiedatasoort):
    klant_niet_aanwezig = OnderhoudstaakdetailstatusReferentiedata(
        code="AFW",
        naam="Klant niet aanwezig",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat de klant niet aanwezig is
    """

    niet_de_juiste_discipline = OnderhoudstaakdetailstatusReferentiedata(
        code="DIS",
        naam="Niet de juiste discipline",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat de vakman niet de juiste discipline heeft
    """

    inspectie_en_of_beoordeling_vereist = OnderhoudstaakdetailstatusReferentiedata(
        code="INS",
        naam="Inspectie/beoordeling vereist",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat inspectie/beoordeling door inspecteur noodzakelijk is
    """

    materiaal_bestellen = OnderhoudstaakdetailstatusReferentiedata(
        code="MAT",
        naam="Materiaal bestellen",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat materiaal besteld moet worden
    """

    offerte_benodigd = OnderhoudstaakdetailstatusReferentiedata(
        code="OFF",
        naam="Offerte benodigd",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat een offerte nodig is
    """

    onvoldoende_tijd = OnderhoudstaakdetailstatusReferentiedata(
        code="ONV",
        naam="Onvoldoende tijd",
        parent=Onderhoudstaakstatus.onderbroken,
    )
    """
    De taak is onderbroken omdat er onvoldoende tijd voor de vakman is
    """
