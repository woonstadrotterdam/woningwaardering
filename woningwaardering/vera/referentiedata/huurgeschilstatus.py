from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class HuurgeschilstatusReferentiedata(Referentiedata):
    pass


class Huurgeschilstatus(Referentiedatasoort):
    afgewezen = HuurgeschilstatusReferentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Het huurgeschil is afgewezen, en daarmee tevens afgehandeld
    """

    in_behandeling = HuurgeschilstatusReferentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    Het huurgeschil is (nog) in behandeling
    """

    toegekend = HuurgeschilstatusReferentiedata(
        code="TOE",
        naam="Toegekend",
    )
    """
    Het huurgeschil is toegekend, en daarmee tevens afgehandeld
    """
