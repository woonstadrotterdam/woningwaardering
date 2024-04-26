from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidenergievoorziening(Enum):
    gasloze_eenheid = Referentiedata(
        code="GLO",
        naam="Gasloze eenheid",
    )
    """
    Kenmerk om aan te geven dat de eenheid géén gasaansluiting heeft
    """

    nul_op_de_meter_eenheid = Referentiedata(
        code="NOM",
        naam="Nul-op-de-meter eenheid",
    )
    """
    De eenheid voldoet aan de criteria voor nul-op-de-meter
    """

    oplaadpunt = Referentiedata(
        code="OPL",
        naam="Oplaadpunt",
    )
    """
    Oplaadpunt voor auto
    """

    oplaadpunt_scootmobiel = Referentiedata(
        code="OPS",
        naam="Oplaadpunt scootmobiel",
    )
    """
    Oplaadpunt voor scootmobiel, als deze in of aan de woning is bevestigd. Een
    oplaadpunt kan ook als afzonderlijke eenheid worden geëxploiteerd, gebruik dan
    Eenheiddetailsoort Scootmobielplek
    """

    zonnepanelen = Referentiedata(
        code="ZON",
        naam="Zonnepanelen",
    )

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
