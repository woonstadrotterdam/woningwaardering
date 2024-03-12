
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PROJECTBUDGETREGELSTATUS:

    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    # aangevraagd = ("AAN", "Aangevraagd")
    """
    Projectbudgetregel betreft aangevraagd, maar nog niet goedgekeurd budget of
    prognosebedrag
    """

    bijgesteld = Referentiedata(
        code="BIJ",
        naam="Bijgesteld",
    )
    # bijgesteld = ("BIJ", "Bijgesteld")
    """
    Projectbudgetregel betreft bijgesteld, maar nog niet aangevraagd budget of
    prognosebedrag
    """

    goedgekeurd = Referentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    # goedgekeurd = ("GOE", "Goedgekeurd")
    """
    Projectbudgetregel betreft goedgekeurd, maar nog niet vrijgegeven budget of
    prognosebedrag
    """

    vrijgegeven = Referentiedata(
        code="VRI",
        naam="Vrijgegeven",
    )
    # vrijgegeven = ("VRI", "Vrijgegeven")
    """
    Projectbudgetregel betreft vrijgegeven budget
    """
