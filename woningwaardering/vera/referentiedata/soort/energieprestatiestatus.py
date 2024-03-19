from vera.bvg.generated import Referentiedata


class Energieprestatiestatus:
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
    Een voorlopige energieprestatie wordt ook wel &#39;pré-label&#39; genoemd en is een op basis
    van woningkenmerken afgeleide (theoretische) prestatie
    """
