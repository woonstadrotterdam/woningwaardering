from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Provincie(Enum):
    drenthe = Referentiedata(
        code="DR",
        naam="Drenthe",
    )

    flevoland = Referentiedata(
        code="FL",
        naam="Flevoland",
    )

    fryslan = Referentiedata(
        code="FR",
        naam="Fryslân",
    )

    gelderland = Referentiedata(
        code="GE",
        naam="Gelderland",
    )

    groningen = Referentiedata(
        code="GR",
        naam="Groningen",
    )

    limburg = Referentiedata(
        code="LI",
        naam="Limburg",
    )

    noord_brabant = Referentiedata(
        code="NB",
        naam="Noord-Brabant",
    )

    noord_holland = Referentiedata(
        code="NH",
        naam="Noord-Holland",
    )

    overijssel = Referentiedata(
        code="OV",
        naam="Overijssel",
    )

    utrecht = Referentiedata(
        code="UT",
        naam="Utrecht",
    )

    zeeland = Referentiedata(
        code="ZE",
        naam="Zeeland",
    )
    """
    Buitenlandse provincie is wel referentiedata maar wordt niet beheert binnen de
    standaard.
    """

    zuid_holland = Referentiedata(
        code="ZH",
        naam="Zuid-Holland",
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
