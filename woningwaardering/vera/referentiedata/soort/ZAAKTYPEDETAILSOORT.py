
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ZAAKTYPEDETAILSOORT:

    agressie_of_bedreiging = Referentiedata(
        code="AGR",
        naam="Agressie/bedreiging",
    )
    # agressie_of_bedreiging = ("AGR", "Agressie/bedreiging")
    """
    Sociale melding over agressie/bedreiging
    """

    bedrijfsmatig_gebruik_woning = Referentiedata(
        code="BED",
        naam="Bedrijfsmatig gebruik woning",
    )
    # bedrijfsmatig_gebruik_woning = ("BED", "Bedrijfsmatig gebruik woning")
    """
    Sociale melding over Bedrijfsmatig gebruik woning
    """

    huisdieren = Referentiedata(
        code="DIE",
        naam="Huisdieren",
    )
    # huisdieren = ("DIE", "Huisdieren")
    """
    Overlast door huisdieren
    """

    dealen_of_drugspanden = Referentiedata(
        code="DRU",
        naam="Dealen/drugspanden",
    )
    # dealen_of_drugspanden = ("DRU", "Dealen/drugspanden")
    """
    Sociale melding over Dealen/drugspanden
    """

    geluidsoverlast = Referentiedata(
        code="GEL",
        naam="Geluidsoverlast",
    )
    # geluidsoverlast = ("GEL", "Geluidsoverlast")
    """
    Sociale melding over Geluidsoverlast
    """

    omgevingsoverlast = Referentiedata(
        code="HAN",
        naam="Omgevingsoverlast",
    )
    # omgevingsoverlast = ("HAN", "Omgevingsoverlast")
    """
    Sociale melding over Omgevingsoverlast
    """

    hennepkwekerij = Referentiedata(
        code="HEN",
        naam="Hennepkwekerij",
    )
    # hennepkwekerij = ("HEN", "Hennepkwekerij")
    """
    Sociale melding over Hennepkwekerij
    """

    oneigenlijk_gebruik_gemeenschappelijke_ruimte = Referentiedata(
        code="KLI",
        naam="Oneigenlijk gebruik gemeenschappelijke ruimte",
    )
    # oneigenlijk_gebruik_gemeenschappelijke_ruimte = ("KLI", "Oneigenlijk gebruik gemeenschappelijke ruimte")
    """
    Sociale melding over Oneigenlijk gebruik gemeenschappelijke ruimte
    """

    ongedierte = Referentiedata(
        code="ONG",
        naam="Ongedierte",
    )
    # ongedierte = ("ONG", "Ongedierte")
    """
    Sociale melding over Ongedierte
    """

    onrechtmatige_bewoning = Referentiedata(
        code="ONR",
        naam="Onrechtmatige bewoning",
    )
    # onrechtmatige_bewoning = ("ONR", "Onrechtmatige bewoning")
    """
    Sociale melding over Onrechtmatige bewoning
    """

    onveiligheid_gemeenschappelijke_ruimte = Referentiedata(
        code="ONV",
        naam="Onveiligheid gemeenschappelijke ruimte",
    )
    # onveiligheid_gemeenschappelijke_ruimte = ("ONV", "Onveiligheid gemeenschappelijke ruimte")
    """
    Sociale melding over Onveiligheid gemeenschappelijke ruimte
    """

    overige = Referentiedata(
        code="OVE",
        naam="Overige",
    )
    # overige = ("OVE", "Overige")
    """
    Sociale melding over Overige
    """

    psychische_problematiek = Referentiedata(
        code="PSY",
        naam="Psychische problematiek",
    )
    # psychische_problematiek = ("PSY", "Psychische problematiek")
    """
    Sociale melding over Psychische problematiek
    """

    burenruzie = Referentiedata(
        code="RUZ",
        naam="Burenruzie",
    )
    # burenruzie = ("RUZ", "Burenruzie")
    """
    Sociale melding over Burenruzie
    """

    stankoverlast = Referentiedata(
        code="STA",
        naam="Stankoverlast",
    )
    # stankoverlast = ("STA", "Stankoverlast")
    """
    Sociale melding over Stankoverlast
    """

    vandalisme = Referentiedata(
        code="VAN",
        naam="Vandalisme",
    )
    # vandalisme = ("VAN", "Vandalisme")
    """
    Sociale melding over Vandalisme
    """

    verslavingsproblematiek = Referentiedata(
        code="VER",
        naam="Verslavingsproblematiek",
    )
    # verslavingsproblematiek = ("VER", "Verslavingsproblematiek")
    """
    Sociale melding over Verslavingsproblematiek
    """

    vervuiling = Referentiedata(
        code="VUI",
        naam="Vervuiling",
    )
    # vervuiling = ("VUI", "Vervuiling")
    """
    Sociale melding over Vervuiling
    """
