
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class OPLEIDINGSNIVEAU:

    hbo_associate_degree = Referentiedata(
        code="HAD",
        naam="HBO Associate degree",
    )
    # hbo_associate_degree = ("HAD", "HBO Associate degree")
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    havo = Referentiedata(
        code="HAV",
        naam="HAVO",
    )
    # havo = ("HAV", "HAVO")

    hbo_bachelor = Referentiedata(
        code="HBA",
        naam="HBO Bachelor",
    )
    # hbo_bachelor = ("HBA", "HBO Bachelor")
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    hoger_beroepsonderwijs = Referentiedata(
        code="HBO",
        naam="Hoger beroepsonderwijs",
    )
    # hoger_beroepsonderwijs = ("HBO", "Hoger beroepsonderwijs")
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    hbo_master = Referentiedata(
        code="HMA",
        naam="HBO Master",
    )
    # hbo_master = ("HMA", "HBO Master")
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    hbo_postinitiele_master = Referentiedata(
        code="HPM",
        naam="HBO Postinitiële master",
    )
    # hbo_postinitiele_master = ("HPM", "HBO Postinitiële master")
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    middelbaar_beroeps_onderwijs = Referentiedata(
        code="MBO",
        naam="Middelbaar beroeps onderwijs",
    )
    # middelbaar_beroeps_onderwijs = ("MBO", "Middelbaar beroeps onderwijs")

    postdoc = Referentiedata(
        code="POD",
        naam="PostDoc",
    )
    # postdoc = ("POD", "PostDoc")
    """
    Gepromoveerd onderzoeker
    """

    promovendus = Referentiedata(
        code="PRO",
        naam="Promovendus",
    )
    # promovendus = ("PRO", "Promovendus")
    """
    Iemand die door een geaccrediteerde instelling formeel erkend is als iemand die
    uitzicht heeft op een promotie tot de academische graad van doctor.LET OP: In VERA
    4.0 wordt code PRO vervangen door code PHD
    """

    voorbereidend_middelbaar_beroeps_onderwijs = Referentiedata(
        code="VMB",
        naam="Voorbereidend middelbaar beroeps onderwijs",
    )
    # voorbereidend_middelbaar_beroeps_onderwijs = ("VMB", "Voorbereidend middelbaar beroeps onderwijs")

    voorbereidend_wetenschappelijk_onderwijs = Referentiedata(
        code="VWO",
        naam="Voorbereidend wetenschappelijk onderwijs",
    )
    # voorbereidend_wetenschappelijk_onderwijs = ("VWO", "Voorbereidend wetenschappelijk onderwijs")

    wo_bachelor = Referentiedata(
        code="WBA",
        naam="WO Bachelor",
    )
    # wo_bachelor = ("WBA", "WO Bachelor")
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    wo_master = Referentiedata(
        code="WMA",
        naam="WO Master",
    )
    # wo_master = ("WMA", "WO Master")
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    wo_postinitiele_master = Referentiedata(
        code="WPM",
        naam="WO Postinitiële master",
    )
    # wo_postinitiele_master = ("WPM", "WO Postinitiële master")
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """
