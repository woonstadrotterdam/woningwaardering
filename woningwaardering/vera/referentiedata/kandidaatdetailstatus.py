from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.kandidaatstatus import Kandidaatstatus


class Kandidaatdetailstatus(Enum):
    aanbieding = Referentiedata(
        code="AAN",
        naam="Aanbieding",
        parent=Kandidaatstatus.aangeboden.value,
    )
    """
    Kandidaat krijgt aanbieding.
    """

    bezichtiging = Referentiedata(
        code="BEZ",
        naam="Bezichtiging",
        parent=Kandidaatstatus.aangeboden.value,
    )
    """
    Kandidaat mag bezichtigen.
    """

    documentcontrole = Referentiedata(
        code="DOC",
        naam="Documentcontrole",
        parent=Kandidaatstatus.aangeboden.value,
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
        parent=Kandidaatstatus.geweigerd.value,
    )
    """
    Kandidaat heeft te laat of niet gereageerd.
    """

    ongeschikt = Referentiedata(
        code="ONG",
        naam="Ongeschikt",
        parent=Kandidaatstatus.afgewezen.value,
    )
    """
    Kandidaat niet geschikt voor omgeving.
    """

    gegevens_onjuist = Referentiedata(
        code="ONJ",
        naam="Gegevens onjuist",
        parent=Kandidaatstatus.afgewezen.value,
    )
    """
    Kandidaat komt niet in aanmerking na controle gegevens.
    """

    overeenkomst_getekend = Referentiedata(
        code="OVE",
        naam="Overeenkomst getekend",
        parent=Kandidaatstatus.aangeboden.value,
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
        parent=Kandidaatstatus.aangeboden.value,
    )
    """
    Kandidaat wordt gevraagd of deze nog steeds belangstelling heeft.
    """

    weigering_aanbieding = Referentiedata(
        code="WEI",
        naam="Weigering aanbieding",
        parent=Kandidaatstatus.geweigerd.value,
    )
    """
    Kandidaat weigert de aanbieding.
    """

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
