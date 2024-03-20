from woningwaardering.vera.bvg.generated import Referentiedata


class Prijsaanpassingsoort:
    korting = Referentiedata(
        code="KOR",
        naam="Korting",
    )

    toeslag = Referentiedata(
        code="TOE",
        naam="Toeslag",
    )
