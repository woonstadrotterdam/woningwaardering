from vera.referentiedata.models import Referentiedata


class Projectbudgetregelstatus:
    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    Projectbudgetregel betreft aangevraagd, maar nog niet goedgekeurd budget of
    prognosebedrag
    """

    bijgesteld = Referentiedata(
        code="BIJ",
        naam="Bijgesteld",
    )
    """
    Projectbudgetregel betreft bijgesteld, maar nog niet aangevraagd budget of
    prognosebedrag
    """

    goedgekeurd = Referentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    """
    Projectbudgetregel betreft goedgekeurd, maar nog niet vrijgegeven budget of
    prognosebedrag
    """

    vrijgegeven = Referentiedata(
        code="VRI",
        naam="Vrijgegeven",
    )
    """
    Projectbudgetregel betreft vrijgegeven budget
    """
