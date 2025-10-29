from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.relatiesoort import (
    Relatiesoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RelatiedetailsoortReferentiedata(Referentiedata):
    pass


class Relatiedetailsoort(Referentiedatasoort):
    huishouden = RelatiedetailsoortReferentiedata(
        code="HUI",
        naam="Huishouden",
        parent=Relatiesoort.relatiegroep,
    )
    """
    Een huishouden bestaat uit één of meer personen die op hetzelfde adres wonen en een
    economisch-consumptieve eenheid vormen. (CORA)
    """
