from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidenergievoorzieningReferentiedata(Referentiedata):
    pass


class Eenheidenergievoorziening(Referentiedatasoort):
    gasloze_eenheid = EenheidenergievoorzieningReferentiedata(
        code="GLO",
        naam="Gasloze eenheid",
    )
    """
    Kenmerk om aan te geven dat de eenheid géén gasaansluiting heeft
    """

    nul_op_de_meter_eenheid = EenheidenergievoorzieningReferentiedata(
        code="NOM",
        naam="Nul-op-de-meter eenheid",
    )
    """
    De eenheid voldoet aan de criteria voor nul-op-de-meter
    """

    oplaadpunt = EenheidenergievoorzieningReferentiedata(
        code="OPL",
        naam="Oplaadpunt",
    )
    """
    Oplaadpunt voor auto
    """

    oplaadpunt_scootmobiel = EenheidenergievoorzieningReferentiedata(
        code="OPS",
        naam="Oplaadpunt scootmobiel",
    )
    """
    Oplaadpunt voor scootmobiel, als deze in of aan de woning is bevestigd. Een
    oplaadpunt kan ook als afzonderlijke eenheid worden geëxploiteerd, gebruik dan
    Eenheiddetailsoort Scootmobielplek
    """

    zonnepanelen = EenheidenergievoorzieningReferentiedata(
        code="ZON",
        naam="Zonnepanelen",
    )
