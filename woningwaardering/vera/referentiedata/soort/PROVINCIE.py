
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PROVINCIE:

    drenthe = Referentiedata(
        code="DR",
        naam="Drenthe",
    )
    # drenthe = ("DR", "Drenthe")

    flevoland = Referentiedata(
        code="FL",
        naam="Flevoland",
    )
    # flevoland = ("FL", "Flevoland")

    fryslan = Referentiedata(
        code="FR",
        naam="Fryslân",
    )
    # fryslan = ("FR", "Fryslân")

    gelderland = Referentiedata(
        code="GE",
        naam="Gelderland",
    )
    # gelderland = ("GE", "Gelderland")

    groningen = Referentiedata(
        code="GR",
        naam="Groningen",
    )
    # groningen = ("GR", "Groningen")

    limburg = Referentiedata(
        code="LI",
        naam="Limburg",
    )
    # limburg = ("LI", "Limburg")

    noord_brabant = Referentiedata(
        code="NB",
        naam="Noord-Brabant",
    )
    # noord_brabant = ("NB", "Noord-Brabant")

    noord_holland = Referentiedata(
        code="NH",
        naam="Noord-Holland",
    )
    # noord_holland = ("NH", "Noord-Holland")

    overijssel = Referentiedata(
        code="OV",
        naam="Overijssel",
    )
    # overijssel = ("OV", "Overijssel")

    utrecht = Referentiedata(
        code="UT",
        naam="Utrecht",
    )
    # utrecht = ("UT", "Utrecht")

    zeeland = Referentiedata(
        code="ZE",
        naam="Zeeland",
    )
    # zeeland = ("ZE", "Zeeland")
    """
    Buitenlandse provincie is wel referentiedata maar wordt niet beheert binnen de
    standaard.
    """

    zuid_holland = Referentiedata(
        code="ZH",
        naam="Zuid-Holland",
    )
    # zuid_holland = ("ZH", "Zuid-Holland")
