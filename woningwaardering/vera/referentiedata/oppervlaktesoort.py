from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Oppervlaktesoort(Enum):
    bruto_vloeroppervlakte = Referentiedata(
        code="BVO",
        naam="Bruto vloeroppervlakte",
    )
    """
    De bruto oppervlakte van een eenheid(verblijfsobject) in gehele vierkante meters,
    gemeten conform NEN 2580.
    """

    functioneel_nuttig_oppervlakte = Referentiedata(
        code="FNO",
        naam="Functioneel nuttig oppervlakte",
    )
    """
    De woon- of werkoppervlakte van een eenheid(verblijfsobject) in gehele vierkante
    meters, gemeten conform NEN 2580.
    """

    gebruiksoppervlakte = Referentiedata(
        code="GBO",
        naam="Gebruiksoppervlakte",
    )
    """
    De gebruiksoppervlakte van een eenheid(verblijfsobject) in gehele vierkante meters,
    gemeten conform NEN 2580.
    """

    gerealiseerd_nuttig_oppervlakte = Referentiedata(
        code="GNO",
        naam="Gerealiseerd nuttig oppervlakte",
    )
    """
    De gerealiseerd nuttig oppervlakte van een eenheid(verblijfsobject) in gehele
    vierkante meters, gemeten conform NEN 2580.
    """

    netto_vloeroppervlakte = Referentiedata(
        code="NVO",
        naam="Netto vloeroppervlakte",
    )
    """
    De netto vloeroppervlakte van een eenheid(verblijfsobject) in gehele vierkante
    meters, gemeten conform NEN 2580.
    """

    verhuurbare_vloeroppervlakte = Referentiedata(
        code="VVO",
        naam="Verhuurbare vloeroppervlakte",
    )
    """
    De verhuurbare vloeroppervlakte van een eenheid(verblijfsobject) in gehele vierkante
    meters, gemeten conform NEN 2580.
    """

    de_woon_of_werk_oppervlakte = Referentiedata(
        code="WOW",
        naam="De woon of werk oppervlakte",
    )
    """
    De gebruiksoppervlakte van een eenheid(verblijfsobject) in gehele vierkante meters,
    gemeten conform NEN 2580.
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
