from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Energieprestatiestatus(Referentiedatasoort):
    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    """
    Een definitieve energieprestatie is een bij de Rijksoverheid afgemelde
    energieprestatie, wat leidt tot een officieel geldig label.
    """

    voorlopig = Referentiedata(
        code="VOO",
        naam="Voorlopig",
    )
    """
    Een voorlopige energieprestatie wordt ook wel 'pré-label' genoemd en is een op basis
    van woningkenmerken afgeleide (theoretische) prestatie
    """
