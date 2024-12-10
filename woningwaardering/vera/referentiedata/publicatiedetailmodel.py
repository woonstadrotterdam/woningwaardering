from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.publicatiemodel import (
    Publicatiemodel,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PublicatiedetailmodelReferentiedata(Referentiedata):
    pass


class Publicatiedetailmodel(Referentiedatasoort):
    leefstijl = PublicatiedetailmodelReferentiedata(
        code="LEE",
        naam="Leefstijl",
        parent=Publicatiemodel.aanbodmodel,
    )
    """
    Eenheden in kwetsbare buurten waarbij leefstijl een belangrijke factor speelt.
    """

    loting = PublicatiedetailmodelReferentiedata(
        code="LOT",
        naam="Loting",
        parent=Publicatiemodel.aanbodmodel,
    )
    """
    Binnen het aanbodmodel wordt geloot nadat eerst een selectie heeft plaatsgevonden.
    """

    omklapcontract = PublicatiedetailmodelReferentiedata(
        code="OMK",
        naam="Omklapcontract",
        parent=Publicatiemodel.distributiemodel,
    )
    """
    Ccontract dat de eerste periode, bijv. een jaar, op naam van een zorgaanbieder of
    begeleidende instantie staat, die de woning doorverhuurt aan een kandidaat die
    moet leren zelfstandig te wonen: als dit goed uitpakt wordt het contract
    omgeklapt, d.w.z. komt het op zijn eigen naam te staan.
    """

    snelzoek = PublicatiedetailmodelReferentiedata(
        code="SNE",
        naam="Snelzoek",
        parent=Publicatiemodel.lotingmodel,
    )
    """
    Eenheden voor huishoudens die snel een woning nodig hebben en daar geen eisen aan
    stellen.
    """
