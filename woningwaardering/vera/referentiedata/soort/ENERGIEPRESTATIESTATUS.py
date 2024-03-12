
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ENERGIEPRESTATIESTATUS:

    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    # definitief = ("DEF", "Definitief")
    """
    Een definitieve energieprestatie is een bij de Rijksoverheid afgemelde
    energieprestatie, wat leidt tot een officieel geldig label.
    """

    voorlopig = Referentiedata(
        code="VOO",
        naam="Voorlopig",
    )
    # voorlopig = ("VOO", "Voorlopig")
    """
    Een voorlopige energieprestatie wordt ook wel 'pré-label' genoemd en is een op basis
    van woningkenmerken afgeleide (theoretische) prestatie
    """
