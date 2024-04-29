from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Opleidingsniveau(Enum):
    hbo_associate_degree = Referentiedata(
        code="HAD",
        naam="HBO Associate degree",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    havo = Referentiedata(
        code="HAV",
        naam="HAVO",
    )

    hbo_bachelor = Referentiedata(
        code="HBA",
        naam="HBO Bachelor",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    hoger_beroepsonderwijs = Referentiedata(
        code="HBO",
        naam="Hoger beroepsonderwijs",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    hbo_master = Referentiedata(
        code="HMA",
        naam="HBO Master",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    hbo_postinitiele_master = Referentiedata(
        code="HPM",
        naam="HBO Postinitiële master",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    middelbaar_beroeps_onderwijs = Referentiedata(
        code="MBO",
        naam="Middelbaar beroeps onderwijs",
    )

    postdoc = Referentiedata(
        code="POD",
        naam="PostDoc",
    )
    """
    Gepromoveerd onderzoeker
    """

    promovendus = Referentiedata(
        code="PRO",
        naam="Promovendus",
    )
    """
    Iemand die door een geaccrediteerde instelling formeel erkend is als iemand die
    uitzicht heeft op een promotie tot de academische graad van doctor.LET OP: In
    VERA 4.0 wordt code PRO vervangen door code PHD
    """

    voorbereidend_middelbaar_beroeps_onderwijs = Referentiedata(
        code="VMB",
        naam="Voorbereidend middelbaar beroeps onderwijs",
    )

    voorbereidend_wetenschappelijk_onderwijs = Referentiedata(
        code="VWO",
        naam="Voorbereidend wetenschappelijk onderwijs",
    )

    wo_bachelor = Referentiedata(
        code="WBA",
        naam="WO Bachelor",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    wo_master = Referentiedata(
        code="WMA",
        naam="WO Master",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    wo_postinitiele_master = Referentiedata(
        code="WPM",
        naam="WO Postinitiële master",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
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
