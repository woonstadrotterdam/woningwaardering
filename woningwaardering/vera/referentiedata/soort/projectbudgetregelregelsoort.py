from vera.referentiedata.models import Referentiedata


class Projectbudgetregelregelsoort:
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
