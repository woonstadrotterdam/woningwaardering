from vera.referentiedata.models import Referentiedata


class Onderhoudslabel:
    basis_onderhoud = Referentiedata(
        code="BAS",
        naam="Basis onderhoud",
    )

    geen_onderhoud = Referentiedata(
        code="GEE",
        naam="Geen onderhoud",
    )

    monument_onderhoud = Referentiedata(
        code="MON",
        naam="Monument onderhoud",
    )

    volledig_onderhoud = Referentiedata(
        code="VOL",
        naam="Volledig onderhoud",
    )

    wind_en_waterdicht_houden = Referentiedata(
        code="WIN",
        naam="Wind en waterdicht houden",
    )
