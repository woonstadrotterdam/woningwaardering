from vera.bvg.generated import Referentiedata


class Boekjaarperiodestatus:
    gesloten_periode = Referentiedata(
        code="GSP",
        naam="Gesloten periode",
    )
    """
    Periode waarin gegevens niet meer kunnen worden gewijzigd, tiegevoegd of verwijderd.
    """

    open_periode = Referentiedata(
        code="OPP",
        naam="Open periode",
    )
    """
    Periode waarin gegevens kunnen worden gewijzigd, tiegevoegd of verwijderd.
    """
