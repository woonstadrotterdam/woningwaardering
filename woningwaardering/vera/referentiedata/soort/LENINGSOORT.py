from woningwaardering.vera.bvg.models import Referentiedata


class LENINGSOORT:
    kredietfaciliteit = Referentiedata(
        code="KRE",
        naam="Kredietfaciliteit",
    )

    lening = Referentiedata(
        code="LEN",
        naam="Lening",
    )
