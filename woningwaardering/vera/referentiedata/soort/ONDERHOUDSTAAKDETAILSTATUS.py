
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ONDERHOUDSTAAKDETAILSTATUS:

    klant_niet_aanwezig = Referentiedata(
        code="AFW",
        naam="Klant niet aanwezig",
    )
    # klant_niet_aanwezig = ("AFW", "Klant niet aanwezig")
    """
    De taak is onderbroken omdat de klant niet aanwezig is
    """

    niet_de_juiste_discipline = Referentiedata(
        code="DIS",
        naam="Niet de juiste discipline",
    )
    # niet_de_juiste_discipline = ("DIS", "Niet de juiste discipline")
    """
    De taak is onderbroken omdat de vakman niet de juiste discipline heeft
    """

    inspectie_of_beoordeling_vereist = Referentiedata(
        code="INS",
        naam="Inspectie/beoordeling vereist",
    )
    # inspectie_of_beoordeling_vereist = ("INS", "Inspectie/beoordeling vereist")
    """
    De taak is onderbroken omdat inspectie/beoordeling door inspecteur noodzakelijk is
    """

    materiaal_bestellen = Referentiedata(
        code="MAT",
        naam="Materiaal bestellen",
    )
    # materiaal_bestellen = ("MAT", "Materiaal bestellen")
    """
    De taak is onderbroken omdat materiaal besteld moet worden
    """

    offerte_benodigd = Referentiedata(
        code="OFF",
        naam="Offerte benodigd",
    )
    # offerte_benodigd = ("OFF", "Offerte benodigd")
    """
    De taak is onderbroken omdat een offerte nodig is
    """

    onvoldoende_tijd = Referentiedata(
        code="ONV",
        naam="Onvoldoende tijd",
    )
    # onvoldoende_tijd = ("ONV", "Onvoldoende tijd")
    """
    De taak is onderbroken omdat er onvoldoende tijd voor de vakman is
    """
