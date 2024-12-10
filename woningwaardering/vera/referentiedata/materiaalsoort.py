from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class MateriaalsoortReferentiedata(Referentiedata):
    pass


class Materiaalsoort(Referentiedatasoort):
    beton = MateriaalsoortReferentiedata(
        code="BET",
        naam="Beton",
    )

    bitumen = MateriaalsoortReferentiedata(
        code="BIT",
        naam="Bitumen",
    )

    cement = MateriaalsoortReferentiedata(
        code="CEM",
        naam="Cement",
    )

    gips = MateriaalsoortReferentiedata(
        code="GIP",
        naam="Gips",
    )

    glas = MateriaalsoortReferentiedata(
        code="GLA",
        naam="Glas",
    )

    grondstof = MateriaalsoortReferentiedata(
        code="GRO",
        naam="Grondstof",
    )

    hout = MateriaalsoortReferentiedata(
        code="HOU",
        naam="Hout",
    )

    isolatie = MateriaalsoortReferentiedata(
        code="ISO",
        naam="Isolatie",
    )

    kunststof = MateriaalsoortReferentiedata(
        code="KUN",
        naam="Kunststof",
    )

    metaal = MateriaalsoortReferentiedata(
        code="MET",
        naam="Metaal",
    )

    natuursteen = MateriaalsoortReferentiedata(
        code="NAT",
        naam="Natuursteen",
    )

    ntb = MateriaalsoortReferentiedata(
        code="NTB",
        naam="Ntb",
    )

    organisch = MateriaalsoortReferentiedata(
        code="ORG",
        naam="Organisch",
    )

    rubber = MateriaalsoortReferentiedata(
        code="RUB",
        naam="Rubber",
    )

    samengesteld = MateriaalsoortReferentiedata(
        code="SAM",
        naam="Samengesteld",
    )

    steenachtig = MateriaalsoortReferentiedata(
        code="STE",
        naam="Steenachtig",
    )
