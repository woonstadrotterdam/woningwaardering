from woningwaardering.vera.bvg.generated import Referentiedata


class Publicatiedetailmodel:
    leefstijl = Referentiedata(
        code="LEE",
        naam="Leefstijl",
    )
    """
    Eenheden in kwetsbare buurten waarbij leefstijl een belangrijke factor speelt.
    """

    loting = Referentiedata(
        code="LOT",
        naam="Loting",
    )
    """
    Binnen het aanbodmodel wordt geloot nadat eerst een selectie heeft plaatsgevonden.
    """

    omklapcontract = Referentiedata(
        code="OMK",
        naam="Omklapcontract",
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
    )
    """
    Eenheden voor huishoudens die snel een woning nodig hebben en daar geen eisen aan
    stellen.
    """
