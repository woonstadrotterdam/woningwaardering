from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class KwaliteitsmetingverzoeksoortReferentiedata(Referentiedata):
    pass


class Kwaliteitsmetingverzoeksoort(Referentiedatasoort):
    algemene_dienstverlening = KwaliteitsmetingverzoeksoortReferentiedata(
        code="ALG",
        naam="Algemene dienstverlening",
    )
    """
    Kwaliteitsmetingverzoek betreffende algemene dienstverlening
    """

    nieuwe_huurders = KwaliteitsmetingverzoeksoortReferentiedata(
        code="HUN",
        naam="Nieuwe huurders",
    )
    """
    Kwaliteitsmetingverzoek betreffende nieuwe huurders
    """

    vertrokken_huurders = KwaliteitsmetingverzoeksoortReferentiedata(
        code="HUV",
        naam="Vertrokken huurders",
    )
    """
    Kwaliteitsmetingverzoek betreffende vertrokken huurders
    """

    onderhoud = KwaliteitsmetingverzoeksoortReferentiedata(
        code="OND",
        naam="Onderhoud",
    )
    """
    Kwaliteitsmetingverzoek betreffende onderhoud
    """

    overig = KwaliteitsmetingverzoeksoortReferentiedata(
        code="OVR",
        naam="Overig",
    )
    """
    Kwaliteitsmetingverzoek betreffende overige onderwerpen
    """

    reparaties = KwaliteitsmetingverzoeksoortReferentiedata(
        code="REP",
        naam="Reparaties",
    )
    """
    Kwaliteitsmetingverzoek betreffende reparaties
    """

    woonomgeving = KwaliteitsmetingverzoeksoortReferentiedata(
        code="WOO",
        naam="Woonomgeving",
    )
    """
    Kwaliteitsmetingverzoek betreffende woonomgeving
    """
