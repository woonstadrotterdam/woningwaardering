from woningwaardering.vera.bvg.models import Referentiedata


class DEBITEURSOORT:
    debiteur_gemeente = Referentiedata(
        code="DGM",
        naam="Debiteur gemeente",
    )

    debiteur_overheid = Referentiedata(
        code="DOH",
        naam="Debiteur overheid",
    )

    huurdebiteur = Referentiedata(
        code="HUU",
        naam="Huurdebiteur",
    )

    overige_debiteur = Referentiedata(
        code="OVE",
        naam="Overige debiteur",
    )
