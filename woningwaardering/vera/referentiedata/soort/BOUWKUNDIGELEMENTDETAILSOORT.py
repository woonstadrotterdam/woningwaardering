
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BOUWKUNDIGELEMENTDETAILSOORT:

    aanrecht = Referentiedata(
        code="AAN",
        naam="Aanrecht",
    )
    # aanrecht = ("AAN", "Aanrecht")
    """
    Werkoppervlak in keukens, uitgerust met spoelbak en ruimte voor het bereiden van
    voedsel. Relatie met IFC codering (IfcFurniture)
    """

    afdekker = Referentiedata(
        code="AFD",
        naam="Afdekker",
    )
    # afdekker = ("AFD", "Afdekker")
    """
    Beschermend element dat het bovenste deel van een constructie bedekt tegen
    weersinvloeden. Relatie met IFC codering (IfcCovering.ROOFING)
    """

    armatuur = Referentiedata(
        code="ARM",
        naam="Armatuur",
    )
    # armatuur = ("ARM", "Armatuur")
    """
    Compleet toestel inclusief behuizing, lamp en fittingen voor lichtverspreiding.
    Relatie met IFC codering (IfcLightFixture)
    """

    bad = Referentiedata(
        code="BAD",
        naam="Bad",
    )
    # bad = ("BAD", "Bad")
    """
    Waterhoudend sanitair gebruiksvoorwerp voor persoonlijke hygiëne. Relatie met IFC
    codering (IfcSanitaryTerminal.BATH)
    """

    balk = Referentiedata(
        code="BLK",
        naam="Balk",
    )
    # balk = ("BLK", "Balk")
    """
    Horizontaal steunelement in constructies, draagt vloer-, daklasten. Relatie met IFC
    codering (IfcBeam.BEAM)
    """

    balkon = Referentiedata(
        code="BKO",
        naam="Balkon",
    )
    # balkon = ("BKO", "Balkon")
    """
    Uitkragend platform aan buitenzijde gebouw, toegankelijk via deur. Relatie met IFC
    codering (IfcSlab.FLOOR)
    """

    balustrade = Referentiedata(
        code="BLU",
        naam="Balustrade",
    )
    # balustrade = ("BLU", "Balustrade")
    """
    Rij van balusters (kleine pilaren), dient als afscheiding of reling. Relatie met IFC
    codering (IfcRailing.BALUSTRADE)
    """

    beglazing = Referentiedata(
        code="BEG",
        naam="Beglazing",
    )
    # beglazing = ("BEG", "Beglazing")
    """
    Glaswerk in kozijnen van ramen en deuren voor lichtinval en isolatie. Relatie met
    IFC codering (IfcWindow.WINDOW)
    """

    boeiboord = Referentiedata(
        code="BOE",
        naam="Boeiboord",
    )
    # boeiboord = ("BOE", "Boeiboord")
    """
    Afwerkingsrand aan de dakrand voor bescherming en esthetiek. Relatie met IFC
    codering (IfcPlate.SHEET)
    """

    boiler = Referentiedata(
        code="BOI",
        naam="Boiler",
    )
    # boiler = ("BOI", "Boiler")
    """
    Apparaat voor opwarming en opslag van gebruikswater. Relatie met IFC codering
    (IfcBoiler)
    """

    borstwering = Referentiedata(
        code="BOR",
        naam="Borstwering",
    )
    # borstwering = ("BOR", "Borstwering")
    """
    Lage muur aan de rand van een balkon, dak of brug. Relatie met IFC codering
    (IfcWall.PARAPET)
    """

    brandblusser = Referentiedata(
        code="BRA",
        naam="Brandblusser",
    )
    # brandblusser = ("BRA", "Brandblusser")
    """
    Draagbaar toestel voor het blussen van beginnende branden. Relatie met IFC codering
    (IfcFurniture)
    """

    brandmeldinstallatie = Referentiedata(
        code="BME",
        naam="Brandmeldinstallatie",
    )
    # brandmeldinstallatie = ("BME", "Brandmeldinstallatie")
    """
    Systeem voor detectie en alarmering van brand in gebouwen. Relatie met IFC codering
    (IfcSystem.FIREPROTECTION)
    """

    closetcombinatie = Referentiedata(
        code="CLO",
        naam="Closetcombinatie",
    )
    # closetcombinatie = ("CLO", "Closetcombinatie")
    """
    Complete toiletopstelling inclusief pot, stortbak en soms bidet. Relatie met IFC
    codering (IfcSanitaryTerminal.TOILETPAN)
    """

    console = Referentiedata(
        code="CON",
        naam="Console",
    )
    # console = ("CON", "Console")
    """
    Uitstekend steunelement aan muur voor dragende functies. Relatie met IFC codering
    (IfcBeam.T-BEAM)
    """

    dak = Referentiedata(
        code="DAK",
        naam="Dak",
    )
    # dak = ("DAK", "Dak")
    """
    Bovenste afdekking van een gebouw, beschermt tegen weersinvloeden. Relatie met IFC
    codering (IfcRoof)
    """

    dakkapel = Referentiedata(
        code="DKA",
        naam="Dakkapel",
    )
    # dakkapel = ("DKA", "Dakkapel")
    """
    Uitbouw op dakvlak, zorgt voor extra ruimte en licht. Relatie met IFC codering
    (IfcRoof)
    """

    dakraam = Referentiedata(
        code="DRA",
        naam="Dakraam",
    )
    # dakraam = ("DRA", "Dakraam")
    """
    Raam geplaatst in dak, voor licht en ventilatie. Relatie met IFC codering
    (IfcWindow.SKYLIGHT)
    """

    dakrand = Referentiedata(
        code="DRN",
        naam="Dakrand",
    )
    # dakrand = ("DRN", "Dakrand")
    """
    Afwerking aan de rand van het dak voor bescherming en esthetiek. Relatie met IFC
    codering (IfcRoof)
    """

    deur = Referentiedata(
        code="DEU",
        naam="Deur",
    )
    # deur = ("DEU", "Deur")
    """
    Beweegbaar element dat toegang biedt of afsluit. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    deurdranger = Referentiedata(
        code="DDR",
        naam="Deurdranger",
    )
    # deurdranger = ("DDR", "Deurdranger")
    """
    Mechanisme dat deuren automatisch sluit na opening. Relatie met IFC codering
    (IfcBuildingElementProxy)
    """

    dorpel = Referentiedata(
        code="DOR",
        naam="Dorpel",
    )
    # dorpel = ("DOR", "Dorpel")
    """
    Onderste deel van een deur- of raamkozijn. houdt vocht buiten. Relatie met IFC
    codering (IfcMember)
    """

    douche = Referentiedata(
        code="DOU",
        naam="Douche",
    )
    # douche = ("DOU", "Douche")
    """
    Installatie voor lichaamsreiniging door middel van waterstralen. Relatie met IFC
    codering (IfcSanitaryTerminal.SHOWER)
    """

    expansievat = Referentiedata(
        code="EXP",
        naam="Expansievat",
    )
    # expansievat = ("EXP", "Expansievat")
    """
    Veiligheidsonderdeel in verwarmingssystemen, vangt drukverschillen op. Relatie met
    IFC codering (IfcTank.EXPANSION)
    """

    fontein = Referentiedata(
        code="FON",
        naam="Fontein",
    )
    # fontein = ("FON", "Fontein")
    """
    Kleine wateruitlaat, vaak decoratief in publieke of privé-ruimtes. Relatie met IFC
    codering (IfcSanitaryTerminal.SINK)
    """

    galerij = Referentiedata(
        code="GAL",
        naam="Galerij",
    )
    # galerij = ("GAL", "Galerij")
    """
    Overdekte, open gang langs buitenzijde van een gebouw. Relatie met IFC codering
    (IfcSlab)
    """

    garagedeur = Referentiedata(
        code="GAR",
        naam="Garagedeur",
    )
    # garagedeur = ("GAR", "Garagedeur")
    """
    Grote deur specifiek ontworpen voor toegang tot een garage. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    goot = Referentiedata(
        code="GOO",
        naam="Goot",
    )
    # goot = ("GOO", "Goot")
    """
    Kanaal voor afvoer van hemelwater van daken. Relatie met IFC codering
    (IfcPipeSegment.GUTTER)
    """

    handmelder = Referentiedata(
        code="HAN",
        naam="Handmelder",
    )
    # handmelder = ("HAN", "Handmelder")
    """
    Handbediend alarmtoestel voor het activeren van brandalarm. Relatie met IFC codering
    (IfcAlarm.MANUALPULLBOX)
    """

    hek = Referentiedata(
        code="HEK",
        naam="Hek",
    )
    # hek = ("HEK", "Hek")
    """
    Omheining of afscheiding, vaak van metaal of hout. Relatie met IFC codering
    (IfcRailing)
    """

    hellingbaan = Referentiedata(
        code="HEL",
        naam="Hellingbaan",
    )
    # hellingbaan = ("HEL", "Hellingbaan")
    """
    Hellend vlak voor toegang met voertuigen of rolstoelen. Relatie met IFC codering
    (IfcRamp)
    """

    hemelwaterafvoer = Referentiedata(
        code="HEM",
        naam="Hemelwaterafvoer",
    )
    # hemelwaterafvoer = ("HEM", "Hemelwaterafvoer")
    """
    Systeem voor afvoer van regenwater van daken naar riolering. Relatie met IFC
    codering (IfcPipeSegment)
    """

    isolatie = Referentiedata(
        code="ISO",
        naam="Isolatie",
    )
    # isolatie = ("ISO", "Isolatie")
    """
    Materiaal gebruikt om warmte, geluid of elektriciteit te beperken. Relatie met IFC
    codering (IfcCovering.INSULATION)
    """

    kanteldeur = Referentiedata(
        code="KAN",
        naam="Kanteldeur",
    )
    # kanteldeur = ("KAN", "Kanteldeur")
    """
    Deur die kantelt om te openen, vaak gebruikt bij garages. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    kast = Referentiedata(
        code="KAS",
        naam="Kast",
    )
    # kast = ("KAS", "Kast")
    """
    Opbergmeubel met deuren of laden. Relatie met IFC codering (IfcFurniture.SHELF)
    """

    ketel = Referentiedata(
        code="KET",
        naam="Ketel",
    )
    # ketel = ("KET", "Ketel")
    """
    Apparaat voor verwarming van water of stoomproductie. Relatie met IFC codering
    (IfcBoiler)
    """

    kolom = Referentiedata(
        code="KOL",
        naam="Kolom",
    )
    # kolom = ("KOL", "Kolom")
    """
    Verticaal steunelement in constructies. Relatie met IFC codering (IfcColumn.COLUMN)
    """

    kozijn = Referentiedata(
        code="KOZ",
        naam="Kozijn",
    )
    # kozijn = ("KOZ", "Kozijn")
    """
    Omlijsting waarin deur of raam bevestigd is. Relatie met IFC codering (IfcWindow)
    """

    leuning = Referentiedata(
        code="LEU",
        naam="Leuning",
    )
    # leuning = ("LEU", "Leuning")
    """
    Steun- of geleidingsreling, vooral bij trappen. Relatie met IFC codering
    (IfcRailing.HANDRAIL)
    """

    lichtkoepel = Referentiedata(
        code="LIC",
        naam="Lichtkoepel",
    )
    # lichtkoepel = ("LIC", "Lichtkoepel")
    """
    Doorzichtig element op daken voor daglichttoetreding. Relatie met IFC codering
    (IfcWindow.LIGHTDOME)
    """

    lichtstraat = Referentiedata(
        code="LST",
        naam="Lichtstraat",
    )
    # lichtstraat = ("LST", "Lichtstraat")
    """
    Serie aaneengesloten ramen of koepels op het dak voor lichtinval. Relatie met IFC
    codering (IfcWindow.LIGHTDOME)
    """

    lift = Referentiedata(
        code="LIF",
        naam="Lift",
    )
    # lift = ("LIF", "Lift")
    """
    Verticaal transportsysteem voor personen of goederen. Relatie met IFC codering
    (IfcTransportElement.ELEVATOR)
    """

    luchtbehandelingskast = Referentiedata(
        code="LUC",
        naam="Luchtbehandelingskast",
    )
    # luchtbehandelingskast = ("LUC", "Luchtbehandelingskast")
    """
    Apparaat voor conditioneren van lucht in gebouwen. Relatie met IFC codering
    (IfcUnitaryEquipment)
    """

    luifel = Referentiedata(
        code="LFE",
        naam="Luifel",
    )
    # luifel = ("LFE", "Luifel")
    """
    Overkapping boven deur of raam tegen weersinvloeden. Relatie met IFC codering
    (IfcRoof)
    """

    luik = Referentiedata(
        code="LUI",
        naam="Luik",
    )
    # luik = ("LUI", "Luik")
    """
    Afsluitbaar paneel in deur, raam of vloer. Relatie met IFC codering
    (IfcDoor.TRAPDOOR)
    """

    meldsirene = Referentiedata(
        code="MEL",
        naam="Meldsirene",
    )
    # meldsirene = ("MEL", "Meldsirene")
    """
    Geluidsapparaat voor waarschuwing bij gevaar, zoals brand. Relatie met IFC codering
    (IfcAlarm.SIREN)
    """

    nvo = Referentiedata(
        code="NVO",
        naam="NVO",
    )
    # nvo = ("NVO", "NVO")
    """
    Niet van toepassing, specificeer term. Relatie met IFC codering (IfcSpace.SPACE)
    """

    paneel = Referentiedata(
        code="PAN",
        naam="Paneel",
    )
    # paneel = ("PAN", "Paneel")
    """
    Vlak element gebruikt in wanden, deuren of meubels. Relatie met IFC codering
    (IfcPlate.SHEET)
    """

    plafond = Referentiedata(
        code="PLA",
        naam="Plafond",
    )
    # plafond = ("PLA", "Plafond")
    """
    Binnenafwerking van bovenzijde ruimte. Relatie met IFC codering
    (IfcCovering.CEILING)
    """

    postkast = Referentiedata(
        code="POS",
        naam="Postkast",
    )
    # postkast = ("POS", "Postkast")
    """
    Kast voor ontvangst van poststukken. Relatie met IFC codering (IfcFurniture)
    """

    privacyscherm = Referentiedata(
        code="PRI",
        naam="Privacyscherm",
    )
    # privacyscherm = ("PRI", "Privacyscherm")
    """
    Afscheiding bedoeld voor het creëren van privacy. Relatie met IFC codering
    (IfcFurniture)
    """

    raam = Referentiedata(
        code="RAA",
        naam="Raam",
    )
    # raam = ("RAA", "Raam")
    """
    Kozijn met glas voor licht en ventilatie. Relatie met IFC codering
    (IfcWindow.WINDOW)
    """

    radiator = Referentiedata(
        code="RAD",
        naam="Radiator",
    )
    # radiator = ("RAD", "Radiator")
    """
    Warmtewisselaar voor verwarming van ruimtes. Relatie met IFC codering
    (IfcSpaceHeater.RADIATOR)
    """

    rookmelder = Referentiedata(
        code="ROO",
        naam="Rookmelder",
    )
    # rookmelder = ("ROO", "Rookmelder")
    """
    Detectieapparaat voor vroegtijdige waarschuwing bij rookontwikkeling. Relatie met
    IFC codering (IfcSensor.SMOKESENSOR)
    """

    rooster = Referentiedata(
        code="RST",
        naam="Rooster",
    )
    # rooster = ("RST", "Rooster")
    """
    Geperforeerd paneel voor ventilatie of afdekking. Relatie met IFC codering
    (IfcAirTerminal.GRILLE)
    """

    schoorsteen = Referentiedata(
        code="SST",
        naam="Schoorsteen",
    )
    # schoorsteen = ("SST", "Schoorsteen")
    """
    Constructie voor afvoer van rook en verbrandingsgassen. Relatie met IFC codering
    (IfcChimney)
    """

    schuifdeur = Referentiedata(
        code="SDE",
        naam="Schuifdeur",
    )
    # schuifdeur = ("SDE", "Schuifdeur")
    """
    Deur die open en dicht gaat door te schuiven. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    schuifpui = Referentiedata(
        code="SPU",
        naam="Schuifpui",
    )
    # schuifpui = ("SPU", "Schuifpui")
    """
    Grote schuifdeur, vaak glas, verbindt binnen met buiten. Relatie met IFC codering
    (IfcWindow.WINDOW)
    """

    trap = Referentiedata(
        code="TRA",
        naam="Trap",
    )
    # trap = ("TRA", "Trap")
    """
    Constructie van treden voor verticale verplaatsing. Relatie met IFC codering
    (IfcStair)
    """

    traplift = Referentiedata(
        code="TLI",
        naam="Traplift",
    )
    # traplift = ("TLI", "Traplift")
    """
    Hulpmiddel voor het overbruggen van trappen door mindervaliden. Relatie met IFC
    codering (IfcTransportElement)
    """

    urinoir = Referentiedata(
        code="URI",
        naam="Urinoir",
    )
    # urinoir = ("URI", "Urinoir")
    """
    Sanitair voor staand urineren door mannen. Relatie met IFC codering
    (IfcSanitaryTerminal.URINAL)
    """

    ventilatiekap = Referentiedata(
        code="VEN",
        naam="Ventilatiekap",
    )
    # ventilatiekap = ("VEN", "Ventilatiekap")
    """
    Afzuigkap boven kookplaat, voert kookdampen af. Relatie met IFC codering
    (IfcStackTerminal.COWL)
    """

    ventilatierooster = Referentiedata(
        code="VRO",
        naam="Ventilatierooster",
    )
    # ventilatierooster = ("VRO", "Ventilatierooster")
    """
    Opening in muur of raam voor luchttoe- of afvoer. Relatie met IFC codering
    (IfcAirTerminal.DIFFUSER)
    """

    vliesgevel = Referentiedata(
        code="VLI",
        naam="Vliesgevel",
    )
    # vliesgevel = ("VLI", "Vliesgevel")
    """
    Lichtgewicht gevelsysteem, veelal van glas. Relatie met IFC codering
    (IfcCurtainWall)
    """

    vlizotrap = Referentiedata(
        code="VTR",
        naam="Vlizotrap",
    )
    # vlizotrap = ("VTR", "Vlizotrap")
    """
    Opvouwbare trap naar zolder of vliering. Relatie met IFC codering (IfcStair)
    """

    vloer = Referentiedata(
        code="VLO",
        naam="Vloer",
    )
    # vloer = ("VLO", "Vloer")
    """
    Horizontaal steunelement, scheidt verschillende verdiepingen. Relatie met IFC
    codering (IfcSlab.FLOOR)
    """

    wand = Referentiedata(
        code="WAN",
        naam="Wand",
    )
    # wand = ("WAN", "Wand")
    """
    Verticaal scheidend element in bouwkundige constructies. Relatie met IFC codering
    (IfcWallStandardCase)
    """

    warmtepomp = Referentiedata(
        code="WAR",
        naam="Warmtepomp",
    )
    # warmtepomp = ("WAR", "Warmtepomp")
    """
    Apparaat dat warmte verplaatst voor verwarming of koeling. Relatie met IFC codering
    (IfcPump)
    """

    warmteterugwinning_apparaat = Referentiedata(
        code="WTE",
        naam="Warmteterugwinning apparaat",
    )
    # warmteterugwinning_apparaat = ("WTE", "Warmteterugwinning apparaat")
    """
    Systeem dat warmte uit afvoerlucht hergebruikt voor energie-efficiëntie. Relatie met
    IFC codering (IfcAirToAirHeatRecovery)
    """

    wastafel = Referentiedata(
        code="WAS",
        naam="Wastafel",
    )
    # wastafel = ("WAS", "Wastafel")
    """
    Sanitair voor handen wassen en persoonlijke verzorging. Relatie met IFC codering
    (IfcSanitaryTerminal.WASHHANDBASIN)
    """

    zonnepaneel = Referentiedata(
        code="ZPA",
        naam="Zonnepaneel",
    )
    # zonnepaneel = ("ZPA", "Zonnepaneel")
    """
    Apparaat dat zonlicht omzet in elektriciteit. Relatie met IFC codering
    (IfcSolarDevice)
    """

    zonwering = Referentiedata(
        code="ZON",
        naam="Zonwering",
    )
    # zonwering = ("ZON", "Zonwering")
    """
    Extern of intern systeem om zonlicht en warmte te reguleren. Relatie met IFC
    codering (IfcShadingDevice)
    """

    afvoer = Referentiedata(
        code="AFV",
        naam="Afvoer",
    )
    # afvoer = ("AFV", "Afvoer")

    balustrades_en_leuningen = Referentiedata(
        code="BAL",
        naam="Balustrades en leuningen",
    )
    # balustrades_en_leuningen = ("BAL", "Balustrades en leuningen")

    beveiliging = Referentiedata(
        code="BEV",
        naam="Beveiliging",
    )
    # beveiliging = ("BEV", "Beveiliging")

    binnenwandafwerking = Referentiedata(
        code="BIA",
        naam="Binnenwandafwerking",
    )
    # binnenwandafwerking = ("BIA", "Binnenwandafwerking")

    binnenwanden = Referentiedata(
        code="BIN",
        naam="Binnenwanden",
    )
    # binnenwanden = ("BIN", "Binnenwanden")

    binnenwandopeningen = Referentiedata(
        code="BIW",
        naam="Binnenwandopeningen",
    )
    # binnenwandopeningen = ("BIW", "Binnenwandopeningen")

    buitenwandafwerking = Referentiedata(
        code="BUA",
        naam="Buitenwandafwerking",
    )
    # buitenwandafwerking = ("BUA", "Buitenwandafwerking")

    buitenwanden = Referentiedata(
        code="BUI",
        naam="Buitenwanden",
    )
    # buitenwanden = ("BUI", "Buitenwanden")

    buitenwandopeningen = Referentiedata(
        code="BUW",
        naam="Buitenwandopeningen",
    )
    # buitenwandopeningen = ("BUW", "Buitenwandopeningen")

    communicatie = Referentiedata(
        code="COM",
        naam="Communicatie",
    )
    # communicatie = ("COM", "Communicatie")

    dakbedekking = Referentiedata(
        code="DBE",
        naam="Dakbedekking",
    )
    # dakbedekking = ("DBE", "Dakbedekking")

    dakopeningen = Referentiedata(
        code="DOP",
        naam="Dakopeningen",
    )
    # dakopeningen = ("DOP", "Dakopeningen")

    elektra = Referentiedata(
        code="ELE",
        naam="Elektra",
    )
    # elektra = ("ELE", "Elektra")

    gas = Referentiedata(
        code="GAS",
        naam="Gas",
    )
    # gas = ("GAS", "Gas")

    keukenvoorzieningen = Referentiedata(
        code="KEU",
        naam="Keukenvoorzieningen",
    )
    # keukenvoorzieningen = ("KEU", "Keukenvoorzieningen")

    losse_opslaginventaris = Referentiedata(
        code="LOS",
        naam="Losse opslaginventaris",
    )
    # losse_opslaginventaris = ("LOS", "Losse opslaginventaris")

    plafondafwerking = Referentiedata(
        code="PAF",
        naam="Plafondafwerking",
    )
    # plafondafwerking = ("PAF", "Plafondafwerking")

    sanitaire_voorzieningen = Referentiedata(
        code="SAN",
        naam="Sanitaire voorzieningen",
    )
    # sanitaire_voorzieningen = ("SAN", "Sanitaire voorzieningen")

    schilderwerk = Referentiedata(
        code="SCH",
        naam="Schilderwerk",
    )
    # schilderwerk = ("SCH", "Schilderwerk")

    terrein = Referentiedata(
        code="TER",
        naam="Terrein",
    )
    # terrein = ("TER", "Terrein")

    trap_en_hellingafwerking = Referentiedata(
        code="THA",
        naam="Trap- en hellingafwerking",
    )
    # trap_en_hellingafwerking = ("THA", "Trap- en hellingafwerking")

    vloerafwerking = Referentiedata(
        code="VAF",
        naam="Vloerafwerking",
    )
    # vloerafwerking = ("VAF", "Vloerafwerking")

    verwarmingsonderdelen = Referentiedata(
        code="VEO",
        naam="Verwarmingsonderdelen",
    )
    # verwarmingsonderdelen = ("VEO", "Verwarmingsonderdelen")

    verlichting = Referentiedata(
        code="VER",
        naam="Verlichting",
    )
    # verlichting = ("VER", "Verlichting")

    vloeropeningen = Referentiedata(
        code="VOP",
        naam="Vloeropeningen",
    )
    # vloeropeningen = ("VOP", "Vloeropeningen")

    verwarmingstoestellen = Referentiedata(
        code="VTO",
        naam="Verwarmingstoestellen",
    )
    # verwarmingstoestellen = ("VTO", "Verwarmingstoestellen")

    waterleiding_of_hoofdkraan = Referentiedata(
        code="WAT",
        naam="Waterleiding/hoofdkraan",
    )
    # waterleiding_of_hoofdkraan = ("WAT", "Waterleiding/hoofdkraan")
