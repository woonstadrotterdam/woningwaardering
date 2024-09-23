from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Materiaaldetailsoort(Enum):
    ntb = Referentiedata(
        code="NTB",
        naam="Ntb",
    )

    generiek = Referentiedata(
        code="GEN",
        naam="Generiek",
    )

    gasbeton = Referentiedata(
        code="GAS",
        naam="Gasbeton",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    bimsbeton = Referentiedata(
        code="BIM",
        naam="Bimsbeton",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    isolatiebeton = Referentiedata(
        code="ISO",
        naam="Isolatiebeton",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    lichtbeton = Referentiedata(
        code="LIC",
        naam="Lichtbeton",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    slakkenbeton = Referentiedata(
        code="SLA",
        naam="Slakkenbeton",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    voorgespannen = Referentiedata(
        code="VOO",
        naam="Voorgespannen",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    cellenbeton = Referentiedata(
        code="CEL",
        naam="Cellenbeton",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    gewapend = Referentiedata(
        code="GEW",
        naam="Gewapend",
    )

    grindbeton = Referentiedata(
        code="GBE",
        naam="Grindbeton",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    schuimbeton = Referentiedata(
        code="SBE",
        naam="Schuimbeton",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    spuitbeton = Referentiedata(
        code="SBT",
        naam="Spuitbeton",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    staalvezelbeton = Referentiedata(
        code="SVE",
        naam="Staalvezelbeton",
        parent=Referentiedata(
            code="BET",
            naam="Beton",
        ),
    )

    asfalt = Referentiedata(
        code="ASF",
        naam="Asfalt",
        parent=Referentiedata(
            code="BIT",
            naam="Bitumen",
        ),
    )

    teer = Referentiedata(
        code="TEE",
        naam="Teer",
        parent=Referentiedata(
            code="BIT",
            naam="Bitumen",
        ),
    )

    asbestcement = Referentiedata(
        code="ACE",
        naam="Asbestcement",
        parent=Referentiedata(
            code="BIT",
            naam="Bitumen",
        ),
    )

    cementstuc = Referentiedata(
        code="CEM",
        naam="Cementstuc",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    grout = Referentiedata(
        code="GRO",
        naam="Grout",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    metselspecie = Referentiedata(
        code="MET",
        naam="Metselspecie",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    mortel = Referentiedata(
        code="MOR",
        naam="Mortel",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    terrazzo = Referentiedata(
        code="TER",
        naam="Terrazzo",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    vezelcement = Referentiedata(
        code="VEZ",
        naam="Vezelcement",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    houtvezelcement = Referentiedata(
        code="HVC",
        naam="Houtvezelcement",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    houtwolcement = Referentiedata(
        code="HWC",
        naam="Houtwolcement",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    spuitmortel = Referentiedata(
        code="SMO",
        naam="Spuitmortel",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    zandcement = Referentiedata(
        code="ZCE",
        naam="Zandcement",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    zandcement_vezel = Referentiedata(
        code="ZCV",
        naam="Zandcement-Vezel",
        parent=Referentiedata(
            code="CEM",
            naam="Cement",
        ),
    )

    anhydriet = Referentiedata(
        code="ANH",
        naam="Anhydriet",
        parent=Referentiedata(
            code="GIP",
            naam="Gips",
        ),
    )

    gipskarton = Referentiedata(
        code="GIP",
        naam="Gipskarton",
        parent=Referentiedata(
            code="GIP",
            naam="Gips",
        ),
    )

    stuc = Referentiedata(
        code="STU",
        naam="Stuc",
        parent=Referentiedata(
            code="GIP",
            naam="Gips",
        ),
    )

    spuitstuc = Referentiedata(
        code="SST",
        naam="Spuitstuc",
        parent=Referentiedata(
            code="GIP",
            naam="Gips",
        ),
    )

    cellulairglas = Referentiedata(
        code="CGL",
        naam="Cellulairglas",
        parent=Referentiedata(
            code="GIP",
            naam="Gips",
        ),
    )

    gehard = Referentiedata(
        code="GEH",
        naam="Gehard",
        parent=Referentiedata(
            code="GLA",
            naam="Glas",
        ),
    )

    helder = Referentiedata(
        code="HEL",
        naam="Helder",
        parent=Referentiedata(
            code="GLA",
            naam="Glas",
        ),
    )

    opaal = Referentiedata(
        code="OPA",
        naam="Opaal",
        parent=Referentiedata(
            code="GLA",
            naam="Glas",
        ),
    )

    spiegelend = Referentiedata(
        code="SPI",
        naam="Spiegelend",
        parent=Referentiedata(
            code="GLA",
            naam="Glas",
        ),
    )

    kwartsglas = Referentiedata(
        code="KWA",
        naam="Kwartsglas",
        parent=Referentiedata(
            code="GLA",
            naam="Glas",
        ),
    )

    bimszand = Referentiedata(
        code="BZA",
        naam="Bimszand",
        parent=Referentiedata(
            code="GLA",
            naam="Glas",
        ),
    )

    grind = Referentiedata(
        code="GRI",
        naam="Grind",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    aarde = Referentiedata(
        code="AAR",
        naam="Aarde",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    klei = Referentiedata(
        code="KLE",
        naam="Klei",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    lucht = Referentiedata(
        code="LUC",
        naam="Lucht",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    split = Referentiedata(
        code="SPL",
        naam="Split",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    turf = Referentiedata(
        code="TUR",
        naam="Turf",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    water = Referentiedata(
        code="WAT",
        naam="Water",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    kalk = Referentiedata(
        code="KAL",
        naam="Kalk",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    leem = Referentiedata(
        code="LEE",
        naam="Leem",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    silt = Referentiedata(
        code="SIL",
        naam="Silt",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    zand = Referentiedata(
        code="ZAN",
        naam="Zand",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    hardboard = Referentiedata(
        code="HBO",
        naam="Hardboard",
        parent=Referentiedata(
            code="GRO",
            naam="Grondstof",
        ),
    )

    hardhout = Referentiedata(
        code="HHO",
        naam="Hardhout",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    houtspaan = Referentiedata(
        code="HSP",
        naam="Houtspaan",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    accoya = Referentiedata(
        code="ACC",
        naam="Accoya",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    azobe = Referentiedata(
        code="AZO",
        naam="Azobe",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    balsa = Referentiedata(
        code="BAL",
        naam="Balsa",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    bangkirai = Referentiedata(
        code="BAN",
        naam="Bangkirai",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    berken = Referentiedata(
        code="BER",
        naam="Berken",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    beuken = Referentiedata(
        code="BEU",
        naam="Beuken",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    bilinga = Referentiedata(
        code="BIL",
        naam="Bilinga",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    board = Referentiedata(
        code="BOA",
        naam="Board",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    clt = Referentiedata(
        code="CLT",
        naam="Clt",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    douglas = Referentiedata(
        code="DOU",
        naam="Douglas",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    ebben = Referentiedata(
        code="EBB",
        naam="Ebben",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    eiken = Referentiedata(
        code="EIK",
        naam="Eiken",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    esdoorn = Referentiedata(
        code="ESD",
        naam="Esdoorn",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    essen = Referentiedata(
        code="ESS",
        naam="Essen",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    gemodificeerd = Referentiedata(
        code="GEM",
        naam="Gemodificeerd",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    grenen = Referentiedata(
        code="GRE",
        naam="Grenen",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    houtvezel = Referentiedata(
        code="HVE",
        naam="Houtvezel",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    houtwol = Referentiedata(
        code="HWO",
        naam="Houtwol",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    kersen = Referentiedata(
        code="KER",
        naam="Kersen",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    lariks = Referentiedata(
        code="LAR",
        naam="Lariks",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    mahonie = Referentiedata(
        code="MAH",
        naam="Mahonie",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    masonite = Referentiedata(
        code="MAS",
        naam="Masonite",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    mdf = Referentiedata(
        code="MDF",
        naam="Mdf",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    multiplex = Referentiedata(
        code="MUL",
        naam="Multiplex",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    noten = Referentiedata(
        code="NOT",
        naam="Noten",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    okoume = Referentiedata(
        code="OKO",
        naam="Okoume",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    osb = Referentiedata(
        code="OSB",
        naam="Osb",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    populieren = Referentiedata(
        code="POP",
        naam="Populieren",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    spaanplaat = Referentiedata(
        code="SPA",
        naam="Spaanplaat",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    triplex = Referentiedata(
        code="TRI",
        naam="Triplex",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    vuren = Referentiedata(
        code="VUR",
        naam="Vuren",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    wenge = Referentiedata(
        code="WEN",
        naam="Wenge",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    ceder = Referentiedata(
        code="CED",
        naam="Ceder",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    zaagsel = Referentiedata(
        code="ZAA",
        naam="Zaagsel",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    meranti = Referentiedata(
        code="MER",
        naam="Meranti",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    merbau = Referentiedata(
        code="MBA",
        naam="Merbau",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    zachtboard = Referentiedata(
        code="ZBO",
        naam="Zachtboard",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    zachthout = Referentiedata(
        code="ZHO",
        naam="Zachthout",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    geexpandeerd_perliet = Referentiedata(
        code="GEP",
        naam="Geexpandeerd-Perliet",
        parent=Referentiedata(
            code="HOU",
            naam="Hout",
        ),
    )

    hardschuim = Referentiedata(
        code="HSC",
        naam="Hardschuim",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    eps = Referentiedata(
        code="EPS",
        naam="Eps",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    fenolhars = Referentiedata(
        code="FEN",
        naam="Fenolhars",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    glaswol = Referentiedata(
        code="GLA",
        naam="Glaswol",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    resolschuim = Referentiedata(
        code="RES",
        naam="Resolschuim",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    pir = Referentiedata(
        code="PIR",
        naam="Pir",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    pur = Referentiedata(
        code="PUR",
        naam="Pur",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    mineralewol = Referentiedata(
        code="MNE",
        naam="Mineralewol",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    steenwol = Referentiedata(
        code="STE",
        naam="Steenwol",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    xps = Referentiedata(
        code="XPS",
        naam="Xps",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    mineraal = Referentiedata(
        code="MIN",
        naam="Mineraal",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    siliperliet = Referentiedata(
        code="SLI",
        naam="Siliperliet",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    solperlite = Referentiedata(
        code="SOL",
        naam="Solperlite",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    hard_kunststof = Referentiedata(
        code="HKU",
        naam="Hard-Kunststof",
        parent=Referentiedata(
            code="ISO",
            naam="Isolatie",
        ),
    )

    loodvervanger = Referentiedata(
        code="LVE",
        naam="Loodvervanger",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    abs = Referentiedata(
        code="ABS",
        naam="Abs",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    aeryl = Referentiedata(
        code="AER",
        naam="Aeryl",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    dpc = Referentiedata(
        code="DPC",
        naam="Dpc",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    elastomere_foam = Referentiedata(
        code="ELA",
        naam="Elastomere-Foam",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    ep = Referentiedata(
        code="EP",
        naam="Ep",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    epoxyhars = Referentiedata(
        code="EPO",
        naam="Epoxyhars",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    hdpe = Referentiedata(
        code="HDP",
        naam="Hdpe",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    hmpe = Referentiedata(
        code="HMP",
        naam="Hmpe",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    hpl = Referentiedata(
        code="HPL",
        naam="Hpl",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    ldpe = Referentiedata(
        code="LDP",
        naam="Ldpe",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    pe = Referentiedata(
        code="PE",
        naam="Pe",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    pmma = Referentiedata(
        code="PMM",
        naam="Pmma",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    pvac = Referentiedata(
        code="PVA",
        naam="Pvac",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    pa = Referentiedata(
        code="PA",
        naam="Pa",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    pc = Referentiedata(
        code="PC",
        naam="Pc",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    pctfe = Referentiedata(
        code="PCT",
        naam="Pctfe",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    plexiglas = Referentiedata(
        code="PLE",
        naam="Plexiglas",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    polyesterhars = Referentiedata(
        code="PLY",
        naam="Polyesterhars",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    pp = Referentiedata(
        code="PP",
        naam="Pp",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    ps = Referentiedata(
        code="PS",
        naam="Ps",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    ptfe = Referentiedata(
        code="PTF",
        naam="Ptfe",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    pu = Referentiedata(
        code="PU",
        naam="Pu",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    pvc = Referentiedata(
        code="PVC",
        naam="Pvc",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    polyester = Referentiedata(
        code="POL",
        naam="Polyester",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    silicagel = Referentiedata(
        code="SLG",
        naam="Silicagel",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    siliconen = Referentiedata(
        code="SLC",
        naam="Siliconen",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    zacht_kunststof = Referentiedata(
        code="ZKU",
        naam="Zacht-Kunststof",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    lood = Referentiedata(
        code="LOO",
        naam="Lood",
        parent=Referentiedata(
            code="KUN",
            naam="Kunststof",
        ),
    )

    platina = Referentiedata(
        code="PLA",
        naam="Platina",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    aluminium = Referentiedata(
        code="ALU",
        naam="Aluminium",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    brons = Referentiedata(
        code="BRO",
        naam="Brons",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    chroom = Referentiedata(
        code="CHR",
        naam="Chroom",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    gietijzer = Referentiedata(
        code="GIE",
        naam="Gietijzer",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    goud = Referentiedata(
        code="GOU",
        naam="Goud",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    ijzer = Referentiedata(
        code="IJZ",
        naam="Ijzer",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    koper = Referentiedata(
        code="KOP",
        naam="Koper",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    messing = Referentiedata(
        code="MES",
        naam="Messing",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    rvs = Referentiedata(
        code="RVS",
        naam="Rvs",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    tin = Referentiedata(
        code="TIN",
        naam="Tin",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    titanium = Referentiedata(
        code="TIT",
        naam="Titanium",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    zilver = Referentiedata(
        code="ZIL",
        naam="Zilver",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    zink = Referentiedata(
        code="ZIN",
        naam="Zink",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    soldeersel = Referentiedata(
        code="SDE",
        naam="Soldeersel",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    staal = Referentiedata(
        code="STA",
        naam="Staal",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    asbest = Referentiedata(
        code="ASB",
        naam="Asbest",
        parent=Referentiedata(
            code="MET",
            naam="Metaal",
        ),
    )

    graniet = Referentiedata(
        code="GRA",
        naam="Graniet",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    gravel = Referentiedata(
        code="GVE",
        naam="Gravel",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    hardsteen = Referentiedata(
        code="HST",
        naam="Hardsteen",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    kwartsiet = Referentiedata(
        code="KSI",
        naam="Kwartsiet",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    poreus_gesteente = Referentiedata(
        code="PGE",
        naam="Poreus-Gesteente",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    basalt = Referentiedata(
        code="BAS",
        naam="Basalt",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    gneiss = Referentiedata(
        code="GNE",
        naam="Gneiss",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    kristallijn_gesteente = Referentiedata(
        code="KRI",
        naam="Kristallijn-Gesteente",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    lei = Referentiedata(
        code="LEI",
        naam="Lei",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    marmer = Referentiedata(
        code="MAR",
        naam="Marmer",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    puimsteen = Referentiedata(
        code="PUI",
        naam="Puimsteen",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    sedimentgesteente = Referentiedata(
        code="SED",
        naam="Sedimentgesteente",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    trachiet = Referentiedata(
        code="TRA",
        naam="Trachiet",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    zandsteen = Referentiedata(
        code="ZST",
        naam="Zandsteen",
        parent=Referentiedata(
            code="NAT",
            naam="Natuursteen",
        ),
    )

    leer = Referentiedata(
        code="LER",
        naam="Leer",
        parent=Referentiedata(
            code="NTB",
            naam="Ntb",
        ),
    )

    plantaardige_vezel = Referentiedata(
        code="PTA",
        naam="Plantaardige-Vezel",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    bamboe = Referentiedata(
        code="BAM",
        naam="Bamboe",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    hennep = Referentiedata(
        code="HEN",
        naam="Hennep",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    jute = Referentiedata(
        code="JUT",
        naam="Jute",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    katoen = Referentiedata(
        code="KAT",
        naam="Katoen",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    kurk = Referentiedata(
        code="KUR",
        naam="Kurk",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    mais = Referentiedata(
        code="MAI",
        naam="Mais",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    papier = Referentiedata(
        code="PAP",
        naam="Papier",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    riet = Referentiedata(
        code="RIE",
        naam="Riet",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    stro = Referentiedata(
        code="STR",
        naam="Stro",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    vegetatie = Referentiedata(
        code="VEG",
        naam="Vegetatie",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    vilt = Referentiedata(
        code="VIL",
        naam="Vilt",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    vlas = Referentiedata(
        code="VLA",
        naam="Vlas",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    wol = Referentiedata(
        code="WOL",
        naam="Wol",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    hard_rubber = Referentiedata(
        code="HRU",
        naam="Hard-Rubber",
        parent=Referentiedata(
            code="ORG",
            naam="Organisch",
        ),
    )

    polysulfide = Referentiedata(
        code="PLS",
        naam="Polysulfide",
        parent=Referentiedata(
            code="RUB",
            naam="Rubber",
        ),
    )

    schuimrubber = Referentiedata(
        code="SRU",
        naam="Schuimrubber",
        parent=Referentiedata(
            code="RUB",
            naam="Rubber",
        ),
    )

    butyl = Referentiedata(
        code="BUT",
        naam="Butyl",
        parent=Referentiedata(
            code="RUB",
            naam="Rubber",
        ),
    )

    epdm = Referentiedata(
        code="EPD",
        naam="Epdm",
        parent=Referentiedata(
            code="RUB",
            naam="Rubber",
        ),
    )

    linoleum = Referentiedata(
        code="LIN",
        naam="Linoleum",
        parent=Referentiedata(
            code="RUB",
            naam="Rubber",
        ),
    )

    natuurrubber = Referentiedata(
        code="NAT",
        naam="Natuurrubber",
        parent=Referentiedata(
            code="RUB",
            naam="Rubber",
        ),
    )

    neopreen = Referentiedata(
        code="NEO",
        naam="Neopreen",
        parent=Referentiedata(
            code="RUB",
            naam="Rubber",
        ),
    )

    tpve = Referentiedata(
        code="TPV",
        naam="Tpve",
        parent=Referentiedata(
            code="RUB",
            naam="Rubber",
        ),
    )

    element = Referentiedata(
        code="ELE",
        naam="Element",
        parent=Referentiedata(
            code="RUB",
            naam="Rubber",
        ),
    )

    product = Referentiedata(
        code="PRO",
        naam="Product",
        parent=Referentiedata(
            code="SAM",
            naam="Samengesteld",
        ),
    )

    geexpandeerde_klei = Referentiedata(
        code="GEK",
        naam="Geexpandeerde-Klei",
        parent=Referentiedata(
            code="SAM",
            naam="Samengesteld",
        ),
    )

    kalksteen = Referentiedata(
        code="KST",
        naam="Kalksteen",
        parent=Referentiedata(
            code="STE",
            naam="Steenachtig",
        ),
    )

    kalkzandsteen = Referentiedata(
        code="KZS",
        naam="Kalkzandsteen",
        parent=Referentiedata(
            code="STE",
            naam="Steenachtig",
        ),
    )

    keramisch = Referentiedata(
        code="KRA",
        naam="Keramisch",
        parent=Referentiedata(
            code="STE",
            naam="Steenachtig",
        ),
    )

    porisosteen = Referentiedata(
        code="PRI",
        naam="Porisosteen",
        parent=Referentiedata(
            code="STE",
            naam="Steenachtig",
        ),
    )

    porselein = Referentiedata(
        code="PSE",
        naam="Porselein",
        parent=Referentiedata(
            code="STE",
            naam="Steenachtig",
        ),
    )

    baksteen = Referentiedata(
        code="BAK",
        naam="Baksteen",
        parent=Referentiedata(
            code="STE",
            naam="Steenachtig",
        ),
    )

    calciumsilicaat = Referentiedata(
        code="CAL",
        naam="Calciumsilicaat",
        parent=Referentiedata(
            code="STE",
            naam="Steenachtig",
        ),
    )

    kunststeen = Referentiedata(
        code="KUN",
        naam="Kunststeen",
        parent=Referentiedata(
            code="STE",
            naam="Steenachtig",
        ),
    )

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
