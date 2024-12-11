from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ProvincieReferentiedata(Referentiedata):
    pass


class Provincie(Referentiedatasoort):
    drenthe = ProvincieReferentiedata(
        code="DR",
        naam="Drenthe",
    )

    flevoland = ProvincieReferentiedata(
        code="FL",
        naam="Flevoland",
    )

    fryslan = ProvincieReferentiedata(
        code="FR",
        naam="Fryslân",
    )

    gelderland = ProvincieReferentiedata(
        code="GE",
        naam="Gelderland",
    )

    groningen = ProvincieReferentiedata(
        code="GR",
        naam="Groningen",
    )

    limburg = ProvincieReferentiedata(
        code="LI",
        naam="Limburg",
    )

    noord_brabant = ProvincieReferentiedata(
        code="NB",
        naam="Noord-Brabant",
    )

    noord_holland = ProvincieReferentiedata(
        code="NH",
        naam="Noord-Holland",
    )

    overijssel = ProvincieReferentiedata(
        code="OV",
        naam="Overijssel",
    )

    utrecht = ProvincieReferentiedata(
        code="UT",
        naam="Utrecht",
    )

    zeeland = ProvincieReferentiedata(
        code="ZE",
        naam="Zeeland",
    )
    """
    Buitenlandse provincie is wel referentiedata maar wordt niet beheert binnen de
    standaard.
    """

    zuid_holland = ProvincieReferentiedata(
        code="ZH",
        naam="Zuid-Holland",
    )
