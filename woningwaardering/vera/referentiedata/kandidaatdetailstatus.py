from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.kandidaatstatus import Kandidaatstatus
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Kandidaatdetailstatus(Referentiedatasoort):
    aanbieding = Referentiedata(
        code="AAN",
        naam="Aanbieding",
        parent=Kandidaatstatus.aangeboden,
    )
    """
    Kandidaat krijgt aanbieding.
    """

    bezichtiging = Referentiedata(
        code="BEZ",
        naam="Bezichtiging",
        parent=Kandidaatstatus.aangeboden,
    )
    """
    Kandidaat mag bezichtigen.
    """

    documentcontrole = Referentiedata(
        code="DOC",
        naam="Documentcontrole",
        parent=Kandidaatstatus.aangeboden,
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
        parent=Kandidaatstatus.geweigerd,
    )
    """
    Kandidaat heeft te laat of niet gereageerd.
    """

    ongeschikt = Referentiedata(
        code="ONG",
        naam="Ongeschikt",
        parent=Kandidaatstatus.afgewezen,
    )
    """
    Kandidaat niet geschikt voor omgeving.
    """

    gegevens_onjuist = Referentiedata(
        code="ONJ",
        naam="Gegevens onjuist",
        parent=Kandidaatstatus.afgewezen,
    )
    """
    Kandidaat komt niet in aanmerking na controle gegevens.
    """

    overeenkomst_getekend = Referentiedata(
        code="OVE",
        naam="Overeenkomst getekend",
        parent=Kandidaatstatus.aangeboden,
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
        parent=Kandidaatstatus.aangeboden,
    )
    """
    Kandidaat wordt gevraagd of deze nog steeds belangstelling heeft.
    """

    weigering_aanbieding = Referentiedata(
        code="WEI",
        naam="Weigering aanbieding",
        parent=Kandidaatstatus.geweigerd,
    )
    """
    Kandidaat weigert de aanbieding.
    """
