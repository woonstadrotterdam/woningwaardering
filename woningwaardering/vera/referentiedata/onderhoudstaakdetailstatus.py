from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Onderhoudstaakdetailstatus(Enum):
    klant_niet_aanwezig = Referentiedata(
        code="AFW",
        naam="Klant niet aanwezig",
        parent=Referentiedata(
            code="OND",
            naam="Onderbroken",
        ),
    )
    """
    De taak is onderbroken omdat de klant niet aanwezig is
    """

    niet_de_juiste_discipline = Referentiedata(
        code="DIS",
        naam="Niet de juiste discipline",
        parent=Referentiedata(
            code="OND",
            naam="Onderbroken",
        ),
    )
    """
    De taak is onderbroken omdat de vakman niet de juiste discipline heeft
    """

    inspectie_en_of_beoordeling_vereist = Referentiedata(
        code="INS",
        naam="Inspectie/beoordeling vereist",
        parent=Referentiedata(
            code="OND",
            naam="Onderbroken",
        ),
    )
    """
    De taak is onderbroken omdat inspectie/beoordeling door inspecteur noodzakelijk is
    """

    materiaal_bestellen = Referentiedata(
        code="MAT",
        naam="Materiaal bestellen",
        parent=Referentiedata(
            code="OND",
            naam="Onderbroken",
        ),
    )
    """
    De taak is onderbroken omdat materiaal besteld moet worden
    """

    offerte_benodigd = Referentiedata(
        code="OFF",
        naam="Offerte benodigd",
        parent=Referentiedata(
            code="OND",
            naam="Onderbroken",
        ),
    )
    """
    De taak is onderbroken omdat een offerte nodig is
    """

    onvoldoende_tijd = Referentiedata(
        code="ONV",
        naam="Onvoldoende tijd",
        parent=Referentiedata(
            code="OND",
            naam="Onderbroken",
        ),
    )
    """
    De taak is onderbroken omdat er onvoldoende tijd voor de vakman is
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
