from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Passendheidssoort(Enum):
    niet_passend = Referentiedata(
        code="NIE",
        naam="Niet passend",
    )
    """
    De toewijzing is niet-passend volgens de Woningwet (toewijzen betaalbare woning aan
    huishoudens met huurtoeslag). Om een niet-passende toewijzing nader te
    verantwoorden kan passendheiddetailsoort worden gebruikt.
    """

    passendheidtoets_niet_van_toepassing = Referentiedata(
        code="NVT",
        naam="Passendheidtoets niet van toepassing",
    )
    """
    De toewijzing valt buiten de regels van de passendheidstoets volgens de Woningwet,
    bijvoorbeeld omdat de woning niet tot de betaalbare woningvoorraad behoort
    """

    passend = Referentiedata(
        code="PAS",
        naam="Passend",
    )
    """
    De toewijzing is passend volgens de Woningwet (toewijzen betaalbare woning aan
    huishoudens met huurtoeslag)
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
