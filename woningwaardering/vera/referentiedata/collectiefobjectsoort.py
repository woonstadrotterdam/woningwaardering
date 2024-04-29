from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Collectiefobjectsoort(Enum):
    achterpad = Referentiedata(
        code="APD",
        naam="Achterpad",
    )

    casco = Referentiedata(
        code="CAS",
        naam="Casco",
    )
    """
    Gevel e.d.
    """

    centrale_hal = Referentiedata(
        code="CEH",
        naam="Centrale hal",
    )

    dak = Referentiedata(
        code="DAK",
        naam="Dak",
    )

    galerij = Referentiedata(
        code="GAL",
        naam="Galerij",
    )

    lift = Referentiedata(
        code="LIF",
        naam="Lift",
    )

    onderdoorgang = Referentiedata(
        code="ONG",
        naam="Onderdoorgang",
    )

    parkeergarage = Referentiedata(
        code="PAG",
        naam="Parkeergarage",
    )

    recreatie_en_of_ontmoetingsruimte = Referentiedata(
        code="ROR",
        naam="Recreatie-/ontmoetingsruimte",
    )

    speelplaats = Referentiedata(
        code="SPP",
        naam="Speelplaats",
    )

    stortkoker = Referentiedata(
        code="STK",
        naam="Stortkoker",
    )

    terrein = Referentiedata(
        code="TER",
        naam="Terrein",
    )
    """
    Parkeerterrein, buitenterrein
    """

    trappenhuis = Referentiedata(
        code="TRH",
        naam="Trappenhuis",
    )

    technische_ruimte = Referentiedata(
        code="TRU",
        naam="Technische ruimte",
    )

    tuin = Referentiedata(
        code="TUI",
        naam="Tuin",
    )
    """
    Gemeenschappelijke tuin
    """

    gemeenschappelijke_badkamer = Referentiedata(
        code="BDK",
        naam="Gemeenschappelijke badkamer",
    )
    """
    Gemeenschappelijke badkamer
    """

    gemeenschappelijk_balkon = Referentiedata(
        code="BAL",
        naam="Gemeenschappelijk balkon",
    )
    """
    Gemeenschappelijk balkon
    """

    gemeenschappelijke_berging = Referentiedata(
        code="BER",
        naam="Gemeenschappelijke berging",
    )
    """
    Gemeenschappelijke berging of berginsgsgang
    """

    gemeenschappelijke_fietsenstalling = Referentiedata(
        code="FTS",
        naam="Gemeenschappelijke fietsenstalling",
    )
    """
    Gemeenschappelijke fietsenstalling
    """

    gemeenschappeijke_keuken = Referentiedata(
        code="KEU",
        naam="Gemeenschappeijke keuken",
    )
    """
    Gemeenschappelijke keuken
    """

    gemeenschappelijke_toilet = Referentiedata(
        code="TOI",
        naam="Gemeenschappelijke toilet",
    )
    """
    Gemeenschappelijk toilet
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
