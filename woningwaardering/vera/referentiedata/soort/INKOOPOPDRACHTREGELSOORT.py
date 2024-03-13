from woningwaardering.vera.bvg.models import Referentiedata


class INKOOPOPDRACHTREGELSOORT:
    initieel = Referentiedata(
        code="INI",
        naam="Initieel",
    )
    """
    De inkoopopdrachtregel betreft &#39;standaard&#39; overeengekomen werkzaamheden
    """

    meerwerk = Referentiedata(
        code="MEE",
        naam="Meerwerk",
    )
    """
    De inkoopopdrachtregel betreft meerwerk t.o.v. de initiële inkoopopdracht
    """

    minderwerk = Referentiedata(
        code="MIN",
        naam="Minderwerk",
    )
    """
    De inkoopopdrachtregel betreft minderwerk t.o.v. de initiële inkoopopdracht
    """
