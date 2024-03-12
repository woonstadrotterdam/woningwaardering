
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class GROOTBOEKREKENINGSOORT:

    rgs_omschrijving_verkort = Referentiedata(
        code="RGS Referentiecode",
        naam="RGS Omschrijving (verkort)",
    )
    # rgs_omschrijving_verkort = ("RGS Referentiecode", "RGS Omschrijving (verkort)")
