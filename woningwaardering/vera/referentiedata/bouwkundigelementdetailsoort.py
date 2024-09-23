from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Bouwkundigelementdetailsoort(Enum):
    aanrecht = Referentiedata(
        code="AAN",
        naam="Aanrecht",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Werkoppervlak in keukens, uitgerust met spoelbak en ruimte voor het bereiden van
    voedsel. Relatie met IFC codering (IfcFurniture)
    """

    afdekker = Referentiedata(
        code="AFD",
        naam="Afdekker",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Beschermend element dat het bovenste deel van een constructie bedekt tegen
    weersinvloeden. Relatie met IFC codering (IfcCovering.ROOFING)
    """

    armatuur = Referentiedata(
        code="ARM",
        naam="Armatuur",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Compleet toestel inclusief behuizing, lamp en fittingen voor lichtverspreiding.
    Relatie met IFC codering (IfcLightFixture)
    """

    bad = Referentiedata(
        code="BAD",
        naam="Bad",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Waterhoudend sanitair gebruiksvoorwerp voor persoonlijke hygiëne. Relatie met IFC
    codering (IfcSanitaryTerminal.BATH)
    """

    balk = Referentiedata(
        code="BLK",
        naam="Balk",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Horizontaal steunelement in constructies, draagt vloer-, daklasten. Relatie met IFC
    codering (IfcBeam.BEAM)
    """

    balkon = Referentiedata(
        code="BKO",
        naam="Balkon",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Uitkragend platform aan buitenzijde gebouw, toegankelijk via deur. Relatie met IFC
    codering (IfcSlab.FLOOR)
    """

    balustrade = Referentiedata(
        code="BLU",
        naam="Balustrade",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Rij van balusters (kleine pilaren), dient als afscheiding of reling. Relatie met IFC
    codering (IfcRailing.BALUSTRADE)
    """

    beglazing = Referentiedata(
        code="BEG",
        naam="Beglazing",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Glaswerk in kozijnen van ramen en deuren voor lichtinval en isolatie. Relatie met
    IFC codering (IfcWindow.WINDOW)
    """

    boeiboord = Referentiedata(
        code="BOE",
        naam="Boeiboord",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Afwerkingsrand aan de dakrand voor bescherming en esthetiek. Relatie met IFC
    codering (IfcPlate.SHEET)
    """

    boiler = Referentiedata(
        code="BOI",
        naam="Boiler",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Apparaat voor opwarming en opslag van gebruikswater. Relatie met IFC codering
    (IfcBoiler)
    """

    borstwering = Referentiedata(
        code="BOR",
        naam="Borstwering",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Lage muur aan de rand van een balkon, dak of brug. Relatie met IFC codering
    (IfcWall.PARAPET)
    """

    brandblusser = Referentiedata(
        code="BRA",
        naam="Brandblusser",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Draagbaar toestel voor het blussen van beginnende branden. Relatie met IFC codering
    (IfcFurniture)
    """

    brandmeldinstallatie = Referentiedata(
        code="BME",
        naam="Brandmeldinstallatie",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Systeem voor detectie en alarmering van brand in gebouwen. Relatie met IFC codering
    (IfcSystem.FIREPROTECTION)
    """

    closetcombinatie = Referentiedata(
        code="CLO",
        naam="Closetcombinatie",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Complete toiletopstelling inclusief pot, stortbak en soms bidet. Relatie met IFC
    codering (IfcSanitaryTerminal.TOILETPAN)
    """

    console = Referentiedata(
        code="CON",
        naam="Console",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Uitstekend steunelement aan muur voor dragende functies. Relatie met IFC codering
    (IfcBeam.T-BEAM)
    """

    dak = Referentiedata(
        code="DAK",
        naam="Dak",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Bovenste afdekking van een gebouw, beschermt tegen weersinvloeden. Relatie met IFC
    codering (IfcRoof)
    """

    dakkapel = Referentiedata(
        code="DKA",
        naam="Dakkapel",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Uitbouw op dakvlak, zorgt voor extra ruimte en licht. Relatie met IFC codering
    (IfcRoof)
    """

    dakraam = Referentiedata(
        code="DRA",
        naam="Dakraam",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Raam geplaatst in dak, voor licht en ventilatie. Relatie met IFC codering
    (IfcWindow.SKYLIGHT)
    """

    dakrand = Referentiedata(
        code="DRN",
        naam="Dakrand",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Afwerking aan de rand van het dak voor bescherming en esthetiek. Relatie met IFC
    codering (IfcRoof)
    """

    deur = Referentiedata(
        code="DEU",
        naam="Deur",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Beweegbaar element dat toegang biedt of afsluit. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    deurdranger = Referentiedata(
        code="DDR",
        naam="Deurdranger",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Mechanisme dat deuren automatisch sluit na opening. Relatie met IFC codering
    (IfcBuildingElementProxy)
    """

    dorpel = Referentiedata(
        code="DOR",
        naam="Dorpel",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Onderste deel van een deur- of raamkozijn. houdt vocht buiten. Relatie met IFC
    codering (IfcMember)
    """

    douche = Referentiedata(
        code="DOU",
        naam="Douche",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Installatie voor lichaamsreiniging door middel van waterstralen. Relatie met IFC
    codering (IfcSanitaryTerminal.SHOWER)
    """

    expansievat = Referentiedata(
        code="EXP",
        naam="Expansievat",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Veiligheidsonderdeel in verwarmingssystemen, vangt drukverschillen op. Relatie met
    IFC codering (IfcTank.EXPANSION)
    """

    fontein = Referentiedata(
        code="FON",
        naam="Fontein",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Kleine wateruitlaat, vaak decoratief in publieke of privé-ruimten. Relatie met IFC
    codering (IfcSanitaryTerminal.SINK)
    """

    galerij = Referentiedata(
        code="GAL",
        naam="Galerij",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Overdekte, open gang langs buitenzijde van een gebouw. Relatie met IFC codering
    (IfcSlab)
    """

    garagedeur = Referentiedata(
        code="GAR",
        naam="Garagedeur",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Grote deur specifiek ontworpen voor toegang tot een garage. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    goot = Referentiedata(
        code="GOO",
        naam="Goot",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Kanaal voor afvoer van hemelwater van daken. Relatie met IFC codering
    (IfcPipeSegment.GUTTER)
    """

    handmelder = Referentiedata(
        code="HAN",
        naam="Handmelder",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Handbediend alarmtoestel voor het activeren van brandalarm. Relatie met IFC codering
    (IfcAlarm.MANUALPULLBOX)
    """

    hek = Referentiedata(
        code="HEK",
        naam="Hek",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Omheining of afscheiding, vaak van metaal of hout. Relatie met IFC codering
    (IfcRailing)
    """

    hellingbaan = Referentiedata(
        code="HEL",
        naam="Hellingbaan",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Hellend vlak voor toegang met voertuigen of rolstoelen. Relatie met IFC codering
    (IfcRamp)
    """

    hemelwaterafvoer = Referentiedata(
        code="HEM",
        naam="Hemelwaterafvoer",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Systeem voor afvoer van regenwater van daken naar riolering. Relatie met IFC
    codering (IfcPipeSegment)
    """

    isolatie = Referentiedata(
        code="ISO",
        naam="Isolatie",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Materiaal gebruikt om warmte, geluid of elektriciteit te beperken. Relatie met IFC
    codering (IfcCovering.INSULATION)
    """

    kanteldeur = Referentiedata(
        code="KAN",
        naam="Kanteldeur",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Deur die kantelt om te openen, vaak gebruikt bij garages. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    kast = Referentiedata(
        code="KAS",
        naam="Kast",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Opbergmeubel met deuren of laden. Relatie met IFC codering (IfcFurniture.SHELF)
    """

    ketel = Referentiedata(
        code="KET",
        naam="Ketel",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Apparaat voor verwarming van water of stoomproductie. Relatie met IFC codering
    (IfcBoiler)
    """

    kolom = Referentiedata(
        code="KOL",
        naam="Kolom",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Verticaal steunelement in constructies. Relatie met IFC codering (IfcColumn.COLUMN)
    """

    kozijn = Referentiedata(
        code="KOZ",
        naam="Kozijn",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Omlijsting waarin deur of raam bevestigd is. Relatie met IFC codering (IfcWindow)
    """

    laadpaal = Referentiedata(
        code="LAA",
        naam="Laadpaal",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Een laadpaal is een elektrisch oplaadstation voor voertuigen, zoals elektrische
    auto's. Het biedt een aansluiting voor opladen, communiceert met het voertuig
    voor veilige energieoverdracht, en kan slimme functies bevatten zoals
    laadtijdbeheer en energiebeheer. Relatie met IFC codering (IfcFlowTerminal)
    """

    leuning = Referentiedata(
        code="LEU",
        naam="Leuning",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Steun- of geleidingsreling, vooral bij trappen. Relatie met IFC codering
    (IfcRailing.HANDRAIL)
    """

    lichtkoepel = Referentiedata(
        code="LIC",
        naam="Lichtkoepel",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Doorzichtig element op daken voor daglichttoetreding. Relatie met IFC codering
    (IfcWindow.LIGHTDOME)
    """

    lichtstraat = Referentiedata(
        code="LST",
        naam="Lichtstraat",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Serie aaneengesloten ramen of koepels op het dak voor lichtinval. Relatie met IFC
    codering (IfcWindow.LIGHTDOME)
    """

    lift = Referentiedata(
        code="LIF",
        naam="Lift",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Verticaal transportsysteem voor personen of goederen. Relatie met IFC codering
    (IfcTransportElement.ELEVATOR)
    """

    luchtbehandelingskast = Referentiedata(
        code="LUC",
        naam="Luchtbehandelingskast",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Apparaat voor conditioneren van lucht in gebouwen. Relatie met IFC codering
    (IfcUnitaryEquipment)
    """

    luifel = Referentiedata(
        code="LFE",
        naam="Luifel",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Overkapping boven deur of raam tegen weersinvloeden. Relatie met IFC codering
    (IfcRoof)
    """

    luik = Referentiedata(
        code="LUI",
        naam="Luik",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Afsluitbaar paneel in deur, raam of vloer. Relatie met IFC codering
    (IfcDoor.TRAPDOOR)
    """

    meldsirene = Referentiedata(
        code="MEL",
        naam="Meldsirene",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Geluidsapparaat voor waarschuwing bij gevaar, zoals brand. Relatie met IFC codering
    (IfcAlarm.SIREN)
    """

    nvo = Referentiedata(
        code="NVO",
        naam="NVO",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Niet van toepassing, specificeer term. Relatie met IFC codering (IfcSpace.SPACE)
    """

    paneel = Referentiedata(
        code="PAN",
        naam="Paneel",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Vlak element gebruikt in wanden, deuren of meubels. Relatie met IFC codering
    (IfcPlate.SHEET)
    """

    plafond = Referentiedata(
        code="PLA",
        naam="Plafond",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Binnenafwerking van bovenzijde ruimte. Relatie met IFC codering
    (IfcCovering.CEILING)
    """

    postkast = Referentiedata(
        code="POS",
        naam="Postkast",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Kast voor ontvangst van poststukken. Relatie met IFC codering (IfcFurniture)
    """

    privacyscherm = Referentiedata(
        code="PRI",
        naam="Privacyscherm",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Afscheiding bedoeld voor het creëren van privacy. Relatie met IFC codering
    (IfcFurniture)
    """

    raam = Referentiedata(
        code="RAA",
        naam="Raam",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Kozijn met glas voor licht en ventilatie. Relatie met IFC codering
    (IfcWindow.WINDOW)
    """

    radiator = Referentiedata(
        code="RAD",
        naam="Radiator",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Warmtewisselaar voor verwarming van ruimten. Relatie met IFC codering
    (IfcSpaceHeater.RADIATOR)
    """

    rookmelder = Referentiedata(
        code="ROO",
        naam="Rookmelder",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Detectieapparaat voor vroegtijdige waarschuwing bij rookontwikkeling. Relatie met
    IFC codering (IfcSensor.SMOKESENSOR)
    """

    rooster = Referentiedata(
        code="RST",
        naam="Rooster",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Geperforeerd paneel voor ventilatie of afdekking. Relatie met IFC codering
    (IfcAirTerminal.GRILLE)
    """

    schoorsteen = Referentiedata(
        code="SST",
        naam="Schoorsteen",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Constructie voor afvoer van rook en verbrandingsgassen. Relatie met IFC codering
    (IfcChimney)
    """

    schuifdeur = Referentiedata(
        code="SDE",
        naam="Schuifdeur",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Deur die open en dicht gaat door te schuiven. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    schuifpui = Referentiedata(
        code="SPU",
        naam="Schuifpui",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Grote schuifdeur, vaak glas, verbindt binnen met buiten. Relatie met IFC codering
    (IfcWindow.WINDOW)
    """

    trap = Referentiedata(
        code="TRA",
        naam="Trap",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Constructie van treden voor verticale verplaatsing. Relatie met IFC codering
    (IfcStair)
    """

    traplift = Referentiedata(
        code="TLI",
        naam="Traplift",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Hulpmiddel voor het overbruggen van trappen door mindervaliden. Relatie met IFC
    codering (IfcTransportElement)
    """

    urinoir = Referentiedata(
        code="URI",
        naam="Urinoir",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Sanitair voor staand urineren door mannen. Relatie met IFC codering
    (IfcSanitaryTerminal.URINAL)
    """

    ventilatiekap = Referentiedata(
        code="VEN",
        naam="Ventilatiekap",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Afzuigkap boven kookplaat, voert kookdampen af. Relatie met IFC codering
    (IfcStackTerminal.COWL)
    """

    ventilatierooster = Referentiedata(
        code="VRO",
        naam="Ventilatierooster",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Opening in muur of raam voor luchttoe- of afvoer. Relatie met IFC codering
    (IfcAirTerminal.DIFFUSER)
    """

    vliesgevel = Referentiedata(
        code="VLI",
        naam="Vliesgevel",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Lichtgewicht gevelsysteem, veelal van glas. Relatie met IFC codering
    (IfcCurtainWall)
    """

    vlizotrap = Referentiedata(
        code="VTR",
        naam="Vlizotrap",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Opvouwbare trap naar zolder of vliering. Relatie met IFC codering (IfcStair)
    """

    vloer = Referentiedata(
        code="VLO",
        naam="Vloer",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Horizontaal steunelement, scheidt verschillende verdiepingen. Relatie met IFC
    codering (IfcSlab.FLOOR)
    """

    wand = Referentiedata(
        code="WAN",
        naam="Wand",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Verticaal scheidend element in bouwkundige constructies. Relatie met IFC codering
    (IfcWallStandardCase)
    """

    warmtepomp = Referentiedata(
        code="WAR",
        naam="Warmtepomp",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Apparaat dat warmte verplaatst voor verwarming of koeling. Relatie met IFC codering
    (IfcPump)
    """

    warmteterugwinning_apparaat = Referentiedata(
        code="WTE",
        naam="Warmteterugwinning apparaat",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Systeem dat warmte uit afvoerlucht hergebruikt voor energie-efficiëntie. Relatie met
    IFC codering (IfcAirToAirHeatRecovery)
    """

    wastafel = Referentiedata(
        code="WAS",
        naam="Wastafel",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Sanitair voor handen wassen en persoonlijke verzorging. Relatie met IFC codering
    (IfcSanitaryTerminal.WASHHANDBASIN)
    """

    zonnepaneel = Referentiedata(
        code="ZPA",
        naam="Zonnepaneel",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Apparaat dat zonlicht omzet in elektriciteit. Relatie met IFC codering
    (IfcSolarDevice)
    """

    zonwering = Referentiedata(
        code="ZON",
        naam="Zonwering",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Extern of intern systeem om zonlicht en warmte te reguleren. Relatie met IFC
    codering (IfcShadingDevice)
    """

    afvoer = Referentiedata(
        code="AFV",
        naam="Afvoer",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    balustrades_en_leuningen = Referentiedata(
        code="BAL",
        naam="Balustrades en leuningen",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    beveiliging = Referentiedata(
        code="BEV",
        naam="Beveiliging",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    binnenwandafwerking = Referentiedata(
        code="BIA",
        naam="Binnenwandafwerking",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    bidet = Referentiedata(
        code="BID",
        naam="Bidet",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    binnenwanden = Referentiedata(
        code="BIN",
        naam="Binnenwanden",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    binnenwandopeningen = Referentiedata(
        code="BIW",
        naam="Binnenwandopeningen",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    buitenwandafwerking = Referentiedata(
        code="BUA",
        naam="Buitenwandafwerking",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    buitenwanden = Referentiedata(
        code="BUI",
        naam="Buitenwanden",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    buitenwandopeningen = Referentiedata(
        code="BUW",
        naam="Buitenwandopeningen",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    communicatie = Referentiedata(
        code="COM",
        naam="Communicatie",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    dakbedekking = Referentiedata(
        code="DBE",
        naam="Dakbedekking",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    dakopeningen = Referentiedata(
        code="DOP",
        naam="Dakopeningen",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    elektra = Referentiedata(
        code="ELE",
        naam="Elektra",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    gas = Referentiedata(
        code="GAS",
        naam="Gas",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    keukenvoorzieningen = Referentiedata(
        code="KEU",
        naam="Keukenvoorzieningen",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    lavet = Referentiedata(
        code="LAV",
        naam="Lavet",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    losse_opslaginventaris = Referentiedata(
        code="LOS",
        naam="Losse opslaginventaris",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    plafondafwerking = Referentiedata(
        code="PAF",
        naam="Plafondafwerking",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    sanitaire_voorzieningen = Referentiedata(
        code="SAN",
        naam="Sanitaire voorzieningen",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    schilderwerk = Referentiedata(
        code="SCH",
        naam="Schilderwerk",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    terrein = Referentiedata(
        code="TER",
        naam="Terrein",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    trap_en_hellingafwerking = Referentiedata(
        code="THA",
        naam="Trap- en hellingafwerking",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    vloerafwerking = Referentiedata(
        code="VAF",
        naam="Vloerafwerking",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    verwarmingsonderdelen = Referentiedata(
        code="VEO",
        naam="Verwarmingsonderdelen",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    verlichting = Referentiedata(
        code="VER",
        naam="Verlichting",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    vloeropeningen = Referentiedata(
        code="VOP",
        naam="Vloeropeningen",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    verwarmingstoestellen = Referentiedata(
        code="VTO",
        naam="Verwarmingstoestellen",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    waterleiding_en_of_hoofdkraan = Referentiedata(
        code="WAT",
        naam="Waterleiding/hoofdkraan",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )

    aanbelfunctie_met_video_en_audioverbinding = Referentiedata(
        code="AAV",
        naam="Aanbelfunctie met video- en audioverbinding",
        parent=Referentiedata(
            code="VOO",
            naam="Voorziening",
        ),
    )
    """
    Systeem dat tweewegcommunicatie (beeld en geluid) mogelijk maakt en waarmee de
    voordeur op afstand geopend kan worden. Relatie met IFC codering
    (IfcCommunicationsAppliance) (UITBREIDING)
    """

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
