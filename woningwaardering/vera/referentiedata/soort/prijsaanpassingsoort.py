from vera.referentiedata.models import Referentiedata


class Prijsaanpassingsoort:
    korting = Referentiedata(
        code="KOR",
        naam="Korting",
    )

    toeslag = Referentiedata(
        code="TOE",
        naam="Toeslag",
    )
