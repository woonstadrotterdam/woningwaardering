from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.kandidaatstatus import (
    Kandidaatstatus,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class KandidaatdetailstatusReferentiedata(Referentiedata):
    pass


class Kandidaatdetailstatus(Referentiedatasoort):
    aanbieding = KandidaatdetailstatusReferentiedata(
        code="AAN",
        naam="Aanbieding",
        parent=Kandidaatstatus.aangeboden,
    )
    """
    Kandidaat krijgt aanbieding.
    """

    bezichtiging = KandidaatdetailstatusReferentiedata(
        code="BEZ",
        naam="Bezichtiging",
        parent=Kandidaatstatus.aangeboden,
    )
    """
    Kandidaat mag bezichtigen.
    """

    documentcontrole = KandidaatdetailstatusReferentiedata(
        code="DOC",
        naam="Documentcontrole",
        parent=Kandidaatstatus.aangeboden,
    )
    """
    Kandidaat moet documenten laten controleren.
    """

    geen_belangstelling_meer = KandidaatdetailstatusReferentiedata(
        code="GEE",
        naam="Geen belangstelling meer",
    )
    """
    Kandidaat geeft aan geen belangstelling (meer) te hebben.
    """

    geinteresseerd = KandidaatdetailstatusReferentiedata(
        code="INT",
        naam="Geïnteresseerd",
    )
    """
    Kandidaat is geïnteresseerd.
    """

    niet_gereageerd = KandidaatdetailstatusReferentiedata(
        code="NRE",
        naam="Niet gereageerd",
        parent=Kandidaatstatus.geweigerd,
    )
    """
    Kandidaat heeft te laat of niet gereageerd.
    """

    ongeschikt = KandidaatdetailstatusReferentiedata(
        code="ONG",
        naam="Ongeschikt",
        parent=Kandidaatstatus.afgewezen,
    )
    """
    Kandidaat niet geschikt voor omgeving.
    """

    gegevens_onjuist = KandidaatdetailstatusReferentiedata(
        code="ONJ",
        naam="Gegevens onjuist",
        parent=Kandidaatstatus.afgewezen,
    )
    """
    Kandidaat komt niet in aanmerking na controle gegevens.
    """

    overeenkomst_getekend = KandidaatdetailstatusReferentiedata(
        code="OVE",
        naam="Overeenkomst getekend",
        parent=Kandidaatstatus.aangeboden,
    )
    """
    Kandidaat heeft huur- of koopovereenkomst getekend.
    """

    geparkeerd = KandidaatdetailstatusReferentiedata(
        code="PAR",
        naam="Geparkeerd",
    )
    """
    Kandidaat wil tijdelijk geen aanbiedingen ontvangen naar aanleiding van de reactie.
    """

    peilen_belangstelling = KandidaatdetailstatusReferentiedata(
        code="PEI",
        naam="Peilen belangstelling",
        parent=Kandidaatstatus.aangeboden,
    )
    """
    Kandidaat wordt gevraagd of deze nog steeds belangstelling heeft.
    """

    weigering_aanbieding = KandidaatdetailstatusReferentiedata(
        code="WEI",
        naam="Weigering aanbieding",
        parent=Kandidaatstatus.geweigerd,
    )
    """
    Kandidaat weigert de aanbieding.
    """
