from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EnergieprestatiestatusReferentiedata(Referentiedata):
    pass


class Energieprestatiestatus(Referentiedatasoort):
    definitief = EnergieprestatiestatusReferentiedata(
        code="DEF",
        naam="Definitief",
    )
    """
    Een definitieve energieprestatie is een bij de Rijksoverheid afgemelde
    energieprestatie, wat leidt tot een officieel geldig label.
    """

    voorlopig = EnergieprestatiestatusReferentiedata(
        code="VOO",
        naam="Voorlopig",
    )
    """
    Een voorlopige energieprestatie wordt ook wel 'pré-label' genoemd en is een op basis
    van woningkenmerken afgeleide (theoretische) prestatie
    """
