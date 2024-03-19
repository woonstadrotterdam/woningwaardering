from vera.bvg.generated import Referentiedata


class Medewerkerrol:
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
