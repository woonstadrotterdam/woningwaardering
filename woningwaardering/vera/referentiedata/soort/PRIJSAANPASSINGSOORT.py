from woningwaardering.vera.bvg.models import Referentiedata


class PRIJSAANPASSINGSOORT:
    korting = Referentiedata(
        code="KOR",
        naam="Korting",
    )

    toeslag = Referentiedata(
        code="TOE",
        naam="Toeslag",
    )
