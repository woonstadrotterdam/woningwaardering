from woningwaardering.vera.bvg.models import Referentiedata


class BTW:
    algemeen = Referentiedata(
        code="ALG",
        naam="Algemeen",
    )
    """
    Over de grondslag (bijvoorbeeld een prijscomponent) is het algemene BTW-tarief van
    toepassing. Dit tarief wordt ook wel &#39;Hoog&#39; genoemd.
    """

    nul = Referentiedata(
        code="NUL",
        naam="Nul",
    )
    """
    Over de grondslag (bijvoorbeeld een prijscomponent) is het 0%-tarief voor de BTW van
    toepassing.
    """

    verlaagd = Referentiedata(
        code="VER",
        naam="Verlaagd",
    )
    """
    Over de grondslag (bijvoorbeeld een prijscomponent) is het verlaagde BTW-tarief van
    toepassing.
    """

    vrijstelling = Referentiedata(
        code="VRI",
        naam="Vrijstelling",
    )
    """
    De grondslag (bijvoorbeeld een prijscomponent) is vrijgesteld van BTW.
    """
