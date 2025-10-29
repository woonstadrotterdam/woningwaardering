from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class WoningwaarderingstelselReferentiedata(Referentiedata):
    pass


class Woningwaarderingstelsel(Referentiedatasoort):
    onzelfstandige_woonruimten = WoningwaarderingstelselReferentiedata(
        code="ONZ",
        naam="Onzelfstandige woonruimten",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    onzelfstandig woonruimten
    """

    standplaatsen = WoningwaarderingstelselReferentiedata(
        code="STA",
        naam="Standplaatsen",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    standplaatsen
    """

    woonwagens = WoningwaarderingstelselReferentiedata(
        code="WOO",
        naam="Woonwagens",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    woonwagens
    """

    zelfstandige_woonruimten = WoningwaarderingstelselReferentiedata(
        code="ZEL",
        naam="Zelfstandige woonruimten",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    zelfstandig woonruimten
    """
