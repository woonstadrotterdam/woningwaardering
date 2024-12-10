from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OpleidingsniveauReferentiedata(Referentiedata):
    pass


class Opleidingsniveau(Referentiedatasoort):
    hbo_associate_degree = OpleidingsniveauReferentiedata(
        code="HAD",
        naam="HBO Associate degree",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    havo = OpleidingsniveauReferentiedata(
        code="HAV",
        naam="HAVO",
    )

    hbo_bachelor = OpleidingsniveauReferentiedata(
        code="HBA",
        naam="HBO Bachelor",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    hoger_beroepsonderwijs = OpleidingsniveauReferentiedata(
        code="HBO",
        naam="Hoger beroepsonderwijs",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    hbo_master = OpleidingsniveauReferentiedata(
        code="HMA",
        naam="HBO Master",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    hbo_postinitiele_master = OpleidingsniveauReferentiedata(
        code="HPM",
        naam="HBO Postinitiële master",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    middelbaar_beroeps_onderwijs = OpleidingsniveauReferentiedata(
        code="MBO",
        naam="Middelbaar beroeps onderwijs",
    )

    postdoc = OpleidingsniveauReferentiedata(
        code="POD",
        naam="PostDoc",
    )
    """
    Gepromoveerd onderzoeker
    """

    promovendus = OpleidingsniveauReferentiedata(
        code="PRO",
        naam="Promovendus",
    )
    """
    Iemand die door een geaccrediteerde instelling formeel erkend is als iemand die
    uitzicht heeft op een promotie tot de academische graad van doctor.LET OP: In
    VERA 4.0 wordt code PRO vervangen door code PHD
    """

    voorbereidend_middelbaar_beroeps_onderwijs = OpleidingsniveauReferentiedata(
        code="VMB",
        naam="Voorbereidend middelbaar beroeps onderwijs",
    )

    voorbereidend_wetenschappelijk_onderwijs = OpleidingsniveauReferentiedata(
        code="VWO",
        naam="Voorbereidend wetenschappelijk onderwijs",
    )

    wo_bachelor = OpleidingsniveauReferentiedata(
        code="WBA",
        naam="WO Bachelor",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    wo_master = OpleidingsniveauReferentiedata(
        code="WMA",
        naam="WO Master",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """

    wo_postinitiele_master = OpleidingsniveauReferentiedata(
        code="WPM",
        naam="WO Postinitiële master",
    )
    """
    Centraal Register Opleidingen Hoger Onderwijs (CROHO)
    """
