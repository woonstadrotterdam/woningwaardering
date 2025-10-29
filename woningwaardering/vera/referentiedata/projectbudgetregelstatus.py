from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ProjectbudgetregelstatusReferentiedata(Referentiedata):
    pass


class Projectbudgetregelstatus(Referentiedatasoort):
    aangevraagd = ProjectbudgetregelstatusReferentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    Projectbudgetregel betreft aangevraagd, maar nog niet goedgekeurd budget of
    prognosebedrag
    """

    bijgesteld = ProjectbudgetregelstatusReferentiedata(
        code="BIJ",
        naam="Bijgesteld",
    )
    """
    Projectbudgetregel betreft bijgesteld, maar nog niet aangevraagd budget of
    prognosebedrag
    """

    goedgekeurd = ProjectbudgetregelstatusReferentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    """
    Projectbudgetregel betreft goedgekeurd, maar nog niet vrijgegeven budget of
    prognosebedrag
    """

    vrijgegeven = ProjectbudgetregelstatusReferentiedata(
        code="VRI",
        naam="Vrijgegeven",
    )
    """
    Projectbudgetregel betreft vrijgegeven budget
    """
