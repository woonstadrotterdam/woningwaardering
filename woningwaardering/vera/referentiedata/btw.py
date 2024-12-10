from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BtwReferentiedata(Referentiedata):
    pass


class Btw(Referentiedatasoort):
    algemeen = BtwReferentiedata(
        code="ALG",
        naam="Algemeen",
    )
    """
    Over de grondslag (bijvoorbeeld een prijscomponent) is het algemene BTW-tarief van
    toepassing. Dit tarief wordt ook wel 'Hoog' genoemd.
    """

    nul = BtwReferentiedata(
        code="NUL",
        naam="Nul",
    )
    """
    Over de grondslag (bijvoorbeeld een prijscomponent) is het 0%-tarief voor de BTW van
    toepassing.
    """

    verlaagd = BtwReferentiedata(
        code="VER",
        naam="Verlaagd",
    )
    """
    Over de grondslag (bijvoorbeeld een prijscomponent) is het verlaagde BTW-tarief van
    toepassing.
    """

    vrijstelling = BtwReferentiedata(
        code="VRI",
        naam="Vrijstelling",
    )
    """
    De grondslag (bijvoorbeeld een prijscomponent) is vrijgesteld van BTW.
    """
