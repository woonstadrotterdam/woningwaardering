
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class RELATIESTATUS:

    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    # actief = ("ACT", "Actief")
    """
    De relatie is een actieve relatie
    """

    inactief = Referentiedata(
        code="INA",
        naam="Inactief",
    )
    # inactief = ("INA", "Inactief")
    """
    De relatie is niet (meer) actief
    """

    slapend = Referentiedata(
        code="SLA",
        naam="Slapend",
    )
    # slapend = ("SLA", "Slapend")
    """
    De relatie betreft een VvE (rechtspersoon) die een slapende status heeft
    """
