from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Zaaktypedetailsoort(Enum):
    agressie_en_of_bedreiging = Referentiedata(
        code="AGR",
        naam="Agressie/bedreiging",
    )
    """
    Sociale melding over agressie/bedreiging
    """

    bedrijfsmatig_gebruik_woning = Referentiedata(
        code="BED",
        naam="Bedrijfsmatig gebruik woning",
    )
    """
    Sociale melding over Bedrijfsmatig gebruik woning
    """

    huisdieren = Referentiedata(
        code="DIE",
        naam="Huisdieren",
    )
    """
    Overlast door huisdieren
    """

    dealen_en_of_drugspanden = Referentiedata(
        code="DRU",
        naam="Dealen/drugspanden",
    )
    """
    Sociale melding over Dealen/drugspanden
    """

    geluidsoverlast = Referentiedata(
        code="GEL",
        naam="Geluidsoverlast",
    )
    """
    Sociale melding over Geluidsoverlast
    """

    omgevingsoverlast = Referentiedata(
        code="HAN",
        naam="Omgevingsoverlast",
    )
    """
    Sociale melding over Omgevingsoverlast
    """

    hennepkwekerij = Referentiedata(
        code="HEN",
        naam="Hennepkwekerij",
    )
    """
    Sociale melding over Hennepkwekerij
    """

    oneigenlijk_gebruik_gemeenschappelijke_ruimte = Referentiedata(
        code="KLI",
        naam="Oneigenlijk gebruik gemeenschappelijke ruimte",
    )
    """
    Sociale melding over Oneigenlijk gebruik gemeenschappelijke ruimte
    """

    ongedierte = Referentiedata(
        code="ONG",
        naam="Ongedierte",
    )
    """
    Sociale melding over Ongedierte
    """

    onrechtmatige_bewoning = Referentiedata(
        code="ONR",
        naam="Onrechtmatige bewoning",
    )
    """
    Sociale melding over Onrechtmatige bewoning
    """

    onveiligheid_gemeenschappelijke_ruimte = Referentiedata(
        code="ONV",
        naam="Onveiligheid gemeenschappelijke ruimte",
    )
    """
    Sociale melding over Onveiligheid gemeenschappelijke ruimte
    """

    overige = Referentiedata(
        code="OVE",
        naam="Overige",
    )
    """
    Sociale melding over Overige
    """

    psychische_problematiek = Referentiedata(
        code="PSY",
        naam="Psychische problematiek",
    )
    """
    Sociale melding over Psychische problematiek
    """

    burenruzie = Referentiedata(
        code="RUZ",
        naam="Burenruzie",
    )
    """
    Sociale melding over Burenruzie
    """

    stankoverlast = Referentiedata(
        code="STA",
        naam="Stankoverlast",
    )
    """
    Sociale melding over Stankoverlast
    """

    vandalisme = Referentiedata(
        code="VAN",
        naam="Vandalisme",
    )
    """
    Sociale melding over Vandalisme
    """

    verslavingsproblematiek = Referentiedata(
        code="VER",
        naam="Verslavingsproblematiek",
    )
    """
    Sociale melding over Verslavingsproblematiek
    """

    vervuiling = Referentiedata(
        code="VUI",
        naam="Vervuiling",
    )
    """
    Sociale melding over Vervuiling
    """

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
