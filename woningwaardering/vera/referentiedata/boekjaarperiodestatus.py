from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BoekjaarperiodestatusReferentiedata(Referentiedata):
    pass


class Boekjaarperiodestatus(Referentiedatasoort):
    gesloten_periode = BoekjaarperiodestatusReferentiedata(
        code="GSP",
        naam="Gesloten periode",
    )
    """
    Periode waarin gegevens niet meer kunnen worden gewijzigd, tiegevoegd of verwijderd.
    """

    open_periode = BoekjaarperiodestatusReferentiedata(
        code="OPP",
        naam="Open periode",
    )
    """
    Periode waarin gegevens kunnen worden gewijzigd, tiegevoegd of verwijderd.
    """
