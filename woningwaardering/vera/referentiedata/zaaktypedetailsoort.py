from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Zaaktypedetailsoort(Enum):
    agressie_en_of_bedreiging = Referentiedata(
        code="AGR",
        naam="Agressie/bedreiging",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over agressie/bedreiging
    """

    bedrijfsmatig_gebruik_woning = Referentiedata(
        code="BED",
        naam="Bedrijfsmatig gebruik woning",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Bedrijfsmatig gebruik woning
    """

    huisdieren = Referentiedata(
        code="DIE",
        naam="Huisdieren",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Overlast door huisdieren
    """

    dealen_en_of_drugspanden = Referentiedata(
        code="DRU",
        naam="Dealen/drugspanden",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Dealen/drugspanden
    """

    geluidsoverlast = Referentiedata(
        code="GEL",
        naam="Geluidsoverlast",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Geluidsoverlast
    """

    omgevingsoverlast = Referentiedata(
        code="HAN",
        naam="Omgevingsoverlast",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Omgevingsoverlast
    """

    hennepkwekerij = Referentiedata(
        code="HEN",
        naam="Hennepkwekerij",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Hennepkwekerij
    """

    oneigenlijk_gebruik_gemeenschappelijke_ruimte = Referentiedata(
        code="KLI",
        naam="Oneigenlijk gebruik gemeenschappelijke ruimte",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Oneigenlijk gebruik gemeenschappelijke ruimte
    """

    ongedierte = Referentiedata(
        code="ONG",
        naam="Ongedierte",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Ongedierte
    """

    onrechtmatige_bewoning = Referentiedata(
        code="ONR",
        naam="Onrechtmatige bewoning",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Onrechtmatige bewoning
    """

    onveiligheid_gemeenschappelijke_ruimte = Referentiedata(
        code="ONV",
        naam="Onveiligheid gemeenschappelijke ruimte",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Onveiligheid gemeenschappelijke ruimte
    """

    overige = Referentiedata(
        code="OVE",
        naam="Overige",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Overige
    """

    psychische_problematiek = Referentiedata(
        code="PSY",
        naam="Psychische problematiek",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Psychische problematiek
    """

    burenruzie = Referentiedata(
        code="RUZ",
        naam="Burenruzie",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Burenruzie
    """

    stankoverlast = Referentiedata(
        code="STA",
        naam="Stankoverlast",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Stankoverlast
    """

    vandalisme = Referentiedata(
        code="VAN",
        naam="Vandalisme",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Vandalisme
    """

    verslavingsproblematiek = Referentiedata(
        code="VER",
        naam="Verslavingsproblematiek",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Verslavingsproblematiek
    """

    vervuiling = Referentiedata(
        code="VUI",
        naam="Vervuiling",
        parent=Referentiedata(
            code="SOC",
            naam="Sociale melding",
        ),
    )
    """
    Sociale melding over Vervuiling
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
