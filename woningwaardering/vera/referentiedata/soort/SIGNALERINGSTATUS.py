from woningwaardering.vera.bvg.models import Referentiedata


class SIGNALERINGSTATUS:
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
