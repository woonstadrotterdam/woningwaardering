
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class COLLECTIEFOBJECTSOORT:

    achterpad = Referentiedata(
        code="APD",
        naam="Achterpad",
    )
    # achterpad = ("APD", "Achterpad")

    casco = Referentiedata(
        code="CAS",
        naam="Casco",
    )
    # casco = ("CAS", "Casco")
    """
    Gevel e.d.
    """

    centrale_hal = Referentiedata(
        code="CEH",
        naam="Centrale hal",
    )
    # centrale_hal = ("CEH", "Centrale hal")

    dak = Referentiedata(
        code="DAK",
        naam="Dak",
    )
    # dak = ("DAK", "Dak")

    galerij = Referentiedata(
        code="GAL",
        naam="Galerij",
    )
    # galerij = ("GAL", "Galerij")

    lift = Referentiedata(
        code="LIF",
        naam="Lift",
    )
    # lift = ("LIF", "Lift")

    onderdoorgang = Referentiedata(
        code="ONG",
        naam="Onderdoorgang",
    )
    # onderdoorgang = ("ONG", "Onderdoorgang")

    parkeergarage = Referentiedata(
        code="PAG",
        naam="Parkeergarage",
    )
    # parkeergarage = ("PAG", "Parkeergarage")

    recreatie_of_ontmoetingsruimte = Referentiedata(
        code="ROR",
        naam="Recreatie-/ontmoetingsruimte",
    )
    # recreatie_of_ontmoetingsruimte = ("ROR", "Recreatie-/ontmoetingsruimte")

    speelplaats = Referentiedata(
        code="SPP",
        naam="Speelplaats",
    )
    # speelplaats = ("SPP", "Speelplaats")

    stortkoker = Referentiedata(
        code="STK",
        naam="Stortkoker",
    )
    # stortkoker = ("STK", "Stortkoker")

    terrein = Referentiedata(
        code="TER",
        naam="Terrein",
    )
    # terrein = ("TER", "Terrein")
    """
    Parkeerterrein, buitenterrein
    """

    trappenhuis = Referentiedata(
        code="TRH",
        naam="Trappenhuis",
    )
    # trappenhuis = ("TRH", "Trappenhuis")

    technische_ruimte = Referentiedata(
        code="TRU",
        naam="Technische ruimte",
    )
    # technische_ruimte = ("TRU", "Technische ruimte")

    tuin = Referentiedata(
        code="TUI",
        naam="Tuin",
    )
    # tuin = ("TUI", "Tuin")
    """
    Gemeenschappelijke tuin
    """

    gemeenschappelijke_badkamer = Referentiedata(
        code="BDK",
        naam="Gemeenschappelijke badkamer",
    )
    # gemeenschappelijke_badkamer = ("BDK", "Gemeenschappelijke badkamer")
    """
    Gemeenschappelijke badkamer
    """

    gemeenschappelijk_balkon = Referentiedata(
        code="BAL",
        naam="Gemeenschappelijk balkon",
    )
    # gemeenschappelijk_balkon = ("BAL", "Gemeenschappelijk balkon")
    """
    Gemeenschappelijk balkon
    """

    gemeenschappelijke_berging = Referentiedata(
        code="BER",
        naam="Gemeenschappelijke berging",
    )
    # gemeenschappelijke_berging = ("BER", "Gemeenschappelijke berging")
    """
    Gemeenschappelijke berging of berginsgsgang
    """

    gemeenschappelijke_fietsenstalling = Referentiedata(
        code="FTS",
        naam="Gemeenschappelijke fietsenstalling",
    )
    # gemeenschappelijke_fietsenstalling = ("FTS", "Gemeenschappelijke fietsenstalling")
    """
    Gemeenschappelijke fietsenstalling
    """

    gemeenschappeijke_keuken = Referentiedata(
        code="KEU",
        naam="Gemeenschappeijke keuken",
    )
    # gemeenschappeijke_keuken = ("KEU", "Gemeenschappeijke keuken")
    """
    Gemeenschappelijke keuken
    """

    gemeenschappelijke_toilet = Referentiedata(
        code="TOI",
        naam="Gemeenschappelijke toilet",
    )
    # gemeenschappelijke_toilet = ("TOI", "Gemeenschappelijke toilet")
    """
    Gemeenschappelijk toilet
    """
