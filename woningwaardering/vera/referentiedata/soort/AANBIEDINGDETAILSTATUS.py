
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class AANBIEDINGDETAILSTATUS:

    andere_woning_geaccepteerd = Referentiedata(
        code="AND",
        naam="Andere woning geaccepteerd",
    )
    # andere_woning_geaccepteerd = ("AND", "Andere woning geaccepteerd")
    """
    Een aanbieding is geweigerd, omdat een kandidaat een andere woning heeft
    geaccepteerd.
    """

    anderen_krijgen_voorrang = Referentiedata(
        code="ANV",
        naam="Anderen krijgen voorrang",
    )
    # anderen_krijgen_voorrang = ("ANV", "Anderen krijgen voorrang")
    """
    Bij het verlenen van huisvestingsvergunningen wordt voorrang gegeven aan
    woningzoekenden die voldoen aan in die verordening vastgelegde sociaal-economische
    kenmerken. Conform Artikel 9 (WBMGP).
    """

    buitenruimte_bevalt_niet = Referentiedata(
        code="BUI",
        naam="Buitenruimte bevalt niet",
    )
    # buitenruimte_bevalt_niet = ("BUI", "Buitenruimte bevalt niet")
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de buitenruimte niet
    voldoet.
    """

    cooptatie_mislukt = Referentiedata(
        code="COO",
        naam="Cooptatie mislukt",
    )
    # cooptatie_mislukt = ("COO", "Cooptatie mislukt")
    """
    Een aanbieding is ingetrokken, omdat een kandidaat is afgevallen in de
    selectieprocedure van de zittende bewoners op basis van het recht van coöptatie.
    """

    documenten_niet_aangeleverd = Referentiedata(
        code="DOC",
        naam="Documenten niet aangeleverd",
    )
    # documenten_niet_aangeleverd = ("DOC", "Documenten niet aangeleverd")
    """
    Een aanbieding is ingetrokken, omdat een kandidaat de vereiste documenten niet heeft
    aangeleverd.
    """

    documenten_niet_akkoord = Referentiedata(
        code="DON",
        naam="Documenten niet akkoord",
    )
    # documenten_niet_akkoord = ("DON", "Documenten niet akkoord")
    """
    Een aanbieding is ingetrokken, omdat de door een kandidaat aangeleverde documenten
    niet voldoen.
    """

    geen_belangstelling_meer = Referentiedata(
        code="GEE",
        naam="Geen belangstelling meer",
    )
    # geen_belangstelling_meer = ("GEE", "Geen belangstelling meer")
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de kandidaat geen
    belangstelling meer heeft.
    """

    gegevens_onjuist = Referentiedata(
        code="GEG",
        naam="Gegevens onjuist",
    )
    # gegevens_onjuist = ("GEG", "Gegevens onjuist")
    """
    Een aanbieding is ingetrokken, omdat de door een kandidaat aangeleverde gegevens
    niet voldoen.
    """

    geen_recht_op_huisvestingsvergunning = Referentiedata(
        code="GER",
        naam="Geen recht op huisvestingsvergunning",
    )
    # geen_recht_op_huisvestingsvergunning = ("GER", "Geen recht op huisvestingsvergunning")
    """
    De huisvestingsvergoeding is niet verleend door een gegrond vermoeden dat het
    huisvesten van de personen van 16 jaar en ouder die zich in een woonruimte in dat
    complex, die straat of dat gebied willen huisvesten, zal leiden tot een toename van
    overlast of criminaliteit in dat complex, die straat of dat gebied. Conform artikel
    10 (WBMGP).
    """

    huurprijs_te_hoog = Referentiedata(
        code="HUU",
        naam="Huurprijs te hoog",
    )
    # huurprijs_te_hoog = ("HUU", "Huurprijs te hoog")
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de huurprijs te hoog is.
    """

    inkomen_te_hoog = Referentiedata(
        code="INH",
        naam="Inkomen te hoog",
    )
    # inkomen_te_hoog = ("INH", "Inkomen te hoog")
    """
    Een aanbieding is ingetrokken, omdat op basis van de aangeleverde inkomensgegevens
    is vastgesteld dat het inkomen van de kandidaat te hoog is.
    """

    inkomen_te_laag = Referentiedata(
        code="INL",
        naam="Inkomen te laag",
    )
    # inkomen_te_laag = ("INL", "Inkomen te laag")
    """
    Een aanbieding is ingetrokken, omdat op basis van de aangeleverde inkomensgegevens
    is vastgesteld dat het inkomen van de kandidaat te laag is.
    """

    niet_verschenen_bij_afspraak = Referentiedata(
        code="NIE",
        naam="Niet verschenen bij afspraak",
    )
    # niet_verschenen_bij_afspraak = ("NIE", "Niet verschenen bij afspraak")
    """
    Een aanbieding is ingetrokken, omdat een kandidaat niet is verschenen op de gemaakte
    afspraak.
    """

    ongeschikt_als_huurder = Referentiedata(
        code="ONG",
        naam="Ongeschikt als huurder",
    )
    # ongeschikt_als_huurder = ("ONG", "Ongeschikt als huurder")
    """
    Een aanbieding is ingetrokken, omdat een kandidaat ongeschikt wordt geacht als
    huurder.
    """

    onterecht_aangeboden = Referentiedata(
        code="ONT",
        naam="Onterecht aangeboden",
    )
    # onterecht_aangeboden = ("ONT", "Onterecht aangeboden")
    """
    Een aanbieding is ingetrokken, omdat de eenheid ten onrechte is aangeboden.
    """

    parkeer_bergingruimte_onvoldoende = Referentiedata(
        code="PAO",
        naam="Parkeer, bergingruimte onvoldoende",
    )
    # parkeer_bergingruimte_onvoldoende = ("PAO", "Parkeer, bergingruimte onvoldoende")
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de parkeer en/of
    bergruimte niet voldoet.
    """

    persoonlijke_omstandigheden = Referentiedata(
        code="PER",
        naam="Persoonlijke omstandigheden",
    )
    # persoonlijke_omstandigheden = ("PER", "Persoonlijke omstandigheden")
    """
    Een aanbieding is geweigerd, met als aangegeven reden persoonlijke omstandigheden.
    """

    reactietermijn_verlopen = Referentiedata(
        code="REA",
        naam="Reactietermijn verlopen",
    )
    # reactietermijn_verlopen = ("REA", "Reactietermijn verlopen")
    """
    Een aanbieding is ingetrokken, omdat een kandidaat niet binnen de reactietermijn
    heeft gereageerd.
    """

    toewijzing_andere_kandidaat = Referentiedata(
        code="TOE",
        naam="Toewijzing andere kandidaat",
    )
    # toewijzing_andere_kandidaat = ("TOE", "Toewijzing andere kandidaat")
    """
    Een aanbieding is ingetrokken, omdat de eenheid is toegewezen aan een andere
    kandidaat.
    """

    woning_bevalt_niet = Referentiedata(
        code="WBN",
        naam="Woning bevalt niet",
    )
    # woning_bevalt_niet = ("WBN", "Woning bevalt niet")
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de woning niet voldoet.
    """

    woningkwaliteit_bevalt_niet = Referentiedata(
        code="WKN",
        naam="Woningkwaliteit bevalt niet",
    )
    # woningkwaliteit_bevalt_niet = ("WKN", "Woningkwaliteit bevalt niet")
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de kwaliteit van de woning
    niet voldoet.
    """

    woonomgeving_bevalt_niet = Referentiedata(
        code="WOB",
        naam="Woonomgeving bevalt niet",
    )
    # woonomgeving_bevalt_niet = ("WOB", "Woonomgeving bevalt niet")
    """
    Een aanbieding is geweigerd, met als aangegeven reden dat de woonomgeving niet
    voldoet.
    """
