from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Reclamatiestatus(Referentiedatasoort):
    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    De reclamatie is afgewezen door commissie.
    """

    in_beroep = Referentiedata(
        code="BER",
        naam="In beroep",
    )
    """
    De reclamatie is in beroep gegaan door de woningzoekende.
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    De reclamatie is in behandeling genomen door de commissie.
    """

    ingediend = Referentiedata(
        code="ING",
        naam="Ingediend",
    )
    """
    De reclamatie is ingediend door de woningzoekende.
    """

    toegekend = Referentiedata(
        code="TOE",
        naam="Toegekend",
    )
    """
    De reclamatie is toegekend door de comissie.
    """
