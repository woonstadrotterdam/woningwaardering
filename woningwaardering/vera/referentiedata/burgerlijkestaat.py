from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Burgerlijkestaat(Referentiedatasoort):
    achtergebleven_partner = Referentiedata(
        code="ACH",
        naam="Achtergebleven partner",
    )

    gehuwd = Referentiedata(
        code="GEH",
        naam="Gehuwd",
    )

    gescheiden = Referentiedata(
        code="GES",
        naam="Gescheiden",
    )

    ongehuwd = Referentiedata(
        code="ONG",
        naam="Ongehuwd",
    )
    """
    En nooit gehuwd of partnerschap
    """

    partnerschap_beeindigd = Referentiedata(
        code="PAB",
        naam="Partnerschap beëindigd",
    )

    partnerschap = Referentiedata(
        code="PAR",
        naam="Partnerschap",
    )
    """
    Geregistreerd partnerschap
    """

    samenwonend = Referentiedata(
        code="SAM",
        naam="Samenwonend",
    )
    """
    Langdurig huishouden voerend
    """

    weduwe_en_of_weduwnaar = Referentiedata(
        code="WED",
        naam="Weduwe/weduwnaar",
    )
