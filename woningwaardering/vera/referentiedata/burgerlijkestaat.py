from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Burgerlijkestaat(Enum):
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

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
