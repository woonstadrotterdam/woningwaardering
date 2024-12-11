from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.bouwkundigelementsoort import (
    Bouwkundigelementsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BouwkundigelementdetailsoortReferentiedata(Referentiedata):
    pass


class Bouwkundigelementdetailsoort(Referentiedatasoort):
    aanrecht = BouwkundigelementdetailsoortReferentiedata(
        code="AAN",
        naam="Aanrecht",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Werkoppervlak in keukens, uitgerust met spoelbak en ruimte voor het bereiden van
    voedsel. Relatie met IFC codering (IfcFurniture)
    """

    afdekker = BouwkundigelementdetailsoortReferentiedata(
        code="AFD",
        naam="Afdekker",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Beschermend element dat het bovenste deel van een constructie bedekt tegen
    weersinvloeden. Relatie met IFC codering (IfcCovering.ROOFING)
    """

    armatuur = BouwkundigelementdetailsoortReferentiedata(
        code="ARM",
        naam="Armatuur",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Compleet toestel inclusief behuizing, lamp en fittingen voor lichtverspreiding.
    Relatie met IFC codering (IfcLightFixture)
    """

    bad = BouwkundigelementdetailsoortReferentiedata(
        code="BAD",
        naam="Bad",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Waterhoudend sanitair gebruiksvoorwerp voor persoonlijke hygiëne. Relatie met IFC
    codering (IfcSanitaryTerminal.BATH)
    """

    balk = BouwkundigelementdetailsoortReferentiedata(
        code="BLK",
        naam="Balk",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Horizontaal steunelement in constructies, draagt vloer-, daklasten. Relatie met IFC
    codering (IfcBeam.BEAM)
    """

    balkon = BouwkundigelementdetailsoortReferentiedata(
        code="BKO",
        naam="Balkon",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Uitkragend platform aan buitenzijde gebouw, toegankelijk via deur. Relatie met IFC
    codering (IfcSlab.FLOOR)
    """

    balustrade = BouwkundigelementdetailsoortReferentiedata(
        code="BLU",
        naam="Balustrade",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Rij van balusters (kleine pilaren), dient als afscheiding of reling. Relatie met IFC
    codering (IfcRailing.BALUSTRADE)
    """

    beglazing = BouwkundigelementdetailsoortReferentiedata(
        code="BEG",
        naam="Beglazing",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Glaswerk in kozijnen van ramen en deuren voor lichtinval en isolatie. Relatie met
    IFC codering (IfcWindow.WINDOW)
    """

    boeiboord = BouwkundigelementdetailsoortReferentiedata(
        code="BOE",
        naam="Boeiboord",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Afwerkingsrand aan de dakrand voor bescherming en esthetiek. Relatie met IFC
    codering (IfcPlate.SHEET)
    """

    boiler = BouwkundigelementdetailsoortReferentiedata(
        code="BOI",
        naam="Boiler",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Apparaat voor opwarming en opslag van gebruikswater. Relatie met IFC codering
    (IfcBoiler)
    """

    borstwering = BouwkundigelementdetailsoortReferentiedata(
        code="BOR",
        naam="Borstwering",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Lage muur aan de rand van een balkon, dak of brug. Relatie met IFC codering
    (IfcWall.PARAPET)
    """

    brandblusser = BouwkundigelementdetailsoortReferentiedata(
        code="BRA",
        naam="Brandblusser",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Draagbaar toestel voor het blussen van beginnende branden. Relatie met IFC codering
    (IfcFurniture)
    """

    brandmeldinstallatie = BouwkundigelementdetailsoortReferentiedata(
        code="BME",
        naam="Brandmeldinstallatie",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Systeem voor detectie en alarmering van brand in gebouwen. Relatie met IFC codering
    (IfcSystem.FIREPROTECTION)
    """

    closetcombinatie = BouwkundigelementdetailsoortReferentiedata(
        code="CLO",
        naam="Closetcombinatie",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Complete toiletopstelling inclusief pot, stortbak en soms bidet. Relatie met IFC
    codering (IfcSanitaryTerminal.TOILETPAN)
    """

    console = BouwkundigelementdetailsoortReferentiedata(
        code="CON",
        naam="Console",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Uitstekend steunelement aan muur voor dragende functies. Relatie met IFC codering
    (IfcBeam.T-BEAM)
    """

    dak = BouwkundigelementdetailsoortReferentiedata(
        code="DAK",
        naam="Dak",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Bovenste afdekking van een gebouw, beschermt tegen weersinvloeden. Relatie met IFC
    codering (IfcRoof)
    """

    dakkapel = BouwkundigelementdetailsoortReferentiedata(
        code="DKA",
        naam="Dakkapel",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Uitbouw op dakvlak, zorgt voor extra ruimte en licht. Relatie met IFC codering
    (IfcRoof)
    """

    dakraam = BouwkundigelementdetailsoortReferentiedata(
        code="DRA",
        naam="Dakraam",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Raam geplaatst in dak, voor licht en ventilatie. Relatie met IFC codering
    (IfcWindow.SKYLIGHT)
    """

    dakrand = BouwkundigelementdetailsoortReferentiedata(
        code="DRN",
        naam="Dakrand",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Afwerking aan de rand van het dak voor bescherming en esthetiek. Relatie met IFC
    codering (IfcRoof)
    """

    deur = BouwkundigelementdetailsoortReferentiedata(
        code="DEU",
        naam="Deur",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Beweegbaar element dat toegang biedt of afsluit. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    deurdranger = BouwkundigelementdetailsoortReferentiedata(
        code="DDR",
        naam="Deurdranger",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Mechanisme dat deuren automatisch sluit na opening. Relatie met IFC codering
    (IfcBuildingElementProxy)
    """

    dorpel = BouwkundigelementdetailsoortReferentiedata(
        code="DOR",
        naam="Dorpel",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Onderste deel van een deur- of raamkozijn. houdt vocht buiten. Relatie met IFC
    codering (IfcMember)
    """

    douche = BouwkundigelementdetailsoortReferentiedata(
        code="DOU",
        naam="Douche",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Installatie voor lichaamsreiniging door middel van waterstralen. Relatie met IFC
    codering (IfcSanitaryTerminal.SHOWER)
    """

    expansievat = BouwkundigelementdetailsoortReferentiedata(
        code="EXP",
        naam="Expansievat",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Veiligheidsonderdeel in verwarmingssystemen, vangt drukverschillen op. Relatie met
    IFC codering (IfcTank.EXPANSION)
    """

    fontein = BouwkundigelementdetailsoortReferentiedata(
        code="FON",
        naam="Fontein",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Kleine wateruitlaat, vaak decoratief in publieke of privé-ruimten. Relatie met IFC
    codering (IfcSanitaryTerminal.SINK)
    """

    galerij = BouwkundigelementdetailsoortReferentiedata(
        code="GAL",
        naam="Galerij",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Overdekte, open gang langs buitenzijde van een gebouw. Relatie met IFC codering
    (IfcSlab)
    """

    garagedeur = BouwkundigelementdetailsoortReferentiedata(
        code="GAR",
        naam="Garagedeur",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Grote deur specifiek ontworpen voor toegang tot een garage. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    goot = BouwkundigelementdetailsoortReferentiedata(
        code="GOO",
        naam="Goot",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Kanaal voor afvoer van hemelwater van daken. Relatie met IFC codering
    (IfcPipeSegment.GUTTER)
    """

    handmelder = BouwkundigelementdetailsoortReferentiedata(
        code="HAN",
        naam="Handmelder",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Handbediend alarmtoestel voor het activeren van brandalarm. Relatie met IFC codering
    (IfcAlarm.MANUALPULLBOX)
    """

    hek = BouwkundigelementdetailsoortReferentiedata(
        code="HEK",
        naam="Hek",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Omheining of afscheiding, vaak van metaal of hout. Relatie met IFC codering
    (IfcRailing)
    """

    hellingbaan = BouwkundigelementdetailsoortReferentiedata(
        code="HEL",
        naam="Hellingbaan",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Hellend vlak voor toegang met voertuigen of rolstoelen. Relatie met IFC codering
    (IfcRamp)
    """

    hemelwaterafvoer = BouwkundigelementdetailsoortReferentiedata(
        code="HEM",
        naam="Hemelwaterafvoer",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Systeem voor afvoer van regenwater van daken naar riolering. Relatie met IFC
    codering (IfcPipeSegment)
    """

    isolatie = BouwkundigelementdetailsoortReferentiedata(
        code="ISO",
        naam="Isolatie",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Materiaal gebruikt om warmte, geluid of elektriciteit te beperken. Relatie met IFC
    codering (IfcCovering.INSULATION)
    """

    kanteldeur = BouwkundigelementdetailsoortReferentiedata(
        code="KAN",
        naam="Kanteldeur",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Deur die kantelt om te openen, vaak gebruikt bij garages. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    kast = BouwkundigelementdetailsoortReferentiedata(
        code="KAS",
        naam="Kast",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Opbergmeubel met deuren of laden. Relatie met IFC codering (IfcFurniture.SHELF)
    """

    ketel = BouwkundigelementdetailsoortReferentiedata(
        code="KET",
        naam="Ketel",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Apparaat voor verwarming van water of stoomproductie. Relatie met IFC codering
    (IfcBoiler)
    """

    kolom = BouwkundigelementdetailsoortReferentiedata(
        code="KOL",
        naam="Kolom",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Verticaal steunelement in constructies. Relatie met IFC codering (IfcColumn.COLUMN)
    """

    kozijn = BouwkundigelementdetailsoortReferentiedata(
        code="KOZ",
        naam="Kozijn",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Omlijsting waarin deur of raam bevestigd is. Relatie met IFC codering (IfcWindow)
    """

    laadpaal = BouwkundigelementdetailsoortReferentiedata(
        code="LAA",
        naam="Laadpaal",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Een laadpaal is een elektrisch oplaadstation voor voertuigen, zoals elektrische
    auto's. Het biedt een aansluiting voor opladen, communiceert met het voertuig
    voor veilige energieoverdracht, en kan slimme functies bevatten zoals
    laadtijdbeheer en energiebeheer. Relatie met IFC codering (IfcFlowTerminal)
    """

    leuning = BouwkundigelementdetailsoortReferentiedata(
        code="LEU",
        naam="Leuning",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Steun- of geleidingsreling, vooral bij trappen. Relatie met IFC codering
    (IfcRailing.HANDRAIL)
    """

    lichtkoepel = BouwkundigelementdetailsoortReferentiedata(
        code="LIC",
        naam="Lichtkoepel",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Doorzichtig element op daken voor daglichttoetreding. Relatie met IFC codering
    (IfcWindow.LIGHTDOME)
    """

    lichtstraat = BouwkundigelementdetailsoortReferentiedata(
        code="LST",
        naam="Lichtstraat",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Serie aaneengesloten ramen of koepels op het dak voor lichtinval. Relatie met IFC
    codering (IfcWindow.LIGHTDOME)
    """

    lift = BouwkundigelementdetailsoortReferentiedata(
        code="LIF",
        naam="Lift",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Verticaal transportsysteem voor personen of goederen. Relatie met IFC codering
    (IfcTransportElement.ELEVATOR)
    """

    luchtbehandelingskast = BouwkundigelementdetailsoortReferentiedata(
        code="LUC",
        naam="Luchtbehandelingskast",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Apparaat voor conditioneren van lucht in gebouwen. Relatie met IFC codering
    (IfcUnitaryEquipment)
    """

    luifel = BouwkundigelementdetailsoortReferentiedata(
        code="LFE",
        naam="Luifel",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Overkapping boven deur of raam tegen weersinvloeden. Relatie met IFC codering
    (IfcRoof)
    """

    luik = BouwkundigelementdetailsoortReferentiedata(
        code="LUI",
        naam="Luik",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Afsluitbaar paneel in deur, raam of vloer. Relatie met IFC codering
    (IfcDoor.TRAPDOOR)
    """

    meldsirene = BouwkundigelementdetailsoortReferentiedata(
        code="MEL",
        naam="Meldsirene",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Geluidsapparaat voor waarschuwing bij gevaar, zoals brand. Relatie met IFC codering
    (IfcAlarm.SIREN)
    """

    nvo = BouwkundigelementdetailsoortReferentiedata(
        code="NVO",
        naam="NVO",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Niet van toepassing, specificeer term. Relatie met IFC codering (IfcSpace.SPACE)
    """

    paneel = BouwkundigelementdetailsoortReferentiedata(
        code="PAN",
        naam="Paneel",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Vlak element gebruikt in wanden, deuren of meubels. Relatie met IFC codering
    (IfcPlate.SHEET)
    """

    plafond = BouwkundigelementdetailsoortReferentiedata(
        code="PLA",
        naam="Plafond",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Binnenafwerking van bovenzijde ruimte. Relatie met IFC codering
    (IfcCovering.CEILING)
    """

    postkast = BouwkundigelementdetailsoortReferentiedata(
        code="POS",
        naam="Postkast",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Kast voor ontvangst van poststukken. Relatie met IFC codering (IfcFurniture)
    """

    privacyscherm = BouwkundigelementdetailsoortReferentiedata(
        code="PRI",
        naam="Privacyscherm",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Afscheiding bedoeld voor het creëren van privacy. Relatie met IFC codering
    (IfcFurniture)
    """

    raam = BouwkundigelementdetailsoortReferentiedata(
        code="RAA",
        naam="Raam",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Kozijn met glas voor licht en ventilatie. Relatie met IFC codering
    (IfcWindow.WINDOW)
    """

    radiator = BouwkundigelementdetailsoortReferentiedata(
        code="RAD",
        naam="Radiator",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Warmtewisselaar voor verwarming van ruimten. Relatie met IFC codering
    (IfcSpaceHeater.RADIATOR)
    """

    rookmelder = BouwkundigelementdetailsoortReferentiedata(
        code="ROO",
        naam="Rookmelder",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Detectieapparaat voor vroegtijdige waarschuwing bij rookontwikkeling. Relatie met
    IFC codering (IfcSensor.SMOKESENSOR)
    """

    rooster = BouwkundigelementdetailsoortReferentiedata(
        code="RST",
        naam="Rooster",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Geperforeerd paneel voor ventilatie of afdekking. Relatie met IFC codering
    (IfcAirTerminal.GRILLE)
    """

    schoorsteen = BouwkundigelementdetailsoortReferentiedata(
        code="SST",
        naam="Schoorsteen",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Constructie voor afvoer van rook en verbrandingsgassen. Relatie met IFC codering
    (IfcChimney)
    """

    schuifdeur = BouwkundigelementdetailsoortReferentiedata(
        code="SDE",
        naam="Schuifdeur",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Deur die open en dicht gaat door te schuiven. Relatie met IFC codering
    (IfcDoor.DOOR)
    """

    schuifpui = BouwkundigelementdetailsoortReferentiedata(
        code="SPU",
        naam="Schuifpui",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Grote schuifdeur, vaak glas, verbindt binnen met buiten. Relatie met IFC codering
    (IfcWindow.WINDOW)
    """

    trap = BouwkundigelementdetailsoortReferentiedata(
        code="TRA",
        naam="Trap",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Constructie van treden voor verticale verplaatsing. Relatie met IFC codering
    (IfcStair)
    """

    traplift = BouwkundigelementdetailsoortReferentiedata(
        code="TLI",
        naam="Traplift",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Hulpmiddel voor het overbruggen van trappen door mindervaliden. Relatie met IFC
    codering (IfcTransportElement)
    """

    urinoir = BouwkundigelementdetailsoortReferentiedata(
        code="URI",
        naam="Urinoir",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Sanitair voor staand urineren door mannen. Relatie met IFC codering
    (IfcSanitaryTerminal.URINAL)
    """

    ventilatiekap = BouwkundigelementdetailsoortReferentiedata(
        code="VEN",
        naam="Ventilatiekap",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Afzuigkap boven kookplaat, voert kookdampen af. Relatie met IFC codering
    (IfcStackTerminal.COWL)
    """

    ventilatierooster = BouwkundigelementdetailsoortReferentiedata(
        code="VRO",
        naam="Ventilatierooster",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Opening in muur of raam voor luchttoe- of afvoer. Relatie met IFC codering
    (IfcAirTerminal.DIFFUSER)
    """

    vliesgevel = BouwkundigelementdetailsoortReferentiedata(
        code="VLI",
        naam="Vliesgevel",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Lichtgewicht gevelsysteem, veelal van glas. Relatie met IFC codering
    (IfcCurtainWall)
    """

    vlizotrap = BouwkundigelementdetailsoortReferentiedata(
        code="VTR",
        naam="Vlizotrap",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Opvouwbare trap naar zolder of vliering. Relatie met IFC codering (IfcStair)
    """

    vloer = BouwkundigelementdetailsoortReferentiedata(
        code="VLO",
        naam="Vloer",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Horizontaal steunelement, scheidt verschillende verdiepingen. Relatie met IFC
    codering (IfcSlab.FLOOR)
    """

    wand = BouwkundigelementdetailsoortReferentiedata(
        code="WAN",
        naam="Wand",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Verticaal scheidend element in bouwkundige constructies. Relatie met IFC codering
    (IfcWallStandardCase)
    """

    warmtepomp = BouwkundigelementdetailsoortReferentiedata(
        code="WAR",
        naam="Warmtepomp",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Apparaat dat warmte verplaatst voor verwarming of koeling. Relatie met IFC codering
    (IfcPump)
    """

    warmteterugwinning_apparaat = BouwkundigelementdetailsoortReferentiedata(
        code="WTE",
        naam="Warmteterugwinning apparaat",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Systeem dat warmte uit afvoerlucht hergebruikt voor energie-efficiëntie. Relatie met
    IFC codering (IfcAirToAirHeatRecovery)
    """

    wastafel = BouwkundigelementdetailsoortReferentiedata(
        code="WAS",
        naam="Wastafel",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Sanitair voor handen wassen en persoonlijke verzorging. Relatie met IFC codering
    (IfcSanitaryTerminal.WASHHANDBASIN)
    """

    zonnepaneel = BouwkundigelementdetailsoortReferentiedata(
        code="ZPA",
        naam="Zonnepaneel",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Apparaat dat zonlicht omzet in elektriciteit. Relatie met IFC codering
    (IfcSolarDevice)
    """

    zonwering = BouwkundigelementdetailsoortReferentiedata(
        code="ZON",
        naam="Zonwering",
        parent=Bouwkundigelementsoort.voorziening,
    )
    """
    Extern of intern systeem om zonlicht en warmte te reguleren. Relatie met IFC
    codering (IfcShadingDevice)
    """

    afvoer = BouwkundigelementdetailsoortReferentiedata(
        code="AFV",
        naam="Afvoer",
        parent=Bouwkundigelementsoort.voorziening,
    )

    balustrades_en_leuningen = BouwkundigelementdetailsoortReferentiedata(
        code="BAL",
        naam="Balustrades en leuningen",
        parent=Bouwkundigelementsoort.voorziening,
    )

    beveiliging = BouwkundigelementdetailsoortReferentiedata(
        code="BEV",
        naam="Beveiliging",
        parent=Bouwkundigelementsoort.voorziening,
    )

    binnenwandafwerking = BouwkundigelementdetailsoortReferentiedata(
        code="BIA",
        naam="Binnenwandafwerking",
        parent=Bouwkundigelementsoort.voorziening,
    )

    bidet = BouwkundigelementdetailsoortReferentiedata(
        code="BID",
        naam="Bidet",
        parent=Bouwkundigelementsoort.voorziening,
    )

    binnenwanden = BouwkundigelementdetailsoortReferentiedata(
        code="BIN",
        naam="Binnenwanden",
        parent=Bouwkundigelementsoort.voorziening,
    )

    binnenwandopeningen = BouwkundigelementdetailsoortReferentiedata(
        code="BIW",
        naam="Binnenwandopeningen",
        parent=Bouwkundigelementsoort.voorziening,
    )

    buitenwandafwerking = BouwkundigelementdetailsoortReferentiedata(
        code="BUA",
        naam="Buitenwandafwerking",
        parent=Bouwkundigelementsoort.voorziening,
    )

    buitenwanden = BouwkundigelementdetailsoortReferentiedata(
        code="BUI",
        naam="Buitenwanden",
        parent=Bouwkundigelementsoort.voorziening,
    )

    buitenwandopeningen = BouwkundigelementdetailsoortReferentiedata(
        code="BUW",
        naam="Buitenwandopeningen",
        parent=Bouwkundigelementsoort.voorziening,
    )

    communicatie = BouwkundigelementdetailsoortReferentiedata(
        code="COM",
        naam="Communicatie",
        parent=Bouwkundigelementsoort.voorziening,
    )

    dakbedekking = BouwkundigelementdetailsoortReferentiedata(
        code="DBE",
        naam="Dakbedekking",
        parent=Bouwkundigelementsoort.voorziening,
    )

    dakopeningen = BouwkundigelementdetailsoortReferentiedata(
        code="DOP",
        naam="Dakopeningen",
        parent=Bouwkundigelementsoort.voorziening,
    )

    elektra = BouwkundigelementdetailsoortReferentiedata(
        code="ELE",
        naam="Elektra",
        parent=Bouwkundigelementsoort.voorziening,
    )

    gas = BouwkundigelementdetailsoortReferentiedata(
        code="GAS",
        naam="Gas",
        parent=Bouwkundigelementsoort.voorziening,
    )

    keukenvoorzieningen = BouwkundigelementdetailsoortReferentiedata(
        code="KEU",
        naam="Keukenvoorzieningen",
        parent=Bouwkundigelementsoort.voorziening,
    )

    lavet = BouwkundigelementdetailsoortReferentiedata(
        code="LAV",
        naam="Lavet",
        parent=Bouwkundigelementsoort.voorziening,
    )

    losse_opslaginventaris = BouwkundigelementdetailsoortReferentiedata(
        code="LOS",
        naam="Losse opslaginventaris",
        parent=Bouwkundigelementsoort.voorziening,
    )

    plafondafwerking = BouwkundigelementdetailsoortReferentiedata(
        code="PAF",
        naam="Plafondafwerking",
        parent=Bouwkundigelementsoort.voorziening,
    )

    sanitaire_voorzieningen = BouwkundigelementdetailsoortReferentiedata(
        code="SAN",
        naam="Sanitaire voorzieningen",
        parent=Bouwkundigelementsoort.voorziening,
    )

    schilderwerk = BouwkundigelementdetailsoortReferentiedata(
        code="SCH",
        naam="Schilderwerk",
        parent=Bouwkundigelementsoort.voorziening,
    )

    terrein = BouwkundigelementdetailsoortReferentiedata(
        code="TER",
        naam="Terrein",
        parent=Bouwkundigelementsoort.voorziening,
    )

    trap_en_hellingafwerking = BouwkundigelementdetailsoortReferentiedata(
        code="THA",
        naam="Trap- en hellingafwerking",
        parent=Bouwkundigelementsoort.voorziening,
    )

    vloerafwerking = BouwkundigelementdetailsoortReferentiedata(
        code="VAF",
        naam="Vloerafwerking",
        parent=Bouwkundigelementsoort.voorziening,
    )

    verwarmingsonderdelen = BouwkundigelementdetailsoortReferentiedata(
        code="VEO",
        naam="Verwarmingsonderdelen",
        parent=Bouwkundigelementsoort.voorziening,
    )

    verlichting = BouwkundigelementdetailsoortReferentiedata(
        code="VER",
        naam="Verlichting",
        parent=Bouwkundigelementsoort.voorziening,
    )

    vloeropeningen = BouwkundigelementdetailsoortReferentiedata(
        code="VOP",
        naam="Vloeropeningen",
        parent=Bouwkundigelementsoort.voorziening,
    )

    verwarmingstoestellen = BouwkundigelementdetailsoortReferentiedata(
        code="VTO",
        naam="Verwarmingstoestellen",
        parent=Bouwkundigelementsoort.voorziening,
    )

    waterleiding_en_of_hoofdkraan = BouwkundigelementdetailsoortReferentiedata(
        code="WAT",
        naam="Waterleiding/hoofdkraan",
        parent=Bouwkundigelementsoort.voorziening,
    )
