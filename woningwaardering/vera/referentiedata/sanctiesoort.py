from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class SanctiesoortReferentiedata(Referentiedata):
    pass


class Sanctiesoort(Referentiedatasoort):
    milde_sanctie = SanctiesoortReferentiedata(
        code="MIL",
        naam="Milde sanctie",
    )
    """
    Milde sanctie
    """

    no_show_sanctie = SanctiesoortReferentiedata(
        code="NOS",
        naam="No-show sanctie",
    )
    """
    No-show sanctie, , verlies van alle zoek-, situatie en zoekpunten
    """

    zware_sanctie = SanctiesoortReferentiedata(
        code="ZWA",
        naam="Zware sanctie",
    )
    """
    Zware sanctie, verlies van alle zoek-, situatie en zoekpunten
    """
