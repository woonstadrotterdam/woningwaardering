from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Zaakstatussoort(Enum):
    aangemaakt = Referentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    De zaak is aangemaakt/geregistreerd maar nog niet toegewezen ter afhandeling
    """

    afgerond = Referentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    De zaak is inhoudelijk afgerond, maar nog niet definitief gesloten
    """

    geannuleerd = Referentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    """
    De afhandeling van de zaak geannuleerd
    """

    gesloten = Referentiedata(
        code="GES",
        naam="Gesloten",
    )
    """
    De zaak is afgerond en gesloten
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    De zaak is in behandeling genomen door of in behandeling gegeven aan iemand, maar er
    zijn nog geen stappen in de uitvoering gezet
    """

    in_uitvoering = Referentiedata(
        code="INU",
        naam="In uitvoering",
    )
    """
    De zaak is in uitvoering
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
