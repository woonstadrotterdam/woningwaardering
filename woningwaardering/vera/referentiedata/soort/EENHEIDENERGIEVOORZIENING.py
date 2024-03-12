
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDENERGIEVOORZIENING:

    gasloze_eenheid = Referentiedata(
        code="GLO",
        naam="Gasloze eenheid",
    )
    # gasloze_eenheid = ("GLO", "Gasloze eenheid")
    """
    Kenmerk om aan te geven dat de eenheid géén gasaansluiting heeft
    """

    nul_op_de_meter_eenheid = Referentiedata(
        code="NOM",
        naam="Nul-op-de-meter eenheid",
    )
    # nul_op_de_meter_eenheid = ("NOM", "Nul-op-de-meter eenheid")
    """
    De eenheid voldoet aan de criteria voor nul-op-de-meter
    """

    oplaadpunt = Referentiedata(
        code="OPL",
        naam="Oplaadpunt",
    )
    # oplaadpunt = ("OPL", "Oplaadpunt")
    """
    Oplaadpunt voor auto
    """

    oplaadpunt_scootmobiel = Referentiedata(
        code="OPS",
        naam="Oplaadpunt scootmobiel",
    )
    # oplaadpunt_scootmobiel = ("OPS", "Oplaadpunt scootmobiel")
    """
    Oplaadpunt voor scootmobiel, als deze in of aan de woning is bevestigd. Een
    oplaadpunt kan ook als afzonderlijke eenheid worden geëxploiteerd, gebruik dan
    Eenheiddetailsoort Scootmobielplek
    """

    zonnepanelen = Referentiedata(
        code="ZON",
        naam="Zonnepanelen",
    )
    # zonnepanelen = ("ZON", "Zonnepanelen")
