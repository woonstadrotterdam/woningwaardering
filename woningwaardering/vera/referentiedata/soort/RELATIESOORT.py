
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class RELATIESOORT:

    relatiegroep = Referentiedata(
        code="GRO",
        naam="Relatiegroep",
    )
    # relatiegroep = ("GRO", "Relatiegroep")
    """
    Een verzameling relaties (bijvoorbeeld een huishouden)
    """

    natuurlijke_persoon = Referentiedata(
        code="NAT",
        naam="Natuurlijke persoon",
    )
    # natuurlijke_persoon = ("NAT", "Natuurlijke persoon")
    """
    Een natuurlijk persoon is iemand, een mens van vlees en bloed, die rechten en
    plichten heeft.
    """

    rechtspersoon = Referentiedata(
        code="REC",
        naam="Rechtspersoon",
    )
    # rechtspersoon = ("REC", "Rechtspersoon")
    """
    Een rechtspersoon is een juridische constructie waardoor een abstracte entiteit of
    organisatie op kan treden als een volwaardig en handelingsbekwaam persoon in het
    rechtsverkeer behept met rechten en plichten zoals een natuurlijk persoon dat kan
    doen.
    """
