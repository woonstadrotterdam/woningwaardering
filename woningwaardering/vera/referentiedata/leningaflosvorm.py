from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class LeningaflosvormReferentiedata(Referentiedata):
    pass


class Leningaflosvorm(Referentiedatasoort):
    annuitair = LeningaflosvormReferentiedata(
        code="ANN",
        naam="Annuitair",
    )
    """
    Jaarlijks wordt met deze vorm een vast bedrag afgelost. Samenstelling van rente en
    aflossing.
    """

    fixe = LeningaflosvormReferentiedata(
        code="FIX",
        naam="Fixe",
    )

    lineair = LeningaflosvormReferentiedata(
        code="LIN",
        naam="Lineair",
    )
    """
    Met deze vorm van lenen wordt een vast bedrag als aflossing betaald. Hierdoor wordt
    de totale lasten (rente + aflossing) steeds lager.
    """
