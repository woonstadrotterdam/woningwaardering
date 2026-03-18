from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.zaaktypesoort import (
    Zaaktypesoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ZaaktypedetailsoortReferentiedata(Referentiedata):
    pass


class Zaaktypedetailsoort(Referentiedatasoort):
    agressie_en_of_bedreiging = ZaaktypedetailsoortReferentiedata(
        code="AGR",
        naam="Agressie/bedreiging",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Afhandelen van melding over agressie of bedreiging.
    """

    bedrijfsmatig_gebruik_woning = ZaaktypedetailsoortReferentiedata(
        code="BED",
        naam="Bedrijfsmatig gebruik woning",
        parent=Zaaktypesoort.woonfraude,
    )
    """
    Behandelen van melding over bedrijfsmatig gebruik van een woning.
    """

    betalingsregeling = ZaaktypedetailsoortReferentiedata(
        code="BET",
        naam="Betalingsregeling",
        parent=Zaaktypesoort.financiele_problematiek,
    )
    """
    Opstellen of naleven van een betalingsregeling.
    """

    huisdieren = ZaaktypedetailsoortReferentiedata(
        code="DIE",
        naam="Huisdieren",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Behandelen van overlast door huisdieren.
    """

    dealen_en_of_drugspanden = ZaaktypedetailsoortReferentiedata(
        code="DRU",
        naam="Dealen/drugspanden",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Afhandelen van melding over dealen of drugspanden.
    """

    geluidsoverlast = ZaaktypedetailsoortReferentiedata(
        code="GEL",
        naam="Geluidsoverlast",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Behandelen van melding over geluidsoverlast.
    """

    omgevingsoverlast = ZaaktypedetailsoortReferentiedata(
        code="HAN",
        naam="Omgevingsoverlast",
        parent=Zaaktypesoort.omgevingsoverlast,
    )
    """
    Afhandelen van melding over omgevingsoverlast.
    """

    hennepkwekerij = ZaaktypedetailsoortReferentiedata(
        code="HEN",
        naam="Hennepkwekerij",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Afhandelen van melding over hennepkwekerij.
    """

    huurachterstand = ZaaktypedetailsoortReferentiedata(
        code="HUA",
        naam="Huurachterstand",
        parent=Zaaktypesoort.financiele_problematiek,
    )
    """
    Oplossen van achterstallige huurbetaling.
    """

    huurverhoging = ZaaktypedetailsoortReferentiedata(
        code="HUR",
        naam="Huurverhoging",
        parent=Zaaktypesoort.financiele_problematiek,
    )
    """
    Afhandelen van bezwaar of klacht over huurverhoging.
    """

    oneigenlijk_gebruik_gemeenschappelijke_ruimte = ZaaktypedetailsoortReferentiedata(
        code="KLI",
        naam="Oneigenlijk gebruik gemeenschappelijke ruimte",
        parent=Zaaktypesoort.woonfraude,
    )
    """
    Behandelen van melding over oneigenlijk gebruik van gemeenschappelijke ruimte.
    """

    klacht_over_medewerker = ZaaktypedetailsoortReferentiedata(
        code="KME",
        naam="Klacht over medewerker",
        parent=Zaaktypesoort.klacht_over_organisatie,
    )
    """
    Afhandelen van een klacht over het handelen, gedrag of de bejegening door een
    medewerker van de corporatie
    """

    klacht_over_samenwerkingspartner = ZaaktypedetailsoortReferentiedata(
        code="KSA",
        naam="Klacht over samenwerkingspartner",
        parent=Zaaktypesoort.klacht_over_organisatie,
    )
    """
    Afhandelen van een klacht over een externe partij die werkzaamheden uitvoert namens
    of in opdracht van de corporatie, zoals een aannemer, zorgpartner of
    incassopartij.
    """

    ongedierte = ZaaktypedetailsoortReferentiedata(
        code="ONG",
        naam="Ongedierte",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Afhandelen van melding over ongedierte.
    """

    onrechtmatige_bewoning = ZaaktypedetailsoortReferentiedata(
        code="ONR",
        naam="Onrechtmatige bewoning",
        parent=Zaaktypesoort.woonfraude,
    )
    """
    Onderzoeken van onrechtmatige bewoning.
    """

    onveiligheid_gemeenschappelijke_ruimte = ZaaktypedetailsoortReferentiedata(
        code="ONV",
        naam="Onveiligheid gemeenschappelijke ruimte",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Behandelen van melding over onveilige gemeenschappelijke ruimte.
    """

    overige = ZaaktypedetailsoortReferentiedata(
        code="OVE",
        naam="Overige",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Afhandelen van overige sociale meldingen.
    """

    psychische_problematiek = ZaaktypedetailsoortReferentiedata(
        code="PSY",
        naam="Psychische problematiek",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Begeleiden bij psychische problematiek.
    """

    burenruzie = ZaaktypedetailsoortReferentiedata(
        code="RUZ",
        naam="Burenruzie",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Behandelen van melding over burenruzie.
    """

    stankoverlast = ZaaktypedetailsoortReferentiedata(
        code="STA",
        naam="Stankoverlast",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Afhandelen van melding over stankoverlast.
    """

    vandalisme = ZaaktypedetailsoortReferentiedata(
        code="VAN",
        naam="Vandalisme",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Afhandelen van melding over vandalisme.
    """

    verslavingsproblematiek = ZaaktypedetailsoortReferentiedata(
        code="VER",
        naam="Verslavingsproblematiek",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Begeleiden bij verslavingsproblematiek.
    """

    vervuiling = ZaaktypedetailsoortReferentiedata(
        code="VUI",
        naam="Vervuiling",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Afhandelen van melding over vervuiling
    """
