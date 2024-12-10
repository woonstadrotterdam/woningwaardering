from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class GrootboekrekeningsoortReferentiedata(Referentiedata):
    pass


class Grootboekrekeningsoort(Referentiedatasoort):
    rgs_omschrijving_verkort = GrootboekrekeningsoortReferentiedata(
        code="RGS Referentiecode",
        naam="RGS Omschrijving (verkort)",
    )
