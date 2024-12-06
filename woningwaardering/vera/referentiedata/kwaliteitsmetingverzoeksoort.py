from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Kwaliteitsmetingverzoeksoort(Referentiedatasoort):
    algemene_dienstverlening = Referentiedata(
        code="ALG",
        naam="Algemene dienstverlening",
    )
    """
    Kwaliteitsmetingverzoek betreffende algemene dienstverlening
    """

    nieuwe_huurders = Referentiedata(
        code="HUN",
        naam="Nieuwe huurders",
    )
    """
    Kwaliteitsmetingverzoek betreffende nieuwe huurders
    """

    vertrokken_huurders = Referentiedata(
        code="HUV",
        naam="Vertrokken huurders",
    )
    """
    Kwaliteitsmetingverzoek betreffende vertrokken huurders
    """

    onderhoud = Referentiedata(
        code="OND",
        naam="Onderhoud",
    )
    """
    Kwaliteitsmetingverzoek betreffende onderhoud
    """

    overig = Referentiedata(
        code="OVR",
        naam="Overig",
    )
    """
    Kwaliteitsmetingverzoek betreffende overige onderwerpen
    """

    reparaties = Referentiedata(
        code="REP",
        naam="Reparaties",
    )
    """
    Kwaliteitsmetingverzoek betreffende reparaties
    """

    woonomgeving = Referentiedata(
        code="WOO",
        naam="Woonomgeving",
    )
    """
    Kwaliteitsmetingverzoek betreffende woonomgeving
    """
