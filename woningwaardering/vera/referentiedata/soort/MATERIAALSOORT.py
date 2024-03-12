
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class MATERIAALSOORT:

    beton = Referentiedata(
        code="BET",
        naam="Beton",
    )
    # beton = ("BET", "Beton")

    bitumen = Referentiedata(
        code="BIT",
        naam="Bitumen",
    )
    # bitumen = ("BIT", "Bitumen")

    cement = Referentiedata(
        code="CEM",
        naam="Cement",
    )
    # cement = ("CEM", "Cement")

    gips = Referentiedata(
        code="GIP",
        naam="Gips",
    )
    # gips = ("GIP", "Gips")

    glas = Referentiedata(
        code="GLA",
        naam="Glas",
    )
    # glas = ("GLA", "Glas")

    grondstof = Referentiedata(
        code="GRO",
        naam="Grondstof",
    )
    # grondstof = ("GRO", "Grondstof")

    hout = Referentiedata(
        code="HOU",
        naam="Hout",
    )
    # hout = ("HOU", "Hout")

    isolatie = Referentiedata(
        code="ISO",
        naam="Isolatie",
    )
    # isolatie = ("ISO", "Isolatie")

    kunststof = Referentiedata(
        code="KUN",
        naam="Kunststof",
    )
    # kunststof = ("KUN", "Kunststof")

    metaal = Referentiedata(
        code="MET",
        naam="Metaal",
    )
    # metaal = ("MET", "Metaal")

    natuursteen = Referentiedata(
        code="NAT",
        naam="Natuursteen",
    )
    # natuursteen = ("NAT", "Natuursteen")

    ntb = Referentiedata(
        code="NTB",
        naam="Ntb",
    )
    # ntb = ("NTB", "Ntb")

    rubber = Referentiedata(
        code="RUB",
        naam="Rubber",
    )
    # rubber = ("RUB", "Rubber")

    samengesteld = Referentiedata(
        code="SAM",
        naam="Samengesteld",
    )
    # samengesteld = ("SAM", "Samengesteld")

    steenachtig = Referentiedata(
        code="STE",
        naam="Steenachtig",
    )
    # steenachtig = ("STE", "Steenachtig")
