from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidprijsconditieReferentiedata(Referentiedata):
    pass


class Eenheidprijsconditie(Referentiedatasoort):
    exclusief_servicekosten = EenheidprijsconditieReferentiedata(
        code="ESE",
        naam="Exclusief servicekosten",
    )
    """
    De vraagprijs is exclusief servicekosten.
    """

    inclusief_servicekosten = EenheidprijsconditieReferentiedata(
        code="ISE",
        naam="Inclusief servicekosten",
    )
    """
    De vraagprijs is inclusief servicekosten.
    """

    inclusief_stookkosten = EenheidprijsconditieReferentiedata(
        code="IST",
        naam="Inclusief stookkosten",
    )
    """
    De vraagprijs is inclusief kosten (voorschot) voor de verwarming van het vastgoed.
    """

    kosten_koper = EenheidprijsconditieReferentiedata(
        code="KKO",
        naam="Kosten Koper",
    )
    """
    De vraagprijs is op basis van kosten koper. De kosten met betrekking tot de
    onroerend goed overdracht zijn voor de koper.
    """

    vrij_op_naam = EenheidprijsconditieReferentiedata(
        code="VON",
        naam="Vrij op naam",
    )
    """
    De kosten voor de overdracht van de woning zijn voor rekening van de verkoper. Het
    betreft hier de BTW of overdrachtsbelasting, de kadastrale kosten en de
    notariskosten voor de transportakte.
    """
