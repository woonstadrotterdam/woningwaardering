from woningwaardering.vera.bvg.generated import Referentiedata


class Onderhoudstaakdetailstatus:
    klant_niet_aanwezig = Referentiedata(
        code="AFW",
        naam="Klant niet aanwezig",
    )
    """
    De taak is onderbroken omdat de klant niet aanwezig is
    """

    niet_de_juiste_discipline = Referentiedata(
        code="DIS",
        naam="Niet de juiste discipline",
    )
    """
    De taak is onderbroken omdat de vakman niet de juiste discipline heeft
    """

    inspectie_en_of_beoordeling_vereist = Referentiedata(
        code="INS",
        naam="Inspectie/beoordeling vereist",
    )
    """
    De taak is onderbroken omdat inspectie/beoordeling door inspecteur noodzakelijk is
    """

    materiaal_bestellen = Referentiedata(
        code="MAT",
        naam="Materiaal bestellen",
    )
    """
    De taak is onderbroken omdat materiaal besteld moet worden
    """

    offerte_benodigd = Referentiedata(
        code="OFF",
        naam="Offerte benodigd",
    )
    """
    De taak is onderbroken omdat een offerte nodig is
    """

    onvoldoende_tijd = Referentiedata(
        code="ONV",
        naam="Onvoldoende tijd",
    )
    """
    De taak is onderbroken omdat er onvoldoende tijd voor de vakman is
    """
