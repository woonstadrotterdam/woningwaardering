from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Projectbudgetregelregelsoort(Referentiedatasoort):
    kostendetailregel = Referentiedata(
        code="KDT",
        naam="Kostendetailregel",
    )
    """
    Projectbudgetregel is een kostenregel binnen de stichtingskosten hiërarchie
    """

    opbrengstendetailregel = Referentiedata(
        code="ODT",
        naam="Opbrengstendetailregel",
    )
    """
    Projectbudgetregel is een opbrengstenregel binnen de stichtingskosten hiërarchie
    """

    subtotaalregel = Referentiedata(
        code="STR",
        naam="Subtotaalregel",
    )
    """
    Projectbudgetregel is een optelling van één of meer onderliggende kosten- of
    opbrengstenregels binnen de stichtingskosten hiërarchie
    """
