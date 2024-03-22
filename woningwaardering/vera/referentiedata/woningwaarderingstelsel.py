from woningwaardering.vera.bvg.generated import Referentiedata


class Woningwaarderingstelsel:
    onzelfstandige_woonruimten = Referentiedata(
        code="ONZ",
        naam="Onzelfstandige woonruimten",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    onzelfstandig woonruimten
    """

    standplaatsen = Referentiedata(
        code="STA",
        naam="Standplaatsen",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    standplaatsen
    """

    woonwagens = Referentiedata(
        code="WOO",
        naam="Woonwagens",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    woonwagens
    """

    zelfstandige_woonruimten = Referentiedata(
        code="ZEL",
        naam="Zelfstandige woonruimten",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    zelfstandig woonruimten
    """
