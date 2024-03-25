from woningwaardering.vera.bvg.generated import Referentiedata


class Relatiestatus:
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    """
    De relatie is een actieve relatie
    """

    inactief = Referentiedata(
        code="INA",
        naam="Inactief",
    )
    """
    De relatie is niet (meer) actief
    """

    slapend = Referentiedata(
        code="SLA",
        naam="Slapend",
    )
    """
    De relatie betreft een VvE (rechtspersoon) die een slapende status heeft
    """
