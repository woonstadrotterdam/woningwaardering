from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.materiaalsoort import Materiaalsoort
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Materiaaldetailsoort(Referentiedatasoort):
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
        parent=Materiaalsoort.beton,
    )

    bimsbeton = Referentiedata(
        code="BIM",
        naam="Bimsbeton",
        parent=Materiaalsoort.beton,
    )

    isolatiebeton = Referentiedata(
        code="ISO",
        naam="Isolatiebeton",
        parent=Materiaalsoort.beton,
    )

    lichtbeton = Referentiedata(
        code="LIC",
        naam="Lichtbeton",
        parent=Materiaalsoort.beton,
    )

    slakkenbeton = Referentiedata(
        code="SLA",
        naam="Slakkenbeton",
        parent=Materiaalsoort.beton,
    )

    voorgespannen = Referentiedata(
        code="VOO",
        naam="Voorgespannen",
        parent=Materiaalsoort.beton,
    )

    cellenbeton = Referentiedata(
        code="CEL",
        naam="Cellenbeton",
        parent=Materiaalsoort.beton,
    )

    gewapend = Referentiedata(
        code="GEW",
        naam="Gewapend",
    )

    grindbeton = Referentiedata(
        code="GBE",
        naam="Grindbeton",
        parent=Materiaalsoort.beton,
    )

    schuimbeton = Referentiedata(
        code="SBE",
        naam="Schuimbeton",
        parent=Materiaalsoort.beton,
    )

    spuitbeton = Referentiedata(
        code="SBT",
        naam="Spuitbeton",
        parent=Materiaalsoort.beton,
    )

    staalvezelbeton = Referentiedata(
        code="SVE",
        naam="Staalvezelbeton",
        parent=Materiaalsoort.beton,
    )

    asfalt = Referentiedata(
        code="ASF",
        naam="Asfalt",
        parent=Materiaalsoort.bitumen,
    )

    teer = Referentiedata(
        code="TEE",
        naam="Teer",
        parent=Materiaalsoort.bitumen,
    )

    asbestcement = Referentiedata(
        code="ACE",
        naam="Asbestcement",
        parent=Materiaalsoort.bitumen,
    )

    cementstuc = Referentiedata(
        code="CEM",
        naam="Cementstuc",
        parent=Materiaalsoort.cement,
    )

    grout = Referentiedata(
        code="GRO",
        naam="Grout",
        parent=Materiaalsoort.cement,
    )

    metselspecie = Referentiedata(
        code="MET",
        naam="Metselspecie",
        parent=Materiaalsoort.cement,
    )

    mortel = Referentiedata(
        code="MOR",
        naam="Mortel",
        parent=Materiaalsoort.cement,
    )

    terrazzo = Referentiedata(
        code="TER",
        naam="Terrazzo",
        parent=Materiaalsoort.cement,
    )

    vezelcement = Referentiedata(
        code="VEZ",
        naam="Vezelcement",
        parent=Materiaalsoort.cement,
    )

    houtvezelcement = Referentiedata(
        code="HVC",
        naam="Houtvezelcement",
        parent=Materiaalsoort.cement,
    )

    houtwolcement = Referentiedata(
        code="HWC",
        naam="Houtwolcement",
        parent=Materiaalsoort.cement,
    )

    spuitmortel = Referentiedata(
        code="SMO",
        naam="Spuitmortel",
        parent=Materiaalsoort.cement,
    )

    zandcement = Referentiedata(
        code="ZCE",
        naam="Zandcement",
        parent=Materiaalsoort.cement,
    )

    zandcement_vezel = Referentiedata(
        code="ZCV",
        naam="Zandcement-Vezel",
        parent=Materiaalsoort.cement,
    )

    anhydriet = Referentiedata(
        code="ANH",
        naam="Anhydriet",
        parent=Materiaalsoort.gips,
    )

    gipskarton = Referentiedata(
        code="GIP",
        naam="Gipskarton",
        parent=Materiaalsoort.gips,
    )

    stuc = Referentiedata(
        code="STU",
        naam="Stuc",
        parent=Materiaalsoort.gips,
    )

    spuitstuc = Referentiedata(
        code="SST",
        naam="Spuitstuc",
        parent=Materiaalsoort.gips,
    )

    cellulairglas = Referentiedata(
        code="CGL",
        naam="Cellulairglas",
        parent=Materiaalsoort.gips,
    )

    gehard = Referentiedata(
        code="GEH",
        naam="Gehard",
        parent=Materiaalsoort.glas,
    )

    helder = Referentiedata(
        code="HEL",
        naam="Helder",
        parent=Materiaalsoort.glas,
    )

    opaal = Referentiedata(
        code="OPA",
        naam="Opaal",
        parent=Materiaalsoort.glas,
    )

    spiegelend = Referentiedata(
        code="SPI",
        naam="Spiegelend",
        parent=Materiaalsoort.glas,
    )

    kwartsglas = Referentiedata(
        code="KWA",
        naam="Kwartsglas",
        parent=Materiaalsoort.glas,
    )

    bimszand = Referentiedata(
        code="BZA",
        naam="Bimszand",
        parent=Materiaalsoort.glas,
    )

    grind = Referentiedata(
        code="GRI",
        naam="Grind",
        parent=Materiaalsoort.grondstof,
    )

    aarde = Referentiedata(
        code="AAR",
        naam="Aarde",
        parent=Materiaalsoort.grondstof,
    )

    klei = Referentiedata(
        code="KLE",
        naam="Klei",
        parent=Materiaalsoort.grondstof,
    )

    lucht = Referentiedata(
        code="LUC",
        naam="Lucht",
        parent=Materiaalsoort.grondstof,
    )

    split = Referentiedata(
        code="SPL",
        naam="Split",
        parent=Materiaalsoort.grondstof,
    )

    turf = Referentiedata(
        code="TUR",
        naam="Turf",
        parent=Materiaalsoort.grondstof,
    )

    water = Referentiedata(
        code="WAT",
        naam="Water",
        parent=Materiaalsoort.grondstof,
    )

    kalk = Referentiedata(
        code="KAL",
        naam="Kalk",
        parent=Materiaalsoort.grondstof,
    )

    leem = Referentiedata(
        code="LEE",
        naam="Leem",
        parent=Materiaalsoort.grondstof,
    )

    silt = Referentiedata(
        code="SIL",
        naam="Silt",
        parent=Materiaalsoort.grondstof,
    )

    zand = Referentiedata(
        code="ZAN",
        naam="Zand",
        parent=Materiaalsoort.grondstof,
    )

    hardboard = Referentiedata(
        code="HBO",
        naam="Hardboard",
        parent=Materiaalsoort.grondstof,
    )

    hardhout = Referentiedata(
        code="HHO",
        naam="Hardhout",
        parent=Materiaalsoort.hout,
    )

    houtspaan = Referentiedata(
        code="HSP",
        naam="Houtspaan",
        parent=Materiaalsoort.hout,
    )

    accoya = Referentiedata(
        code="ACC",
        naam="Accoya",
        parent=Materiaalsoort.hout,
    )

    azobe = Referentiedata(
        code="AZO",
        naam="Azobe",
        parent=Materiaalsoort.hout,
    )

    balsa = Referentiedata(
        code="BAL",
        naam="Balsa",
        parent=Materiaalsoort.hout,
    )

    bangkirai = Referentiedata(
        code="BAN",
        naam="Bangkirai",
        parent=Materiaalsoort.hout,
    )

    berken = Referentiedata(
        code="BER",
        naam="Berken",
        parent=Materiaalsoort.hout,
    )

    beuken = Referentiedata(
        code="BEU",
        naam="Beuken",
        parent=Materiaalsoort.hout,
    )

    bilinga = Referentiedata(
        code="BIL",
        naam="Bilinga",
        parent=Materiaalsoort.hout,
    )

    board = Referentiedata(
        code="BOA",
        naam="Board",
        parent=Materiaalsoort.hout,
    )

    clt = Referentiedata(
        code="CLT",
        naam="Clt",
        parent=Materiaalsoort.hout,
    )

    douglas = Referentiedata(
        code="DOU",
        naam="Douglas",
        parent=Materiaalsoort.hout,
    )

    ebben = Referentiedata(
        code="EBB",
        naam="Ebben",
        parent=Materiaalsoort.hout,
    )

    eiken = Referentiedata(
        code="EIK",
        naam="Eiken",
        parent=Materiaalsoort.hout,
    )

    esdoorn = Referentiedata(
        code="ESD",
        naam="Esdoorn",
        parent=Materiaalsoort.hout,
    )

    essen = Referentiedata(
        code="ESS",
        naam="Essen",
        parent=Materiaalsoort.hout,
    )

    gemodificeerd = Referentiedata(
        code="GEM",
        naam="Gemodificeerd",
        parent=Materiaalsoort.hout,
    )

    grenen = Referentiedata(
        code="GRE",
        naam="Grenen",
        parent=Materiaalsoort.hout,
    )

    houtvezel = Referentiedata(
        code="HVE",
        naam="Houtvezel",
        parent=Materiaalsoort.hout,
    )

    houtwol = Referentiedata(
        code="HWO",
        naam="Houtwol",
        parent=Materiaalsoort.hout,
    )

    kersen = Referentiedata(
        code="KER",
        naam="Kersen",
        parent=Materiaalsoort.hout,
    )

    lariks = Referentiedata(
        code="LAR",
        naam="Lariks",
        parent=Materiaalsoort.hout,
    )

    mahonie = Referentiedata(
        code="MAH",
        naam="Mahonie",
        parent=Materiaalsoort.hout,
    )

    masonite = Referentiedata(
        code="MAS",
        naam="Masonite",
        parent=Materiaalsoort.hout,
    )

    mdf = Referentiedata(
        code="MDF",
        naam="Mdf",
        parent=Materiaalsoort.hout,
    )

    multiplex = Referentiedata(
        code="MUL",
        naam="Multiplex",
        parent=Materiaalsoort.hout,
    )

    noten = Referentiedata(
        code="NOT",
        naam="Noten",
        parent=Materiaalsoort.hout,
    )

    okoume = Referentiedata(
        code="OKO",
        naam="Okoume",
        parent=Materiaalsoort.hout,
    )

    osb = Referentiedata(
        code="OSB",
        naam="Osb",
        parent=Materiaalsoort.hout,
    )

    populieren = Referentiedata(
        code="POP",
        naam="Populieren",
        parent=Materiaalsoort.hout,
    )

    spaanplaat = Referentiedata(
        code="SPA",
        naam="Spaanplaat",
        parent=Materiaalsoort.hout,
    )

    triplex = Referentiedata(
        code="TRI",
        naam="Triplex",
        parent=Materiaalsoort.hout,
    )

    vuren = Referentiedata(
        code="VUR",
        naam="Vuren",
        parent=Materiaalsoort.hout,
    )

    wenge = Referentiedata(
        code="WEN",
        naam="Wenge",
        parent=Materiaalsoort.hout,
    )

    ceder = Referentiedata(
        code="CED",
        naam="Ceder",
        parent=Materiaalsoort.hout,
    )

    zaagsel = Referentiedata(
        code="ZAA",
        naam="Zaagsel",
        parent=Materiaalsoort.hout,
    )

    meranti = Referentiedata(
        code="MER",
        naam="Meranti",
        parent=Materiaalsoort.hout,
    )

    merbau = Referentiedata(
        code="MBA",
        naam="Merbau",
        parent=Materiaalsoort.hout,
    )

    zachtboard = Referentiedata(
        code="ZBO",
        naam="Zachtboard",
        parent=Materiaalsoort.hout,
    )

    zachthout = Referentiedata(
        code="ZHO",
        naam="Zachthout",
        parent=Materiaalsoort.hout,
    )

    geexpandeerd_perliet = Referentiedata(
        code="GEP",
        naam="Geexpandeerd-Perliet",
        parent=Materiaalsoort.hout,
    )

    hardschuim = Referentiedata(
        code="HSC",
        naam="Hardschuim",
        parent=Materiaalsoort.isolatie,
    )

    eps = Referentiedata(
        code="EPS",
        naam="Eps",
        parent=Materiaalsoort.isolatie,
    )

    fenolhars = Referentiedata(
        code="FEN",
        naam="Fenolhars",
        parent=Materiaalsoort.isolatie,
    )

    glaswol = Referentiedata(
        code="GLA",
        naam="Glaswol",
        parent=Materiaalsoort.isolatie,
    )

    resolschuim = Referentiedata(
        code="RES",
        naam="Resolschuim",
        parent=Materiaalsoort.isolatie,
    )

    pir = Referentiedata(
        code="PIR",
        naam="Pir",
        parent=Materiaalsoort.isolatie,
    )

    pur = Referentiedata(
        code="PUR",
        naam="Pur",
        parent=Materiaalsoort.isolatie,
    )

    mineralewol = Referentiedata(
        code="MNE",
        naam="Mineralewol",
        parent=Materiaalsoort.isolatie,
    )

    steenwol = Referentiedata(
        code="STE",
        naam="Steenwol",
        parent=Materiaalsoort.isolatie,
    )

    xps = Referentiedata(
        code="XPS",
        naam="Xps",
        parent=Materiaalsoort.isolatie,
    )

    mineraal = Referentiedata(
        code="MIN",
        naam="Mineraal",
        parent=Materiaalsoort.isolatie,
    )

    siliperliet = Referentiedata(
        code="SLI",
        naam="Siliperliet",
        parent=Materiaalsoort.isolatie,
    )

    solperlite = Referentiedata(
        code="SOL",
        naam="Solperlite",
        parent=Materiaalsoort.isolatie,
    )

    hard_kunststof = Referentiedata(
        code="HKU",
        naam="Hard-Kunststof",
        parent=Materiaalsoort.isolatie,
    )

    loodvervanger = Referentiedata(
        code="LVE",
        naam="Loodvervanger",
        parent=Materiaalsoort.kunststof,
    )

    abs = Referentiedata(
        code="ABS",
        naam="Abs",
        parent=Materiaalsoort.kunststof,
    )

    aeryl = Referentiedata(
        code="AER",
        naam="Aeryl",
        parent=Materiaalsoort.kunststof,
    )

    dpc = Referentiedata(
        code="DPC",
        naam="Dpc",
        parent=Materiaalsoort.kunststof,
    )

    elastomere_foam = Referentiedata(
        code="ELA",
        naam="Elastomere-Foam",
        parent=Materiaalsoort.kunststof,
    )

    ep = Referentiedata(
        code="EP",
        naam="Ep",
        parent=Materiaalsoort.kunststof,
    )

    epoxyhars = Referentiedata(
        code="EPO",
        naam="Epoxyhars",
        parent=Materiaalsoort.kunststof,
    )

    hdpe = Referentiedata(
        code="HDP",
        naam="Hdpe",
        parent=Materiaalsoort.kunststof,
    )

    hmpe = Referentiedata(
        code="HMP",
        naam="Hmpe",
        parent=Materiaalsoort.kunststof,
    )

    hpl = Referentiedata(
        code="HPL",
        naam="Hpl",
        parent=Materiaalsoort.kunststof,
    )

    ldpe = Referentiedata(
        code="LDP",
        naam="Ldpe",
        parent=Materiaalsoort.kunststof,
    )

    pe = Referentiedata(
        code="PE",
        naam="Pe",
        parent=Materiaalsoort.kunststof,
    )

    pmma = Referentiedata(
        code="PMM",
        naam="Pmma",
        parent=Materiaalsoort.kunststof,
    )

    pvac = Referentiedata(
        code="PVA",
        naam="Pvac",
        parent=Materiaalsoort.kunststof,
    )

    pa = Referentiedata(
        code="PA",
        naam="Pa",
        parent=Materiaalsoort.kunststof,
    )

    pc = Referentiedata(
        code="PC",
        naam="Pc",
        parent=Materiaalsoort.kunststof,
    )

    pctfe = Referentiedata(
        code="PCT",
        naam="Pctfe",
        parent=Materiaalsoort.kunststof,
    )

    plexiglas = Referentiedata(
        code="PLE",
        naam="Plexiglas",
        parent=Materiaalsoort.kunststof,
    )

    polyesterhars = Referentiedata(
        code="PLY",
        naam="Polyesterhars",
        parent=Materiaalsoort.kunststof,
    )

    pp = Referentiedata(
        code="PP",
        naam="Pp",
        parent=Materiaalsoort.kunststof,
    )

    ps = Referentiedata(
        code="PS",
        naam="Ps",
        parent=Materiaalsoort.kunststof,
    )

    ptfe = Referentiedata(
        code="PTF",
        naam="Ptfe",
        parent=Materiaalsoort.kunststof,
    )

    pu = Referentiedata(
        code="PU",
        naam="Pu",
        parent=Materiaalsoort.kunststof,
    )

    pvc = Referentiedata(
        code="PVC",
        naam="Pvc",
        parent=Materiaalsoort.kunststof,
    )

    polyester = Referentiedata(
        code="POL",
        naam="Polyester",
        parent=Materiaalsoort.kunststof,
    )

    silicagel = Referentiedata(
        code="SLG",
        naam="Silicagel",
        parent=Materiaalsoort.kunststof,
    )

    siliconen = Referentiedata(
        code="SLC",
        naam="Siliconen",
        parent=Materiaalsoort.kunststof,
    )

    zacht_kunststof = Referentiedata(
        code="ZKU",
        naam="Zacht-Kunststof",
        parent=Materiaalsoort.kunststof,
    )

    lood = Referentiedata(
        code="LOO",
        naam="Lood",
        parent=Materiaalsoort.kunststof,
    )

    platina = Referentiedata(
        code="PLA",
        naam="Platina",
        parent=Materiaalsoort.metaal,
    )

    aluminium = Referentiedata(
        code="ALU",
        naam="Aluminium",
        parent=Materiaalsoort.metaal,
    )

    brons = Referentiedata(
        code="BRO",
        naam="Brons",
        parent=Materiaalsoort.metaal,
    )

    chroom = Referentiedata(
        code="CHR",
        naam="Chroom",
        parent=Materiaalsoort.metaal,
    )

    gietijzer = Referentiedata(
        code="GIE",
        naam="Gietijzer",
        parent=Materiaalsoort.metaal,
    )

    goud = Referentiedata(
        code="GOU",
        naam="Goud",
        parent=Materiaalsoort.metaal,
    )

    ijzer = Referentiedata(
        code="IJZ",
        naam="Ijzer",
        parent=Materiaalsoort.metaal,
    )

    koper = Referentiedata(
        code="KOP",
        naam="Koper",
        parent=Materiaalsoort.metaal,
    )

    messing = Referentiedata(
        code="MES",
        naam="Messing",
        parent=Materiaalsoort.metaal,
    )

    rvs = Referentiedata(
        code="RVS",
        naam="Rvs",
        parent=Materiaalsoort.metaal,
    )

    tin = Referentiedata(
        code="TIN",
        naam="Tin",
        parent=Materiaalsoort.metaal,
    )

    titanium = Referentiedata(
        code="TIT",
        naam="Titanium",
        parent=Materiaalsoort.metaal,
    )

    zilver = Referentiedata(
        code="ZIL",
        naam="Zilver",
        parent=Materiaalsoort.metaal,
    )

    zink = Referentiedata(
        code="ZIN",
        naam="Zink",
        parent=Materiaalsoort.metaal,
    )

    soldeersel = Referentiedata(
        code="SDE",
        naam="Soldeersel",
        parent=Materiaalsoort.metaal,
    )

    staal = Referentiedata(
        code="STA",
        naam="Staal",
        parent=Materiaalsoort.metaal,
    )

    asbest = Referentiedata(
        code="ASB",
        naam="Asbest",
        parent=Materiaalsoort.metaal,
    )

    graniet = Referentiedata(
        code="GRA",
        naam="Graniet",
        parent=Materiaalsoort.natuursteen,
    )

    gravel = Referentiedata(
        code="GVE",
        naam="Gravel",
        parent=Materiaalsoort.natuursteen,
    )

    hardsteen = Referentiedata(
        code="HST",
        naam="Hardsteen",
        parent=Materiaalsoort.natuursteen,
    )

    kwartsiet = Referentiedata(
        code="KSI",
        naam="Kwartsiet",
        parent=Materiaalsoort.natuursteen,
    )

    poreus_gesteente = Referentiedata(
        code="PGE",
        naam="Poreus-Gesteente",
        parent=Materiaalsoort.natuursteen,
    )

    basalt = Referentiedata(
        code="BAS",
        naam="Basalt",
        parent=Materiaalsoort.natuursteen,
    )

    gneiss = Referentiedata(
        code="GNE",
        naam="Gneiss",
        parent=Materiaalsoort.natuursteen,
    )

    kristallijn_gesteente = Referentiedata(
        code="KRI",
        naam="Kristallijn-Gesteente",
        parent=Materiaalsoort.natuursteen,
    )

    lei = Referentiedata(
        code="LEI",
        naam="Lei",
        parent=Materiaalsoort.natuursteen,
    )

    marmer = Referentiedata(
        code="MAR",
        naam="Marmer",
        parent=Materiaalsoort.natuursteen,
    )

    puimsteen = Referentiedata(
        code="PUI",
        naam="Puimsteen",
        parent=Materiaalsoort.natuursteen,
    )

    sedimentgesteente = Referentiedata(
        code="SED",
        naam="Sedimentgesteente",
        parent=Materiaalsoort.natuursteen,
    )

    trachiet = Referentiedata(
        code="TRA",
        naam="Trachiet",
        parent=Materiaalsoort.natuursteen,
    )

    zandsteen = Referentiedata(
        code="ZST",
        naam="Zandsteen",
        parent=Materiaalsoort.natuursteen,
    )

    leer = Referentiedata(
        code="LER",
        naam="Leer",
        parent=Materiaalsoort.ntb,
    )

    plantaardige_vezel = Referentiedata(
        code="PTA",
        naam="Plantaardige-Vezel",
        parent=Materiaalsoort.organisch,
    )

    bamboe = Referentiedata(
        code="BAM",
        naam="Bamboe",
        parent=Materiaalsoort.organisch,
    )

    hennep = Referentiedata(
        code="HEN",
        naam="Hennep",
        parent=Materiaalsoort.organisch,
    )

    jute = Referentiedata(
        code="JUT",
        naam="Jute",
        parent=Materiaalsoort.organisch,
    )

    katoen = Referentiedata(
        code="KAT",
        naam="Katoen",
        parent=Materiaalsoort.organisch,
    )

    kurk = Referentiedata(
        code="KUR",
        naam="Kurk",
        parent=Materiaalsoort.organisch,
    )

    mais = Referentiedata(
        code="MAI",
        naam="Mais",
        parent=Materiaalsoort.organisch,
    )

    papier = Referentiedata(
        code="PAP",
        naam="Papier",
        parent=Materiaalsoort.organisch,
    )

    riet = Referentiedata(
        code="RIE",
        naam="Riet",
        parent=Materiaalsoort.organisch,
    )

    stro = Referentiedata(
        code="STR",
        naam="Stro",
        parent=Materiaalsoort.organisch,
    )

    vegetatie = Referentiedata(
        code="VEG",
        naam="Vegetatie",
        parent=Materiaalsoort.organisch,
    )

    vilt = Referentiedata(
        code="VIL",
        naam="Vilt",
        parent=Materiaalsoort.organisch,
    )

    vlas = Referentiedata(
        code="VLA",
        naam="Vlas",
        parent=Materiaalsoort.organisch,
    )

    wol = Referentiedata(
        code="WOL",
        naam="Wol",
        parent=Materiaalsoort.organisch,
    )

    hard_rubber = Referentiedata(
        code="HRU",
        naam="Hard-Rubber",
        parent=Materiaalsoort.organisch,
    )

    polysulfide = Referentiedata(
        code="PLS",
        naam="Polysulfide",
        parent=Materiaalsoort.rubber,
    )

    schuimrubber = Referentiedata(
        code="SRU",
        naam="Schuimrubber",
        parent=Materiaalsoort.rubber,
    )

    butyl = Referentiedata(
        code="BUT",
        naam="Butyl",
        parent=Materiaalsoort.rubber,
    )

    epdm = Referentiedata(
        code="EPD",
        naam="Epdm",
        parent=Materiaalsoort.rubber,
    )

    linoleum = Referentiedata(
        code="LIN",
        naam="Linoleum",
        parent=Materiaalsoort.rubber,
    )

    natuurrubber = Referentiedata(
        code="NAT",
        naam="Natuurrubber",
        parent=Materiaalsoort.rubber,
    )

    neopreen = Referentiedata(
        code="NEO",
        naam="Neopreen",
        parent=Materiaalsoort.rubber,
    )

    tpve = Referentiedata(
        code="TPV",
        naam="Tpve",
        parent=Materiaalsoort.rubber,
    )

    element = Referentiedata(
        code="ELE",
        naam="Element",
        parent=Materiaalsoort.rubber,
    )

    product = Referentiedata(
        code="PRO",
        naam="Product",
        parent=Materiaalsoort.samengesteld,
    )

    geexpandeerde_klei = Referentiedata(
        code="GEK",
        naam="Geexpandeerde-Klei",
        parent=Materiaalsoort.samengesteld,
    )

    kalksteen = Referentiedata(
        code="KST",
        naam="Kalksteen",
        parent=Materiaalsoort.steenachtig,
    )

    kalkzandsteen = Referentiedata(
        code="KZS",
        naam="Kalkzandsteen",
        parent=Materiaalsoort.steenachtig,
    )

    keramisch = Referentiedata(
        code="KRA",
        naam="Keramisch",
        parent=Materiaalsoort.steenachtig,
    )

    porisosteen = Referentiedata(
        code="PRI",
        naam="Porisosteen",
        parent=Materiaalsoort.steenachtig,
    )

    porselein = Referentiedata(
        code="PSE",
        naam="Porselein",
        parent=Materiaalsoort.steenachtig,
    )

    baksteen = Referentiedata(
        code="BAK",
        naam="Baksteen",
        parent=Materiaalsoort.steenachtig,
    )

    calciumsilicaat = Referentiedata(
        code="CAL",
        naam="Calciumsilicaat",
        parent=Materiaalsoort.steenachtig,
    )

    kunststeen = Referentiedata(
        code="KUN",
        naam="Kunststeen",
        parent=Materiaalsoort.steenachtig,
    )
