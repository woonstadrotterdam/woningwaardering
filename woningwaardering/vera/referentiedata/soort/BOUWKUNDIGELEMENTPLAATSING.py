
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BOUWKUNDIGELEMENTPLAATSING:

    individuele_wmo_voorziening = Referentiedata(
        code="IWV",
        naam="Individuele WMO voorziening",
    )
    # individuele_wmo_voorziening = ("IWV", "Individuele WMO voorziening")
    """
    Het bouwkundig element is aangebracht als individuele WMO voorziening.
    """

    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )
    # overig = ("OVE", "Overig")
    """
    Het bouwkundig element is aangebracht zonder dat deze onder een specifieke regeling
    (ZAV, WMO) valt.
    """

    wet_maatschappelijke_ondersteuning = Referentiedata(
        code="WMO",
        naam="Wet maatschappelijke ondersteuning",
    )
    # wet_maatschappelijke_ondersteuning = ("WMO", "Wet maatschappelijke ondersteuning")
    """
    Het bouwkundig element is aangebracht onder de voorwaarden van de Wet
    Maatschappelijke Ondersteuning.
    """

    zelf_aangebrachte_voorziening = Referentiedata(
        code="ZAV",
        naam="Zelf aangebrachte voorziening",
    )
    # zelf_aangebrachte_voorziening = ("ZAV", "Zelf aangebrachte voorziening")
    """
    Het bouwkundig element is aangebracht als zelf aangebrachte voorziening.
    """
