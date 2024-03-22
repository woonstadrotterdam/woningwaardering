from woningwaardering.vera.bvg.generated import Referentiedata


class Leningaflosvorm:
    annuitair = Referentiedata(
        code="ANN",
        naam="Annuitair",
    )
    """
    Jaarlijks wordt met deze vorm een vast bedrag afgelost. Samenstelling van rente en
    aflossing.
    """

    fixe = Referentiedata(
        code="FIX",
        naam="Fixe",
    )

    lineair = Referentiedata(
        code="LIN",
        naam="Lineair",
    )
    """
    Met deze vorm van lenen wordt een vast bedrag als aflossing betaald. Hierdoor wordt
    de totale lasten (rente + aflossing) steeds lager.
    """
