from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Kandidaatdetailstatus(Enum):
    aanbieding = Referentiedata(
        code="AAN",
        naam="Aanbieding",
        parent=Referentiedata(
            code="AAN",
            naam="Aangeboden",
        ),
    )
    """
    Kandidaat krijgt aanbieding.
    """

    bezichtiging = Referentiedata(
        code="BEZ",
        naam="Bezichtiging",
        parent=Referentiedata(
            code="AAN",
            naam="Aangeboden",
        ),
    )
    """
    Kandidaat mag bezichtigen.
    """

    documentcontrole = Referentiedata(
        code="DOC",
        naam="Documentcontrole",
        parent=Referentiedata(
            code="AAN",
            naam="Aangeboden",
        ),
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
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    Kandidaat heeft te laat of niet gereageerd.
    """

    ongeschikt = Referentiedata(
        code="ONG",
        naam="Ongeschikt",
        parent=Referentiedata(
            code="AFG",
            naam="Afgewezen",
        ),
    )
    """
    Kandidaat niet geschikt voor omgeving.
    """

    gegevens_onjuist = Referentiedata(
        code="ONJ",
        naam="Gegevens onjuist",
        parent=Referentiedata(
            code="AFG",
            naam="Afgewezen",
        ),
    )
    """
    Kandidaat komt niet in aanmerking na controle gegevens.
    """

    overeenkomst_getekend = Referentiedata(
        code="OVE",
        naam="Overeenkomst getekend",
        parent=Referentiedata(
            code="AAN",
            naam="Aangeboden",
        ),
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
        parent=Referentiedata(
            code="AAN",
            naam="Aangeboden",
        ),
    )
    """
    Kandidaat wordt gevraagd of deze nog steeds belangstelling heeft.
    """

    weigering_aanbieding = Referentiedata(
        code="WEI",
        naam="Weigering aanbieding",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
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
