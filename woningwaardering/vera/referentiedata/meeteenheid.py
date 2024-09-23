from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Meeteenheid(Enum):
    centimeter = Referentiedata(
        code="CM",
        naam="Centimeter",
    )
    """
    Aantal uitgedrukt in centimeters
    """

    omvang_personeelsbestand = Referentiedata(
        code="FTE",
        naam="Omvang personeelsbestand",
    )

    gram = Referentiedata(
        code="GRM",
        naam="Gram",
    )
    """
    Aantal uitgedrukt in gram
    """

    kilogram = Referentiedata(
        code="KGR",
        naam="Kilogram",
    )

    liter = Referentiedata(
        code="LTR",
        naam="Liter",
    )

    vierkante_meter_m2 = Referentiedata(
        code="M2",
        naam="Vierkante meter, m2",
    )

    kubieke_meter_m3 = Referentiedata(
        code="M3",
        naam="Kubieke meter, m3",
    )

    millimeter = Referentiedata(
        code="MIL",
        naam="Millimeter",
    )
    """
    Aantal uitgedrukt in millimeters
    """

    minuten = Referentiedata(
        code="MIN",
        naam="Minuten",
    )
    """
    Aantal uitgedrukt in minuten, bijvoorbeeld 15 minuten reistijd
    """

    meter = Referentiedata(
        code="MTR",
        naam="Meter",
    )

    stuks = Referentiedata(
        code="STU",
        naam="Stuks",
    )
    """
    Aantal uitgedrukt per stuk, bijvoorbeeld 2 stuks deurklink, 10 stuks schroeven, etc.
    """

    uren = Referentiedata(
        code="UUR",
        naam="Uren",
    )
    """
    Aantal uitgedrukt in uren, bijvoorbeeld 2,5 uur werktijd. 15 minuten kan uitgedrukt
    worden in 0,25 uur
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
