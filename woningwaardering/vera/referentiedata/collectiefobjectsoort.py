from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class CollectiefobjectsoortReferentiedata(Referentiedata):
    pass


class Collectiefobjectsoort(Referentiedatasoort):
    achterpad = CollectiefobjectsoortReferentiedata(
        code="APD",
        naam="Achterpad",
    )

    casco = CollectiefobjectsoortReferentiedata(
        code="CAS",
        naam="Casco",
    )
    """
    Gevel e.d.
    """

    centrale_hal = CollectiefobjectsoortReferentiedata(
        code="CEH",
        naam="Centrale hal",
    )

    dak = CollectiefobjectsoortReferentiedata(
        code="DAK",
        naam="Dak",
    )

    galerij = CollectiefobjectsoortReferentiedata(
        code="GAL",
        naam="Galerij",
    )

    lift = CollectiefobjectsoortReferentiedata(
        code="LIF",
        naam="Lift",
    )

    onderdoorgang = CollectiefobjectsoortReferentiedata(
        code="ONG",
        naam="Onderdoorgang",
    )

    parkeergarage = CollectiefobjectsoortReferentiedata(
        code="PAG",
        naam="Parkeergarage",
    )

    recreatie_en_of_ontmoetingsruimte = CollectiefobjectsoortReferentiedata(
        code="ROR",
        naam="Recreatie-/ontmoetingsruimte",
    )

    speelplaats = CollectiefobjectsoortReferentiedata(
        code="SPP",
        naam="Speelplaats",
    )

    stortkoker = CollectiefobjectsoortReferentiedata(
        code="STK",
        naam="Stortkoker",
    )

    terrein = CollectiefobjectsoortReferentiedata(
        code="TER",
        naam="Terrein",
    )
    """
    Parkeerterrein, buitenterrein
    """

    trappenhuis = CollectiefobjectsoortReferentiedata(
        code="TRH",
        naam="Trappenhuis",
    )

    technische_ruimte = CollectiefobjectsoortReferentiedata(
        code="TRU",
        naam="Technische ruimte",
    )

    tuin = CollectiefobjectsoortReferentiedata(
        code="TUI",
        naam="Tuin",
    )
    """
    Gemeenschappelijke tuin
    """

    gemeenschappelijke_badkamer = CollectiefobjectsoortReferentiedata(
        code="BDK",
        naam="Gemeenschappelijke badkamer",
    )
    """
    Gemeenschappelijke badkamer
    """

    gemeenschappelijk_balkon = CollectiefobjectsoortReferentiedata(
        code="BAL",
        naam="Gemeenschappelijk balkon",
    )
    """
    Gemeenschappelijk balkon
    """

    gemeenschappelijke_berging = CollectiefobjectsoortReferentiedata(
        code="BER",
        naam="Gemeenschappelijke berging",
    )
    """
    Gemeenschappelijke berging of berginsgsgang
    """

    gemeenschappelijke_fietsenstalling = CollectiefobjectsoortReferentiedata(
        code="FTS",
        naam="Gemeenschappelijke fietsenstalling",
    )
    """
    Gemeenschappelijke fietsenstalling
    """

    gemeenschappeijke_keuken = CollectiefobjectsoortReferentiedata(
        code="KEU",
        naam="Gemeenschappeijke keuken",
    )
    """
    Gemeenschappelijke keuken
    """

    gemeenschappelijke_toilet = CollectiefobjectsoortReferentiedata(
        code="TOI",
        naam="Gemeenschappelijke toilet",
    )
    """
    Gemeenschappelijk toilet
    """

    wasruimte = CollectiefobjectsoortReferentiedata(
        code="WAS",
        naam="Wasruimte",
    )
    """
    Een gemeenschappelijke wasruimte.
    """
