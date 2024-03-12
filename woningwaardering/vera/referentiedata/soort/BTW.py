
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BTW:

    algemeen = Referentiedata(
        code="ALG",
        naam="Algemeen",
    )
    # algemeen = ("ALG", "Algemeen")
    """
    Over de grondslag (bijvoorbeeld een prijscomponent) is het algemene BTW-tarief van
    toepassing. Dit tarief wordt ook wel 'Hoog' genoemd.
    """

    nul = Referentiedata(
        code="NUL",
        naam="Nul",
    )
    # nul = ("NUL", "Nul")
    """
    Over de grondslag (bijvoorbeeld een prijscomponent) is het 0%-tarief voor de BTW van
    toepassing.
    """

    verlaagd = Referentiedata(
        code="VER",
        naam="Verlaagd",
    )
    # verlaagd = ("VER", "Verlaagd")
    """
    Over de grondslag (bijvoorbeeld een prijscomponent) is het verlaagde BTW-tarief van
    toepassing.
    """

    vrijstelling = Referentiedata(
        code="VRI",
        naam="Vrijstelling",
    )
    # vrijstelling = ("VRI", "Vrijstelling")
    """
    De grondslag (bijvoorbeeld een prijscomponent) is vrijgesteld van BTW.
    """
