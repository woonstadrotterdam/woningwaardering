from vera.referentiedata.models import Referentiedata


class Signaleringstatus:
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )

    passief = Referentiedata(
        code="PAS",
        naam="Passief",
    )

    vervallen = Referentiedata(
        code="VER",
        naam="Vervallen",
    )
