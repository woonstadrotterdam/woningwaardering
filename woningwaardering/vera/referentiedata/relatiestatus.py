from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RelatiestatusReferentiedata(Referentiedata):
    pass


class Relatiestatus(Referentiedatasoort):
    actief = RelatiestatusReferentiedata(
        code="ACT",
        naam="Actief",
    )
    """
    De relatie is een actieve relatie
    """

    inactief = RelatiestatusReferentiedata(
        code="INA",
        naam="Inactief",
    )
    """
    De relatie is niet (meer) actief
    """

    slapend = RelatiestatusReferentiedata(
        code="SLA",
        naam="Slapend",
    )
    """
    De relatie betreft een VvE (rechtspersoon) die een slapende status heeft
    """
