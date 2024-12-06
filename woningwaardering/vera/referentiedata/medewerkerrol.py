from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Medewerkerrol(Referentiedatasoort):
    bhv_er = Referentiedata(
        code="BHV",
        naam="BHV-er",
    )

    scrummaster = Referentiedata(
        code="SCR",
        naam="Scrummaster",
    )

    vertrouwenspersoon = Referentiedata(
        code="VER",
        naam="Vertrouwenspersoon",
    )
