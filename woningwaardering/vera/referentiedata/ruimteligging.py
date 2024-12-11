from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RuimteliggingReferentiedata(Referentiedata):
    pass


class Ruimteligging(Referentiedatasoort):
    noord = RuimteliggingReferentiedata(
        code="NOO",
        naam="Noord",
    )

    noordoost = RuimteliggingReferentiedata(
        code="NOS",
        naam="Noordoost",
    )

    noordwest = RuimteliggingReferentiedata(
        code="NWE",
        naam="Noordwest",
    )

    oost = RuimteliggingReferentiedata(
        code="OOS",
        naam="Oost",
    )

    west = RuimteliggingReferentiedata(
        code="WES",
        naam="West",
    )

    zuidoost = RuimteliggingReferentiedata(
        code="ZOO",
        naam="Zuidoost",
    )

    zuid = RuimteliggingReferentiedata(
        code="ZUI",
        naam="Zuid",
    )

    zuidwest = RuimteliggingReferentiedata(
        code="ZWE",
        naam="Zuidwest",
    )
