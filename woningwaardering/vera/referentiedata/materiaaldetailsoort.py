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
    )

    bimsbeton = Referentiedata(
        code="BIM",
        naam="Bimsbeton",
    )

    isolatiebeton = Referentiedata(
        code="ISO",
        naam="Isolatiebeton",
    )

    lichtbeton = Referentiedata(
        code="LIC",
        naam="Lichtbeton",
    )

    slakkenbeton = Referentiedata(
        code="SLA",
        naam="Slakkenbeton",
    )

    voorgespannen = Referentiedata(
        code="VOO",
        naam="Voorgespannen",
    )

    cellenbeton = Referentiedata(
        code="CEL",
        naam="Cellenbeton",
    )

    gewapend = Referentiedata(
        code="GEW",
        naam="Gewapend",
    )

    grindbeton = Referentiedata(
        code="GBE",
        naam="Grindbeton",
    )

    schuimbeton = Referentiedata(
        code="SBE",
        naam="Schuimbeton",
    )

    spuitbeton = Referentiedata(
        code="SBT",
        naam="Spuitbeton",
    )

    staalvezelbeton = Referentiedata(
        code="SVE",
        naam="Staalvezelbeton",
    )

    asfalt = Referentiedata(
        code="ASF",
        naam="Asfalt",
    )

    teer = Referentiedata(
        code="TEE",
        naam="Teer",
    )

    asbestcement = Referentiedata(
        code="ACE",
        naam="Asbestcement",
    )

    cementstuc = Referentiedata(
        code="CEM",
        naam="Cementstuc",
    )

    grout = Referentiedata(
        code="GRO",
        naam="Grout",
    )

    metselspecie = Referentiedata(
        code="MET",
        naam="Metselspecie",
    )

    mortel = Referentiedata(
        code="MOR",
        naam="Mortel",
    )

    terrazzo = Referentiedata(
        code="TER",
        naam="Terrazzo",
    )

    vezelcement = Referentiedata(
        code="VEZ",
        naam="Vezelcement",
    )

    houtvezelcement = Referentiedata(
        code="HVC",
        naam="Houtvezelcement",
    )

    houtwolcement = Referentiedata(
        code="HWC",
        naam="Houtwolcement",
    )

    spuitmortel = Referentiedata(
        code="SMO",
        naam="Spuitmortel",
    )

    zandcement = Referentiedata(
        code="ZCE",
        naam="Zandcement",
    )

    zandcement_vezel = Referentiedata(
        code="ZCV",
        naam="Zandcement-Vezel",
    )

    anhydriet = Referentiedata(
        code="ANH",
        naam="Anhydriet",
    )

    gipskarton = Referentiedata(
        code="GIP",
        naam="Gipskarton",
    )

    stuc = Referentiedata(
        code="STU",
        naam="Stuc",
    )

    spuitstuc = Referentiedata(
        code="SST",
        naam="Spuitstuc",
    )

    cellulairglas = Referentiedata(
        code="CGL",
        naam="Cellulairglas",
    )

    gehard = Referentiedata(
        code="GEH",
        naam="Gehard",
    )

    helder = Referentiedata(
        code="HEL",
        naam="Helder",
    )

    opaal = Referentiedata(
        code="OPA",
        naam="Opaal",
    )

    spiegelend = Referentiedata(
        code="SPI",
        naam="Spiegelend",
    )

    kwartsglas = Referentiedata(
        code="KWA",
        naam="Kwartsglas",
    )

    bimszand = Referentiedata(
        code="BZA",
        naam="Bimszand",
    )

    grind = Referentiedata(
        code="GRI",
        naam="Grind",
    )

    aarde = Referentiedata(
        code="AAR",
        naam="Aarde",
    )

    klei = Referentiedata(
        code="KLE",
        naam="Klei",
    )

    lucht = Referentiedata(
        code="LUC",
        naam="Lucht",
    )

    split = Referentiedata(
        code="SPL",
        naam="Split",
    )

    turf = Referentiedata(
        code="TUR",
        naam="Turf",
    )

    water = Referentiedata(
        code="WAT",
        naam="Water",
    )

    kalk = Referentiedata(
        code="KAL",
        naam="Kalk",
    )

    leem = Referentiedata(
        code="LEE",
        naam="Leem",
    )

    silt = Referentiedata(
        code="SIL",
        naam="Silt",
    )

    zand = Referentiedata(
        code="ZAN",
        naam="Zand",
    )

    hardboard = Referentiedata(
        code="HBO",
        naam="Hardboard",
    )

    hardhout = Referentiedata(
        code="HHO",
        naam="Hardhout",
    )

    houtspaan = Referentiedata(
        code="HSP",
        naam="Houtspaan",
    )

    accoya = Referentiedata(
        code="ACC",
        naam="Accoya",
    )

    azobe = Referentiedata(
        code="AZO",
        naam="Azobe",
    )

    balsa = Referentiedata(
        code="BAL",
        naam="Balsa",
    )

    bangkirai = Referentiedata(
        code="BAN",
        naam="Bangkirai",
    )

    berken = Referentiedata(
        code="BER",
        naam="Berken",
    )

    beuken = Referentiedata(
        code="BEU",
        naam="Beuken",
    )

    bilinga = Referentiedata(
        code="BIL",
        naam="Bilinga",
    )

    board = Referentiedata(
        code="BOA",
        naam="Board",
    )

    clt = Referentiedata(
        code="CLT",
        naam="Clt",
    )

    douglas = Referentiedata(
        code="DOU",
        naam="Douglas",
    )

    ebben = Referentiedata(
        code="EBB",
        naam="Ebben",
    )

    eiken = Referentiedata(
        code="EIK",
        naam="Eiken",
    )

    esdoorn = Referentiedata(
        code="ESD",
        naam="Esdoorn",
    )

    essen = Referentiedata(
        code="ESS",
        naam="Essen",
    )

    gemodificeerd = Referentiedata(
        code="GEM",
        naam="Gemodificeerd",
    )

    grenen = Referentiedata(
        code="GRE",
        naam="Grenen",
    )

    houtvezel = Referentiedata(
        code="HVE",
        naam="Houtvezel",
    )

    houtwol = Referentiedata(
        code="HWO",
        naam="Houtwol",
    )

    kersen = Referentiedata(
        code="KER",
        naam="Kersen",
    )

    lariks = Referentiedata(
        code="LAR",
        naam="Lariks",
    )

    mahonie = Referentiedata(
        code="MAH",
        naam="Mahonie",
    )

    masonite = Referentiedata(
        code="MAS",
        naam="Masonite",
    )

    mdf = Referentiedata(
        code="MDF",
        naam="Mdf",
    )

    multiplex = Referentiedata(
        code="MUL",
        naam="Multiplex",
    )

    noten = Referentiedata(
        code="NOT",
        naam="Noten",
    )

    okoume = Referentiedata(
        code="OKO",
        naam="Okoume",
    )

    osb = Referentiedata(
        code="OSB",
        naam="Osb",
    )

    populieren = Referentiedata(
        code="POP",
        naam="Populieren",
    )

    spaanplaat = Referentiedata(
        code="SPA",
        naam="Spaanplaat",
    )

    triplex = Referentiedata(
        code="TRI",
        naam="Triplex",
    )

    vuren = Referentiedata(
        code="VUR",
        naam="Vuren",
    )

    wenge = Referentiedata(
        code="WEN",
        naam="Wenge",
    )

    ceder = Referentiedata(
        code="CED",
        naam="Ceder",
    )

    zaagsel = Referentiedata(
        code="ZAA",
        naam="Zaagsel",
    )

    meranti = Referentiedata(
        code="MER",
        naam="Meranti",
    )

    merbau = Referentiedata(
        code="MBA",
        naam="Merbau",
    )

    zachtboard = Referentiedata(
        code="ZBO",
        naam="Zachtboard",
    )

    zachthout = Referentiedata(
        code="ZHO",
        naam="Zachthout",
    )

    geexpandeerd_perliet = Referentiedata(
        code="GEP",
        naam="Geexpandeerd-Perliet",
    )

    hardschuim = Referentiedata(
        code="HSC",
        naam="Hardschuim",
    )

    eps = Referentiedata(
        code="EPS",
        naam="Eps",
    )

    fenolhars = Referentiedata(
        code="FEN",
        naam="Fenolhars",
    )

    glaswol = Referentiedata(
        code="GLA",
        naam="Glaswol",
    )

    resolschuim = Referentiedata(
        code="RES",
        naam="Resolschuim",
    )

    pir = Referentiedata(
        code="PIR",
        naam="Pir",
    )

    pur = Referentiedata(
        code="PUR",
        naam="Pur",
    )

    mineralewol = Referentiedata(
        code="MNE",
        naam="Mineralewol",
    )

    steenwol = Referentiedata(
        code="STE",
        naam="Steenwol",
    )

    xps = Referentiedata(
        code="XPS",
        naam="Xps",
    )

    mineraal = Referentiedata(
        code="MIN",
        naam="Mineraal",
    )

    siliperliet = Referentiedata(
        code="SLI",
        naam="Siliperliet",
    )

    solperlite = Referentiedata(
        code="SOL",
        naam="Solperlite",
    )

    hard_kunststof = Referentiedata(
        code="HKU",
        naam="Hard-Kunststof",
    )

    loodvervanger = Referentiedata(
        code="LVE",
        naam="Loodvervanger",
    )

    abs = Referentiedata(
        code="ABS",
        naam="Abs",
    )

    aeryl = Referentiedata(
        code="AER",
        naam="Aeryl",
    )

    dpc = Referentiedata(
        code="DPC",
        naam="Dpc",
    )

    elastomere_foam = Referentiedata(
        code="ELA",
        naam="Elastomere-Foam",
    )

    ep = Referentiedata(
        code="EP",
        naam="Ep",
    )

    epoxyhars = Referentiedata(
        code="EPO",
        naam="Epoxyhars",
    )

    hdpe = Referentiedata(
        code="HDP",
        naam="Hdpe",
    )

    hmpe = Referentiedata(
        code="HMP",
        naam="Hmpe",
    )

    hpl = Referentiedata(
        code="HPL",
        naam="Hpl",
    )

    ldpe = Referentiedata(
        code="LDP",
        naam="Ldpe",
    )

    pe = Referentiedata(
        code="PE",
        naam="Pe",
    )

    pmma = Referentiedata(
        code="PMM",
        naam="Pmma",
    )

    pvac = Referentiedata(
        code="PVA",
        naam="Pvac",
    )

    pa = Referentiedata(
        code="PA",
        naam="Pa",
    )

    pc = Referentiedata(
        code="PC",
        naam="Pc",
    )

    pctfe = Referentiedata(
        code="PCT",
        naam="Pctfe",
    )

    plexiglas = Referentiedata(
        code="PLE",
        naam="Plexiglas",
    )

    polyesterhars = Referentiedata(
        code="PLY",
        naam="Polyesterhars",
    )

    pp = Referentiedata(
        code="PP",
        naam="Pp",
    )

    ps = Referentiedata(
        code="PS",
        naam="Ps",
    )

    ptfe = Referentiedata(
        code="PTF",
        naam="Ptfe",
    )

    pu = Referentiedata(
        code="PU",
        naam="Pu",
    )

    pvc = Referentiedata(
        code="PVC",
        naam="Pvc",
    )

    polyester = Referentiedata(
        code="POL",
        naam="Polyester",
    )

    silicagel = Referentiedata(
        code="SLG",
        naam="Silicagel",
    )

    siliconen = Referentiedata(
        code="SLC",
        naam="Siliconen",
    )

    zacht_kunststof = Referentiedata(
        code="ZKU",
        naam="Zacht-Kunststof",
    )

    lood = Referentiedata(
        code="LOO",
        naam="Lood",
    )

    platina = Referentiedata(
        code="PLA",
        naam="Platina",
    )

    aluminium = Referentiedata(
        code="ALU",
        naam="Aluminium",
    )

    brons = Referentiedata(
        code="BRO",
        naam="Brons",
    )

    chroom = Referentiedata(
        code="CHR",
        naam="Chroom",
    )

    gietijzer = Referentiedata(
        code="GIE",
        naam="Gietijzer",
    )

    goud = Referentiedata(
        code="GOU",
        naam="Goud",
    )

    ijzer = Referentiedata(
        code="IJZ",
        naam="Ijzer",
    )

    koper = Referentiedata(
        code="KOP",
        naam="Koper",
    )

    messing = Referentiedata(
        code="MES",
        naam="Messing",
    )

    rvs = Referentiedata(
        code="RVS",
        naam="Rvs",
    )

    tin = Referentiedata(
        code="TIN",
        naam="Tin",
    )

    titanium = Referentiedata(
        code="TIT",
        naam="Titanium",
    )

    zilver = Referentiedata(
        code="ZIL",
        naam="Zilver",
    )

    zink = Referentiedata(
        code="ZIN",
        naam="Zink",
    )

    soldeersel = Referentiedata(
        code="SDE",
        naam="Soldeersel",
    )

    staal = Referentiedata(
        code="STA",
        naam="Staal",
    )

    asbest = Referentiedata(
        code="ASB",
        naam="Asbest",
    )

    graniet = Referentiedata(
        code="GRA",
        naam="Graniet",
    )

    gravel = Referentiedata(
        code="GVE",
        naam="Gravel",
    )

    hardsteen = Referentiedata(
        code="HST",
        naam="Hardsteen",
    )

    kwartsiet = Referentiedata(
        code="KSI",
        naam="Kwartsiet",
    )

    poreus_gesteente = Referentiedata(
        code="PGE",
        naam="Poreus-Gesteente",
    )

    basalt = Referentiedata(
        code="BAS",
        naam="Basalt",
    )

    gneiss = Referentiedata(
        code="GNE",
        naam="Gneiss",
    )

    kristallijn_gesteente = Referentiedata(
        code="KRI",
        naam="Kristallijn-Gesteente",
    )

    lei = Referentiedata(
        code="LEI",
        naam="Lei",
    )

    marmer = Referentiedata(
        code="MAR",
        naam="Marmer",
    )

    puimsteen = Referentiedata(
        code="PUI",
        naam="Puimsteen",
    )

    sedimentgesteente = Referentiedata(
        code="SED",
        naam="Sedimentgesteente",
    )

    trachiet = Referentiedata(
        code="TRA",
        naam="Trachiet",
    )

    zandsteen = Referentiedata(
        code="ZST",
        naam="Zandsteen",
    )

    leer = Referentiedata(
        code="LER",
        naam="Leer",
    )

    plantaardige_vezel = Referentiedata(
        code="PTA",
        naam="Plantaardige-Vezel",
    )

    bamboe = Referentiedata(
        code="BAM",
        naam="Bamboe",
    )

    hennep = Referentiedata(
        code="HEN",
        naam="Hennep",
    )

    jute = Referentiedata(
        code="JUT",
        naam="Jute",
    )

    katoen = Referentiedata(
        code="KAT",
        naam="Katoen",
    )

    kurk = Referentiedata(
        code="KUR",
        naam="Kurk",
    )

    mais = Referentiedata(
        code="MAI",
        naam="Mais",
    )

    papier = Referentiedata(
        code="PAP",
        naam="Papier",
    )

    riet = Referentiedata(
        code="RIE",
        naam="Riet",
    )

    stro = Referentiedata(
        code="STR",
        naam="Stro",
    )

    vegetatie = Referentiedata(
        code="VEG",
        naam="Vegetatie",
    )

    vilt = Referentiedata(
        code="VIL",
        naam="Vilt",
    )

    vlas = Referentiedata(
        code="VLA",
        naam="Vlas",
    )

    wol = Referentiedata(
        code="WOL",
        naam="Wol",
    )

    hard_rubber = Referentiedata(
        code="HRU",
        naam="Hard-Rubber",
    )

    polysulfide = Referentiedata(
        code="PLS",
        naam="Polysulfide",
    )

    schuimrubber = Referentiedata(
        code="SRU",
        naam="Schuimrubber",
    )

    butyl = Referentiedata(
        code="BUT",
        naam="Butyl",
    )

    epdm = Referentiedata(
        code="EPD",
        naam="Epdm",
    )

    linoleum = Referentiedata(
        code="LIN",
        naam="Linoleum",
    )

    natuurrubber = Referentiedata(
        code="NAT",
        naam="Natuurrubber",
    )

    neopreen = Referentiedata(
        code="NEO",
        naam="Neopreen",
    )

    tpve = Referentiedata(
        code="TPV",
        naam="Tpve",
    )

    element = Referentiedata(
        code="ELE",
        naam="Element",
    )

    product = Referentiedata(
        code="PRO",
        naam="Product",
    )

    geexpandeerde_klei = Referentiedata(
        code="GEK",
        naam="Geexpandeerde-Klei",
    )

    kalksteen = Referentiedata(
        code="KST",
        naam="Kalksteen",
    )

    kalkzandsteen = Referentiedata(
        code="KZS",
        naam="Kalkzandsteen",
    )

    keramisch = Referentiedata(
        code="KRA",
        naam="Keramisch",
    )

    porisosteen = Referentiedata(
        code="PRI",
        naam="Porisosteen",
    )

    porselein = Referentiedata(
        code="PSE",
        naam="Porselein",
    )

    baksteen = Referentiedata(
        code="BAK",
        naam="Baksteen",
    )

    calciumsilicaat = Referentiedata(
        code="CAL",
        naam="Calciumsilicaat",
    )

    kunststeen = Referentiedata(
        code="KUN",
        naam="Kunststeen",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
