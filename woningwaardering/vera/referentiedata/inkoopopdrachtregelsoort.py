from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InkoopopdrachtregelsoortReferentiedata(Referentiedata):
    pass


class Inkoopopdrachtregelsoort(Referentiedatasoort):
    initieel = InkoopopdrachtregelsoortReferentiedata(
        code="INI",
        naam="Initieel",
    )
    """
    De inkoopopdrachtregel betreft 'standaard' overeengekomen werkzaamheden
    """

    meerwerk = InkoopopdrachtregelsoortReferentiedata(
        code="MEE",
        naam="Meerwerk",
    )
    """
    De inkoopopdrachtregel betreft meerwerk t.o.v. de initiële inkoopopdracht
    """

    minderwerk = InkoopopdrachtregelsoortReferentiedata(
        code="MIN",
        naam="Minderwerk",
    )
    """
    De inkoopopdrachtregel betreft minderwerk t.o.v. de initiële inkoopopdracht
    """
