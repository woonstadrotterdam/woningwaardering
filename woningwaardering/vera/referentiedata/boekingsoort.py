from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Boekingsoort(Enum):
    belastingen_en_premies_sv = Referentiedata(
        code="BEP",
        naam="Belastingen en premies SV",
    )
    """
    Boeking van af te dragen / afdracht van loonheffing, premies en sociale
    verzekeringswetten op salarissen, btw op belastbare verhuur en verlegde btw op
    onderhoudsfacturen.
    """

    budget = Referentiedata(
        code="BUD",
        naam="Budget",
    )
    """
    Boeking voor opvoer of wijziging van een budget of budgetregel
    """

    memoriaal = Referentiedata(
        code="MEM",
        naam="Memoriaal",
    )
    """
    Boeking voor het corrigeren of afboeken van het saldo van een boeking of groep van
    boekingen, meestal van soort VOR.
    """

    onderhoud = Referentiedata(
        code="OHD",
        naam="Onderhoud",
    )
    """
    Boeking ten behoeve van of voortkomend uit de onderhoudsadministratie.
    """

    ontvangst = Referentiedata(
        code="ONT",
        naam="Ontvangst",
    )
    """
    Boeking van een ontvangen bedrag in relatie tot een andere boeking of groep van
    boekingen, zoals een vordering, aanmaning, borg, betalingsregelingtermijn of
    eindafrekening.
    """

    projecten = Referentiedata(
        code="PRJ",
        naam="Projecten",
    )
    """
    Boeking ten behoeve van of voortkomend uit de projectadministratie.
    """

    salaris = Referentiedata(
        code="SAL",
        naam="Salaris",
    )
    """
    Boeking ten behoeve van of voortkomend uit de salarisadministratie.
    """

    servicekosten = Referentiedata(
        code="SKS",
        naam="Servicekosten",
    )
    """
    Boeking ten behoeve van of voortkomend uit de servicekostenadministratie.
    """

    uitbetaling = Referentiedata(
        code="UIT",
        naam="Uitbetaling",
    )
    """
    Boeking van een betaald bedrag in relatie tot een andere boeking of groep van
    boekingen, zoals een vordering, borg of eindafrekening.
    """

    vordering = Referentiedata(
        code="VOR",
        naam="Vordering",
    )
    """
    Boeking van een te vorderen bedrag op een huurder of derde.
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
