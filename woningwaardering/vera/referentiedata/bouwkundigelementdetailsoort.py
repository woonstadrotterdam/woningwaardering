from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Bouwkundigelementdetailsoort(Enum):
    aanrecht = Referentiedata(
        code="AAN",
        naam="Aanrecht",
    )
    """
    Werkoppervlak in keukens, uitgerust met spoelbak en ruimte voor het bereiden van
    voedsel. Relatie met IFC codering (IfcFurniture)
    """

    afdekker = Referentiedata(
        code="AFD",
        naam="Afdekker",
    )
    """
    Beschermend element dat het bovenste deel van een constructie bedekt tegen
    weersinvloeden. Relatie met IFC codering (IfcCovering.ROOFING)
    """

    armatuur = Referentiedata(
        code="ARM",
        naam="Armatuur",
    )
    """
    Compleet toestel inclusief behuizing, lamp en fittingen voor lichtverspreiding.
    Relatie met IFC codering (IfcLightFixture)
    """

    bad = Referentiedata(
        code="BAD",
        naam="Bad",
    )
    """
    Waterhoudend sanitair gebruiksvoorwerp voor persoonlijke hygiëne. Relatie met IFC
    codering (IfcSanitaryTerminal.BATH)
    """

    balk = Referentiedata(
        code="BLK",
        naam="Balk",
    )
    """
    Horizontaal steunelement in constructies, draagt vloer-, daklasten. Relatie met IFC
    codering (IfcBeam.BEAM)
    """

    balkon = Referentiedata(
        code="BKO",
        naam="Balkon",
    )
    """
    Uitkragend platform aan buitenzijde gebouw, toegankelijk via deur. Relatie met IFC
    codering (IfcSlab.FLOOR)
    """

    balustrade = Referentiedata(
        code="BLU",
        naam="Balustrade",
    )
    """
    Rij van balusters (kleine pilaren), dient als afscheiding of reling. Relatie met IFC
    codering (IfcRailing.BALUSTRADE)
    """

    beglazing = Referentiedata(
        code="BEG",
        naam="Beglazing",
    )
    """
    Glaswerk in kozijnen van ramen en deuren voor lichtinval en isolatie. Relatie met
    IFC codering (IfcWindow.WINDOW)
    """

    boeiboord = Referentiedata(
        code="BOE",
        naam="Boeiboord",
    )
    """
    Afwerkingsrand aan de dakrand voor bescherming en esthetiek. Relatie met IFC
    codering (IfcPlate.SHEET)
    """

    boiler = Referentiedata(
        code="BOI",
        naam="Boiler",
    )
    """
    Apparaat voor opwarming en opslag van gebruikswater. Relatie met IFC codering
    (IfcBoiler)
    """

    borstwering = Referentiedata(
        code="BOR",
        naam="Borstwering",
    )
    """
    Lage muur aan de rand van een balkon, dak of brug. Relatie met IFC codering
    (IfcWall.PARAPET)
    """

    brandblusser = Referentiedata(
        code="BRA",
        naam="Brandblusser",
    )
    """
    Draagbaar toestel voor het blussen van beginnende branden. Relatie met IFC codering
    (IfcFurniture)
    """

    brandmeldinstallatie = Referentiedata(
        code="BME",
        naam="Brandmeldinstallatie",
    )
    """
    Systeem voor detectie en alarmering van brand in gebouwen. Relatie met IFC codering
    (IfcSystem.FIREPROTECTION)
    """

    closetcombinatie = Referentiedata(
        code="CLO",
        naam="Closetcombinatie",
    )
    """
    Complete toiletopstelling inclusief pot, stortbak en soms bidet. Relatie met IFC
    codering (IfcSanitaryTerminal.TOILETPAN)
    """

    console = Referentiedata(
        code="CON",
        naam="Console",
    )
    """
    Uitstekend steunelement aan muur voor dragende functies. Relatie met IFC codering
    (IfcBeam.T-BEAM)
    """

    dak = Referentiedata(
        code="DAK",
        naam="Dak",
    )
    """
    Bovenste afdekking van een gebouw, beschermt tegen weersinvloeden. Relatie met IFC
    codering (IfcRoof)
    """

    dakkapel = Referentiedata(
        code="DKA",
        naam="Dakkapel",
    )
    """
    Uitbouw op dakvlak, zorgt voor extra ruimte en licht. Relatie met IFC codering
    (IfcRoof)
    """

    dakraam = Referentiedata(
        code="DRA",
        naam="Dakraam",
    )
    """
    Raam geplaatst in dak, voor licht en ventilatie. Relatie met IFC codering
    (IfcWindow.SKYLIGHT)
    """

    dakrand = Referentiedata(
        code="DRN",
        naam="Dakrand",
    )
    """
    Afwerking aan de rand van het dak voor bescherming en esthetiek. Relatie met IFC
    codering (IfcRoof)
    """

    deur = Referentiedata(
        code="DEU",
        naam="Deur",
    )
    """
    Beweegbaar element dat toegang biedt of afsluit. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    deurdranger = Referentiedata(
        code="DDR",
        naam="Deurdranger",
    )
    """
    Mechanisme dat deuren automatisch sluit na opening. Relatie met IFC codering
    (IfcBuildingElementProxy)
    """

    dorpel = Referentiedata(
        code="DOR",
        naam="Dorpel",
    )
    """
    Onderste deel van een deur- of raamkozijn. houdt vocht buiten. Relatie met IFC
    codering (IfcMember)
    """

    douche = Referentiedata(
        code="DOU",
        naam="Douche",
    )
    """
    Installatie voor lichaamsreiniging door middel van waterstralen. Relatie met IFC
    codering (IfcSanitaryTerminal.SHOWER)
    """

    expansievat = Referentiedata(
        code="EXP",
        naam="Expansievat",
    )
    """
    Veiligheidsonderdeel in verwarmingssystemen, vangt drukverschillen op. Relatie met
    IFC codering (IfcTank.EXPANSION)
    """

    fontein = Referentiedata(
        code="FON",
        naam="Fontein",
    )
    """
    Kleine wateruitlaat, vaak decoratief in publieke of privé-ruimtes. Relatie met IFC
    codering (IfcSanitaryTerminal.SINK)
    """

    galerij = Referentiedata(
        code="GAL",
        naam="Galerij",
    )
    """
    Overdekte, open gang langs buitenzijde van een gebouw. Relatie met IFC codering
    (IfcSlab)
    """

    garagedeur = Referentiedata(
        code="GAR",
        naam="Garagedeur",
    )
    """
    Grote deur specifiek ontworpen voor toegang tot een garage. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    goot = Referentiedata(
        code="GOO",
        naam="Goot",
    )
    """
    Kanaal voor afvoer van hemelwater van daken. Relatie met IFC codering
    (IfcPipeSegment.GUTTER)
    """

    handmelder = Referentiedata(
        code="HAN",
        naam="Handmelder",
    )
    """
    Handbediend alarmtoestel voor het activeren van brandalarm. Relatie met IFC codering
    (IfcAlarm.MANUALPULLBOX)
    """

    hek = Referentiedata(
        code="HEK",
        naam="Hek",
    )
    """
    Omheining of afscheiding, vaak van metaal of hout. Relatie met IFC codering
    (IfcRailing)
    """

    hellingbaan = Referentiedata(
        code="HEL",
        naam="Hellingbaan",
    )
    """
    Hellend vlak voor toegang met voertuigen of rolstoelen. Relatie met IFC codering
    (IfcRamp)
    """

    hemelwaterafvoer = Referentiedata(
        code="HEM",
        naam="Hemelwaterafvoer",
    )
    """
    Systeem voor afvoer van regenwater van daken naar riolering. Relatie met IFC
    codering (IfcPipeSegment)
    """

    isolatie = Referentiedata(
        code="ISO",
        naam="Isolatie",
    )
    """
    Materiaal gebruikt om warmte, geluid of elektriciteit te beperken. Relatie met IFC
    codering (IfcCovering.INSULATION)
    """

    kanteldeur = Referentiedata(
        code="KAN",
        naam="Kanteldeur",
    )
    """
    Deur die kantelt om te openen, vaak gebruikt bij garages. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    kast = Referentiedata(
        code="KAS",
        naam="Kast",
    )
    """
    Opbergmeubel met deuren of laden. Relatie met IFC codering (IfcFurniture.SHELF)
    """

    ketel = Referentiedata(
        code="KET",
        naam="Ketel",
    )
    """
    Apparaat voor verwarming van water of stoomproductie. Relatie met IFC codering
    (IfcBoiler)
    """

    kolom = Referentiedata(
        code="KOL",
        naam="Kolom",
    )
    """
    Verticaal steunelement in constructies. Relatie met IFC codering (IfcColumn.COLUMN)
    """

    kozijn = Referentiedata(
        code="KOZ",
        naam="Kozijn",
    )
    """
    Omlijsting waarin deur of raam bevestigd is. Relatie met IFC codering (IfcWindow)
    """

    leuning = Referentiedata(
        code="LEU",
        naam="Leuning",
    )
    """
    Steun- of geleidingsreling, vooral bij trappen. Relatie met IFC codering
    (IfcRailing.HANDRAIL)
    """

    lichtkoepel = Referentiedata(
        code="LIC",
        naam="Lichtkoepel",
    )
    """
    Doorzichtig element op daken voor daglichttoetreding. Relatie met IFC codering
    (IfcWindow.LIGHTDOME)
    """

    lichtstraat = Referentiedata(
        code="LST",
        naam="Lichtstraat",
    )
    """
    Serie aaneengesloten ramen of koepels op het dak voor lichtinval. Relatie met IFC
    codering (IfcWindow.LIGHTDOME)
    """

    lift = Referentiedata(
        code="LIF",
        naam="Lift",
    )
    """
    Verticaal transportsysteem voor personen of goederen. Relatie met IFC codering
    (IfcTransportElement.ELEVATOR)
    """

    luchtbehandelingskast = Referentiedata(
        code="LUC",
        naam="Luchtbehandelingskast",
    )
    """
    Apparaat voor conditioneren van lucht in gebouwen. Relatie met IFC codering
    (IfcUnitaryEquipment)
    """

    luifel = Referentiedata(
        code="LFE",
        naam="Luifel",
    )
    """
    Overkapping boven deur of raam tegen weersinvloeden. Relatie met IFC codering
    (IfcRoof)
    """

    luik = Referentiedata(
        code="LUI",
        naam="Luik",
    )
    """
    Afsluitbaar paneel in deur, raam of vloer. Relatie met IFC codering
    (IfcDoor.TRAPDOOR)
    """

    meldsirene = Referentiedata(
        code="MEL",
        naam="Meldsirene",
    )
    """
    Geluidsapparaat voor waarschuwing bij gevaar, zoals brand. Relatie met IFC codering
    (IfcAlarm.SIREN)
    """

    nvo = Referentiedata(
        code="NVO",
        naam="NVO",
    )
    """
    Niet van toepassing, specificeer term. Relatie met IFC codering (IfcSpace.SPACE)
    """

    paneel = Referentiedata(
        code="PAN",
        naam="Paneel",
    )
    """
    Vlak element gebruikt in wanden, deuren of meubels. Relatie met IFC codering
    (IfcPlate.SHEET)
    """

    plafond = Referentiedata(
        code="PLA",
        naam="Plafond",
    )
    """
    Binnenafwerking van bovenzijde ruimte. Relatie met IFC codering
    (IfcCovering.CEILING)
    """

    postkast = Referentiedata(
        code="POS",
        naam="Postkast",
    )
    """
    Kast voor ontvangst van poststukken. Relatie met IFC codering (IfcFurniture)
    """

    privacyscherm = Referentiedata(
        code="PRI",
        naam="Privacyscherm",
    )
    """
    Afscheiding bedoeld voor het creëren van privacy. Relatie met IFC codering
    (IfcFurniture)
    """

    raam = Referentiedata(
        code="RAA",
        naam="Raam",
    )
    """
    Kozijn met glas voor licht en ventilatie. Relatie met IFC codering
    (IfcWindow.WINDOW)
    """

    radiator = Referentiedata(
        code="RAD",
        naam="Radiator",
    )
    """
    Warmtewisselaar voor verwarming van ruimtes. Relatie met IFC codering
    (IfcSpaceHeater.RADIATOR)
    """

    rookmelder = Referentiedata(
        code="ROO",
        naam="Rookmelder",
    )
    """
    Detectieapparaat voor vroegtijdige waarschuwing bij rookontwikkeling. Relatie met
    IFC codering (IfcSensor.SMOKESENSOR)
    """

    rooster = Referentiedata(
        code="RST",
        naam="Rooster",
    )
    """
    Geperforeerd paneel voor ventilatie of afdekking. Relatie met IFC codering
    (IfcAirTerminal.GRILLE)
    """

    schoorsteen = Referentiedata(
        code="SST",
        naam="Schoorsteen",
    )
    """
    Constructie voor afvoer van rook en verbrandingsgassen. Relatie met IFC codering
    (IfcChimney)
    """

    schuifdeur = Referentiedata(
        code="SDE",
        naam="Schuifdeur",
    )
    """
    Deur die open en dicht gaat door te schuiven. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    schuifpui = Referentiedata(
        code="SPU",
        naam="Schuifpui",
    )
    """
    Grote schuifdeur, vaak glas, verbindt binnen met buiten. Relatie met IFC codering
    (IfcWindow.WINDOW)
    """

    trap = Referentiedata(
        code="TRA",
        naam="Trap",
    )
    """
    Constructie van treden voor verticale verplaatsing. Relatie met IFC codering
    (IfcStair)
    """

    traplift = Referentiedata(
        code="TLI",
        naam="Traplift",
    )
    """
    Hulpmiddel voor het overbruggen van trappen door mindervaliden. Relatie met IFC
    codering (IfcTransportElement)
    """

    urinoir = Referentiedata(
        code="URI",
        naam="Urinoir",
    )
    """
    Sanitair voor staand urineren door mannen. Relatie met IFC codering
    (IfcSanitaryTerminal.URINAL)
    """

    ventilatiekap = Referentiedata(
        code="VEN",
        naam="Ventilatiekap",
    )
    """
    Afzuigkap boven kookplaat, voert kookdampen af. Relatie met IFC codering
    (IfcStackTerminal.COWL)
    """

    ventilatierooster = Referentiedata(
        code="VRO",
        naam="Ventilatierooster",
    )
    """
    Opening in muur of raam voor luchttoe- of afvoer. Relatie met IFC codering
    (IfcAirTerminal.DIFFUSER)
    """

    vliesgevel = Referentiedata(
        code="VLI",
        naam="Vliesgevel",
    )
    """
    Lichtgewicht gevelsysteem, veelal van glas. Relatie met IFC codering
    (IfcCurtainWall)
    """

    vlizotrap = Referentiedata(
        code="VTR",
        naam="Vlizotrap",
    )
    """
    Opvouwbare trap naar zolder of vliering. Relatie met IFC codering (IfcStair)
    """

    vloer = Referentiedata(
        code="VLO",
        naam="Vloer",
    )
    """
    Horizontaal steunelement, scheidt verschillende verdiepingen. Relatie met IFC
    codering (IfcSlab.FLOOR)
    """

    wand = Referentiedata(
        code="WAN",
        naam="Wand",
    )
    """
    Verticaal scheidend element in bouwkundige constructies. Relatie met IFC codering
    (IfcWallStandardCase)
    """

    warmtepomp = Referentiedata(
        code="WAR",
        naam="Warmtepomp",
    )
    """
    Apparaat dat warmte verplaatst voor verwarming of koeling. Relatie met IFC codering
    (IfcPump)
    """

    warmteterugwinning_apparaat = Referentiedata(
        code="WTE",
        naam="Warmteterugwinning apparaat",
    )
    """
    Systeem dat warmte uit afvoerlucht hergebruikt voor energie-efficiëntie. Relatie met
    IFC codering (IfcAirToAirHeatRecovery)
    """

    wastafel = Referentiedata(
        code="WAS",
        naam="Wastafel",
    )
    """
    Sanitair voor handen wassen en persoonlijke verzorging. Relatie met IFC codering
    (IfcSanitaryTerminal.WASHHANDBASIN)
    """

    zonnepaneel = Referentiedata(
        code="ZPA",
        naam="Zonnepaneel",
    )
    """
    Apparaat dat zonlicht omzet in elektriciteit. Relatie met IFC codering
    (IfcSolarDevice)
    """

    zonwering = Referentiedata(
        code="ZON",
        naam="Zonwering",
    )
    """
    Extern of intern systeem om zonlicht en warmte te reguleren. Relatie met IFC
    codering (IfcShadingDevice)
    """

    afvoer = Referentiedata(
        code="AFV",
        naam="Afvoer",
    )

    balustrades_en_leuningen = Referentiedata(
        code="BAL",
        naam="Balustrades en leuningen",
    )

    beveiliging = Referentiedata(
        code="BEV",
        naam="Beveiliging",
    )

    binnenwandafwerking = Referentiedata(
        code="BIA",
        naam="Binnenwandafwerking",
    )

    binnenwanden = Referentiedata(
        code="BIN",
        naam="Binnenwanden",
    )

    binnenwandopeningen = Referentiedata(
        code="BIW",
        naam="Binnenwandopeningen",
    )

    buitenwandafwerking = Referentiedata(
        code="BUA",
        naam="Buitenwandafwerking",
    )

    buitenwanden = Referentiedata(
        code="BUI",
        naam="Buitenwanden",
    )

    buitenwandopeningen = Referentiedata(
        code="BUW",
        naam="Buitenwandopeningen",
    )

    communicatie = Referentiedata(
        code="COM",
        naam="Communicatie",
    )

    dakbedekking = Referentiedata(
        code="DBE",
        naam="Dakbedekking",
    )

    dakopeningen = Referentiedata(
        code="DOP",
        naam="Dakopeningen",
    )

    elektra = Referentiedata(
        code="ELE",
        naam="Elektra",
    )

    gas = Referentiedata(
        code="GAS",
        naam="Gas",
    )

    keukenvoorzieningen = Referentiedata(
        code="KEU",
        naam="Keukenvoorzieningen",
    )

    losse_opslaginventaris = Referentiedata(
        code="LOS",
        naam="Losse opslaginventaris",
    )

    plafondafwerking = Referentiedata(
        code="PAF",
        naam="Plafondafwerking",
    )

    sanitaire_voorzieningen = Referentiedata(
        code="SAN",
        naam="Sanitaire voorzieningen",
    )

    schilderwerk = Referentiedata(
        code="SCH",
        naam="Schilderwerk",
    )

    terrein = Referentiedata(
        code="TER",
        naam="Terrein",
    )

    trap_en_hellingafwerking = Referentiedata(
        code="THA",
        naam="Trap- en hellingafwerking",
    )

    vloerafwerking = Referentiedata(
        code="VAF",
        naam="Vloerafwerking",
    )

    verwarmingsonderdelen = Referentiedata(
        code="VEO",
        naam="Verwarmingsonderdelen",
    )

    verlichting = Referentiedata(
        code="VER",
        naam="Verlichting",
    )

    vloeropeningen = Referentiedata(
        code="VOP",
        naam="Vloeropeningen",
    )

    verwarmingstoestellen = Referentiedata(
        code="VTO",
        naam="Verwarmingstoestellen",
    )

    waterleiding_en_of_hoofdkraan = Referentiedata(
        code="WAT",
        naam="Waterleiding/hoofdkraan",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
