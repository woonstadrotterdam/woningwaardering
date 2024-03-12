
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class MEETEENHEID:

    centimeter = Referentiedata(
        code="CM",
        naam="Centimeter",
    )
    # centimeter = ("CM", "Centimeter")
    """
    Aantal uitgedrukt in centimeters
    """

    omvang_personeelsbestand = Referentiedata(
        code="FTE",
        naam="Omvang personeelsbestand",
    )
    # omvang_personeelsbestand = ("FTE", "Omvang personeelsbestand")

    gram = Referentiedata(
        code="GRM",
        naam="Gram",
    )
    # gram = ("GRM", "Gram")
    """
    Aantal uitgedrukt in gram
    """

    kilogram = Referentiedata(
        code="KGR",
        naam="Kilogram",
    )
    # kilogram = ("KGR", "Kilogram")

    liter = Referentiedata(
        code="LTR",
        naam="Liter",
    )
    # liter = ("LTR", "Liter")

    vierkante_meter_m2 = Referentiedata(
        code="M2",
        naam="Vierkante meter, m2",
    )
    # vierkante_meter_m2 = ("M2", "Vierkante meter, m2")

    kubieke_meter_m3 = Referentiedata(
        code="M3",
        naam="Kubieke meter, m3",
    )
    # kubieke_meter_m3 = ("M3", "Kubieke meter, m3")

    minuten = Referentiedata(
        code="MIN",
        naam="Minuten",
    )
    # minuten = ("MIN", "Minuten")
    """
    Aantal uitgedrukt in minuten, bijvoorbeeld 15 minuten reistijd
    """

    meter = Referentiedata(
        code="MTR",
        naam="Meter",
    )
    # meter = ("MTR", "Meter")

    stuks = Referentiedata(
        code="STU",
        naam="Stuks",
    )
    # stuks = ("STU", "Stuks")
    """
    Aantal uitgedrukt per stuk, bijvoorbeeld 2 stuks deurklink, 10 stuks schroeven, etc.
    """

    uren = Referentiedata(
        code="UUR",
        naam="Uren",
    )
    # uren = ("UUR", "Uren")
    """
    Aantal uitgedrukt in uren, bijvoorbeeld 2,5 uur werktijd. 15 minuten kan uitgedrukt
    worden in 0,25 uur
    """
