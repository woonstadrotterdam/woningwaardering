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
    Sociale melding over agressie/bedreiging
    """

    bedrijfsmatig_gebruik_woning = ZaaktypedetailsoortReferentiedata(
        code="BED",
        naam="Bedrijfsmatig gebruik woning",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Bedrijfsmatig gebruik woning
    """

    huisdieren = ZaaktypedetailsoortReferentiedata(
        code="DIE",
        naam="Huisdieren",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Overlast door huisdieren
    """

    dealen_en_of_drugspanden = ZaaktypedetailsoortReferentiedata(
        code="DRU",
        naam="Dealen/drugspanden",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Dealen/drugspanden
    """

    geluidsoverlast = ZaaktypedetailsoortReferentiedata(
        code="GEL",
        naam="Geluidsoverlast",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Geluidsoverlast
    """

    omgevingsoverlast = ZaaktypedetailsoortReferentiedata(
        code="HAN",
        naam="Omgevingsoverlast",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Omgevingsoverlast
    """

    hennepkwekerij = ZaaktypedetailsoortReferentiedata(
        code="HEN",
        naam="Hennepkwekerij",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Hennepkwekerij
    """

    oneigenlijk_gebruik_gemeenschappelijke_ruimte = ZaaktypedetailsoortReferentiedata(
        code="KLI",
        naam="Oneigenlijk gebruik gemeenschappelijke ruimte",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Oneigenlijk gebruik gemeenschappelijke ruimte
    """

    ongedierte = ZaaktypedetailsoortReferentiedata(
        code="ONG",
        naam="Ongedierte",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Ongedierte
    """

    onrechtmatige_bewoning = ZaaktypedetailsoortReferentiedata(
        code="ONR",
        naam="Onrechtmatige bewoning",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Onrechtmatige bewoning
    """

    onveiligheid_gemeenschappelijke_ruimte = ZaaktypedetailsoortReferentiedata(
        code="ONV",
        naam="Onveiligheid gemeenschappelijke ruimte",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Onveiligheid gemeenschappelijke ruimte
    """

    overige = ZaaktypedetailsoortReferentiedata(
        code="OVE",
        naam="Overige",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Overige
    """

    psychische_problematiek = ZaaktypedetailsoortReferentiedata(
        code="PSY",
        naam="Psychische problematiek",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Psychische problematiek
    """

    burenruzie = ZaaktypedetailsoortReferentiedata(
        code="RUZ",
        naam="Burenruzie",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Burenruzie
    """

    stankoverlast = ZaaktypedetailsoortReferentiedata(
        code="STA",
        naam="Stankoverlast",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Stankoverlast
    """

    vandalisme = ZaaktypedetailsoortReferentiedata(
        code="VAN",
        naam="Vandalisme",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Vandalisme
    """

    verslavingsproblematiek = ZaaktypedetailsoortReferentiedata(
        code="VER",
        naam="Verslavingsproblematiek",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Verslavingsproblematiek
    """

    vervuiling = ZaaktypedetailsoortReferentiedata(
        code="VUI",
        naam="Vervuiling",
        parent=Zaaktypesoort.sociale_melding,
    )
    """
    Sociale melding over Vervuiling
    """
