from vera.referentiedata.models import Referentiedata


class Kandidaatdetailstatus:
    aanbieding = Referentiedata(
        code="AAN",
        naam="Aanbieding",
    )
    """
    Kandidaat krijgt aanbieding.
    """

    bezichtiging = Referentiedata(
        code="BEZ",
        naam="Bezichtiging",
    )
    """
    Kandidaat mag bezichtigen.
    """

    documentcontrole = Referentiedata(
        code="DOC",
        naam="Documentcontrole",
    )
    """
    Kandidaat moet documenten laten controleren.
    """

    geen_belangstelling_meer = Referentiedata(
        code="GEE",
        naam="Geen belangstelling meer",
    )
    """
    Kandidaat geeft aan geen belangstelling (meer) te hebben.
    """

    geinteresseerd = Referentiedata(
        code="INT",
        naam="Geïnteresseerd",
    )
    """
    Kandidaat is geïnteresseerd.
    """

    niet_gereageerd = Referentiedata(
        code="NRE",
        naam="Niet gereageerd",
    )
    """
    Kandidaat heeft te laat of niet gereageerd.
    """

    ongeschikt = Referentiedata(
        code="ONG",
        naam="Ongeschikt",
    )
    """
    Kandidaat niet geschikt voor omgeving.
    """

    gegevens_onjuist = Referentiedata(
        code="ONJ",
        naam="Gegevens onjuist",
    )
    """
    Kandidaat komt niet in aanmerking na controle gegevens.
    """

    overeenkomst_getekend = Referentiedata(
        code="OVE",
        naam="Overeenkomst getekend",
    )
    """
    Kandidaat heeft huur- of koopovereenkomst getekend.
    """

    geparkeerd = Referentiedata(
        code="PAR",
        naam="Geparkeerd",
    )
    """
    Kandidaat wil tijdelijk geen aanbiedingen ontvangen naar aanleiding van de reactie.
    """

    peilen_belangstelling = Referentiedata(
        code="PEI",
        naam="Peilen belangstelling",
    )
    """
    Kandidaat wordt gevraagd of deze nog steeds belangstelling heeft.
    """

    weigering_aanbieding = Referentiedata(
        code="WEI",
        naam="Weigering aanbieding",
    )
    """
    Kandidaat weigert de aanbieding.
    """
