from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.bouwkundigelementsoort import (
    Bouwkundigelementsoort,
)


class Bouwkundigelementdetailsoort(Enum):
    aanrecht = Referentiedata(
        code="AAN",
        naam="Aanrecht",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Werkoppervlak in keukens, uitgerust met spoelbak en ruimte voor het bereiden van
    voedsel. Relatie met IFC codering (IfcFurniture)
    """

    afdekker = Referentiedata(
        code="AFD",
        naam="Afdekker",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Beschermend element dat het bovenste deel van een constructie bedekt tegen
    weersinvloeden. Relatie met IFC codering (IfcCovering.ROOFING)
    """

    armatuur = Referentiedata(
        code="ARM",
        naam="Armatuur",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Compleet toestel inclusief behuizing, lamp en fittingen voor lichtverspreiding.
    Relatie met IFC codering (IfcLightFixture)
    """

    bad = Referentiedata(
        code="BAD",
        naam="Bad",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Waterhoudend sanitair gebruiksvoorwerp voor persoonlijke hygiëne. Relatie met IFC
    codering (IfcSanitaryTerminal.BATH)
    """

    balk = Referentiedata(
        code="BLK",
        naam="Balk",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Horizontaal steunelement in constructies, draagt vloer-, daklasten. Relatie met IFC
    codering (IfcBeam.BEAM)
    """

    balkon = Referentiedata(
        code="BKO",
        naam="Balkon",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Uitkragend platform aan buitenzijde gebouw, toegankelijk via deur. Relatie met IFC
    codering (IfcSlab.FLOOR)
    """

    balustrade = Referentiedata(
        code="BLU",
        naam="Balustrade",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Rij van balusters (kleine pilaren), dient als afscheiding of reling. Relatie met IFC
    codering (IfcRailing.BALUSTRADE)
    """

    beglazing = Referentiedata(
        code="BEG",
        naam="Beglazing",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Glaswerk in kozijnen van ramen en deuren voor lichtinval en isolatie. Relatie met
    IFC codering (IfcWindow.WINDOW)
    """

    boeiboord = Referentiedata(
        code="BOE",
        naam="Boeiboord",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Afwerkingsrand aan de dakrand voor bescherming en esthetiek. Relatie met IFC
    codering (IfcPlate.SHEET)
    """

    boiler = Referentiedata(
        code="BOI",
        naam="Boiler",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Apparaat voor opwarming en opslag van gebruikswater. Relatie met IFC codering
    (IfcBoiler)
    """

    borstwering = Referentiedata(
        code="BOR",
        naam="Borstwering",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Lage muur aan de rand van een balkon, dak of brug. Relatie met IFC codering
    (IfcWall.PARAPET)
    """

    brandblusser = Referentiedata(
        code="BRA",
        naam="Brandblusser",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Draagbaar toestel voor het blussen van beginnende branden. Relatie met IFC codering
    (IfcFurniture)
    """

    brandmeldinstallatie = Referentiedata(
        code="BME",
        naam="Brandmeldinstallatie",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Systeem voor detectie en alarmering van brand in gebouwen. Relatie met IFC codering
    (IfcSystem.FIREPROTECTION)
    """

    closetcombinatie = Referentiedata(
        code="CLO",
        naam="Closetcombinatie",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Complete toiletopstelling inclusief pot, stortbak en soms bidet. Relatie met IFC
    codering (IfcSanitaryTerminal.TOILETPAN)
    """

    console = Referentiedata(
        code="CON",
        naam="Console",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Uitstekend steunelement aan muur voor dragende functies. Relatie met IFC codering
    (IfcBeam.T-BEAM)
    """

    dak = Referentiedata(
        code="DAK",
        naam="Dak",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Bovenste afdekking van een gebouw, beschermt tegen weersinvloeden. Relatie met IFC
    codering (IfcRoof)
    """

    dakkapel = Referentiedata(
        code="DKA",
        naam="Dakkapel",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Uitbouw op dakvlak, zorgt voor extra ruimte en licht. Relatie met IFC codering
    (IfcRoof)
    """

    dakraam = Referentiedata(
        code="DRA",
        naam="Dakraam",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Raam geplaatst in dak, voor licht en ventilatie. Relatie met IFC codering
    (IfcWindow.SKYLIGHT)
    """

    dakrand = Referentiedata(
        code="DRN",
        naam="Dakrand",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Afwerking aan de rand van het dak voor bescherming en esthetiek. Relatie met IFC
    codering (IfcRoof)
    """

    deur = Referentiedata(
        code="DEU",
        naam="Deur",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Beweegbaar element dat toegang biedt of afsluit. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    deurdranger = Referentiedata(
        code="DDR",
        naam="Deurdranger",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Mechanisme dat deuren automatisch sluit na opening. Relatie met IFC codering
    (IfcBuildingElementProxy)
    """

    dorpel = Referentiedata(
        code="DOR",
        naam="Dorpel",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Onderste deel van een deur- of raamkozijn. houdt vocht buiten. Relatie met IFC
    codering (IfcMember)
    """

    douche = Referentiedata(
        code="DOU",
        naam="Douche",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Installatie voor lichaamsreiniging door middel van waterstralen. Relatie met IFC
    codering (IfcSanitaryTerminal.SHOWER)
    """

    expansievat = Referentiedata(
        code="EXP",
        naam="Expansievat",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Veiligheidsonderdeel in verwarmingssystemen, vangt drukverschillen op. Relatie met
    IFC codering (IfcTank.EXPANSION)
    """

    fontein = Referentiedata(
        code="FON",
        naam="Fontein",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Kleine wateruitlaat, vaak decoratief in publieke of privé-ruimten. Relatie met IFC
    codering (IfcSanitaryTerminal.SINK)
    """

    galerij = Referentiedata(
        code="GAL",
        naam="Galerij",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Overdekte, open gang langs buitenzijde van een gebouw. Relatie met IFC codering
    (IfcSlab)
    """

    garagedeur = Referentiedata(
        code="GAR",
        naam="Garagedeur",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Grote deur specifiek ontworpen voor toegang tot een garage. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    goot = Referentiedata(
        code="GOO",
        naam="Goot",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Kanaal voor afvoer van hemelwater van daken. Relatie met IFC codering
    (IfcPipeSegment.GUTTER)
    """

    handmelder = Referentiedata(
        code="HAN",
        naam="Handmelder",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Handbediend alarmtoestel voor het activeren van brandalarm. Relatie met IFC codering
    (IfcAlarm.MANUALPULLBOX)
    """

    hek = Referentiedata(
        code="HEK",
        naam="Hek",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Omheining of afscheiding, vaak van metaal of hout. Relatie met IFC codering
    (IfcRailing)
    """

    hellingbaan = Referentiedata(
        code="HEL",
        naam="Hellingbaan",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Hellend vlak voor toegang met voertuigen of rolstoelen. Relatie met IFC codering
    (IfcRamp)
    """

    hemelwaterafvoer = Referentiedata(
        code="HEM",
        naam="Hemelwaterafvoer",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Systeem voor afvoer van regenwater van daken naar riolering. Relatie met IFC
    codering (IfcPipeSegment)
    """

    isolatie = Referentiedata(
        code="ISO",
        naam="Isolatie",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Materiaal gebruikt om warmte, geluid of elektriciteit te beperken. Relatie met IFC
    codering (IfcCovering.INSULATION)
    """

    kanteldeur = Referentiedata(
        code="KAN",
        naam="Kanteldeur",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Deur die kantelt om te openen, vaak gebruikt bij garages. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    kast = Referentiedata(
        code="KAS",
        naam="Kast",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Opbergmeubel met deuren of laden. Relatie met IFC codering (IfcFurniture.SHELF)
    """

    ketel = Referentiedata(
        code="KET",
        naam="Ketel",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Apparaat voor verwarming van water of stoomproductie. Relatie met IFC codering
    (IfcBoiler)
    """

    kolom = Referentiedata(
        code="KOL",
        naam="Kolom",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Verticaal steunelement in constructies. Relatie met IFC codering (IfcColumn.COLUMN)
    """

    kozijn = Referentiedata(
        code="KOZ",
        naam="Kozijn",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Omlijsting waarin deur of raam bevestigd is. Relatie met IFC codering (IfcWindow)
    """

    laadpaal = Referentiedata(
        code="LAA",
        naam="Laadpaal",
        parent=Bouwkundigelementsoort.voorziening.value,
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
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Steun- of geleidingsreling, vooral bij trappen. Relatie met IFC codering
    (IfcRailing.HANDRAIL)
    """

    lichtkoepel = Referentiedata(
        code="LIC",
        naam="Lichtkoepel",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Doorzichtig element op daken voor daglichttoetreding. Relatie met IFC codering
    (IfcWindow.LIGHTDOME)
    """

    lichtstraat = Referentiedata(
        code="LST",
        naam="Lichtstraat",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Serie aaneengesloten ramen of koepels op het dak voor lichtinval. Relatie met IFC
    codering (IfcWindow.LIGHTDOME)
    """

    lift = Referentiedata(
        code="LIF",
        naam="Lift",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Verticaal transportsysteem voor personen of goederen. Relatie met IFC codering
    (IfcTransportElement.ELEVATOR)
    """

    luchtbehandelingskast = Referentiedata(
        code="LUC",
        naam="Luchtbehandelingskast",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Apparaat voor conditioneren van lucht in gebouwen. Relatie met IFC codering
    (IfcUnitaryEquipment)
    """

    luifel = Referentiedata(
        code="LFE",
        naam="Luifel",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Overkapping boven deur of raam tegen weersinvloeden. Relatie met IFC codering
    (IfcRoof)
    """

    luik = Referentiedata(
        code="LUI",
        naam="Luik",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Afsluitbaar paneel in deur, raam of vloer. Relatie met IFC codering
    (IfcDoor.TRAPDOOR)
    """

    meldsirene = Referentiedata(
        code="MEL",
        naam="Meldsirene",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Geluidsapparaat voor waarschuwing bij gevaar, zoals brand. Relatie met IFC codering
    (IfcAlarm.SIREN)
    """

    nvo = Referentiedata(
        code="NVO",
        naam="NVO",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Niet van toepassing, specificeer term. Relatie met IFC codering (IfcSpace.SPACE)
    """

    paneel = Referentiedata(
        code="PAN",
        naam="Paneel",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Vlak element gebruikt in wanden, deuren of meubels. Relatie met IFC codering
    (IfcPlate.SHEET)
    """

    plafond = Referentiedata(
        code="PLA",
        naam="Plafond",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Binnenafwerking van bovenzijde ruimte. Relatie met IFC codering
    (IfcCovering.CEILING)
    """

    postkast = Referentiedata(
        code="POS",
        naam="Postkast",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Kast voor ontvangst van poststukken. Relatie met IFC codering (IfcFurniture)
    """

    privacyscherm = Referentiedata(
        code="PRI",
        naam="Privacyscherm",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Afscheiding bedoeld voor het creëren van privacy. Relatie met IFC codering
    (IfcFurniture)
    """

    raam = Referentiedata(
        code="RAA",
        naam="Raam",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Kozijn met glas voor licht en ventilatie. Relatie met IFC codering
    (IfcWindow.WINDOW)
    """

    radiator = Referentiedata(
        code="RAD",
        naam="Radiator",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Warmtewisselaar voor verwarming van ruimten. Relatie met IFC codering
    (IfcSpaceHeater.RADIATOR)
    """

    rookmelder = Referentiedata(
        code="ROO",
        naam="Rookmelder",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Detectieapparaat voor vroegtijdige waarschuwing bij rookontwikkeling. Relatie met
    IFC codering (IfcSensor.SMOKESENSOR)
    """

    rooster = Referentiedata(
        code="RST",
        naam="Rooster",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Geperforeerd paneel voor ventilatie of afdekking. Relatie met IFC codering
    (IfcAirTerminal.GRILLE)
    """

    schoorsteen = Referentiedata(
        code="SST",
        naam="Schoorsteen",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Constructie voor afvoer van rook en verbrandingsgassen. Relatie met IFC codering
    (IfcChimney)
    """

    schuifdeur = Referentiedata(
        code="SDE",
        naam="Schuifdeur",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Deur die open en dicht gaat door te schuiven. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    schuifpui = Referentiedata(
        code="SPU",
        naam="Schuifpui",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Grote schuifdeur, vaak glas, verbindt binnen met buiten. Relatie met IFC codering
    (IfcWindow.WINDOW)
    """

    trap = Referentiedata(
        code="TRA",
        naam="Trap",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Constructie van treden voor verticale verplaatsing. Relatie met IFC codering
    (IfcStair)
    """

    traplift = Referentiedata(
        code="TLI",
        naam="Traplift",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Hulpmiddel voor het overbruggen van trappen door mindervaliden. Relatie met IFC
    codering (IfcTransportElement)
    """

    urinoir = Referentiedata(
        code="URI",
        naam="Urinoir",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Sanitair voor staand urineren door mannen. Relatie met IFC codering
    (IfcSanitaryTerminal.URINAL)
    """

    ventilatiekap = Referentiedata(
        code="VEN",
        naam="Ventilatiekap",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Afzuigkap boven kookplaat, voert kookdampen af. Relatie met IFC codering
    (IfcStackTerminal.COWL)
    """

    ventilatierooster = Referentiedata(
        code="VRO",
        naam="Ventilatierooster",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Opening in muur of raam voor luchttoe- of afvoer. Relatie met IFC codering
    (IfcAirTerminal.DIFFUSER)
    """

    vliesgevel = Referentiedata(
        code="VLI",
        naam="Vliesgevel",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Lichtgewicht gevelsysteem, veelal van glas. Relatie met IFC codering
    (IfcCurtainWall)
    """

    vlizotrap = Referentiedata(
        code="VTR",
        naam="Vlizotrap",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Opvouwbare trap naar zolder of vliering. Relatie met IFC codering (IfcStair)
    """

    vloer = Referentiedata(
        code="VLO",
        naam="Vloer",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Horizontaal steunelement, scheidt verschillende verdiepingen. Relatie met IFC
    codering (IfcSlab.FLOOR)
    """

    wand = Referentiedata(
        code="WAN",
        naam="Wand",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Verticaal scheidend element in bouwkundige constructies. Relatie met IFC codering
    (IfcWallStandardCase)
    """

    warmtepomp = Referentiedata(
        code="WAR",
        naam="Warmtepomp",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Apparaat dat warmte verplaatst voor verwarming of koeling. Relatie met IFC codering
    (IfcPump)
    """

    warmteterugwinning_apparaat = Referentiedata(
        code="WTE",
        naam="Warmteterugwinning apparaat",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Systeem dat warmte uit afvoerlucht hergebruikt voor energie-efficiëntie. Relatie met
    IFC codering (IfcAirToAirHeatRecovery)
    """

    wastafel = Referentiedata(
        code="WAS",
        naam="Wastafel",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Sanitair voor handen wassen en persoonlijke verzorging. Relatie met IFC codering
    (IfcSanitaryTerminal.WASHHANDBASIN)
    """

    zonnepaneel = Referentiedata(
        code="ZPA",
        naam="Zonnepaneel",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Apparaat dat zonlicht omzet in elektriciteit. Relatie met IFC codering
    (IfcSolarDevice)
    """

    zonwering = Referentiedata(
        code="ZON",
        naam="Zonwering",
        parent=Bouwkundigelementsoort.voorziening.value,
    )
    """
    Extern of intern systeem om zonlicht en warmte te reguleren. Relatie met IFC
    codering (IfcShadingDevice)
    """

    afvoer = Referentiedata(
        code="AFV",
        naam="Afvoer",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    balustrades_en_leuningen = Referentiedata(
        code="BAL",
        naam="Balustrades en leuningen",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    beveiliging = Referentiedata(
        code="BEV",
        naam="Beveiliging",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    binnenwandafwerking = Referentiedata(
        code="BIA",
        naam="Binnenwandafwerking",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    bidet = Referentiedata(
        code="BID",
        naam="Bidet",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    binnenwanden = Referentiedata(
        code="BIN",
        naam="Binnenwanden",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    binnenwandopeningen = Referentiedata(
        code="BIW",
        naam="Binnenwandopeningen",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    buitenwandafwerking = Referentiedata(
        code="BUA",
        naam="Buitenwandafwerking",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    buitenwanden = Referentiedata(
        code="BUI",
        naam="Buitenwanden",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    buitenwandopeningen = Referentiedata(
        code="BUW",
        naam="Buitenwandopeningen",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    communicatie = Referentiedata(
        code="COM",
        naam="Communicatie",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    dakbedekking = Referentiedata(
        code="DBE",
        naam="Dakbedekking",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    dakopeningen = Referentiedata(
        code="DOP",
        naam="Dakopeningen",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    elektra = Referentiedata(
        code="ELE",
        naam="Elektra",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    gas = Referentiedata(
        code="GAS",
        naam="Gas",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    keukenvoorzieningen = Referentiedata(
        code="KEU",
        naam="Keukenvoorzieningen",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    lavet = Referentiedata(
        code="LAV",
        naam="Lavet",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    losse_opslaginventaris = Referentiedata(
        code="LOS",
        naam="Losse opslaginventaris",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    plafondafwerking = Referentiedata(
        code="PAF",
        naam="Plafondafwerking",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    sanitaire_voorzieningen = Referentiedata(
        code="SAN",
        naam="Sanitaire voorzieningen",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    schilderwerk = Referentiedata(
        code="SCH",
        naam="Schilderwerk",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    terrein = Referentiedata(
        code="TER",
        naam="Terrein",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    trap_en_hellingafwerking = Referentiedata(
        code="THA",
        naam="Trap- en hellingafwerking",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    vloerafwerking = Referentiedata(
        code="VAF",
        naam="Vloerafwerking",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    verwarmingsonderdelen = Referentiedata(
        code="VEO",
        naam="Verwarmingsonderdelen",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    verlichting = Referentiedata(
        code="VER",
        naam="Verlichting",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    vloeropeningen = Referentiedata(
        code="VOP",
        naam="Vloeropeningen",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    verwarmingstoestellen = Referentiedata(
        code="VTO",
        naam="Verwarmingstoestellen",
        parent=Bouwkundigelementsoort.voorziening.value,
    )

    waterleiding_en_of_hoofdkraan = Referentiedata(
        code="WAT",
        naam="Waterleiding/hoofdkraan",
        parent=Bouwkundigelementsoort.voorziening.value,
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
