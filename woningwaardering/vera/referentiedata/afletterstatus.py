from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AfletterstatusReferentiedata(Referentiedata):
    pass


class Afletterstatus(Referentiedatasoort):
    deels_afgeletterd = AfletterstatusReferentiedata(
        code="DEE",
        naam="Deels afgeletterd",
    )
    """
    Boeking is deels afgeletterd tegen andere boekingen. Voor vorderingen houdt dit in
    dat er betalingen zijn gedaan maar dat er nog een openstaand saldo is. Voor
    ontvangsten betekent dit dat een deel van de ontvangst is afgeletterd tegen een
    vordering maar dat er nog saldo op de boeking staat die nog gekoppeld moet
    worden.
    """

    niet_afgeletterd = AfletterstatusReferentiedata(
        code="NIE",
        naam="Niet afgeletterd",
    )
    """
    Boeking is (nog) niet afgeletterd tegen andere boekingen. Voor vorderingen houdt dit
    in dat deze nog volledig open staat. Voor ontvangsten betekent dit dat deze nog
    niet gekoppeld is aan een vordering.
    """

    volledig_afgeletterd = AfletterstatusReferentiedata(
        code="VOL",
        naam="Volledig afgeletterd",
    )
    """
    Boeking is volledig afgeletterd tegen andere boekingen. Voor vorderingen houdt dit
    in dat er geen openstaand saldo meer is. Voor ontvangsten betekent dit dat de
    ontvangst volledig is afgeletterd tegen vordering(en).
    """
