from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Grootboekrekeningsoort(Referentiedatasoort):
    rgs_omschrijving_verkort = Referentiedata(
        code="RGS Referentiecode",
        naam="RGS Omschrijving (verkort)",
    )
