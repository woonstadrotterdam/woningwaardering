
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ONDERHOUDSLABEL:

    basis_onderhoud = Referentiedata(
        code="BAS",
        naam="Basis onderhoud",
    )
    # basis_onderhoud = ("BAS", "Basis onderhoud")

    geen_onderhoud = Referentiedata(
        code="GEE",
        naam="Geen onderhoud",
    )
    # geen_onderhoud = ("GEE", "Geen onderhoud")

    monument_onderhoud = Referentiedata(
        code="MON",
        naam="Monument onderhoud",
    )
    # monument_onderhoud = ("MON", "Monument onderhoud")

    volledig_onderhoud = Referentiedata(
        code="VOL",
        naam="Volledig onderhoud",
    )
    # volledig_onderhoud = ("VOL", "Volledig onderhoud")

    wind_en_waterdicht_houden = Referentiedata(
        code="WIN",
        naam="Wind en waterdicht houden",
    )
    # wind_en_waterdicht_houden = ("WIN", "Wind en waterdicht houden")
