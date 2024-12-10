from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PublicatiestatusReferentiedata(Referentiedata):
    pass


class Publicatiestatus(Referentiedatasoort):
    in_aanbieding = PublicatiestatusReferentiedata(
        code="AAN",
        naam="In aanbieding",
    )
    """
    Het gepubliceerde vastgoed is in aanbieding.
    """

    afgerond = PublicatiestatusReferentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    De publicatie van het vastgoed is afgerond.
    """

    gepubliceerd = PublicatiestatusReferentiedata(
        code="GEP",
        naam="Gepubliceerd",
    )
    """
    Het beschikbaar vastgoed is gepubliceerd.
    """

    gereed_voor_publicatie = PublicatiestatusReferentiedata(
        code="GER",
        naam="Gereed voor publicatie",
    )
    """
    De publicatie van beschikbaar vastgoed is gereed voor publicatie.
    """

    ingetrokken = PublicatiestatusReferentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    """
    De publicatie van het vastgoed is ingetrokken.
    """

    in_voorbereiding = PublicatiestatusReferentiedata(
        code="VOO",
        naam="In voorbereiding",
    )
    """
    De publicatie van beschikbaar vastgoed is in voorbereiding.
    """
