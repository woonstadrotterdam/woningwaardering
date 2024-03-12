
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BOEKINGSOORT:

    belastingen_en_premies_sv = Referentiedata(
        code="BEP",
        naam="Belastingen en premies SV",
    )
    # belastingen_en_premies_sv = ("BEP", "Belastingen en premies SV")
    """
    Boeking van af te dragen / afdracht van loonheffing, premies en sociale
    verzekeringswetten op salarissen, btw op belastbare verhuur en verlegde btw op
    onderhoudsfacturen.
    """

    budget = Referentiedata(
        code="BUD",
        naam="Budget",
    )
    # budget = ("BUD", "Budget")
    """
    Boeking voor opvoer of wijziging van een budget of budgetregel
    """

    memoriaal = Referentiedata(
        code="MEM",
        naam="Memoriaal",
    )
    # memoriaal = ("MEM", "Memoriaal")
    """
    Boeking voor het corrigeren of afboeken van het saldo van een boeking of groep van
    boekingen, meestal van soort VOR.
    """

    onderhoud = Referentiedata(
        code="OHD",
        naam="Onderhoud",
    )
    # onderhoud = ("OHD", "Onderhoud")
    """
    Boeking ten behoeve van of voortkomend uit de onderhoudsadministratie.
    """

    ontvangst = Referentiedata(
        code="ONT",
        naam="Ontvangst",
    )
    # ontvangst = ("ONT", "Ontvangst")
    """
    Boeking van een ontvangen bedrag in relatie tot een andere boeking of groep van
    boekingen, zoals een vordering, aanmaning, borg, betalingsregelingtermijn of
    eindafrekening.
    """

    projecten = Referentiedata(
        code="PRJ",
        naam="Projecten",
    )
    # projecten = ("PRJ", "Projecten")
    """
    Boeking ten behoeve van of voortkomend uit de projectadministratie.
    """

    salaris = Referentiedata(
        code="SAL",
        naam="Salaris",
    )
    # salaris = ("SAL", "Salaris")
    """
    Boeking ten behoeve van of voortkomend uit de salarisadministratie.
    """

    servicekosten = Referentiedata(
        code="SKS",
        naam="Servicekosten",
    )
    # servicekosten = ("SKS", "Servicekosten")
    """
    Boeking ten behoeve van of voortkomend uit de servicekostenadministratie.
    """

    uitbetaling = Referentiedata(
        code="UIT",
        naam="Uitbetaling",
    )
    # uitbetaling = ("UIT", "Uitbetaling")
    """
    Boeking van een betaald bedrag in relatie tot een andere boeking of groep van
    boekingen, zoals een vordering, borg of eindafrekening.
    """

    vordering = Referentiedata(
        code="VOR",
        naam="Vordering",
    )
    # vordering = ("VOR", "Vordering")
    """
    Boeking van een te vorderen bedrag op een huurder of derde.
    """
