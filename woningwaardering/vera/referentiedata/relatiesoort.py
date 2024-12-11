from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RelatiesoortReferentiedata(Referentiedata):
    pass


class Relatiesoort(Referentiedatasoort):
    relatiegroep = RelatiesoortReferentiedata(
        code="GRO",
        naam="Relatiegroep",
    )
    """
    Een verzameling relaties (bijvoorbeeld een huishouden)
    """

    natuurlijke_persoon = RelatiesoortReferentiedata(
        code="NAT",
        naam="Natuurlijke persoon",
    )
    """
    Een natuurlijk persoon is iemand, een mens van vlees en bloed, die rechten en
    plichten heeft.
    """

    rechtspersoon = RelatiesoortReferentiedata(
        code="REC",
        naam="Rechtspersoon",
    )
    """
    Een rechtspersoon is een juridische constructie waardoor een abstracte entiteit of
    organisatie op kan treden als een volwaardig en handelingsbekwaam persoon in het
    rechtsverkeer behept met rechten en plichten zoals een natuurlijk persoon dat
    kan doen.
    """
