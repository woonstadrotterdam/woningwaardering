from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Sanctiesoort(Referentiedatasoort):
    milde_sanctie = Referentiedata(
        code="MIL",
        naam="Milde sanctie",
    )
    """
    Milde sanctie
    """

    no_show_sanctie = Referentiedata(
        code="NOS",
        naam="No-show sanctie",
    )
    """
    No-show sanctie, , verlies van alle zoek-, situatie en zoekpunten
    """

    zware_sanctie = Referentiedata(
        code="ZWA",
        naam="Zware sanctie",
    )
    """
    Zware sanctie, verlies van alle zoek-, situatie en zoekpunten
    """
