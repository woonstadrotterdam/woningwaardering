
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class MEDEWERKERROL:

    bhv_er = Referentiedata(
        code="BHV",
        naam="BHV-er",
    )
    # bhv_er = ("BHV", "BHV-er")

    scrummaster = Referentiedata(
        code="SCR",
        naam="Scrummaster",
    )
    # scrummaster = ("SCR", "Scrummaster")

    vertrouwenspersoon = Referentiedata(
        code="VER",
        naam="Vertrouwenspersoon",
    )
    # vertrouwenspersoon = ("VER", "Vertrouwenspersoon")
