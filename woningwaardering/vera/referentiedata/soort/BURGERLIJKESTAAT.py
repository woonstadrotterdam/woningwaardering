
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BURGERLIJKESTAAT:

    achtergebleven_partner = Referentiedata(
        code="ACH",
        naam="Achtergebleven partner",
    )
    # achtergebleven_partner = ("ACH", "Achtergebleven partner")

    gehuwd = Referentiedata(
        code="GEH",
        naam="Gehuwd",
    )
    # gehuwd = ("GEH", "Gehuwd")

    gescheiden = Referentiedata(
        code="GES",
        naam="Gescheiden",
    )
    # gescheiden = ("GES", "Gescheiden")

    ongehuwd = Referentiedata(
        code="ONG",
        naam="Ongehuwd",
    )
    # ongehuwd = ("ONG", "Ongehuwd")
    """
    En nooit gehuwd of partnerschap
    """

    partnerschap_beeindigd = Referentiedata(
        code="PAB",
        naam="Partnerschap beëindigd",
    )
    # partnerschap_beeindigd = ("PAB", "Partnerschap beëindigd")

    partnerschap = Referentiedata(
        code="PAR",
        naam="Partnerschap",
    )
    # partnerschap = ("PAR", "Partnerschap")
    """
    Geregistreerd partnerschap
    """

    samenwonend = Referentiedata(
        code="SAM",
        naam="Samenwonend",
    )
    # samenwonend = ("SAM", "Samenwonend")
    """
    Langdurig huishouden voerend
    """

    weduwe_of_weduwnaar = Referentiedata(
        code="WED",
        naam="Weduwe/weduwnaar",
    )
    # weduwe_of_weduwnaar = ("WED", "Weduwe/weduwnaar")
