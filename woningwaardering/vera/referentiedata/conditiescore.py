from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ConditiescoreReferentiedata(Referentiedata):
    pass


class Conditiescore(Referentiedatasoort):
    uitstekende_conditie = ConditiescoreReferentiedata(
        code="1",
        naam="Uitstekende conditie",
    )
    """
    Incidenteel geringe gebreken. (Conditiescore 1 van NEN 2767)
    """

    goede_conditie = ConditiescoreReferentiedata(
        code="2",
        naam="Goede conditie",
    )
    """
    Incidenteel beginnende veroudering. (Conditiescore 2 van NEN 2767)
    """

    redelijke_conditie = ConditiescoreReferentiedata(
        code="3",
        naam="Redelijke conditie",
    )
    """
    Plaatselijk zichtbare veroudering Functievervulling van bouw- en installatiedelen
    niet in gevaar. (Conditiescore 3 van NEN 2767)
    """

    matige_conditie = ConditiescoreReferentiedata(
        code="4",
        naam="Matige conditie",
    )
    """
    Functievervulling van bouw- en installatiedelen incidenteel in gevaar.
    (Conditiescore 4 van NEN 2767)
    """

    slechte_conditie = ConditiescoreReferentiedata(
        code="5",
        naam="Slechte conditie",
    )
    """
    De veroudering is onomkeerbaar. (Conditiescore 5 van NEN 2767)
    """

    zeer_slechte_conditie = ConditiescoreReferentiedata(
        code="6",
        naam="Zeer slechte conditie",
    )
    """
    Technisch rijp voor sloop. (Conditiescore 6 van NEN 2767)
    """
