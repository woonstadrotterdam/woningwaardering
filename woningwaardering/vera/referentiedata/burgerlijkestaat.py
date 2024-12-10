from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BurgerlijkestaatReferentiedata(Referentiedata):
    pass


class Burgerlijkestaat(Referentiedatasoort):
    achtergebleven_partner = BurgerlijkestaatReferentiedata(
        code="ACH",
        naam="Achtergebleven partner",
    )

    gehuwd = BurgerlijkestaatReferentiedata(
        code="GEH",
        naam="Gehuwd",
    )

    gescheiden = BurgerlijkestaatReferentiedata(
        code="GES",
        naam="Gescheiden",
    )

    ongehuwd = BurgerlijkestaatReferentiedata(
        code="ONG",
        naam="Ongehuwd",
    )
    """
    En nooit gehuwd of partnerschap
    """

    partnerschap_beeindigd = BurgerlijkestaatReferentiedata(
        code="PAB",
        naam="Partnerschap beëindigd",
    )

    partnerschap = BurgerlijkestaatReferentiedata(
        code="PAR",
        naam="Partnerschap",
    )
    """
    Geregistreerd partnerschap
    """

    samenwonend = BurgerlijkestaatReferentiedata(
        code="SAM",
        naam="Samenwonend",
    )
    """
    Langdurig huishouden voerend
    """

    weduwe_en_of_weduwnaar = BurgerlijkestaatReferentiedata(
        code="WED",
        naam="Weduwe/weduwnaar",
    )
