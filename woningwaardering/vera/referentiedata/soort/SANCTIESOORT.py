
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class SANCTIESOORT:

    milde_sanctie = Referentiedata(
        code="MIL",
        naam="Milde sanctie",
    )
    # milde_sanctie = ("MIL", "Milde sanctie")
    """
    Milde sanctie
    """

    no_show_sanctie = Referentiedata(
        code="NOS",
        naam="No-show sanctie",
    )
    # no_show_sanctie = ("NOS", "No-show sanctie")
    """
    No-show sanctie, , verlies van alle zoek-, situatie en zoekpunten
    """

    zware_sanctie = Referentiedata(
        code="ZWA",
        naam="Zware sanctie",
    )
    # zware_sanctie = ("ZWA", "Zware sanctie")
    """
    Zware sanctie, verlies van alle zoek-, situatie en zoekpunten
    """
