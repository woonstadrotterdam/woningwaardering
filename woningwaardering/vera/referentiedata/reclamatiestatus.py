from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ReclamatiestatusReferentiedata(Referentiedata):
    pass


class Reclamatiestatus(Referentiedatasoort):
    afgewezen = ReclamatiestatusReferentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    De reclamatie is afgewezen door commissie.
    """

    in_beroep = ReclamatiestatusReferentiedata(
        code="BER",
        naam="In beroep",
    )
    """
    De reclamatie is in beroep gegaan door de woningzoekende.
    """

    in_behandeling = ReclamatiestatusReferentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    De reclamatie is in behandeling genomen door de commissie.
    """

    ingediend = ReclamatiestatusReferentiedata(
        code="ING",
        naam="Ingediend",
    )
    """
    De reclamatie is ingediend door de woningzoekende.
    """

    toegekend = ReclamatiestatusReferentiedata(
        code="TOE",
        naam="Toegekend",
    )
    """
    De reclamatie is toegekend door de comissie.
    """
