from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class HuurklasseReferentiedata(Referentiedata):
    pass


class Huurklasse(Referentiedatasoort):
    betaalbaar = HuurklasseReferentiedata(
        code="BET",
        naam="Betaalbaar",
    )
    """
    Eenheid waarvan de netto huur (kale huur) per maand op of boven de
    kwaliteitskortingsgrens en onder de aftoppingsgrens (hoog) ligt.
    """

    boven_huurtoeslaggrens = HuurklasseReferentiedata(
        code="BOV",
        naam="Boven huurtoeslaggrens",
    )
    """
    Eenheid waarvan de netto huur (kale huur) per maand op of boven de huurtoeslaggrens
    (liberalisatiegrens) ligt.
    """

    duur = HuurklasseReferentiedata(
        code="DUU",
        naam="Duur",
    )
    """
    Eenheid waarvan de netto huur (kale huur) per maand op of boven de aftoppingsgrens
    (hoog) en onder de huurtoeslaggrens ligt.
    """

    goedkoop = HuurklasseReferentiedata(
        code="GOE",
        naam="Goedkoop",
    )
    """
    Eenheid waarvan de netto huur (kale huur) per maand onder de kwaliteitskortingsgrens
    ligt.
    """
