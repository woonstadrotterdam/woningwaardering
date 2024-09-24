from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Aanbiedingdetailstatus(Enum):
    andere_woning_geaccepteerd = Referentiedata(
        code="AND",
        naam="Andere woning geaccepteerd",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is geweigerd, omdat een kandidaat een andere woning heeft
    geaccepteerd.
    """

    anderen_krijgen_voorrang = Referentiedata(
        code="ANV",
        naam="Anderen krijgen voorrang",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    Bij het verlenen van huisvestingsvergunningen wordt voorrang gegeven aan
    woningzoekenden die voldoen aan in die verordening vastgelegde
    sociaal-economische kenmerken. Conform Artikel 9 (WBMGP).
    """

    buitenruimte_bevalt_niet = Referentiedata(
        code="BUI",
        naam="Buitenruimte bevalt niet",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de buitenruimte niet
    voldoet.
    """

    cooptatie_mislukt = Referentiedata(
        code="COO",
        naam="Cooptatie mislukt",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat een kandidaat is afgevallen in de
    selectieprocedure van de zittende bewoners op basis van het recht van coöptatie.
    """

    documenten_niet_aangeleverd = Referentiedata(
        code="DOC",
        naam="Documenten niet aangeleverd",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat een kandidaat de vereiste documenten niet heeft
    aangeleverd.
    """

    documenten_niet_akkoord = Referentiedata(
        code="DON",
        naam="Documenten niet akkoord",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat de door een kandidaat aangeleverde documenten
    niet voldoen.
    """

    geen_belangstelling_meer = Referentiedata(
        code="GEE",
        naam="Geen belangstelling meer",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de kandidaat geen
    belangstelling meer heeft.
    """

    gegevens_onjuist = Referentiedata(
        code="GEG",
        naam="Gegevens onjuist",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat de door een kandidaat aangeleverde gegevens
    niet voldoen.
    """

    geen_recht_op_huisvestingsvergunning = Referentiedata(
        code="GER",
        naam="Geen recht op huisvestingsvergunning",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    De huisvestingsvergoeding is niet verleend door een gegrond vermoeden dat het
    huisvesten van de personen van 16 jaar en ouder die zich in een woonruimte in
    dat complex, die straat of dat gebied willen huisvesten, zal leiden tot een
    toename van overlast of criminaliteit in dat complex, die straat of dat gebied.
    Conform artikel 10 (WBMGP).
    """

    huurprijs_te_hoog = Referentiedata(
        code="HUU",
        naam="Huurprijs te hoog",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de huurprijs te hoog is.
    """

    inkomen_te_hoog = Referentiedata(
        code="INH",
        naam="Inkomen te hoog",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat op basis van de aangeleverde inkomensgegevens
    is vastgesteld dat het inkomen van de kandidaat te hoog is.
    """

    inkomen_te_laag = Referentiedata(
        code="INL",
        naam="Inkomen te laag",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat op basis van de aangeleverde inkomensgegevens
    is vastgesteld dat het inkomen van de kandidaat te laag is.
    """

    niet_verschenen_bij_afspraak = Referentiedata(
        code="NIE",
        naam="Niet verschenen bij afspraak",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat een kandidaat niet is verschenen op de gemaakte
    afspraak.
    """

    ongeschikt_als_huurder = Referentiedata(
        code="ONG",
        naam="Ongeschikt als huurder",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat een kandidaat ongeschikt wordt geacht als
    huurder.
    """

    onterecht_aangeboden = Referentiedata(
        code="ONT",
        naam="Onterecht aangeboden",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat de eenheid ten onrechte is aangeboden.
    """

    parkeer_bergingruimte_onvoldoende = Referentiedata(
        code="PAO",
        naam="Parkeer, bergingruimte onvoldoende",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de parkeer en/of
    bergruimte niet voldoet.
    """

    persoonlijke_omstandigheden = Referentiedata(
        code="PER",
        naam="Persoonlijke omstandigheden",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden persoonlijke omstandigheden.
    """

    reactietermijn_verlopen = Referentiedata(
        code="REA",
        naam="Reactietermijn verlopen",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat een kandidaat niet binnen de reactietermijn
    heeft gereageerd.
    """

    toewijzing_andere_kandidaat = Referentiedata(
        code="TOE",
        naam="Toewijzing andere kandidaat",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Een aanbieding is ingetrokken, omdat de eenheid is toegewezen aan een andere
    kandidaat.
    """

    woning_bevalt_niet = Referentiedata(
        code="WBN",
        naam="Woning bevalt niet",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de woning niet voldoet.
    """

    woningkwaliteit_bevalt_niet = Referentiedata(
        code="WKN",
        naam="Woningkwaliteit bevalt niet",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de kwaliteit van de woning
    niet voldoet.
    """

    woonomgeving_bevalt_niet = Referentiedata(
        code="WOB",
        naam="Woonomgeving bevalt niet",
        parent=Referentiedata(
            code="GEW",
            naam="Geweigerd",
        ),
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de woonomgeving niet
    voldoet.
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
