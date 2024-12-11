from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BouwkundigelementplaatsingReferentiedata(Referentiedata):
    pass


class Bouwkundigelementplaatsing(Referentiedatasoort):
    individuele_wmo_voorziening = BouwkundigelementplaatsingReferentiedata(
        code="IWV",
        naam="Individuele WMO voorziening",
    )
    """
    Het bouwkundig element is aangebracht als individuele WMO voorziening.
    """

    overig = BouwkundigelementplaatsingReferentiedata(
        code="OVE",
        naam="Overig",
    )
    """
    Het bouwkundig element is aangebracht zonder dat deze onder een specifieke regeling
    (ZAV, WMO) valt.
    """

    wet_maatschappelijke_ondersteuning = BouwkundigelementplaatsingReferentiedata(
        code="WMO",
        naam="Wet maatschappelijke ondersteuning",
    )
    """
    Het bouwkundig element is aangebracht onder de voorwaarden van de Wet
    Maatschappelijke Ondersteuning.
    """

    zelf_aangebrachte_voorziening = BouwkundigelementplaatsingReferentiedata(
        code="ZAV",
        naam="Zelf aangebrachte voorziening",
    )
    """
    Het bouwkundig element is aangebracht als zelf aangebrachte voorziening.
    """
