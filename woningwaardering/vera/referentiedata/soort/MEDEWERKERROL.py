from woningwaardering.vera.bvg.models import Referentiedata


class MEDEWERKERROL:
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
