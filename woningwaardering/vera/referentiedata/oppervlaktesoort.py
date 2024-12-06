from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Oppervlaktesoort(Referentiedatasoort):
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

    gebruiksoppervlakte_thermische_zone = Referentiedata(
        code="GTZ",
        naam="Gebruiksoppervlakte thermische zone",
    )
    """
    Gebruiksoppervlakte van de thermische zone, afgebakend volgens NTA 8800
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
