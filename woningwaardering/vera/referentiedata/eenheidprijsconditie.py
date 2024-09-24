from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidprijsconditie(Enum):
    exclusief_servicekosten = Referentiedata(
        code="ESE",
        naam="Exclusief servicekosten",
    )
    """
    De vraagprijs is exclusief servicekosten.
    """

    inclusief_servicekosten = Referentiedata(
        code="ISE",
        naam="Inclusief servicekosten",
    )
    """
    De vraagprijs is inclusief servicekosten.
    """

    inclusief_stookkosten = Referentiedata(
        code="IST",
        naam="Inclusief stookkosten",
    )
    """
    De vraagprijs is inclusief kosten (voorschot) voor de verwarming van het vastgoed.
    """

    kosten_koper = Referentiedata(
        code="KKO",
        naam="Kosten Koper",
    )
    """
    De vraagprijs is op basis van kosten koper. De kosten met betrekking tot de
    onroerend goed overdracht zijn voor de koper.
    """

    vrij_op_naam = Referentiedata(
        code="VON",
        naam="Vrij op naam",
    )
    """
    De kosten voor de overdracht van de woning zijn voor rekening van de verkoper. Het
    betreft hier de BTW of overdrachtsbelasting, de kadastrale kosten en de
    notariskosten voor de transportakte.
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
