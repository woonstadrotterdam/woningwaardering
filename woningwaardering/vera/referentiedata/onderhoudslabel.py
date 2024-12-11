from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OnderhoudslabelReferentiedata(Referentiedata):
    pass


class Onderhoudslabel(Referentiedatasoort):
    basis_onderhoud = OnderhoudslabelReferentiedata(
        code="BAS",
        naam="Basis onderhoud",
    )

    geen_onderhoud = OnderhoudslabelReferentiedata(
        code="GEE",
        naam="Geen onderhoud",
    )

    monument_onderhoud = OnderhoudslabelReferentiedata(
        code="MON",
        naam="Monument onderhoud",
    )

    volledig_onderhoud = OnderhoudslabelReferentiedata(
        code="VOL",
        naam="Volledig onderhoud",
    )

    wind_en_waterdicht_houden = OnderhoudslabelReferentiedata(
        code="WIN",
        naam="Wind en waterdicht houden",
    )
