from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.materiaalsoort import (
    Materiaalsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class MateriaaldetailsoortReferentiedata(Referentiedata):
    pass


class Materiaaldetailsoort(Referentiedatasoort):
    ntb = MateriaaldetailsoortReferentiedata(
        code="NTB",
        naam="Ntb",
    )

    generiek = MateriaaldetailsoortReferentiedata(
        code="GEN",
        naam="Generiek",
    )

    gasbeton = MateriaaldetailsoortReferentiedata(
        code="GAS",
        naam="Gasbeton",
        parent=Materiaalsoort.beton,
    )

    bimsbeton = MateriaaldetailsoortReferentiedata(
        code="BIM",
        naam="Bimsbeton",
        parent=Materiaalsoort.beton,
    )

    isolatiebeton = MateriaaldetailsoortReferentiedata(
        code="ISO",
        naam="Isolatiebeton",
        parent=Materiaalsoort.beton,
    )

    lichtbeton = MateriaaldetailsoortReferentiedata(
        code="LIC",
        naam="Lichtbeton",
        parent=Materiaalsoort.beton,
    )

    slakkenbeton = MateriaaldetailsoortReferentiedata(
        code="SLA",
        naam="Slakkenbeton",
        parent=Materiaalsoort.beton,
    )

    voorgespannen = MateriaaldetailsoortReferentiedata(
        code="VOO",
        naam="Voorgespannen",
        parent=Materiaalsoort.beton,
    )

    cellenbeton = MateriaaldetailsoortReferentiedata(
        code="CEL",
        naam="Cellenbeton",
        parent=Materiaalsoort.beton,
    )

    gewapend = MateriaaldetailsoortReferentiedata(
        code="GEW",
        naam="Gewapend",
    )

    grindbeton = MateriaaldetailsoortReferentiedata(
        code="GBE",
        naam="Grindbeton",
        parent=Materiaalsoort.beton,
    )

    schuimbeton = MateriaaldetailsoortReferentiedata(
        code="SBE",
        naam="Schuimbeton",
        parent=Materiaalsoort.beton,
    )

    spuitbeton = MateriaaldetailsoortReferentiedata(
        code="SBT",
        naam="Spuitbeton",
        parent=Materiaalsoort.beton,
    )

    staalvezelbeton = MateriaaldetailsoortReferentiedata(
        code="SVE",
        naam="Staalvezelbeton",
        parent=Materiaalsoort.beton,
    )

    asfalt = MateriaaldetailsoortReferentiedata(
        code="ASF",
        naam="Asfalt",
        parent=Materiaalsoort.bitumen,
    )

    teer = MateriaaldetailsoortReferentiedata(
        code="TEE",
        naam="Teer",
        parent=Materiaalsoort.bitumen,
    )

    asbestcement = MateriaaldetailsoortReferentiedata(
        code="ACE",
        naam="Asbestcement",
        parent=Materiaalsoort.bitumen,
    )

    cementstuc = MateriaaldetailsoortReferentiedata(
        code="CEM",
        naam="Cementstuc",
        parent=Materiaalsoort.cement,
    )

    grout = MateriaaldetailsoortReferentiedata(
        code="GRO",
        naam="Grout",
        parent=Materiaalsoort.cement,
    )

    metselspecie = MateriaaldetailsoortReferentiedata(
        code="MET",
        naam="Metselspecie",
        parent=Materiaalsoort.cement,
    )

    mortel = MateriaaldetailsoortReferentiedata(
        code="MOR",
        naam="Mortel",
        parent=Materiaalsoort.cement,
    )

    terrazzo = MateriaaldetailsoortReferentiedata(
        code="TER",
        naam="Terrazzo",
        parent=Materiaalsoort.cement,
    )

    vezelcement = MateriaaldetailsoortReferentiedata(
        code="VEZ",
        naam="Vezelcement",
        parent=Materiaalsoort.cement,
    )

    houtvezelcement = MateriaaldetailsoortReferentiedata(
        code="HVC",
        naam="Houtvezelcement",
        parent=Materiaalsoort.cement,
    )

    houtwolcement = MateriaaldetailsoortReferentiedata(
        code="HWC",
        naam="Houtwolcement",
        parent=Materiaalsoort.cement,
    )

    spuitmortel = MateriaaldetailsoortReferentiedata(
        code="SMO",
        naam="Spuitmortel",
        parent=Materiaalsoort.cement,
    )

    zandcement = MateriaaldetailsoortReferentiedata(
        code="ZCE",
        naam="Zandcement",
        parent=Materiaalsoort.cement,
    )

    zandcement_vezel = MateriaaldetailsoortReferentiedata(
        code="ZCV",
        naam="Zandcement-Vezel",
        parent=Materiaalsoort.cement,
    )

    anhydriet = MateriaaldetailsoortReferentiedata(
        code="ANH",
        naam="Anhydriet",
        parent=Materiaalsoort.gips,
    )

    gipskarton = MateriaaldetailsoortReferentiedata(
        code="GIP",
        naam="Gipskarton",
        parent=Materiaalsoort.gips,
    )

    stuc = MateriaaldetailsoortReferentiedata(
        code="STU",
        naam="Stuc",
        parent=Materiaalsoort.gips,
    )

    spuitstuc = MateriaaldetailsoortReferentiedata(
        code="SST",
        naam="Spuitstuc",
        parent=Materiaalsoort.gips,
    )

    cellulairglas = MateriaaldetailsoortReferentiedata(
        code="CGL",
        naam="Cellulairglas",
        parent=Materiaalsoort.gips,
    )

    gehard = MateriaaldetailsoortReferentiedata(
        code="GEH",
        naam="Gehard",
        parent=Materiaalsoort.glas,
    )

    helder = MateriaaldetailsoortReferentiedata(
        code="HEL",
        naam="Helder",
        parent=Materiaalsoort.glas,
    )

    opaal = MateriaaldetailsoortReferentiedata(
        code="OPA",
        naam="Opaal",
        parent=Materiaalsoort.glas,
    )

    spiegelend = MateriaaldetailsoortReferentiedata(
        code="SPI",
        naam="Spiegelend",
        parent=Materiaalsoort.glas,
    )

    kwartsglas = MateriaaldetailsoortReferentiedata(
        code="KWA",
        naam="Kwartsglas",
        parent=Materiaalsoort.glas,
    )

    bimszand = MateriaaldetailsoortReferentiedata(
        code="BZA",
        naam="Bimszand",
        parent=Materiaalsoort.glas,
    )

    grind = MateriaaldetailsoortReferentiedata(
        code="GRI",
        naam="Grind",
        parent=Materiaalsoort.grondstof,
    )

    aarde = MateriaaldetailsoortReferentiedata(
        code="AAR",
        naam="Aarde",
        parent=Materiaalsoort.grondstof,
    )

    klei = MateriaaldetailsoortReferentiedata(
        code="KLE",
        naam="Klei",
        parent=Materiaalsoort.grondstof,
    )

    lucht = MateriaaldetailsoortReferentiedata(
        code="LUC",
        naam="Lucht",
        parent=Materiaalsoort.grondstof,
    )

    split = MateriaaldetailsoortReferentiedata(
        code="SPL",
        naam="Split",
        parent=Materiaalsoort.grondstof,
    )

    turf = MateriaaldetailsoortReferentiedata(
        code="TUR",
        naam="Turf",
        parent=Materiaalsoort.grondstof,
    )

    water = MateriaaldetailsoortReferentiedata(
        code="WAT",
        naam="Water",
        parent=Materiaalsoort.grondstof,
    )

    kalk = MateriaaldetailsoortReferentiedata(
        code="KAL",
        naam="Kalk",
        parent=Materiaalsoort.grondstof,
    )

    leem = MateriaaldetailsoortReferentiedata(
        code="LEE",
        naam="Leem",
        parent=Materiaalsoort.grondstof,
    )

    silt = MateriaaldetailsoortReferentiedata(
        code="SIL",
        naam="Silt",
        parent=Materiaalsoort.grondstof,
    )

    zand = MateriaaldetailsoortReferentiedata(
        code="ZAN",
        naam="Zand",
        parent=Materiaalsoort.grondstof,
    )

    hardboard = MateriaaldetailsoortReferentiedata(
        code="HBO",
        naam="Hardboard",
        parent=Materiaalsoort.grondstof,
    )

    hardhout = MateriaaldetailsoortReferentiedata(
        code="HHO",
        naam="Hardhout",
        parent=Materiaalsoort.hout,
    )

    houtspaan = MateriaaldetailsoortReferentiedata(
        code="HSP",
        naam="Houtspaan",
        parent=Materiaalsoort.hout,
    )

    accoya = MateriaaldetailsoortReferentiedata(
        code="ACC",
        naam="Accoya",
        parent=Materiaalsoort.hout,
    )

    azobe = MateriaaldetailsoortReferentiedata(
        code="AZO",
        naam="Azobe",
        parent=Materiaalsoort.hout,
    )

    balsa = MateriaaldetailsoortReferentiedata(
        code="BAL",
        naam="Balsa",
        parent=Materiaalsoort.hout,
    )

    bangkirai = MateriaaldetailsoortReferentiedata(
        code="BAN",
        naam="Bangkirai",
        parent=Materiaalsoort.hout,
    )

    berken = MateriaaldetailsoortReferentiedata(
        code="BER",
        naam="Berken",
        parent=Materiaalsoort.hout,
    )

    beuken = MateriaaldetailsoortReferentiedata(
        code="BEU",
        naam="Beuken",
        parent=Materiaalsoort.hout,
    )

    bilinga = MateriaaldetailsoortReferentiedata(
        code="BIL",
        naam="Bilinga",
        parent=Materiaalsoort.hout,
    )

    board = MateriaaldetailsoortReferentiedata(
        code="BOA",
        naam="Board",
        parent=Materiaalsoort.hout,
    )

    clt = MateriaaldetailsoortReferentiedata(
        code="CLT",
        naam="Clt",
        parent=Materiaalsoort.hout,
    )

    douglas = MateriaaldetailsoortReferentiedata(
        code="DOU",
        naam="Douglas",
        parent=Materiaalsoort.hout,
    )

    ebben = MateriaaldetailsoortReferentiedata(
        code="EBB",
        naam="Ebben",
        parent=Materiaalsoort.hout,
    )

    eiken = MateriaaldetailsoortReferentiedata(
        code="EIK",
        naam="Eiken",
        parent=Materiaalsoort.hout,
    )

    esdoorn = MateriaaldetailsoortReferentiedata(
        code="ESD",
        naam="Esdoorn",
        parent=Materiaalsoort.hout,
    )

    essen = MateriaaldetailsoortReferentiedata(
        code="ESS",
        naam="Essen",
        parent=Materiaalsoort.hout,
    )

    gemodificeerd = MateriaaldetailsoortReferentiedata(
        code="GEM",
        naam="Gemodificeerd",
        parent=Materiaalsoort.hout,
    )

    grenen = MateriaaldetailsoortReferentiedata(
        code="GRE",
        naam="Grenen",
        parent=Materiaalsoort.hout,
    )

    houtvezel = MateriaaldetailsoortReferentiedata(
        code="HVE",
        naam="Houtvezel",
        parent=Materiaalsoort.hout,
    )

    houtwol = MateriaaldetailsoortReferentiedata(
        code="HWO",
        naam="Houtwol",
        parent=Materiaalsoort.hout,
    )

    kersen = MateriaaldetailsoortReferentiedata(
        code="KER",
        naam="Kersen",
        parent=Materiaalsoort.hout,
    )

    lariks = MateriaaldetailsoortReferentiedata(
        code="LAR",
        naam="Lariks",
        parent=Materiaalsoort.hout,
    )

    mahonie = MateriaaldetailsoortReferentiedata(
        code="MAH",
        naam="Mahonie",
        parent=Materiaalsoort.hout,
    )

    masonite = MateriaaldetailsoortReferentiedata(
        code="MAS",
        naam="Masonite",
        parent=Materiaalsoort.hout,
    )

    mdf = MateriaaldetailsoortReferentiedata(
        code="MDF",
        naam="Mdf",
        parent=Materiaalsoort.hout,
    )

    multiplex = MateriaaldetailsoortReferentiedata(
        code="MUL",
        naam="Multiplex",
        parent=Materiaalsoort.hout,
    )

    noten = MateriaaldetailsoortReferentiedata(
        code="NOT",
        naam="Noten",
        parent=Materiaalsoort.hout,
    )

    okoume = MateriaaldetailsoortReferentiedata(
        code="OKO",
        naam="Okoume",
        parent=Materiaalsoort.hout,
    )

    osb = MateriaaldetailsoortReferentiedata(
        code="OSB",
        naam="Osb",
        parent=Materiaalsoort.hout,
    )

    populieren = MateriaaldetailsoortReferentiedata(
        code="POP",
        naam="Populieren",
        parent=Materiaalsoort.hout,
    )

    spaanplaat = MateriaaldetailsoortReferentiedata(
        code="SPA",
        naam="Spaanplaat",
        parent=Materiaalsoort.hout,
    )

    triplex = MateriaaldetailsoortReferentiedata(
        code="TRI",
        naam="Triplex",
        parent=Materiaalsoort.hout,
    )

    vuren = MateriaaldetailsoortReferentiedata(
        code="VUR",
        naam="Vuren",
        parent=Materiaalsoort.hout,
    )

    wenge = MateriaaldetailsoortReferentiedata(
        code="WEN",
        naam="Wenge",
        parent=Materiaalsoort.hout,
    )

    ceder = MateriaaldetailsoortReferentiedata(
        code="CED",
        naam="Ceder",
        parent=Materiaalsoort.hout,
    )

    zaagsel = MateriaaldetailsoortReferentiedata(
        code="ZAA",
        naam="Zaagsel",
        parent=Materiaalsoort.hout,
    )

    meranti = MateriaaldetailsoortReferentiedata(
        code="MER",
        naam="Meranti",
        parent=Materiaalsoort.hout,
    )

    merbau = MateriaaldetailsoortReferentiedata(
        code="MBA",
        naam="Merbau",
        parent=Materiaalsoort.hout,
    )

    zachtboard = MateriaaldetailsoortReferentiedata(
        code="ZBO",
        naam="Zachtboard",
        parent=Materiaalsoort.hout,
    )

    zachthout = MateriaaldetailsoortReferentiedata(
        code="ZHO",
        naam="Zachthout",
        parent=Materiaalsoort.hout,
    )

    geexpandeerd_perliet = MateriaaldetailsoortReferentiedata(
        code="GEP",
        naam="Geexpandeerd-Perliet",
        parent=Materiaalsoort.hout,
    )

    hardschuim = MateriaaldetailsoortReferentiedata(
        code="HSC",
        naam="Hardschuim",
        parent=Materiaalsoort.isolatie,
    )

    eps = MateriaaldetailsoortReferentiedata(
        code="EPS",
        naam="Eps",
        parent=Materiaalsoort.isolatie,
    )

    fenolhars = MateriaaldetailsoortReferentiedata(
        code="FEN",
        naam="Fenolhars",
        parent=Materiaalsoort.isolatie,
    )

    glaswol = MateriaaldetailsoortReferentiedata(
        code="GLA",
        naam="Glaswol",
        parent=Materiaalsoort.isolatie,
    )

    resolschuim = MateriaaldetailsoortReferentiedata(
        code="RES",
        naam="Resolschuim",
        parent=Materiaalsoort.isolatie,
    )

    pir = MateriaaldetailsoortReferentiedata(
        code="PIR",
        naam="Pir",
        parent=Materiaalsoort.isolatie,
    )

    pur = MateriaaldetailsoortReferentiedata(
        code="PUR",
        naam="Pur",
        parent=Materiaalsoort.isolatie,
    )

    mineralewol = MateriaaldetailsoortReferentiedata(
        code="MNE",
        naam="Mineralewol",
        parent=Materiaalsoort.isolatie,
    )

    steenwol = MateriaaldetailsoortReferentiedata(
        code="STE",
        naam="Steenwol",
        parent=Materiaalsoort.isolatie,
    )

    xps = MateriaaldetailsoortReferentiedata(
        code="XPS",
        naam="Xps",
        parent=Materiaalsoort.isolatie,
    )

    mineraal = MateriaaldetailsoortReferentiedata(
        code="MIN",
        naam="Mineraal",
        parent=Materiaalsoort.isolatie,
    )

    siliperliet = MateriaaldetailsoortReferentiedata(
        code="SLI",
        naam="Siliperliet",
        parent=Materiaalsoort.isolatie,
    )

    solperlite = MateriaaldetailsoortReferentiedata(
        code="SOL",
        naam="Solperlite",
        parent=Materiaalsoort.isolatie,
    )

    hard_kunststof = MateriaaldetailsoortReferentiedata(
        code="HKU",
        naam="Hard-Kunststof",
        parent=Materiaalsoort.isolatie,
    )

    loodvervanger = MateriaaldetailsoortReferentiedata(
        code="LVE",
        naam="Loodvervanger",
        parent=Materiaalsoort.kunststof,
    )

    abs = MateriaaldetailsoortReferentiedata(
        code="ABS",
        naam="Abs",
        parent=Materiaalsoort.kunststof,
    )

    aeryl = MateriaaldetailsoortReferentiedata(
        code="AER",
        naam="Aeryl",
        parent=Materiaalsoort.kunststof,
    )

    dpc = MateriaaldetailsoortReferentiedata(
        code="DPC",
        naam="Dpc",
        parent=Materiaalsoort.kunststof,
    )

    elastomere_foam = MateriaaldetailsoortReferentiedata(
        code="ELA",
        naam="Elastomere-Foam",
        parent=Materiaalsoort.kunststof,
    )

    ep = MateriaaldetailsoortReferentiedata(
        code="EP",
        naam="Ep",
        parent=Materiaalsoort.kunststof,
    )

    epoxyhars = MateriaaldetailsoortReferentiedata(
        code="EPO",
        naam="Epoxyhars",
        parent=Materiaalsoort.kunststof,
    )

    hdpe = MateriaaldetailsoortReferentiedata(
        code="HDP",
        naam="Hdpe",
        parent=Materiaalsoort.kunststof,
    )

    hmpe = MateriaaldetailsoortReferentiedata(
        code="HMP",
        naam="Hmpe",
        parent=Materiaalsoort.kunststof,
    )

    hpl = MateriaaldetailsoortReferentiedata(
        code="HPL",
        naam="Hpl",
        parent=Materiaalsoort.kunststof,
    )

    ldpe = MateriaaldetailsoortReferentiedata(
        code="LDP",
        naam="Ldpe",
        parent=Materiaalsoort.kunststof,
    )

    pe = MateriaaldetailsoortReferentiedata(
        code="PE",
        naam="Pe",
        parent=Materiaalsoort.kunststof,
    )

    pmma = MateriaaldetailsoortReferentiedata(
        code="PMM",
        naam="Pmma",
        parent=Materiaalsoort.kunststof,
    )

    pvac = MateriaaldetailsoortReferentiedata(
        code="PVA",
        naam="Pvac",
        parent=Materiaalsoort.kunststof,
    )

    pa = MateriaaldetailsoortReferentiedata(
        code="PA",
        naam="Pa",
        parent=Materiaalsoort.kunststof,
    )

    pc = MateriaaldetailsoortReferentiedata(
        code="PC",
        naam="Pc",
        parent=Materiaalsoort.kunststof,
    )

    pctfe = MateriaaldetailsoortReferentiedata(
        code="PCT",
        naam="Pctfe",
        parent=Materiaalsoort.kunststof,
    )

    plexiglas = MateriaaldetailsoortReferentiedata(
        code="PLE",
        naam="Plexiglas",
        parent=Materiaalsoort.kunststof,
    )

    polyesterhars = MateriaaldetailsoortReferentiedata(
        code="PLY",
        naam="Polyesterhars",
        parent=Materiaalsoort.kunststof,
    )

    pp = MateriaaldetailsoortReferentiedata(
        code="PP",
        naam="Pp",
        parent=Materiaalsoort.kunststof,
    )

    ps = MateriaaldetailsoortReferentiedata(
        code="PS",
        naam="Ps",
        parent=Materiaalsoort.kunststof,
    )

    ptfe = MateriaaldetailsoortReferentiedata(
        code="PTF",
        naam="Ptfe",
        parent=Materiaalsoort.kunststof,
    )

    pu = MateriaaldetailsoortReferentiedata(
        code="PU",
        naam="Pu",
        parent=Materiaalsoort.kunststof,
    )

    pvc = MateriaaldetailsoortReferentiedata(
        code="PVC",
        naam="Pvc",
        parent=Materiaalsoort.kunststof,
    )

    polyester = MateriaaldetailsoortReferentiedata(
        code="POL",
        naam="Polyester",
        parent=Materiaalsoort.kunststof,
    )

    silicagel = MateriaaldetailsoortReferentiedata(
        code="SLG",
        naam="Silicagel",
        parent=Materiaalsoort.kunststof,
    )

    siliconen = MateriaaldetailsoortReferentiedata(
        code="SLC",
        naam="Siliconen",
        parent=Materiaalsoort.kunststof,
    )

    zacht_kunststof = MateriaaldetailsoortReferentiedata(
        code="ZKU",
        naam="Zacht-Kunststof",
        parent=Materiaalsoort.kunststof,
    )

    lood = MateriaaldetailsoortReferentiedata(
        code="LOO",
        naam="Lood",
        parent=Materiaalsoort.kunststof,
    )

    platina = MateriaaldetailsoortReferentiedata(
        code="PLA",
        naam="Platina",
        parent=Materiaalsoort.metaal,
    )

    aluminium = MateriaaldetailsoortReferentiedata(
        code="ALU",
        naam="Aluminium",
        parent=Materiaalsoort.metaal,
    )

    brons = MateriaaldetailsoortReferentiedata(
        code="BRO",
        naam="Brons",
        parent=Materiaalsoort.metaal,
    )

    chroom = MateriaaldetailsoortReferentiedata(
        code="CHR",
        naam="Chroom",
        parent=Materiaalsoort.metaal,
    )

    gietijzer = MateriaaldetailsoortReferentiedata(
        code="GIE",
        naam="Gietijzer",
        parent=Materiaalsoort.metaal,
    )

    goud = MateriaaldetailsoortReferentiedata(
        code="GOU",
        naam="Goud",
        parent=Materiaalsoort.metaal,
    )

    ijzer = MateriaaldetailsoortReferentiedata(
        code="IJZ",
        naam="Ijzer",
        parent=Materiaalsoort.metaal,
    )

    koper = MateriaaldetailsoortReferentiedata(
        code="KOP",
        naam="Koper",
        parent=Materiaalsoort.metaal,
    )

    messing = MateriaaldetailsoortReferentiedata(
        code="MES",
        naam="Messing",
        parent=Materiaalsoort.metaal,
    )

    rvs = MateriaaldetailsoortReferentiedata(
        code="RVS",
        naam="Rvs",
        parent=Materiaalsoort.metaal,
    )

    tin = MateriaaldetailsoortReferentiedata(
        code="TIN",
        naam="Tin",
        parent=Materiaalsoort.metaal,
    )

    titanium = MateriaaldetailsoortReferentiedata(
        code="TIT",
        naam="Titanium",
        parent=Materiaalsoort.metaal,
    )

    zilver = MateriaaldetailsoortReferentiedata(
        code="ZIL",
        naam="Zilver",
        parent=Materiaalsoort.metaal,
    )

    zink = MateriaaldetailsoortReferentiedata(
        code="ZIN",
        naam="Zink",
        parent=Materiaalsoort.metaal,
    )

    soldeersel = MateriaaldetailsoortReferentiedata(
        code="SDE",
        naam="Soldeersel",
        parent=Materiaalsoort.metaal,
    )

    staal = MateriaaldetailsoortReferentiedata(
        code="STA",
        naam="Staal",
        parent=Materiaalsoort.metaal,
    )

    asbest = MateriaaldetailsoortReferentiedata(
        code="ASB",
        naam="Asbest",
        parent=Materiaalsoort.metaal,
    )

    graniet = MateriaaldetailsoortReferentiedata(
        code="GRA",
        naam="Graniet",
        parent=Materiaalsoort.natuursteen,
    )

    gravel = MateriaaldetailsoortReferentiedata(
        code="GVE",
        naam="Gravel",
        parent=Materiaalsoort.natuursteen,
    )

    hardsteen = MateriaaldetailsoortReferentiedata(
        code="HST",
        naam="Hardsteen",
        parent=Materiaalsoort.natuursteen,
    )

    kwartsiet = MateriaaldetailsoortReferentiedata(
        code="KSI",
        naam="Kwartsiet",
        parent=Materiaalsoort.natuursteen,
    )

    poreus_gesteente = MateriaaldetailsoortReferentiedata(
        code="PGE",
        naam="Poreus-Gesteente",
        parent=Materiaalsoort.natuursteen,
    )

    basalt = MateriaaldetailsoortReferentiedata(
        code="BAS",
        naam="Basalt",
        parent=Materiaalsoort.natuursteen,
    )

    gneiss = MateriaaldetailsoortReferentiedata(
        code="GNE",
        naam="Gneiss",
        parent=Materiaalsoort.natuursteen,
    )

    kristallijn_gesteente = MateriaaldetailsoortReferentiedata(
        code="KRI",
        naam="Kristallijn-Gesteente",
        parent=Materiaalsoort.natuursteen,
    )

    lei = MateriaaldetailsoortReferentiedata(
        code="LEI",
        naam="Lei",
        parent=Materiaalsoort.natuursteen,
    )

    marmer = MateriaaldetailsoortReferentiedata(
        code="MAR",
        naam="Marmer",
        parent=Materiaalsoort.natuursteen,
    )

    puimsteen = MateriaaldetailsoortReferentiedata(
        code="PUI",
        naam="Puimsteen",
        parent=Materiaalsoort.natuursteen,
    )

    sedimentgesteente = MateriaaldetailsoortReferentiedata(
        code="SED",
        naam="Sedimentgesteente",
        parent=Materiaalsoort.natuursteen,
    )

    trachiet = MateriaaldetailsoortReferentiedata(
        code="TRA",
        naam="Trachiet",
        parent=Materiaalsoort.natuursteen,
    )

    zandsteen = MateriaaldetailsoortReferentiedata(
        code="ZST",
        naam="Zandsteen",
        parent=Materiaalsoort.natuursteen,
    )

    leer = MateriaaldetailsoortReferentiedata(
        code="LER",
        naam="Leer",
        parent=Materiaalsoort.ntb,
    )

    plantaardige_vezel = MateriaaldetailsoortReferentiedata(
        code="PTA",
        naam="Plantaardige-Vezel",
        parent=Materiaalsoort.organisch,
    )

    bamboe = MateriaaldetailsoortReferentiedata(
        code="BAM",
        naam="Bamboe",
        parent=Materiaalsoort.organisch,
    )

    hennep = MateriaaldetailsoortReferentiedata(
        code="HEN",
        naam="Hennep",
        parent=Materiaalsoort.organisch,
    )

    jute = MateriaaldetailsoortReferentiedata(
        code="JUT",
        naam="Jute",
        parent=Materiaalsoort.organisch,
    )

    katoen = MateriaaldetailsoortReferentiedata(
        code="KAT",
        naam="Katoen",
        parent=Materiaalsoort.organisch,
    )

    kurk = MateriaaldetailsoortReferentiedata(
        code="KUR",
        naam="Kurk",
        parent=Materiaalsoort.organisch,
    )

    mais = MateriaaldetailsoortReferentiedata(
        code="MAI",
        naam="Mais",
        parent=Materiaalsoort.organisch,
    )

    papier = MateriaaldetailsoortReferentiedata(
        code="PAP",
        naam="Papier",
        parent=Materiaalsoort.organisch,
    )

    riet = MateriaaldetailsoortReferentiedata(
        code="RIE",
        naam="Riet",
        parent=Materiaalsoort.organisch,
    )

    stro = MateriaaldetailsoortReferentiedata(
        code="STR",
        naam="Stro",
        parent=Materiaalsoort.organisch,
    )

    vegetatie = MateriaaldetailsoortReferentiedata(
        code="VEG",
        naam="Vegetatie",
        parent=Materiaalsoort.organisch,
    )

    vilt = MateriaaldetailsoortReferentiedata(
        code="VIL",
        naam="Vilt",
        parent=Materiaalsoort.organisch,
    )

    vlas = MateriaaldetailsoortReferentiedata(
        code="VLA",
        naam="Vlas",
        parent=Materiaalsoort.organisch,
    )

    wol = MateriaaldetailsoortReferentiedata(
        code="WOL",
        naam="Wol",
        parent=Materiaalsoort.organisch,
    )

    hard_rubber = MateriaaldetailsoortReferentiedata(
        code="HRU",
        naam="Hard-Rubber",
        parent=Materiaalsoort.organisch,
    )

    polysulfide = MateriaaldetailsoortReferentiedata(
        code="PLS",
        naam="Polysulfide",
        parent=Materiaalsoort.rubber,
    )

    schuimrubber = MateriaaldetailsoortReferentiedata(
        code="SRU",
        naam="Schuimrubber",
        parent=Materiaalsoort.rubber,
    )

    butyl = MateriaaldetailsoortReferentiedata(
        code="BUT",
        naam="Butyl",
        parent=Materiaalsoort.rubber,
    )

    epdm = MateriaaldetailsoortReferentiedata(
        code="EPD",
        naam="Epdm",
        parent=Materiaalsoort.rubber,
    )

    linoleum = MateriaaldetailsoortReferentiedata(
        code="LIN",
        naam="Linoleum",
        parent=Materiaalsoort.rubber,
    )

    natuurrubber = MateriaaldetailsoortReferentiedata(
        code="NAT",
        naam="Natuurrubber",
        parent=Materiaalsoort.rubber,
    )

    neopreen = MateriaaldetailsoortReferentiedata(
        code="NEO",
        naam="Neopreen",
        parent=Materiaalsoort.rubber,
    )

    tpve = MateriaaldetailsoortReferentiedata(
        code="TPV",
        naam="Tpve",
        parent=Materiaalsoort.rubber,
    )

    element = MateriaaldetailsoortReferentiedata(
        code="ELE",
        naam="Element",
        parent=Materiaalsoort.rubber,
    )

    product = MateriaaldetailsoortReferentiedata(
        code="PRO",
        naam="Product",
        parent=Materiaalsoort.samengesteld,
    )

    geexpandeerde_klei = MateriaaldetailsoortReferentiedata(
        code="GEK",
        naam="Geexpandeerde-Klei",
        parent=Materiaalsoort.samengesteld,
    )

    kalksteen = MateriaaldetailsoortReferentiedata(
        code="KST",
        naam="Kalksteen",
        parent=Materiaalsoort.steenachtig,
    )

    kalkzandsteen = MateriaaldetailsoortReferentiedata(
        code="KZS",
        naam="Kalkzandsteen",
        parent=Materiaalsoort.steenachtig,
    )

    keramisch = MateriaaldetailsoortReferentiedata(
        code="KRA",
        naam="Keramisch",
        parent=Materiaalsoort.steenachtig,
    )

    porisosteen = MateriaaldetailsoortReferentiedata(
        code="PRI",
        naam="Porisosteen",
        parent=Materiaalsoort.steenachtig,
    )

    porselein = MateriaaldetailsoortReferentiedata(
        code="PSE",
        naam="Porselein",
        parent=Materiaalsoort.steenachtig,
    )

    baksteen = MateriaaldetailsoortReferentiedata(
        code="BAK",
        naam="Baksteen",
        parent=Materiaalsoort.steenachtig,
    )

    calciumsilicaat = MateriaaldetailsoortReferentiedata(
        code="CAL",
        naam="Calciumsilicaat",
        parent=Materiaalsoort.steenachtig,
    )

    kunststeen = MateriaaldetailsoortReferentiedata(
        code="KUN",
        naam="Kunststeen",
        parent=Materiaalsoort.steenachtig,
    )
