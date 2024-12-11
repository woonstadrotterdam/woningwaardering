from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.aanbiedingstatus import (
    Aanbiedingstatus,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AanbiedingdetailstatusReferentiedata(Referentiedata):
    pass


class Aanbiedingdetailstatus(Referentiedatasoort):
    andere_woning_geaccepteerd = AanbiedingdetailstatusReferentiedata(
        code="AND",
        naam="Andere woning geaccepteerd",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is geweigerd, omdat een kandidaat een andere woning heeft
    geaccepteerd.
    """

    anderen_krijgen_voorrang = AanbiedingdetailstatusReferentiedata(
        code="ANV",
        naam="Anderen krijgen voorrang",
        parent=Aanbiedingstatus.geweigerd,
    )
    """
    Bij het verlenen van huisvestingsvergunningen wordt voorrang gegeven aan
    woningzoekenden die voldoen aan in die verordening vastgelegde
    sociaal-economische kenmerken. Conform Artikel 9 (WBMGP).
    """

    buitenruimte_bevalt_niet = AanbiedingdetailstatusReferentiedata(
        code="BUI",
        naam="Buitenruimte bevalt niet",
        parent=Aanbiedingstatus.geweigerd,
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de buitenruimte niet
    voldoet.
    """

    cooptatie_mislukt = AanbiedingdetailstatusReferentiedata(
        code="COO",
        naam="Cooptatie mislukt",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat een kandidaat is afgevallen in de
    selectieprocedure van de zittende bewoners op basis van het recht van coöptatie.
    """

    documenten_niet_aangeleverd = AanbiedingdetailstatusReferentiedata(
        code="DOC",
        naam="Documenten niet aangeleverd",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat een kandidaat de vereiste documenten niet heeft
    aangeleverd.
    """

    documenten_niet_akkoord = AanbiedingdetailstatusReferentiedata(
        code="DON",
        naam="Documenten niet akkoord",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat de door een kandidaat aangeleverde documenten
    niet voldoen.
    """

    geen_belangstelling_meer = AanbiedingdetailstatusReferentiedata(
        code="GEE",
        naam="Geen belangstelling meer",
        parent=Aanbiedingstatus.geweigerd,
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de kandidaat geen
    belangstelling meer heeft.
    """

    gegevens_onjuist = AanbiedingdetailstatusReferentiedata(
        code="GEG",
        naam="Gegevens onjuist",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat de door een kandidaat aangeleverde gegevens
    niet voldoen.
    """

    geen_recht_op_huisvestingsvergunning = AanbiedingdetailstatusReferentiedata(
        code="GER",
        naam="Geen recht op huisvestingsvergunning",
        parent=Aanbiedingstatus.geweigerd,
    )
    """
    De huisvestingsvergoeding is niet verleend door een gegrond vermoeden dat het
    huisvesten van de personen van 16 jaar en ouder die zich in een woonruimte in
    dat complex, die straat of dat gebied willen huisvesten, zal leiden tot een
    toename van overlast of criminaliteit in dat complex, die straat of dat gebied.
    Conform artikel 10 (WBMGP).
    """

    huurprijs_te_hoog = AanbiedingdetailstatusReferentiedata(
        code="HUU",
        naam="Huurprijs te hoog",
        parent=Aanbiedingstatus.geweigerd,
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de huurprijs te hoog is.
    """

    inkomen_te_hoog = AanbiedingdetailstatusReferentiedata(
        code="INH",
        naam="Inkomen te hoog",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat op basis van de aangeleverde inkomensgegevens
    is vastgesteld dat het inkomen van de kandidaat te hoog is.
    """

    inkomen_te_laag = AanbiedingdetailstatusReferentiedata(
        code="INL",
        naam="Inkomen te laag",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat op basis van de aangeleverde inkomensgegevens
    is vastgesteld dat het inkomen van de kandidaat te laag is.
    """

    niet_verschenen_bij_afspraak = AanbiedingdetailstatusReferentiedata(
        code="NIE",
        naam="Niet verschenen bij afspraak",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat een kandidaat niet is verschenen op de gemaakte
    afspraak.
    """

    ongeschikt_als_huurder = AanbiedingdetailstatusReferentiedata(
        code="ONG",
        naam="Ongeschikt als huurder",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat een kandidaat ongeschikt wordt geacht als
    huurder.
    """

    onterecht_aangeboden = AanbiedingdetailstatusReferentiedata(
        code="ONT",
        naam="Onterecht aangeboden",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat de eenheid ten onrechte is aangeboden.
    """

    parkeer_bergingruimte_onvoldoende = AanbiedingdetailstatusReferentiedata(
        code="PAO",
        naam="Parkeer, bergingruimte onvoldoende",
        parent=Aanbiedingstatus.geweigerd,
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de parkeer en/of
    bergruimte niet voldoet.
    """

    persoonlijke_omstandigheden = AanbiedingdetailstatusReferentiedata(
        code="PER",
        naam="Persoonlijke omstandigheden",
        parent=Aanbiedingstatus.geweigerd,
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden persoonlijke omstandigheden.
    """

    reactietermijn_verlopen = AanbiedingdetailstatusReferentiedata(
        code="REA",
        naam="Reactietermijn verlopen",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat een kandidaat niet binnen de reactietermijn
    heeft gereageerd.
    """

    toewijzing_andere_kandidaat = AanbiedingdetailstatusReferentiedata(
        code="TOE",
        naam="Toewijzing andere kandidaat",
        parent=Aanbiedingstatus.ingetrokken,
    )
    """
    Een aanbieding is ingetrokken, omdat de eenheid is toegewezen aan een andere
    kandidaat.
    """

    woning_bevalt_niet = AanbiedingdetailstatusReferentiedata(
        code="WBN",
        naam="Woning bevalt niet",
        parent=Aanbiedingstatus.geweigerd,
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de woning niet voldoet.
    """

    woningkwaliteit_bevalt_niet = AanbiedingdetailstatusReferentiedata(
        code="WKN",
        naam="Woningkwaliteit bevalt niet",
        parent=Aanbiedingstatus.geweigerd,
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de kwaliteit van de woning
    niet voldoet.
    """

    woonomgeving_bevalt_niet = AanbiedingdetailstatusReferentiedata(
        code="WOB",
        naam="Woonomgeving bevalt niet",
        parent=Aanbiedingstatus.geweigerd,
    )
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de woonomgeving niet
    voldoet.
    """
