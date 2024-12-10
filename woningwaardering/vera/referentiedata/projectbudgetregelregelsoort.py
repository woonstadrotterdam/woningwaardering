from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ProjectbudgetregelregelsoortReferentiedata(Referentiedata):
    pass


class Projectbudgetregelregelsoort(Referentiedatasoort):
    kostendetailregel = ProjectbudgetregelregelsoortReferentiedata(
        code="KDT",
        naam="Kostendetailregel",
    )
    """
    Projectbudgetregel is een kostenregel binnen de stichtingskosten hiërarchie
    """

    opbrengstendetailregel = ProjectbudgetregelregelsoortReferentiedata(
        code="ODT",
        naam="Opbrengstendetailregel",
    )
    """
    Projectbudgetregel is een opbrengstenregel binnen de stichtingskosten hiërarchie
    """

    subtotaalregel = ProjectbudgetregelregelsoortReferentiedata(
        code="STR",
        naam="Subtotaalregel",
    )
    """
    Projectbudgetregel is een optelling van één of meer onderliggende kosten- of
    opbrengstenregels binnen de stichtingskosten hiërarchie
    """
