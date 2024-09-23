from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Contactgegevensoort(Enum):
    e_mail = Referentiedata(
        code="EMA",
        naam="E-mail",
    )

    fax = Referentiedata(
        code="FAX",
        naam="Fax",
    )

    mobiele_telefoon = Referentiedata(
        code="MOB",
        naam="Mobiele telefoon",
    )
    """
    Mobiel telefoonnummer, ook geschikt voor SMS
    """

    pager = Referentiedata(
        code="PAG",
        naam="Pager",
    )

    post = Referentiedata(
        code="POS",
        naam="Post",
    )

    social_media = Referentiedata(
        code="SOC",
        naam="Social media",
    )

    telefoon = Referentiedata(
        code="TEL",
        naam="Telefoon",
    )
    """
    Gewoon telefoonnummer
    """

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
