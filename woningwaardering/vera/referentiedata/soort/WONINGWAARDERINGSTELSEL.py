
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class WONINGWAARDERINGSTELSEL:

    onzelfstandige_woonruimten = Referentiedata(
        code="ONZ",
        naam="Onzelfstandige woonruimten",
    )
    # onzelfstandige_woonruimten = ("ONZ", "Onzelfstandige woonruimten")
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    onzelfstandig woonruimten
    """

    standplaatsen = Referentiedata(
        code="STA",
        naam="Standplaatsen",
    )
    # standplaatsen = ("STA", "Standplaatsen")
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    standplaatsen
    """

    woonwagens = Referentiedata(
        code="WOO",
        naam="Woonwagens",
    )
    # woonwagens = ("WOO", "Woonwagens")
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    woonwagens
    """

    zelfstandige_woonruimten = Referentiedata(
        code="ZEL",
        naam="Zelfstandige woonruimten",
    )
    # zelfstandige_woonruimten = ("ZEL", "Zelfstandige woonruimten")
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    zelfstandig woonruimten
    """
