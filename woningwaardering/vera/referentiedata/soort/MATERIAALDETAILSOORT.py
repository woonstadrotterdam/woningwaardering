
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class MATERIAALDETAILSOORT:

    ntb = Referentiedata(
        code="NTB",
        naam="Ntb",
    )
    # ntb = ("NTB", "Ntb")

    generiek = Referentiedata(
        code="GEN",
        naam="Generiek",
    )
    # generiek = ("GEN", "Generiek")

    gasbeton = Referentiedata(
        code="GAS",
        naam="Gasbeton",
    )
    # gasbeton = ("GAS", "Gasbeton")

    bimsbeton = Referentiedata(
        code="BIM",
        naam="Bimsbeton",
    )
    # bimsbeton = ("BIM", "Bimsbeton")

    isolatiebeton = Referentiedata(
        code="ISO",
        naam="Isolatiebeton",
    )
    # isolatiebeton = ("ISO", "Isolatiebeton")

    lichtbeton = Referentiedata(
        code="LIC",
        naam="Lichtbeton",
    )
    # lichtbeton = ("LIC", "Lichtbeton")

    slakkenbeton = Referentiedata(
        code="SLA",
        naam="Slakkenbeton",
    )
    # slakkenbeton = ("SLA", "Slakkenbeton")

    voorgespannen = Referentiedata(
        code="VOO",
        naam="Voorgespannen",
    )
    # voorgespannen = ("VOO", "Voorgespannen")

    cellenbeton = Referentiedata(
        code="CEL",
        naam="Cellenbeton",
    )
    # cellenbeton = ("CEL", "Cellenbeton")

    gewapend = Referentiedata(
        code="GEW",
        naam="Gewapend",
    )
    # gewapend = ("GEW", "Gewapend")

    grindbeton = Referentiedata(
        code="GBE",
        naam="Grindbeton",
    )
    # grindbeton = ("GBE", "Grindbeton")

    schuimbeton = Referentiedata(
        code="SBE",
        naam="Schuimbeton",
    )
    # schuimbeton = ("SBE", "Schuimbeton")

    spuitbeton = Referentiedata(
        code="SBT",
        naam="Spuitbeton",
    )
    # spuitbeton = ("SBT", "Spuitbeton")

    staalvezelbeton = Referentiedata(
        code="SVE",
        naam="Staalvezelbeton",
    )
    # staalvezelbeton = ("SVE", "Staalvezelbeton")

    asfalt = Referentiedata(
        code="ASF",
        naam="Asfalt",
    )
    # asfalt = ("ASF", "Asfalt")

    teer = Referentiedata(
        code="TEE",
        naam="Teer",
    )
    # teer = ("TEE", "Teer")

    asbestcement = Referentiedata(
        code="ACE",
        naam="Asbestcement",
    )
    # asbestcement = ("ACE", "Asbestcement")

    cementstuc = Referentiedata(
        code="CEM",
        naam="Cementstuc",
    )
    # cementstuc = ("CEM", "Cementstuc")

    grout = Referentiedata(
        code="GRO",
        naam="Grout",
    )
    # grout = ("GRO", "Grout")

    metselspecie = Referentiedata(
        code="MET",
        naam="Metselspecie",
    )
    # metselspecie = ("MET", "Metselspecie")

    mortel = Referentiedata(
        code="MOR",
        naam="Mortel",
    )
    # mortel = ("MOR", "Mortel")

    terrazzo = Referentiedata(
        code="TER",
        naam="Terrazzo",
    )
    # terrazzo = ("TER", "Terrazzo")

    vezelcement = Referentiedata(
        code="VEZ",
        naam="Vezelcement",
    )
    # vezelcement = ("VEZ", "Vezelcement")

    houtvezelcement = Referentiedata(
        code="HVC",
        naam="Houtvezelcement",
    )
    # houtvezelcement = ("HVC", "Houtvezelcement")

    houtwolcement = Referentiedata(
        code="HWC",
        naam="Houtwolcement",
    )
    # houtwolcement = ("HWC", "Houtwolcement")

    spuitmortel = Referentiedata(
        code="SMO",
        naam="Spuitmortel",
    )
    # spuitmortel = ("SMO", "Spuitmortel")

    zandcement = Referentiedata(
        code="ZCE",
        naam="Zandcement",
    )
    # zandcement = ("ZCE", "Zandcement")

    zandcement_vezel = Referentiedata(
        code="ZCV",
        naam="Zandcement-Vezel",
    )
    # zandcement_vezel = ("ZCV", "Zandcement-Vezel")

    anhydriet = Referentiedata(
        code="ANH",
        naam="Anhydriet",
    )
    # anhydriet = ("ANH", "Anhydriet")

    gipskarton = Referentiedata(
        code="GIP",
        naam="Gipskarton",
    )
    # gipskarton = ("GIP", "Gipskarton")

    stuc = Referentiedata(
        code="STU",
        naam="Stuc",
    )
    # stuc = ("STU", "Stuc")

    spuitstuc = Referentiedata(
        code="SST",
        naam="Spuitstuc",
    )
    # spuitstuc = ("SST", "Spuitstuc")

    cellulairglas = Referentiedata(
        code="CGL",
        naam="Cellulairglas",
    )
    # cellulairglas = ("CGL", "Cellulairglas")

    gehard = Referentiedata(
        code="GEH",
        naam="Gehard",
    )
    # gehard = ("GEH", "Gehard")

    helder = Referentiedata(
        code="HEL",
        naam="Helder",
    )
    # helder = ("HEL", "Helder")

    opaal = Referentiedata(
        code="OPA",
        naam="Opaal",
    )
    # opaal = ("OPA", "Opaal")

    spiegelend = Referentiedata(
        code="SPI",
        naam="Spiegelend",
    )
    # spiegelend = ("SPI", "Spiegelend")

    kwartsglas = Referentiedata(
        code="KWA",
        naam="Kwartsglas",
    )
    # kwartsglas = ("KWA", "Kwartsglas")

    bimszand = Referentiedata(
        code="BZA",
        naam="Bimszand",
    )
    # bimszand = ("BZA", "Bimszand")

    grind = Referentiedata(
        code="GRI",
        naam="Grind",
    )
    # grind = ("GRI", "Grind")

    aarde = Referentiedata(
        code="AAR",
        naam="Aarde",
    )
    # aarde = ("AAR", "Aarde")

    klei = Referentiedata(
        code="KLE",
        naam="Klei",
    )
    # klei = ("KLE", "Klei")

    lucht = Referentiedata(
        code="LUC",
        naam="Lucht",
    )
    # lucht = ("LUC", "Lucht")

    split = Referentiedata(
        code="SPL",
        naam="Split",
    )
    # split = ("SPL", "Split")

    turf = Referentiedata(
        code="TUR",
        naam="Turf",
    )
    # turf = ("TUR", "Turf")

    water = Referentiedata(
        code="WAT",
        naam="Water",
    )
    # water = ("WAT", "Water")

    kalk = Referentiedata(
        code="KAL",
        naam="Kalk",
    )
    # kalk = ("KAL", "Kalk")

    leem = Referentiedata(
        code="LEE",
        naam="Leem",
    )
    # leem = ("LEE", "Leem")

    silt = Referentiedata(
        code="SIL",
        naam="Silt",
    )
    # silt = ("SIL", "Silt")

    zand = Referentiedata(
        code="ZAN",
        naam="Zand",
    )
    # zand = ("ZAN", "Zand")

    hardboard = Referentiedata(
        code="HBO",
        naam="Hardboard",
    )
    # hardboard = ("HBO", "Hardboard")

    hardhout = Referentiedata(
        code="HHO",
        naam="Hardhout",
    )
    # hardhout = ("HHO", "Hardhout")

    houtspaan = Referentiedata(
        code="HSP",
        naam="Houtspaan",
    )
    # houtspaan = ("HSP", "Houtspaan")

    accoya = Referentiedata(
        code="ACC",
        naam="Accoya",
    )
    # accoya = ("ACC", "Accoya")

    azobe = Referentiedata(
        code="AZO",
        naam="Azobe",
    )
    # azobe = ("AZO", "Azobe")

    balsa = Referentiedata(
        code="BAL",
        naam="Balsa",
    )
    # balsa = ("BAL", "Balsa")

    bangkirai = Referentiedata(
        code="BAN",
        naam="Bangkirai",
    )
    # bangkirai = ("BAN", "Bangkirai")

    berken = Referentiedata(
        code="BER",
        naam="Berken",
    )
    # berken = ("BER", "Berken")

    beuken = Referentiedata(
        code="BEU",
        naam="Beuken",
    )
    # beuken = ("BEU", "Beuken")

    bilinga = Referentiedata(
        code="BIL",
        naam="Bilinga",
    )
    # bilinga = ("BIL", "Bilinga")

    board = Referentiedata(
        code="BOA",
        naam="Board",
    )
    # board = ("BOA", "Board")

    clt = Referentiedata(
        code="CLT",
        naam="Clt",
    )
    # clt = ("CLT", "Clt")

    douglas = Referentiedata(
        code="DOU",
        naam="Douglas",
    )
    # douglas = ("DOU", "Douglas")

    ebben = Referentiedata(
        code="EBB",
        naam="Ebben",
    )
    # ebben = ("EBB", "Ebben")

    eiken = Referentiedata(
        code="EIK",
        naam="Eiken",
    )
    # eiken = ("EIK", "Eiken")

    esdoorn = Referentiedata(
        code="ESD",
        naam="Esdoorn",
    )
    # esdoorn = ("ESD", "Esdoorn")

    essen = Referentiedata(
        code="ESS",
        naam="Essen",
    )
    # essen = ("ESS", "Essen")

    gemodificeerd = Referentiedata(
        code="GEM",
        naam="Gemodificeerd",
    )
    # gemodificeerd = ("GEM", "Gemodificeerd")

    grenen = Referentiedata(
        code="GRE",
        naam="Grenen",
    )
    # grenen = ("GRE", "Grenen")

    houtvezel = Referentiedata(
        code="HVE",
        naam="Houtvezel",
    )
    # houtvezel = ("HVE", "Houtvezel")

    houtwol = Referentiedata(
        code="HWO",
        naam="Houtwol",
    )
    # houtwol = ("HWO", "Houtwol")

    kersen = Referentiedata(
        code="KER",
        naam="Kersen",
    )
    # kersen = ("KER", "Kersen")

    lariks = Referentiedata(
        code="LAR",
        naam="Lariks",
    )
    # lariks = ("LAR", "Lariks")

    mahonie = Referentiedata(
        code="MAH",
        naam="Mahonie",
    )
    # mahonie = ("MAH", "Mahonie")

    masonite = Referentiedata(
        code="MAS",
        naam="Masonite",
    )
    # masonite = ("MAS", "Masonite")

    mdf = Referentiedata(
        code="MDF",
        naam="Mdf",
    )
    # mdf = ("MDF", "Mdf")

    multiplex = Referentiedata(
        code="MUL",
        naam="Multiplex",
    )
    # multiplex = ("MUL", "Multiplex")

    noten = Referentiedata(
        code="NOT",
        naam="Noten",
    )
    # noten = ("NOT", "Noten")

    okoume = Referentiedata(
        code="OKO",
        naam="Okoume",
    )
    # okoume = ("OKO", "Okoume")

    osb = Referentiedata(
        code="OSB",
        naam="Osb",
    )
    # osb = ("OSB", "Osb")

    populieren = Referentiedata(
        code="POP",
        naam="Populieren",
    )
    # populieren = ("POP", "Populieren")

    spaanplaat = Referentiedata(
        code="SPA",
        naam="Spaanplaat",
    )
    # spaanplaat = ("SPA", "Spaanplaat")

    triplex = Referentiedata(
        code="TRI",
        naam="Triplex",
    )
    # triplex = ("TRI", "Triplex")

    vuren = Referentiedata(
        code="VUR",
        naam="Vuren",
    )
    # vuren = ("VUR", "Vuren")

    wenge = Referentiedata(
        code="WEN",
        naam="Wenge",
    )
    # wenge = ("WEN", "Wenge")

    ceder = Referentiedata(
        code="CED",
        naam="Ceder",
    )
    # ceder = ("CED", "Ceder")

    zaagsel = Referentiedata(
        code="ZAA",
        naam="Zaagsel",
    )
    # zaagsel = ("ZAA", "Zaagsel")

    meranti = Referentiedata(
        code="MER",
        naam="Meranti",
    )
    # meranti = ("MER", "Meranti")

    merbau = Referentiedata(
        code="MBA",
        naam="Merbau",
    )
    # merbau = ("MBA", "Merbau")

    zachtboard = Referentiedata(
        code="ZBO",
        naam="Zachtboard",
    )
    # zachtboard = ("ZBO", "Zachtboard")

    zachthout = Referentiedata(
        code="ZHO",
        naam="Zachthout",
    )
    # zachthout = ("ZHO", "Zachthout")

    geexpandeerd_perliet = Referentiedata(
        code="GEP",
        naam="Geexpandeerd-Perliet",
    )
    # geexpandeerd_perliet = ("GEP", "Geexpandeerd-Perliet")

    hardschuim = Referentiedata(
        code="HSC",
        naam="Hardschuim",
    )
    # hardschuim = ("HSC", "Hardschuim")

    eps = Referentiedata(
        code="EPS",
        naam="Eps",
    )
    # eps = ("EPS", "Eps")

    fenolhars = Referentiedata(
        code="FEN",
        naam="Fenolhars",
    )
    # fenolhars = ("FEN", "Fenolhars")

    glaswol = Referentiedata(
        code="GLA",
        naam="Glaswol",
    )
    # glaswol = ("GLA", "Glaswol")

    resolschuim = Referentiedata(
        code="RES",
        naam="Resolschuim",
    )
    # resolschuim = ("RES", "Resolschuim")

    pir = Referentiedata(
        code="PIR",
        naam="Pir",
    )
    # pir = ("PIR", "Pir")

    pur = Referentiedata(
        code="PUR",
        naam="Pur",
    )
    # pur = ("PUR", "Pur")

    mineralewol = Referentiedata(
        code="MNE",
        naam="Mineralewol",
    )
    # mineralewol = ("MNE", "Mineralewol")

    steenwol = Referentiedata(
        code="STE",
        naam="Steenwol",
    )
    # steenwol = ("STE", "Steenwol")

    xps = Referentiedata(
        code="XPS",
        naam="Xps",
    )
    # xps = ("XPS", "Xps")

    mineraal = Referentiedata(
        code="MIN",
        naam="Mineraal",
    )
    # mineraal = ("MIN", "Mineraal")

    siliperliet = Referentiedata(
        code="SLI",
        naam="Siliperliet",
    )
    # siliperliet = ("SLI", "Siliperliet")

    solperlite = Referentiedata(
        code="SOL",
        naam="Solperlite",
    )
    # solperlite = ("SOL", "Solperlite")

    hard_kunststof = Referentiedata(
        code="HKU",
        naam="Hard-Kunststof",
    )
    # hard_kunststof = ("HKU", "Hard-Kunststof")

    loodvervanger = Referentiedata(
        code="LVE",
        naam="Loodvervanger",
    )
    # loodvervanger = ("LVE", "Loodvervanger")

    abs = Referentiedata(
        code="ABS",
        naam="Abs",
    )
    # abs = ("ABS", "Abs")

    aeryl = Referentiedata(
        code="AER",
        naam="Aeryl",
    )
    # aeryl = ("AER", "Aeryl")

    dpc = Referentiedata(
        code="DPC",
        naam="Dpc",
    )
    # dpc = ("DPC", "Dpc")

    elastomere_foam = Referentiedata(
        code="ELA",
        naam="Elastomere-Foam",
    )
    # elastomere_foam = ("ELA", "Elastomere-Foam")

    ep = Referentiedata(
        code="EP",
        naam="Ep",
    )
    # ep = ("EP", "Ep")

    epoxyhars = Referentiedata(
        code="EPO",
        naam="Epoxyhars",
    )
    # epoxyhars = ("EPO", "Epoxyhars")

    hdpe = Referentiedata(
        code="HDP",
        naam="Hdpe",
    )
    # hdpe = ("HDP", "Hdpe")

    hmpe = Referentiedata(
        code="HMP",
        naam="Hmpe",
    )
    # hmpe = ("HMP", "Hmpe")

    hpl = Referentiedata(
        code="HPL",
        naam="Hpl",
    )
    # hpl = ("HPL", "Hpl")

    ldpe = Referentiedata(
        code="LDP",
        naam="Ldpe",
    )
    # ldpe = ("LDP", "Ldpe")

    pe = Referentiedata(
        code="PE",
        naam="Pe",
    )
    # pe = ("PE", "Pe")

    pmma = Referentiedata(
        code="PMM",
        naam="Pmma",
    )
    # pmma = ("PMM", "Pmma")

    pvac = Referentiedata(
        code="PVA",
        naam="Pvac",
    )
    # pvac = ("PVA", "Pvac")

    pa = Referentiedata(
        code="PA",
        naam="Pa",
    )
    # pa = ("PA", "Pa")

    pc = Referentiedata(
        code="PC",
        naam="Pc",
    )
    # pc = ("PC", "Pc")

    pctfe = Referentiedata(
        code="PCT",
        naam="Pctfe",
    )
    # pctfe = ("PCT", "Pctfe")

    plexiglas = Referentiedata(
        code="PLE",
        naam="Plexiglas",
    )
    # plexiglas = ("PLE", "Plexiglas")

    polyesterhars = Referentiedata(
        code="PLY",
        naam="Polyesterhars",
    )
    # polyesterhars = ("PLY", "Polyesterhars")

    pp = Referentiedata(
        code="PP",
        naam="Pp",
    )
    # pp = ("PP", "Pp")

    ps = Referentiedata(
        code="PS",
        naam="Ps",
    )
    # ps = ("PS", "Ps")

    ptfe = Referentiedata(
        code="PTF",
        naam="Ptfe",
    )
    # ptfe = ("PTF", "Ptfe")

    pu = Referentiedata(
        code="PU",
        naam="Pu",
    )
    # pu = ("PU", "Pu")

    pvc = Referentiedata(
        code="PVC",
        naam="Pvc",
    )
    # pvc = ("PVC", "Pvc")

    polyester = Referentiedata(
        code="POL",
        naam="Polyester",
    )
    # polyester = ("POL", "Polyester")

    silicagel = Referentiedata(
        code="SLG",
        naam="Silicagel",
    )
    # silicagel = ("SLG", "Silicagel")

    siliconen = Referentiedata(
        code="SLC",
        naam="Siliconen",
    )
    # siliconen = ("SLC", "Siliconen")

    zacht_kunststof = Referentiedata(
        code="ZKU",
        naam="Zacht-Kunststof",
    )
    # zacht_kunststof = ("ZKU", "Zacht-Kunststof")

    lood = Referentiedata(
        code="LOO",
        naam="Lood",
    )
    # lood = ("LOO", "Lood")

    platina = Referentiedata(
        code="PLA",
        naam="Platina",
    )
    # platina = ("PLA", "Platina")

    aluminium = Referentiedata(
        code="ALU",
        naam="Aluminium",
    )
    # aluminium = ("ALU", "Aluminium")

    brons = Referentiedata(
        code="BRO",
        naam="Brons",
    )
    # brons = ("BRO", "Brons")

    chroom = Referentiedata(
        code="CHR",
        naam="Chroom",
    )
    # chroom = ("CHR", "Chroom")

    gietijzer = Referentiedata(
        code="GIE",
        naam="Gietijzer",
    )
    # gietijzer = ("GIE", "Gietijzer")

    goud = Referentiedata(
        code="GOU",
        naam="Goud",
    )
    # goud = ("GOU", "Goud")

    ijzer = Referentiedata(
        code="IJZ",
        naam="Ijzer",
    )
    # ijzer = ("IJZ", "Ijzer")

    koper = Referentiedata(
        code="KOP",
        naam="Koper",
    )
    # koper = ("KOP", "Koper")

    messing = Referentiedata(
        code="MES",
        naam="Messing",
    )
    # messing = ("MES", "Messing")

    rvs = Referentiedata(
        code="RVS",
        naam="Rvs",
    )
    # rvs = ("RVS", "Rvs")

    tin = Referentiedata(
        code="TIN",
        naam="Tin",
    )
    # tin = ("TIN", "Tin")

    titanium = Referentiedata(
        code="TIT",
        naam="Titanium",
    )
    # titanium = ("TIT", "Titanium")

    zilver = Referentiedata(
        code="ZIL",
        naam="Zilver",
    )
    # zilver = ("ZIL", "Zilver")

    zink = Referentiedata(
        code="ZIN",
        naam="Zink",
    )
    # zink = ("ZIN", "Zink")

    soldeersel = Referentiedata(
        code="SDE",
        naam="Soldeersel",
    )
    # soldeersel = ("SDE", "Soldeersel")

    staal = Referentiedata(
        code="STA",
        naam="Staal",
    )
    # staal = ("STA", "Staal")

    asbest = Referentiedata(
        code="ASB",
        naam="Asbest",
    )
    # asbest = ("ASB", "Asbest")

    graniet = Referentiedata(
        code="GRA",
        naam="Graniet",
    )
    # graniet = ("GRA", "Graniet")

    gravel = Referentiedata(
        code="GVE",
        naam="Gravel",
    )
    # gravel = ("GVE", "Gravel")

    hardsteen = Referentiedata(
        code="HST",
        naam="Hardsteen",
    )
    # hardsteen = ("HST", "Hardsteen")

    kwartsiet = Referentiedata(
        code="KSI",
        naam="Kwartsiet",
    )
    # kwartsiet = ("KSI", "Kwartsiet")

    poreus_gesteente = Referentiedata(
        code="PGE",
        naam="Poreus-Gesteente",
    )
    # poreus_gesteente = ("PGE", "Poreus-Gesteente")

    basalt = Referentiedata(
        code="BAS",
        naam="Basalt",
    )
    # basalt = ("BAS", "Basalt")

    gneiss = Referentiedata(
        code="GNE",
        naam="Gneiss",
    )
    # gneiss = ("GNE", "Gneiss")

    kristallijn_gesteente = Referentiedata(
        code="KRI",
        naam="Kristallijn-Gesteente",
    )
    # kristallijn_gesteente = ("KRI", "Kristallijn-Gesteente")

    lei = Referentiedata(
        code="LEI",
        naam="Lei",
    )
    # lei = ("LEI", "Lei")

    marmer = Referentiedata(
        code="MAR",
        naam="Marmer",
    )
    # marmer = ("MAR", "Marmer")

    puimsteen = Referentiedata(
        code="PUI",
        naam="Puimsteen",
    )
    # puimsteen = ("PUI", "Puimsteen")

    sedimentgesteente = Referentiedata(
        code="SED",
        naam="Sedimentgesteente",
    )
    # sedimentgesteente = ("SED", "Sedimentgesteente")

    trachiet = Referentiedata(
        code="TRA",
        naam="Trachiet",
    )
    # trachiet = ("TRA", "Trachiet")

    zandsteen = Referentiedata(
        code="ZST",
        naam="Zandsteen",
    )
    # zandsteen = ("ZST", "Zandsteen")

    leer = Referentiedata(
        code="LER",
        naam="Leer",
    )
    # leer = ("LER", "Leer")

    plantaardige_vezel = Referentiedata(
        code="PTA",
        naam="Plantaardige-Vezel",
    )
    # plantaardige_vezel = ("PTA", "Plantaardige-Vezel")

    bamboe = Referentiedata(
        code="BAM",
        naam="Bamboe",
    )
    # bamboe = ("BAM", "Bamboe")

    hennep = Referentiedata(
        code="HEN",
        naam="Hennep",
    )
    # hennep = ("HEN", "Hennep")

    jute = Referentiedata(
        code="JUT",
        naam="Jute",
    )
    # jute = ("JUT", "Jute")

    katoen = Referentiedata(
        code="KAT",
        naam="Katoen",
    )
    # katoen = ("KAT", "Katoen")

    kurk = Referentiedata(
        code="KUR",
        naam="Kurk",
    )
    # kurk = ("KUR", "Kurk")

    mais = Referentiedata(
        code="MAI",
        naam="Mais",
    )
    # mais = ("MAI", "Mais")

    papier = Referentiedata(
        code="PAP",
        naam="Papier",
    )
    # papier = ("PAP", "Papier")

    riet = Referentiedata(
        code="RIE",
        naam="Riet",
    )
    # riet = ("RIE", "Riet")

    stro = Referentiedata(
        code="STR",
        naam="Stro",
    )
    # stro = ("STR", "Stro")

    vegetatie = Referentiedata(
        code="VEG",
        naam="Vegetatie",
    )
    # vegetatie = ("VEG", "Vegetatie")

    vilt = Referentiedata(
        code="VIL",
        naam="Vilt",
    )
    # vilt = ("VIL", "Vilt")

    vlas = Referentiedata(
        code="VLA",
        naam="Vlas",
    )
    # vlas = ("VLA", "Vlas")

    wol = Referentiedata(
        code="WOL",
        naam="Wol",
    )
    # wol = ("WOL", "Wol")

    hard_rubber = Referentiedata(
        code="HRU",
        naam="Hard-Rubber",
    )
    # hard_rubber = ("HRU", "Hard-Rubber")

    polysulfide = Referentiedata(
        code="PLS",
        naam="Polysulfide",
    )
    # polysulfide = ("PLS", "Polysulfide")

    schuimrubber = Referentiedata(
        code="SRU",
        naam="Schuimrubber",
    )
    # schuimrubber = ("SRU", "Schuimrubber")

    butyl = Referentiedata(
        code="BUT",
        naam="Butyl",
    )
    # butyl = ("BUT", "Butyl")

    epdm = Referentiedata(
        code="EPD",
        naam="Epdm",
    )
    # epdm = ("EPD", "Epdm")

    linoleum = Referentiedata(
        code="LIN",
        naam="Linoleum",
    )
    # linoleum = ("LIN", "Linoleum")

    natuurrubber = Referentiedata(
        code="NAT",
        naam="Natuurrubber",
    )
    # natuurrubber = ("NAT", "Natuurrubber")

    neopreen = Referentiedata(
        code="NEO",
        naam="Neopreen",
    )
    # neopreen = ("NEO", "Neopreen")

    tpve = Referentiedata(
        code="TPV",
        naam="Tpve",
    )
    # tpve = ("TPV", "Tpve")

    element = Referentiedata(
        code="ELE",
        naam="Element",
    )
    # element = ("ELE", "Element")

    product = Referentiedata(
        code="PRO",
        naam="Product",
    )
    # product = ("PRO", "Product")

    geexpandeerde_klei = Referentiedata(
        code="GEK",
        naam="Geexpandeerde-Klei",
    )
    # geexpandeerde_klei = ("GEK", "Geexpandeerde-Klei")

    kalksteen = Referentiedata(
        code="KST",
        naam="Kalksteen",
    )
    # kalksteen = ("KST", "Kalksteen")

    kalkzandsteen = Referentiedata(
        code="KZS",
        naam="Kalkzandsteen",
    )
    # kalkzandsteen = ("KZS", "Kalkzandsteen")

    keramisch = Referentiedata(
        code="KRA",
        naam="Keramisch",
    )
    # keramisch = ("KRA", "Keramisch")

    porisosteen = Referentiedata(
        code="PRI",
        naam="Porisosteen",
    )
    # porisosteen = ("PRI", "Porisosteen")

    porselein = Referentiedata(
        code="PSE",
        naam="Porselein",
    )
    # porselein = ("PSE", "Porselein")

    baksteen = Referentiedata(
        code="BAK",
        naam="Baksteen",
    )
    # baksteen = ("BAK", "Baksteen")

    calciumsilicaat = Referentiedata(
        code="CAL",
        naam="Calciumsilicaat",
    )
    # calciumsilicaat = ("CAL", "Calciumsilicaat")

    kunststeen = Referentiedata(
        code="KUN",
        naam="Kunststeen",
    )
    # kunststeen = ("KUN", "Kunststeen")
