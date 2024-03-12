
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class INKOOPOPDRACHTREGELSOORT:

    initieel = Referentiedata(
        code="INI",
        naam="Initieel",
    )
    # initieel = ("INI", "Initieel")
    """
    De inkoopopdrachtregel betreft 'standaard' overeengekomen werkzaamheden
    """

    meerwerk = Referentiedata(
        code="MEE",
        naam="Meerwerk",
    )
    # meerwerk = ("MEE", "Meerwerk")
    """
    De inkoopopdrachtregel betreft meerwerk t.o.v. de initiële inkoopopdracht
    """

    minderwerk = Referentiedata(
        code="MIN",
        naam="Minderwerk",
    )
    # minderwerk = ("MIN", "Minderwerk")
    """
    De inkoopopdrachtregel betreft minderwerk t.o.v. de initiële inkoopopdracht
    """
