
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PROJECTBUDGETREGELREGELSOORT:

    kostendetailregel = Referentiedata(
        code="KDT",
        naam="Kostendetailregel",
    )
    # kostendetailregel = ("KDT", "Kostendetailregel")
    """
    Projectbudgetregel is een kostenregel binnen de stichtingskosten hiërarchie
    """

    opbrengstendetailregel = Referentiedata(
        code="ODT",
        naam="Opbrengstendetailregel",
    )
    # opbrengstendetailregel = ("ODT", "Opbrengstendetailregel")
    """
    Projectbudgetregel is een opbrengstenregel binnen de stichtingskosten hiërarchie
    """

    subtotaalregel = Referentiedata(
        code="STR",
        naam="Subtotaalregel",
    )
    # subtotaalregel = ("STR", "Subtotaalregel")
    """
    Projectbudgetregel is een optelling van één of meer onderliggende kosten- of
    opbrengstenregels binnen de stichtingskosten hiërarchie
    """
