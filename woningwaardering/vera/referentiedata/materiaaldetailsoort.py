from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.materiaalsoort import Materiaalsoort


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
        parent=Materiaalsoort.beton.value,
    )

    bimsbeton = Referentiedata(
        code="BIM",
        naam="Bimsbeton",
        parent=Materiaalsoort.beton.value,
    )

    isolatiebeton = Referentiedata(
        code="ISO",
        naam="Isolatiebeton",
        parent=Materiaalsoort.beton.value,
    )

    lichtbeton = Referentiedata(
        code="LIC",
        naam="Lichtbeton",
        parent=Materiaalsoort.beton.value,
    )

    slakkenbeton = Referentiedata(
        code="SLA",
        naam="Slakkenbeton",
        parent=Materiaalsoort.beton.value,
    )

    voorgespannen = Referentiedata(
        code="VOO",
        naam="Voorgespannen",
        parent=Materiaalsoort.beton.value,
    )

    cellenbeton = Referentiedata(
        code="CEL",
        naam="Cellenbeton",
        parent=Materiaalsoort.beton.value,
    )

    gewapend = Referentiedata(
        code="GEW",
        naam="Gewapend",
    )

    grindbeton = Referentiedata(
        code="GBE",
        naam="Grindbeton",
        parent=Materiaalsoort.beton.value,
    )

    schuimbeton = Referentiedata(
        code="SBE",
        naam="Schuimbeton",
        parent=Materiaalsoort.beton.value,
    )

    spuitbeton = Referentiedata(
        code="SBT",
        naam="Spuitbeton",
        parent=Materiaalsoort.beton.value,
    )

    staalvezelbeton = Referentiedata(
        code="SVE",
        naam="Staalvezelbeton",
        parent=Materiaalsoort.beton.value,
    )

    asfalt = Referentiedata(
        code="ASF",
        naam="Asfalt",
        parent=Materiaalsoort.bitumen.value,
    )

    teer = Referentiedata(
        code="TEE",
        naam="Teer",
        parent=Materiaalsoort.bitumen.value,
    )

    asbestcement = Referentiedata(
        code="ACE",
        naam="Asbestcement",
        parent=Materiaalsoort.bitumen.value,
    )

    cementstuc = Referentiedata(
        code="CEM",
        naam="Cementstuc",
        parent=Materiaalsoort.cement.value,
    )

    grout = Referentiedata(
        code="GRO",
        naam="Grout",
        parent=Materiaalsoort.cement.value,
    )

    metselspecie = Referentiedata(
        code="MET",
        naam="Metselspecie",
        parent=Materiaalsoort.cement.value,
    )

    mortel = Referentiedata(
        code="MOR",
        naam="Mortel",
        parent=Materiaalsoort.cement.value,
    )

    terrazzo = Referentiedata(
        code="TER",
        naam="Terrazzo",
        parent=Materiaalsoort.cement.value,
    )

    vezelcement = Referentiedata(
        code="VEZ",
        naam="Vezelcement",
        parent=Materiaalsoort.cement.value,
    )

    houtvezelcement = Referentiedata(
        code="HVC",
        naam="Houtvezelcement",
        parent=Materiaalsoort.cement.value,
    )

    houtwolcement = Referentiedata(
        code="HWC",
        naam="Houtwolcement",
        parent=Materiaalsoort.cement.value,
    )

    spuitmortel = Referentiedata(
        code="SMO",
        naam="Spuitmortel",
        parent=Materiaalsoort.cement.value,
    )

    zandcement = Referentiedata(
        code="ZCE",
        naam="Zandcement",
        parent=Materiaalsoort.cement.value,
    )

    zandcement_vezel = Referentiedata(
        code="ZCV",
        naam="Zandcement-Vezel",
        parent=Materiaalsoort.cement.value,
    )

    anhydriet = Referentiedata(
        code="ANH",
        naam="Anhydriet",
        parent=Materiaalsoort.gips.value,
    )

    gipskarton = Referentiedata(
        code="GIP",
        naam="Gipskarton",
        parent=Materiaalsoort.gips.value,
    )

    stuc = Referentiedata(
        code="STU",
        naam="Stuc",
        parent=Materiaalsoort.gips.value,
    )

    spuitstuc = Referentiedata(
        code="SST",
        naam="Spuitstuc",
        parent=Materiaalsoort.gips.value,
    )

    cellulairglas = Referentiedata(
        code="CGL",
        naam="Cellulairglas",
        parent=Materiaalsoort.gips.value,
    )

    gehard = Referentiedata(
        code="GEH",
        naam="Gehard",
        parent=Materiaalsoort.glas.value,
    )

    helder = Referentiedata(
        code="HEL",
        naam="Helder",
        parent=Materiaalsoort.glas.value,
    )

    opaal = Referentiedata(
        code="OPA",
        naam="Opaal",
        parent=Materiaalsoort.glas.value,
    )

    spiegelend = Referentiedata(
        code="SPI",
        naam="Spiegelend",
        parent=Materiaalsoort.glas.value,
    )

    kwartsglas = Referentiedata(
        code="KWA",
        naam="Kwartsglas",
        parent=Materiaalsoort.glas.value,
    )

    bimszand = Referentiedata(
        code="BZA",
        naam="Bimszand",
        parent=Materiaalsoort.glas.value,
    )

    grind = Referentiedata(
        code="GRI",
        naam="Grind",
        parent=Materiaalsoort.grondstof.value,
    )

    aarde = Referentiedata(
        code="AAR",
        naam="Aarde",
        parent=Materiaalsoort.grondstof.value,
    )

    klei = Referentiedata(
        code="KLE",
        naam="Klei",
        parent=Materiaalsoort.grondstof.value,
    )

    lucht = Referentiedata(
        code="LUC",
        naam="Lucht",
        parent=Materiaalsoort.grondstof.value,
    )

    split = Referentiedata(
        code="SPL",
        naam="Split",
        parent=Materiaalsoort.grondstof.value,
    )

    turf = Referentiedata(
        code="TUR",
        naam="Turf",
        parent=Materiaalsoort.grondstof.value,
    )

    water = Referentiedata(
        code="WAT",
        naam="Water",
        parent=Materiaalsoort.grondstof.value,
    )

    kalk = Referentiedata(
        code="KAL",
        naam="Kalk",
        parent=Materiaalsoort.grondstof.value,
    )

    leem = Referentiedata(
        code="LEE",
        naam="Leem",
        parent=Materiaalsoort.grondstof.value,
    )

    silt = Referentiedata(
        code="SIL",
        naam="Silt",
        parent=Materiaalsoort.grondstof.value,
    )

    zand = Referentiedata(
        code="ZAN",
        naam="Zand",
        parent=Materiaalsoort.grondstof.value,
    )

    hardboard = Referentiedata(
        code="HBO",
        naam="Hardboard",
        parent=Materiaalsoort.grondstof.value,
    )

    hardhout = Referentiedata(
        code="HHO",
        naam="Hardhout",
        parent=Materiaalsoort.hout.value,
    )

    houtspaan = Referentiedata(
        code="HSP",
        naam="Houtspaan",
        parent=Materiaalsoort.hout.value,
    )

    accoya = Referentiedata(
        code="ACC",
        naam="Accoya",
        parent=Materiaalsoort.hout.value,
    )

    azobe = Referentiedata(
        code="AZO",
        naam="Azobe",
        parent=Materiaalsoort.hout.value,
    )

    balsa = Referentiedata(
        code="BAL",
        naam="Balsa",
        parent=Materiaalsoort.hout.value,
    )

    bangkirai = Referentiedata(
        code="BAN",
        naam="Bangkirai",
        parent=Materiaalsoort.hout.value,
    )

    berken = Referentiedata(
        code="BER",
        naam="Berken",
        parent=Materiaalsoort.hout.value,
    )

    beuken = Referentiedata(
        code="BEU",
        naam="Beuken",
        parent=Materiaalsoort.hout.value,
    )

    bilinga = Referentiedata(
        code="BIL",
        naam="Bilinga",
        parent=Materiaalsoort.hout.value,
    )

    board = Referentiedata(
        code="BOA",
        naam="Board",
        parent=Materiaalsoort.hout.value,
    )

    clt = Referentiedata(
        code="CLT",
        naam="Clt",
        parent=Materiaalsoort.hout.value,
    )

    douglas = Referentiedata(
        code="DOU",
        naam="Douglas",
        parent=Materiaalsoort.hout.value,
    )

    ebben = Referentiedata(
        code="EBB",
        naam="Ebben",
        parent=Materiaalsoort.hout.value,
    )

    eiken = Referentiedata(
        code="EIK",
        naam="Eiken",
        parent=Materiaalsoort.hout.value,
    )

    esdoorn = Referentiedata(
        code="ESD",
        naam="Esdoorn",
        parent=Materiaalsoort.hout.value,
    )

    essen = Referentiedata(
        code="ESS",
        naam="Essen",
        parent=Materiaalsoort.hout.value,
    )

    gemodificeerd = Referentiedata(
        code="GEM",
        naam="Gemodificeerd",
        parent=Materiaalsoort.hout.value,
    )

    grenen = Referentiedata(
        code="GRE",
        naam="Grenen",
        parent=Materiaalsoort.hout.value,
    )

    houtvezel = Referentiedata(
        code="HVE",
        naam="Houtvezel",
        parent=Materiaalsoort.hout.value,
    )

    houtwol = Referentiedata(
        code="HWO",
        naam="Houtwol",
        parent=Materiaalsoort.hout.value,
    )

    kersen = Referentiedata(
        code="KER",
        naam="Kersen",
        parent=Materiaalsoort.hout.value,
    )

    lariks = Referentiedata(
        code="LAR",
        naam="Lariks",
        parent=Materiaalsoort.hout.value,
    )

    mahonie = Referentiedata(
        code="MAH",
        naam="Mahonie",
        parent=Materiaalsoort.hout.value,
    )

    masonite = Referentiedata(
        code="MAS",
        naam="Masonite",
        parent=Materiaalsoort.hout.value,
    )

    mdf = Referentiedata(
        code="MDF",
        naam="Mdf",
        parent=Materiaalsoort.hout.value,
    )

    multiplex = Referentiedata(
        code="MUL",
        naam="Multiplex",
        parent=Materiaalsoort.hout.value,
    )

    noten = Referentiedata(
        code="NOT",
        naam="Noten",
        parent=Materiaalsoort.hout.value,
    )

    okoume = Referentiedata(
        code="OKO",
        naam="Okoume",
        parent=Materiaalsoort.hout.value,
    )

    osb = Referentiedata(
        code="OSB",
        naam="Osb",
        parent=Materiaalsoort.hout.value,
    )

    populieren = Referentiedata(
        code="POP",
        naam="Populieren",
        parent=Materiaalsoort.hout.value,
    )

    spaanplaat = Referentiedata(
        code="SPA",
        naam="Spaanplaat",
        parent=Materiaalsoort.hout.value,
    )

    triplex = Referentiedata(
        code="TRI",
        naam="Triplex",
        parent=Materiaalsoort.hout.value,
    )

    vuren = Referentiedata(
        code="VUR",
        naam="Vuren",
        parent=Materiaalsoort.hout.value,
    )

    wenge = Referentiedata(
        code="WEN",
        naam="Wenge",
        parent=Materiaalsoort.hout.value,
    )

    ceder = Referentiedata(
        code="CED",
        naam="Ceder",
        parent=Materiaalsoort.hout.value,
    )

    zaagsel = Referentiedata(
        code="ZAA",
        naam="Zaagsel",
        parent=Materiaalsoort.hout.value,
    )

    meranti = Referentiedata(
        code="MER",
        naam="Meranti",
        parent=Materiaalsoort.hout.value,
    )

    merbau = Referentiedata(
        code="MBA",
        naam="Merbau",
        parent=Materiaalsoort.hout.value,
    )

    zachtboard = Referentiedata(
        code="ZBO",
        naam="Zachtboard",
        parent=Materiaalsoort.hout.value,
    )

    zachthout = Referentiedata(
        code="ZHO",
        naam="Zachthout",
        parent=Materiaalsoort.hout.value,
    )

    geexpandeerd_perliet = Referentiedata(
        code="GEP",
        naam="Geexpandeerd-Perliet",
        parent=Materiaalsoort.hout.value,
    )

    hardschuim = Referentiedata(
        code="HSC",
        naam="Hardschuim",
        parent=Materiaalsoort.isolatie.value,
    )

    eps = Referentiedata(
        code="EPS",
        naam="Eps",
        parent=Materiaalsoort.isolatie.value,
    )

    fenolhars = Referentiedata(
        code="FEN",
        naam="Fenolhars",
        parent=Materiaalsoort.isolatie.value,
    )

    glaswol = Referentiedata(
        code="GLA",
        naam="Glaswol",
        parent=Materiaalsoort.isolatie.value,
    )

    resolschuim = Referentiedata(
        code="RES",
        naam="Resolschuim",
        parent=Materiaalsoort.isolatie.value,
    )

    pir = Referentiedata(
        code="PIR",
        naam="Pir",
        parent=Materiaalsoort.isolatie.value,
    )

    pur = Referentiedata(
        code="PUR",
        naam="Pur",
        parent=Materiaalsoort.isolatie.value,
    )

    mineralewol = Referentiedata(
        code="MNE",
        naam="Mineralewol",
        parent=Materiaalsoort.isolatie.value,
    )

    steenwol = Referentiedata(
        code="STE",
        naam="Steenwol",
        parent=Materiaalsoort.isolatie.value,
    )

    xps = Referentiedata(
        code="XPS",
        naam="Xps",
        parent=Materiaalsoort.isolatie.value,
    )

    mineraal = Referentiedata(
        code="MIN",
        naam="Mineraal",
        parent=Materiaalsoort.isolatie.value,
    )

    siliperliet = Referentiedata(
        code="SLI",
        naam="Siliperliet",
        parent=Materiaalsoort.isolatie.value,
    )

    solperlite = Referentiedata(
        code="SOL",
        naam="Solperlite",
        parent=Materiaalsoort.isolatie.value,
    )

    hard_kunststof = Referentiedata(
        code="HKU",
        naam="Hard-Kunststof",
        parent=Materiaalsoort.isolatie.value,
    )

    loodvervanger = Referentiedata(
        code="LVE",
        naam="Loodvervanger",
        parent=Materiaalsoort.kunststof.value,
    )

    abs = Referentiedata(
        code="ABS",
        naam="Abs",
        parent=Materiaalsoort.kunststof.value,
    )

    aeryl = Referentiedata(
        code="AER",
        naam="Aeryl",
        parent=Materiaalsoort.kunststof.value,
    )

    dpc = Referentiedata(
        code="DPC",
        naam="Dpc",
        parent=Materiaalsoort.kunststof.value,
    )

    elastomere_foam = Referentiedata(
        code="ELA",
        naam="Elastomere-Foam",
        parent=Materiaalsoort.kunststof.value,
    )

    ep = Referentiedata(
        code="EP",
        naam="Ep",
        parent=Materiaalsoort.kunststof.value,
    )

    epoxyhars = Referentiedata(
        code="EPO",
        naam="Epoxyhars",
        parent=Materiaalsoort.kunststof.value,
    )

    hdpe = Referentiedata(
        code="HDP",
        naam="Hdpe",
        parent=Materiaalsoort.kunststof.value,
    )

    hmpe = Referentiedata(
        code="HMP",
        naam="Hmpe",
        parent=Materiaalsoort.kunststof.value,
    )

    hpl = Referentiedata(
        code="HPL",
        naam="Hpl",
        parent=Materiaalsoort.kunststof.value,
    )

    ldpe = Referentiedata(
        code="LDP",
        naam="Ldpe",
        parent=Materiaalsoort.kunststof.value,
    )

    pe = Referentiedata(
        code="PE",
        naam="Pe",
        parent=Materiaalsoort.kunststof.value,
    )

    pmma = Referentiedata(
        code="PMM",
        naam="Pmma",
        parent=Materiaalsoort.kunststof.value,
    )

    pvac = Referentiedata(
        code="PVA",
        naam="Pvac",
        parent=Materiaalsoort.kunststof.value,
    )

    pa = Referentiedata(
        code="PA",
        naam="Pa",
        parent=Materiaalsoort.kunststof.value,
    )

    pc = Referentiedata(
        code="PC",
        naam="Pc",
        parent=Materiaalsoort.kunststof.value,
    )

    pctfe = Referentiedata(
        code="PCT",
        naam="Pctfe",
        parent=Materiaalsoort.kunststof.value,
    )

    plexiglas = Referentiedata(
        code="PLE",
        naam="Plexiglas",
        parent=Materiaalsoort.kunststof.value,
    )

    polyesterhars = Referentiedata(
        code="PLY",
        naam="Polyesterhars",
        parent=Materiaalsoort.kunststof.value,
    )

    pp = Referentiedata(
        code="PP",
        naam="Pp",
        parent=Materiaalsoort.kunststof.value,
    )

    ps = Referentiedata(
        code="PS",
        naam="Ps",
        parent=Materiaalsoort.kunststof.value,
    )

    ptfe = Referentiedata(
        code="PTF",
        naam="Ptfe",
        parent=Materiaalsoort.kunststof.value,
    )

    pu = Referentiedata(
        code="PU",
        naam="Pu",
        parent=Materiaalsoort.kunststof.value,
    )

    pvc = Referentiedata(
        code="PVC",
        naam="Pvc",
        parent=Materiaalsoort.kunststof.value,
    )

    polyester = Referentiedata(
        code="POL",
        naam="Polyester",
        parent=Materiaalsoort.kunststof.value,
    )

    silicagel = Referentiedata(
        code="SLG",
        naam="Silicagel",
        parent=Materiaalsoort.kunststof.value,
    )

    siliconen = Referentiedata(
        code="SLC",
        naam="Siliconen",
        parent=Materiaalsoort.kunststof.value,
    )

    zacht_kunststof = Referentiedata(
        code="ZKU",
        naam="Zacht-Kunststof",
        parent=Materiaalsoort.kunststof.value,
    )

    lood = Referentiedata(
        code="LOO",
        naam="Lood",
        parent=Materiaalsoort.kunststof.value,
    )

    platina = Referentiedata(
        code="PLA",
        naam="Platina",
        parent=Materiaalsoort.metaal.value,
    )

    aluminium = Referentiedata(
        code="ALU",
        naam="Aluminium",
        parent=Materiaalsoort.metaal.value,
    )

    brons = Referentiedata(
        code="BRO",
        naam="Brons",
        parent=Materiaalsoort.metaal.value,
    )

    chroom = Referentiedata(
        code="CHR",
        naam="Chroom",
        parent=Materiaalsoort.metaal.value,
    )

    gietijzer = Referentiedata(
        code="GIE",
        naam="Gietijzer",
        parent=Materiaalsoort.metaal.value,
    )

    goud = Referentiedata(
        code="GOU",
        naam="Goud",
        parent=Materiaalsoort.metaal.value,
    )

    ijzer = Referentiedata(
        code="IJZ",
        naam="Ijzer",
        parent=Materiaalsoort.metaal.value,
    )

    koper = Referentiedata(
        code="KOP",
        naam="Koper",
        parent=Materiaalsoort.metaal.value,
    )

    messing = Referentiedata(
        code="MES",
        naam="Messing",
        parent=Materiaalsoort.metaal.value,
    )

    rvs = Referentiedata(
        code="RVS",
        naam="Rvs",
        parent=Materiaalsoort.metaal.value,
    )

    tin = Referentiedata(
        code="TIN",
        naam="Tin",
        parent=Materiaalsoort.metaal.value,
    )

    titanium = Referentiedata(
        code="TIT",
        naam="Titanium",
        parent=Materiaalsoort.metaal.value,
    )

    zilver = Referentiedata(
        code="ZIL",
        naam="Zilver",
        parent=Materiaalsoort.metaal.value,
    )

    zink = Referentiedata(
        code="ZIN",
        naam="Zink",
        parent=Materiaalsoort.metaal.value,
    )

    soldeersel = Referentiedata(
        code="SDE",
        naam="Soldeersel",
        parent=Materiaalsoort.metaal.value,
    )

    staal = Referentiedata(
        code="STA",
        naam="Staal",
        parent=Materiaalsoort.metaal.value,
    )

    asbest = Referentiedata(
        code="ASB",
        naam="Asbest",
        parent=Materiaalsoort.metaal.value,
    )

    graniet = Referentiedata(
        code="GRA",
        naam="Graniet",
        parent=Materiaalsoort.natuursteen.value,
    )

    gravel = Referentiedata(
        code="GVE",
        naam="Gravel",
        parent=Materiaalsoort.natuursteen.value,
    )

    hardsteen = Referentiedata(
        code="HST",
        naam="Hardsteen",
        parent=Materiaalsoort.natuursteen.value,
    )

    kwartsiet = Referentiedata(
        code="KSI",
        naam="Kwartsiet",
        parent=Materiaalsoort.natuursteen.value,
    )

    poreus_gesteente = Referentiedata(
        code="PGE",
        naam="Poreus-Gesteente",
        parent=Materiaalsoort.natuursteen.value,
    )

    basalt = Referentiedata(
        code="BAS",
        naam="Basalt",
        parent=Materiaalsoort.natuursteen.value,
    )

    gneiss = Referentiedata(
        code="GNE",
        naam="Gneiss",
        parent=Materiaalsoort.natuursteen.value,
    )

    kristallijn_gesteente = Referentiedata(
        code="KRI",
        naam="Kristallijn-Gesteente",
        parent=Materiaalsoort.natuursteen.value,
    )

    lei = Referentiedata(
        code="LEI",
        naam="Lei",
        parent=Materiaalsoort.natuursteen.value,
    )

    marmer = Referentiedata(
        code="MAR",
        naam="Marmer",
        parent=Materiaalsoort.natuursteen.value,
    )

    puimsteen = Referentiedata(
        code="PUI",
        naam="Puimsteen",
        parent=Materiaalsoort.natuursteen.value,
    )

    sedimentgesteente = Referentiedata(
        code="SED",
        naam="Sedimentgesteente",
        parent=Materiaalsoort.natuursteen.value,
    )

    trachiet = Referentiedata(
        code="TRA",
        naam="Trachiet",
        parent=Materiaalsoort.natuursteen.value,
    )

    zandsteen = Referentiedata(
        code="ZST",
        naam="Zandsteen",
        parent=Materiaalsoort.natuursteen.value,
    )

    leer = Referentiedata(
        code="LER",
        naam="Leer",
        parent=Materiaalsoort.ntb.value,
    )

    plantaardige_vezel = Referentiedata(
        code="PTA",
        naam="Plantaardige-Vezel",
        parent=Materiaalsoort.organisch.value,
    )

    bamboe = Referentiedata(
        code="BAM",
        naam="Bamboe",
        parent=Materiaalsoort.organisch.value,
    )

    hennep = Referentiedata(
        code="HEN",
        naam="Hennep",
        parent=Materiaalsoort.organisch.value,
    )

    jute = Referentiedata(
        code="JUT",
        naam="Jute",
        parent=Materiaalsoort.organisch.value,
    )

    katoen = Referentiedata(
        code="KAT",
        naam="Katoen",
        parent=Materiaalsoort.organisch.value,
    )

    kurk = Referentiedata(
        code="KUR",
        naam="Kurk",
        parent=Materiaalsoort.organisch.value,
    )

    mais = Referentiedata(
        code="MAI",
        naam="Mais",
        parent=Materiaalsoort.organisch.value,
    )

    papier = Referentiedata(
        code="PAP",
        naam="Papier",
        parent=Materiaalsoort.organisch.value,
    )

    riet = Referentiedata(
        code="RIE",
        naam="Riet",
        parent=Materiaalsoort.organisch.value,
    )

    stro = Referentiedata(
        code="STR",
        naam="Stro",
        parent=Materiaalsoort.organisch.value,
    )

    vegetatie = Referentiedata(
        code="VEG",
        naam="Vegetatie",
        parent=Materiaalsoort.organisch.value,
    )

    vilt = Referentiedata(
        code="VIL",
        naam="Vilt",
        parent=Materiaalsoort.organisch.value,
    )

    vlas = Referentiedata(
        code="VLA",
        naam="Vlas",
        parent=Materiaalsoort.organisch.value,
    )

    wol = Referentiedata(
        code="WOL",
        naam="Wol",
        parent=Materiaalsoort.organisch.value,
    )

    hard_rubber = Referentiedata(
        code="HRU",
        naam="Hard-Rubber",
        parent=Materiaalsoort.organisch.value,
    )

    polysulfide = Referentiedata(
        code="PLS",
        naam="Polysulfide",
        parent=Materiaalsoort.rubber.value,
    )

    schuimrubber = Referentiedata(
        code="SRU",
        naam="Schuimrubber",
        parent=Materiaalsoort.rubber.value,
    )

    butyl = Referentiedata(
        code="BUT",
        naam="Butyl",
        parent=Materiaalsoort.rubber.value,
    )

    epdm = Referentiedata(
        code="EPD",
        naam="Epdm",
        parent=Materiaalsoort.rubber.value,
    )

    linoleum = Referentiedata(
        code="LIN",
        naam="Linoleum",
        parent=Materiaalsoort.rubber.value,
    )

    natuurrubber = Referentiedata(
        code="NAT",
        naam="Natuurrubber",
        parent=Materiaalsoort.rubber.value,
    )

    neopreen = Referentiedata(
        code="NEO",
        naam="Neopreen",
        parent=Materiaalsoort.rubber.value,
    )

    tpve = Referentiedata(
        code="TPV",
        naam="Tpve",
        parent=Materiaalsoort.rubber.value,
    )

    element = Referentiedata(
        code="ELE",
        naam="Element",
        parent=Materiaalsoort.rubber.value,
    )

    product = Referentiedata(
        code="PRO",
        naam="Product",
        parent=Materiaalsoort.samengesteld.value,
    )

    geexpandeerde_klei = Referentiedata(
        code="GEK",
        naam="Geexpandeerde-Klei",
        parent=Materiaalsoort.samengesteld.value,
    )

    kalksteen = Referentiedata(
        code="KST",
        naam="Kalksteen",
        parent=Materiaalsoort.steenachtig.value,
    )

    kalkzandsteen = Referentiedata(
        code="KZS",
        naam="Kalkzandsteen",
        parent=Materiaalsoort.steenachtig.value,
    )

    keramisch = Referentiedata(
        code="KRA",
        naam="Keramisch",
        parent=Materiaalsoort.steenachtig.value,
    )

    porisosteen = Referentiedata(
        code="PRI",
        naam="Porisosteen",
        parent=Materiaalsoort.steenachtig.value,
    )

    porselein = Referentiedata(
        code="PSE",
        naam="Porselein",
        parent=Materiaalsoort.steenachtig.value,
    )

    baksteen = Referentiedata(
        code="BAK",
        naam="Baksteen",
        parent=Materiaalsoort.steenachtig.value,
    )

    calciumsilicaat = Referentiedata(
        code="CAL",
        naam="Calciumsilicaat",
        parent=Materiaalsoort.steenachtig.value,
    )

    kunststeen = Referentiedata(
        code="KUN",
        naam="Kunststeen",
        parent=Materiaalsoort.steenachtig.value,
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
