from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class MedewerkerrolReferentiedata(Referentiedata):
    pass


class Medewerkerrol(Referentiedatasoort):
    bhv_er = MedewerkerrolReferentiedata(
        code="BHV",
        naam="BHV-er",
    )

    scrummaster = MedewerkerrolReferentiedata(
        code="SCR",
        naam="Scrummaster",
    )

    vertrouwenspersoon = MedewerkerrolReferentiedata(
        code="VER",
        naam="Vertrouwenspersoon",
    )
