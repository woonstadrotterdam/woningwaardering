
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class RECLAMATIESTATUS:

    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    # afgewezen = ("AFG", "Afgewezen")
    """
    De reclamatie is afgewezen door commissie.
    """

    in_beroep = Referentiedata(
        code="BER",
        naam="In beroep",
    )
    # in_beroep = ("BER", "In beroep")
    """
    De reclamatie is in beroep gegaan door de woningzoekende.
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    # in_behandeling = ("INB", "In behandeling")
    """
    De reclamatie is in behandeling genomen door de commissie.
    """

    ingediend = Referentiedata(
        code="ING",
        naam="Ingediend",
    )
    # ingediend = ("ING", "Ingediend")
    """
    De reclamatie is ingediend door de woningzoekende.
    """

    toegekend = Referentiedata(
        code="TOE",
        naam="Toegekend",
    )
    # toegekend = ("TOE", "Toegekend")
    """
    De reclamatie is toegekend door de comissie.
    """
