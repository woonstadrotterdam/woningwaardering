from vera.referentiedata.models import Referentiedata


class Provincie:
    drenthe = Referentiedata(
        code="DR",
        naam="Drenthe",
    )

    flevoland = Referentiedata(
        code="FL",
        naam="Flevoland",
    )

    fryslan = Referentiedata(
        code="FR",
        naam="Fryslân",
    )

    gelderland = Referentiedata(
        code="GE",
        naam="Gelderland",
    )

    groningen = Referentiedata(
        code="GR",
        naam="Groningen",
    )

    limburg = Referentiedata(
        code="LI",
        naam="Limburg",
    )

    noord_brabant = Referentiedata(
        code="NB",
        naam="Noord-Brabant",
    )

    noord_holland = Referentiedata(
        code="NH",
        naam="Noord-Holland",
    )

    overijssel = Referentiedata(
        code="OV",
        naam="Overijssel",
    )

    utrecht = Referentiedata(
        code="UT",
        naam="Utrecht",
    )

    zeeland = Referentiedata(
        code="ZE",
        naam="Zeeland",
    )
    """
    Buitenlandse provincie is wel referentiedata maar wordt niet beheert binnen de
    standaard.
    """

    zuid_holland = Referentiedata(
        code="ZH",
        naam="Zuid-Holland",
    )
