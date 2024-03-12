
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class OPPERVLAKTESOORT:

    bruto_vloeroppervlakte = Referentiedata(
        code="BVO",
        naam="Bruto vloeroppervlakte",
    )
    # bruto_vloeroppervlakte = ("BVO", "Bruto vloeroppervlakte")
    """
    De bruto oppervlakte van een eenheid(verblijfsobject) in gehele vierkante meters,
    gemeten conform NEN 2580.
    """

    functioneel_nuttig_oppervlakte = Referentiedata(
        code="FNO",
        naam="Functioneel nuttig oppervlakte",
    )
    # functioneel_nuttig_oppervlakte = ("FNO", "Functioneel nuttig oppervlakte")
    """
    De woon- of werkoppervlakte van een eenheid(verblijfsobject) in gehele vierkante
    meters, gemeten conform NEN 2580.
    """

    gebruiksoppervlakte = Referentiedata(
        code="GBO",
        naam="Gebruiksoppervlakte",
    )
    # gebruiksoppervlakte = ("GBO", "Gebruiksoppervlakte")
    """
    De gebruiksoppervlakte van een eenheid(verblijfsobject) in gehele vierkante meters,
    gemeten conform NEN 2580.
    """

    gerealiseerd_nuttig_oppervlakte = Referentiedata(
        code="GNO",
        naam="Gerealiseerd nuttig oppervlakte",
    )
    # gerealiseerd_nuttig_oppervlakte = ("GNO", "Gerealiseerd nuttig oppervlakte")
    """
    De gerealiseerd nuttig oppervlakte van een eenheid(verblijfsobject) in gehele
    vierkante meters, gemeten conform NEN 2580.
    """

    netto_vloeroppervlakte = Referentiedata(
        code="NVO",
        naam="Netto vloeroppervlakte",
    )
    # netto_vloeroppervlakte = ("NVO", "Netto vloeroppervlakte")
    """
    De netto vloeroppervlakte van een eenheid(verblijfsobject) in gehele vierkante
    meters, gemeten conform NEN 2580.
    """

    verhuurbare_vloeroppervlakte = Referentiedata(
        code="VVO",
        naam="Verhuurbare vloeroppervlakte",
    )
    # verhuurbare_vloeroppervlakte = ("VVO", "Verhuurbare vloeroppervlakte")
    """
    De verhuurbare vloeroppervlakte van een eenheid(verblijfsobject) in gehele vierkante
    meters, gemeten conform NEN 2580.
    """

    de_woon_of_werk_oppervlakte = Referentiedata(
        code="WOW",
        naam="De woon of werk oppervlakte",
    )
    # de_woon_of_werk_oppervlakte = ("WOW", "De woon of werk oppervlakte")
    """
    De gebruiksoppervlakte van een eenheid(verblijfsobject) in gehele vierkante meters,
    gemeten conform NEN 2580.
    """
