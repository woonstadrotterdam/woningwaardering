from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.publicatiemodel import Publicatiemodel


class Publicatiedetailmodel(Enum):
    leefstijl = Referentiedata(
        code="LEE",
        naam="Leefstijl",
        parent=Publicatiemodel.aanbodmodel.value,
    )
    """
    Eenheden in kwetsbare buurten waarbij leefstijl een belangrijke factor speelt.
    """

    loting = Referentiedata(
        code="LOT",
        naam="Loting",
        parent=Publicatiemodel.aanbodmodel.value,
    )
    """
    Binnen het aanbodmodel wordt geloot nadat eerst een selectie heeft plaatsgevonden.
    """

    omklapcontract = Referentiedata(
        code="OMK",
        naam="Omklapcontract",
        parent=Publicatiemodel.distributiemodel.value,
    )
    """
    Ccontract dat de eerste periode, bijv. een jaar, op naam van een zorgaanbieder of
    begeleidende instantie staat, die de woning doorverhuurt aan een kandidaat die
    moet leren zelfstandig te wonen: als dit goed uitpakt wordt het contract
    omgeklapt, d.w.z. komt het op zijn eigen naam te staan.
    """

    snelzoek = Referentiedata(
        code="SNE",
        naam="Snelzoek",
        parent=Publicatiemodel.lotingmodel.value,
    )
    """
    Eenheden voor huishoudens die snel een woning nodig hebben en daar geen eisen aan
    stellen.
    """

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
