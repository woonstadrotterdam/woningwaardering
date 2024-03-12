
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class KANDIDAATDETAILSTATUS:

    aanbieding = Referentiedata(
        code="AAN",
        naam="Aanbieding",
    )
    # aanbieding = ("AAN", "Aanbieding")
    """
    Kandidaat krijgt aanbieding.
    """

    bezichtiging = Referentiedata(
        code="BEZ",
        naam="Bezichtiging",
    )
    # bezichtiging = ("BEZ", "Bezichtiging")
    """
    Kandidaat mag bezichtigen.
    """

    documentcontrole = Referentiedata(
        code="DOC",
        naam="Documentcontrole",
    )
    # documentcontrole = ("DOC", "Documentcontrole")
    """
    Kandidaat moet documenten laten controleren.
    """

    geen_belangstelling_meer = Referentiedata(
        code="GEE",
        naam="Geen belangstelling meer",
    )
    # geen_belangstelling_meer = ("GEE", "Geen belangstelling meer")
    """
    Kandidaat geeft aan geen belangstelling (meer) te hebben.
    """

    geinteresseerd = Referentiedata(
        code="INT",
        naam="Geïnteresseerd",
    )
    # geinteresseerd = ("INT", "Geïnteresseerd")
    """
    Kandidaat is geïnteresseerd.
    """

    niet_gereageerd = Referentiedata(
        code="NRE",
        naam="Niet gereageerd",
    )
    # niet_gereageerd = ("NRE", "Niet gereageerd")
    """
    Kandidaat heeft te laat of niet gereageerd.
    """

    ongeschikt = Referentiedata(
        code="ONG",
        naam="Ongeschikt",
    )
    # ongeschikt = ("ONG", "Ongeschikt")
    """
    Kandidaat niet geschikt voor omgeving.
    """

    gegevens_onjuist = Referentiedata(
        code="ONJ",
        naam="Gegevens onjuist",
    )
    # gegevens_onjuist = ("ONJ", "Gegevens onjuist")
    """
    Kandidaat komt niet in aanmerking na controle gegevens.
    """

    overeenkomst_getekend = Referentiedata(
        code="OVE",
        naam="Overeenkomst getekend",
    )
    # overeenkomst_getekend = ("OVE", "Overeenkomst getekend")
    """
    Kandidaat heeft huur- of koopovereenkomst getekend.
    """

    geparkeerd = Referentiedata(
        code="PAR",
        naam="Geparkeerd",
    )
    # geparkeerd = ("PAR", "Geparkeerd")
    """
    Kandidaat wil tijdelijk geen aanbiedingen ontvangen naar aanleiding van de reactie.
    """

    peilen_belangstelling = Referentiedata(
        code="PEI",
        naam="Peilen belangstelling",
    )
    # peilen_belangstelling = ("PEI", "Peilen belangstelling")
    """
    Kandidaat wordt gevraagd of deze nog steeds belangstelling heeft.
    """

    weigering_aanbieding = Referentiedata(
        code="WEI",
        naam="Weigering aanbieding",
    )
    # weigering_aanbieding = ("WEI", "Weigering aanbieding")
    """
    Kandidaat weigert de aanbieding.
    """
