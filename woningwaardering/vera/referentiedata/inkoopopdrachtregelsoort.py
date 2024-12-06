from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Inkoopopdrachtregelsoort(Referentiedatasoort):
    initieel = Referentiedata(
        code="INI",
        naam="Initieel",
    )
    """
    De inkoopopdrachtregel betreft 'standaard' overeengekomen werkzaamheden
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
