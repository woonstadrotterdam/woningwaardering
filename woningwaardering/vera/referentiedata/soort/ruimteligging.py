from vera.referentiedata.models import Referentiedata


class Ruimteligging:
    noord = Referentiedata(
        code="NOO",
        naam="Noord",
    )

    noordoost = Referentiedata(
        code="NOS",
        naam="Noordoost",
    )

    noordwest = Referentiedata(
        code="NWE",
        naam="Noordwest",
    )

    oost = Referentiedata(
        code="OOS",
        naam="Oost",
    )

    west = Referentiedata(
        code="WES",
        naam="West",
    )

    zuidoost = Referentiedata(
        code="ZOO",
        naam="Zuidoost",
    )

    zuid = Referentiedata(
        code="ZUI",
        naam="Zuid",
    )

    zuidwest = Referentiedata(
        code="ZWE",
        naam="Zuidwest",
    )
