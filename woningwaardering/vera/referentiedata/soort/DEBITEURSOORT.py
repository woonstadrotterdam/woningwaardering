
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class DEBITEURSOORT:

    debiteur_gemeente = Referentiedata(
        code="DGM",
        naam="Debiteur gemeente",
    )
    # debiteur_gemeente = ("DGM", "Debiteur gemeente")

    debiteur_overheid = Referentiedata(
        code="DOH",
        naam="Debiteur overheid",
    )
    # debiteur_overheid = ("DOH", "Debiteur overheid")

    huurdebiteur = Referentiedata(
        code="HUU",
        naam="Huurdebiteur",
    )
    # huurdebiteur = ("HUU", "Huurdebiteur")

    overige_debiteur = Referentiedata(
        code="OVE",
        naam="Overige debiteur",
    )
    # overige_debiteur = ("OVE", "Overige debiteur")
