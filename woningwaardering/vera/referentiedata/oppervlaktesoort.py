from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OppervlaktesoortReferentiedata(Referentiedata):
    pass


class Oppervlaktesoort(Referentiedatasoort):
    bruto_vloeroppervlakte = OppervlaktesoortReferentiedata(
        code="BVO",
        naam="Bruto vloeroppervlakte",
    )
    """
    De bruto oppervlakte van een eenheid(verblijfsobject) in gehele vierkante meters,
    gemeten conform NEN 2580.
    """

    functioneel_nuttig_oppervlakte = OppervlaktesoortReferentiedata(
        code="FNO",
        naam="Functioneel nuttig oppervlakte",
    )
    """
    De woon- of werkoppervlakte van een eenheid(verblijfsobject) in gehele vierkante
    meters, gemeten conform NEN 2580.
    """

    gebruiksoppervlakte = OppervlaktesoortReferentiedata(
        code="GBO",
        naam="Gebruiksoppervlakte",
    )
    """
    De gebruiksoppervlakte van een eenheid(verblijfsobject) in gehele vierkante meters,
    gemeten conform NEN 2580.
    """

    gerealiseerd_nuttig_oppervlakte = OppervlaktesoortReferentiedata(
        code="GNO",
        naam="Gerealiseerd nuttig oppervlakte",
    )
    """
    De gerealiseerd nuttig oppervlakte van een eenheid(verblijfsobject) in gehele
    vierkante meters, gemeten conform NEN 2580.
    """

    gebruiksoppervlakte_thermische_zone = OppervlaktesoortReferentiedata(
        code="GTZ",
        naam="Gebruiksoppervlakte thermische zone",
    )
    """
    Gebruiksoppervlakte van de thermische zone, afgebakend volgens NTA 8800
    """

    netto_vloeroppervlakte = OppervlaktesoortReferentiedata(
        code="NVO",
        naam="Netto vloeroppervlakte",
    )
    """
    De netto vloeroppervlakte van een eenheid(verblijfsobject) in gehele vierkante
    meters, gemeten conform NEN 2580.
    """

    verhuurbare_vloeroppervlakte = OppervlaktesoortReferentiedata(
        code="VVO",
        naam="Verhuurbare vloeroppervlakte",
    )
    """
    De verhuurbare vloeroppervlakte van een eenheid(verblijfsobject) in gehele vierkante
    meters, gemeten conform NEN 2580.
    """

    de_woon_of_werk_oppervlakte = OppervlaktesoortReferentiedata(
        code="WOW",
        naam="De woon of werk oppervlakte",
    )
    """
    De gebruiksoppervlakte van een eenheid(verblijfsobject) in gehele vierkante meters,
    gemeten conform NEN 2580.
    """
