from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class DebiteursoortReferentiedata(Referentiedata):
    pass


class Debiteursoort(Referentiedatasoort):
    debiteur_gemeente = DebiteursoortReferentiedata(
        code="DGM",
        naam="Debiteur gemeente",
    )

    debiteur_overheid = DebiteursoortReferentiedata(
        code="DOH",
        naam="Debiteur overheid",
    )

    huurdebiteur = DebiteursoortReferentiedata(
        code="HUU",
        naam="Huurdebiteur",
    )

    overige_debiteur = DebiteursoortReferentiedata(
        code="OVE",
        naam="Overige debiteur",
    )
