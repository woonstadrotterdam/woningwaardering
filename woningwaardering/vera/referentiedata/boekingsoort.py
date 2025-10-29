from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BoekingsoortReferentiedata(Referentiedata):
    pass


class Boekingsoort(Referentiedatasoort):
    belastingen_en_premies_sv = BoekingsoortReferentiedata(
        code="BEP",
        naam="Belastingen en premies SV",
    )
    """
    Boeking van af te dragen / afdracht van loonheffing, premies en sociale
    verzekeringswetten op salarissen, btw op belastbare verhuur en verlegde btw op
    onderhoudsfacturen.
    """

    budget = BoekingsoortReferentiedata(
        code="BUD",
        naam="Budget",
    )
    """
    Boeking voor opvoer of wijziging van een budget of budgetregel
    """

    memoriaal = BoekingsoortReferentiedata(
        code="MEM",
        naam="Memoriaal",
    )
    """
    Boeking voor het corrigeren of afboeken van het saldo van een boeking of groep van
    boekingen, meestal van soort VOR.
    """

    onderhoud = BoekingsoortReferentiedata(
        code="OHD",
        naam="Onderhoud",
    )
    """
    Boeking ten behoeve van of voortkomend uit de onderhoudsadministratie.
    """

    ontvangst = BoekingsoortReferentiedata(
        code="ONT",
        naam="Ontvangst",
    )
    """
    Boeking van een ontvangen bedrag in relatie tot een andere boeking of groep van
    boekingen, zoals een vordering, aanmaning, borg, betalingsregelingtermijn of
    eindafrekening.
    """

    projecten = BoekingsoortReferentiedata(
        code="PRJ",
        naam="Projecten",
    )
    """
    Boeking ten behoeve van of voortkomend uit de projectadministratie.
    """

    salaris = BoekingsoortReferentiedata(
        code="SAL",
        naam="Salaris",
    )
    """
    Boeking ten behoeve van of voortkomend uit de salarisadministratie.
    """

    servicekosten = BoekingsoortReferentiedata(
        code="SKS",
        naam="Servicekosten",
    )
    """
    Boeking ten behoeve van of voortkomend uit de servicekostenadministratie.
    """

    uitbetaling = BoekingsoortReferentiedata(
        code="UIT",
        naam="Uitbetaling",
    )
    """
    Boeking van een betaald bedrag in relatie tot een andere boeking of groep van
    boekingen, zoals een vordering, borg of eindafrekening.
    """

    vordering = BoekingsoortReferentiedata(
        code="VOR",
        naam="Vordering",
    )
    """
    Boeking van een te vorderen bedrag op een huurder of derde.
    """
