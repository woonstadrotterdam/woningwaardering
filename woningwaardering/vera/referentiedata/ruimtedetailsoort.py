from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Ruimtedetailsoort(Enum):
    atrium_en_of_patio = Referentiedata(
        code="ATR",
        naam="Atrium / Patio",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Niet overdekt atrium of patio
    """

    achtertuin = Referentiedata(
        code="ATU",
        naam="Achtertuin",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: tuim gelegen aan de achterzijde van de woning. Deze waarde kan
    gebruikt worden voor de woningwaardering indien deze duiding van tuin bekend is.
    """

    badkamer = Referentiedata(
        code="BAD",
        naam="Badkamer",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Vertrek: voor een sanitaire ruimte in een woning, dat wil zeggen een ruimte die
    speciaal is ingericht voor lichaamsverzorging. Een badkamer moet voldoen aan: en
    waterdichte vloerafwerking, De ruimte heeft over ten minste 50% van de
    oppervlakte een vrije hoogte van 2,00 m (gemeten vanaf de vloer tot het
    zichtbare plafond), Waterdichte afwerking tot 1,50 m hoogte voor badruimte en
    1,80 m voor doucheruimte, Een wastafel inclusief (tweehands-)mengkraan en een
    spiegel, Een douche of bad met aansluitpunten voor warm en koud water (niet
    zijnde een warmwaterapparaat) en voorzien van een warm- en koudwaterkraan of een
    mengkraan. Een bad in een vertrek met een niet-waterdichte vloer wordt door de
    Huurcommissie wel gewaardeerd, omdat het bad zelf als een waterdichte afwerking
    wordt gezien.
    """

    balkon = Referentiedata(
        code="BAL",
        naam="Balkon",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Een balkon.
    """

    badkamer_met_toilet = Referentiedata(
        code="BAT",
        naam="Badkamer met toilet",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Gecombineerde badkamer/toilet
    """

    berging = Referentiedata(
        code="BER",
        naam="Berging",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Berging voor eigen gebruik, overige ruimte
    """

    bijkeuken = Referentiedata(
        code="BIJ",
        naam="Bijkeuken",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Overige ruimte: grenzend aan de eigenlijke keuken die voor ondersteunende
    huishoudelijke handelingen gebruikt wordt, zoals wassen, drogen en strijken,
    maar ook voor het opbergen en bewaren van (etens)voorraden en schoonmaakspullen.
    """

    dakterras = Referentiedata(
        code="DAK",
        naam="Dakterras",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Een dakterras.
    """

    gemeenschappelijk_dakterras_gak = Referentiedata(
        code="GAK",
        naam="Gemeenschappelijk dakterras",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: een gemeenschappelijk dakterras
    """

    doucheruimte = Referentiedata(
        code="DOU",
        naam="Doucheruimte",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Vertrek: sanitaire ruimte met een douche.
    """

    gang = Referentiedata(
        code="GAN",
        naam="Gang",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Ruimte : is een betrekkelijk smalle en lange ruimte omgeven door muren en afgedekt
    door een plafond of zoldering, in een gebouw, als verbinding van vertrekken
    waarvan de deuren erop uitkomen.
    """

    gemeenschappelijke_parkeerruimte_niet_specifieke_plek = Referentiedata(
        code="GPN",
        naam="Gemeenschappelijke parkeerruimte niet specifieke plek",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: een afsluitbare gemeenschappelijke parkeerruimte, zonder dak, en
    zonder privé plek. Al dan niet evenveel parkeerplekken als eenheden.
    """

    gemeenschappelijke_parkeerruimte_specifieke_plek = Referentiedata(
        code="GPS",
        naam="Gemeenschappelijke parkeerruimte specifieke plek",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: een afsluitbare gemeenschappelijke parkeerruimte, zonder dak, met
    privé plek.
    """

    gemeenschappelijke_tuin = Referentiedata(
        code="GTU",
        naam="Gemeenschappelijke tuin",
        parent=Referentiedata(
            code="GEM",
            naam="Gemeenschappelijke ruimten en voorzieningen",
        ),
    )

    gemeenschappelijk_dakterras_gda = Referentiedata(
        code="GDA",
        naam="Gemeenschappelijk dakterras",
        parent=Referentiedata(
            code="GEM",
            naam="Gemeenschappelijke ruimten en voorzieningen",
        ),
    )

    hal = Referentiedata(
        code="HAL",
        naam="Hal",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Verkeersruimte bijv. entree, Hal, overloop, speelhal etc.
    """

    kelder = Referentiedata(
        code="KEL",
        naam="Kelder",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Overige ruimte: dat gedeelte van een gebouw dat onder de grond (onder het maaiveld)
    is gelegen.
    """

    keuken = Referentiedata(
        code="KEU",
        naam="Keuken",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Vertrek of plaats in een gebouw waarin mensen hun voedsel bereiden of laten bereiden
    """

    overige_ruimte = Referentiedata(
        code="OBR",
        naam="Overige ruimte",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte die niet nader is gespecifeerd als ruimtedetailsoort. Bijvoorbeeld een
    platje.
    """

    overige_gemeenschappelijke_ruimte_of_voorziening = Referentiedata(
        code="OGR",
        naam="Overige gemeenschappelijke ruimte of voorziening",
        parent=Referentiedata(
            code="GEM",
            naam="Gemeenschappelijke ruimten en voorzieningen",
        ),
    )
    """
    Gemeenschappelijke ruimte of voorziening die niet nader is gespecifeerd als
    ruimtedetailsoort. Bijvoorbeeld gemeenschappelijke hobbyruimte, wasruimte.
    """

    open_parkeergarage_niet_specifieke_plek = Referentiedata(
        code="OPN",
        naam="Open parkeergarage niet specifieke plek",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: een tot het complex behorende open parkeergarage (een open ruimte, dus
    geen wanden maar wel een dak, bijvoorbeeld onder een complex appartementen)
    zonder een specifiek toegewezen parkeerplaats.
    """

    open_parkeergarage_specifieke_plek = Referentiedata(
        code="OPS",
        naam="Open parkeergarage specifieke plek",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: een tot het complex behorende open parkeergarage (een open ruimte, dus
    geen wanden maar wel een dak, bijvoorbeeld onder een complex appartementen) met
    voor elke woning een specifiek toegewezen parkeerplaats.
    """

    overig_vertrek = Referentiedata(
        code="OVT",
        naam="Overig vertrek",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Vertrek dat niet nader gespecifeerd is als ruimtedetailsoort. Bijvoorbeeld eetkamer,
    hobbykamer, studeerkamer etc.
    """

    parkeerplaats = Referentiedata(
        code="PAR",
        naam="Parkeerplaats",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Eigen parkeerplaats of oprit bij de woning
    """

    parkeergarage_niet_specifieke_plek = Referentiedata(
        code="PNS",
        naam="Parkeergarage niet specifieke plek",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Overige ruimte: een gesloten parkeergarage met voor elke woning een, al dan niet
    afgebakende, parkeerplaats (alle betrokken huurders moeten  op elk moment van de
    dag kunnen parkeren).
    """

    parkeergarage_specifieke_plek = Referentiedata(
        code="PSP",
        naam="Parkeergarage specifieke plek",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Overige ruimte: een gesloten parkeergarage (bijvoorbeeld in de onderbouw van een
    appartementencomplex) met een specifiek tot de woning behorende, afgebakende
    parkeerplaats.
    """

    recreatieruimte = Referentiedata(
        code="REC",
        naam="Recreatieruimte",
        parent=Referentiedata(
            code="GEM",
            naam="Gemeenschappelijke ruimten en voorzieningen",
        ),
    )
    """
    Een ruimte binnen de eenheid die recreatie als gebruiksdoel heeft. Bijvoorbeeld
    binnen een zorginstelling.
    """

    tuin_rondom = Referentiedata(
        code="RON",
        naam="Tuin Rondom",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: tuin gelegen rondom de eenheid. Deze waarde kan gebruikt worden voor
    de woningwaardering indien deze duiding van tuin bekend is.
    """

    schuur = Referentiedata(
        code="SCH",
        naam="Schuur",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Buitenruimte: veelal vrijstaand gebouw, dat gebruikt wordt om goederen of voedsel in
    op te slaan, en ook als werkruimte kan dienen, maar niet als woning bedoeld is.
    """

    serre = Referentiedata(
        code="SER",
        naam="Serre",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Vertrek: glazen veranda verbonden aan een woning.
    """

    slaapkamer = Referentiedata(
        code="SLA",
        naam="Slaapkamer",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Vertrek: ruimte in een woning waarin men kan slapen.
    """

    terras = Referentiedata(
        code="TER",
        naam="Terras",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: deel van een buitenruimte met een vlakke oppervlakte die wordt
    gebruikt om op te zitten, te eten, te drinken of andere activiteiten te doen.
    """

    toiletruimte = Referentiedata(
        code="TOI",
        naam="Toiletruimte",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Overige ruimte: Sanitaire ruimte met een toilet.
    """

    tuin = Referentiedata(
        code="TUI",
        naam="Tuin",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: indien geen specificatie/verbijzondering bekend is van tuin kan voor
    deze algemenere duiding van tuin gebruikt worden.
    """

    tussenkamer = Referentiedata(
        code="TUS",
        naam="Tussenkamer",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Vertrek: ruimte gelegen tussen en verbonden met twee andere kamers.
    """

    vliering = Referentiedata(
        code="VLI",
        naam="Vliering",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Overige ruimte: een meestal niet of beperkt afgewerkte opslagruimte onder het dak,
    die alleen bereikbaar is met een vlizotrap en die niet altijd hoog genoeg is om
    rechtop te kunnen staan.
    """

    voortuin = Referentiedata(
        code="VTU",
        naam="Voortuin",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: tuin gelegen voor de voorgevellijn, waar meestal de voordeur van een
    woning is gelegen. Deze waarde kan gebruikt worden voor de woningwaardering
    indien deze duiding van tuin bekend is.
    """

    wasruimte = Referentiedata(
        code="WAS",
        naam="Wasruimte",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Overige ruimte: Specifieke ruimte voor wasmachine, droger, strijken, voor eigen
    gebruik.
    """

    woonkamer_en_of_keuken = Referentiedata(
        code="WOK",
        naam="Woonkamer/keuken",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Vertrek: ruimte met een gecombineerde functie van keuken en woonkamer
    """

    woonkamer = Referentiedata(
        code="WOO",
        naam="Woonkamer",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Vertrek: de kamer in een huis waar het dagelijkse gezinsleven zich afspeelt. Het is
    een van de grootste vertrekken en bevindt zich meestal op de begane grond, voor
    zover het niet gaat om een appartement in een flat.
    """

    woon_en_of_slaapkamer = Referentiedata(
        code="WSL",
        naam="Woon-/slaapkamer",
        parent=Referentiedata(
            code="VTK",
            naam="Vertrek",
        ),
    )
    """
    Vertrek: ruimte met een gecombineerde functie van woonkamer en slaapkamer.
    """

    zijtuin = Referentiedata(
        code="ZIJ",
        naam="Zijtuin",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: tuin gelegen aan de zijkant van een woning. Deze waarde kan gebruikt
    worden voor de woningwaardering indien deze duiding van tuin bekend is.
    """

    loggia = Referentiedata(
        code="LOG",
        naam="Loggia",
        parent=Referentiedata(
            code="BTR",
            naam="Buitenruimte",
        ),
    )
    """
    Buitenruimte: een inpandig balkon.
    """

    zolder = Referentiedata(
        code="ZOL",
        naam="Zolder",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Overige ruimte: is de bovenste verdieping direct onder het dak van een gebouw met
    een vaste trap zoals gedefinieerd voor het bepalen van de woningwaardering. De
    term wordt vooral gebruikt bij gebouwen met een puntdak. De bovenste verdieping
    van een gebouw met plat dak wordt meestal geen zolder genoemd. Een ruimte mag
    als vertrek worden gezien indien deze een vast trap heeft, de vloer begaanbaar
    en het dak beschoten is. Zolders zonder vaste trap leggen we niet vast als
    vertrek. Indien een woning een zolder heeft met een vlizotrap kan dit in de
    advertentietekst worden gemeld.
    """

    overloop = Referentiedata(
        code="OVL",
        naam="Overloop",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Verkeersruimte: (UITBREIDING) Gang op een bovenverdieping.
    """

    entree = Referentiedata(
        code="ENT",
        naam="Entree",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Verkeersruimte: (UITBREIDING) Ingang van een gebouw.
    """

    kast = Referentiedata(
        code="KAS",
        naam="Kast",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Overige ruimte: (UITBREIDING)
    """

    trappenhuis = Referentiedata(
        code="TRH",
        naam="Trappenhuis",
        parent=Referentiedata(
            code="OVR",
            naam="Overige ruimten",
        ),
    )
    """
    Verkeersruimte: (UITBREIDING) Verkeersruimte waarin een trap ligt
    """

    carport = Referentiedata(
        code="CAR",
        naam="Carport",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Parkeergelegenheid: een overdekte, open parkeerruimte voor een of meer auto's. In
    tegenstelling tot een garage heeft een carport meestal geen muren of deuren.
    Carports kunnen vrijstaand zijn of aan een gebouw bevestigd worden. Onder
    carport vallen ook ander soortige overdekte (buiten) parkeervakken, zoals die in
    de plint (begane grond) van een appartementencomplex.
    """

    garage_inpandig = Referentiedata(
        code="GAI",
        naam="Garage inpandig",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Parkeergelegenheid: een garage die deel uitmaakt van de hoofdbebouwing van een huis
    of ander gebouw. Deze ruimte is meestal direct toegankelijk vanuit het interieur
    van het gebouw, bijvoorbeeld via een deur die leidt naar een gang, keuken, of
    bijkeuken. De garage is voorzien van een garagedeur die naar buiten opent.
    """

    garage_uitpandig = Referentiedata(
        code="GAU",
        naam="Garage uitpandig",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een uitpandige garage is een garage die geen deel uitmaakt van de hoofdbebouwing van
    een huis of ander gebouw. Deze ruimte is niet direct toegankelijk vanuit het
    interieur van het gebouw. De uitpandige garage is via de oprijlaan van de
    woonruimte te bereiken en daarom betreft het een aanhorigheid van de woonruimte.
    De garage is voorzien van een garagedeur die naar buiten opent.
    """

    garagebox = Referentiedata(
        code="GAR",
        naam="Garagebox",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een garagebox is een afgesloten, individuele ruimte bedoeld voor het stallen van een
    voertuig of het opslaan van goederen. Garageboxen zijn voorzien van een
    garagedeur die op slot kan, vaak een kanteldeur of een roldeur. Deze boxen
    kunnen losstaand zijn of deel uitmaken van een groter complex met meerdere
    garageboxen. Een garagebox is een afzonderlijk object van een woonruimte als het
    een vrijstaande garagebox is die middels een afzonderlijk terrein bereikbaar is
    of als het een garagebox is die in de plint (begane grond) van een
    appartementencomplex zit.
    """

    parkeergarage = Referentiedata(
        code="PAG",
        naam="Parkeergarage",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een parkeergarage is een gebouwde parkeervoorziening met meerdere parkeerplaatsen,
    soms verdeeld over meerdere verdiepingen en kan zowel bovengronds als
    ondergronds (parkeerkelder) zijn.
    """

    parkeerterrein = Referentiedata(
        code="PAT",
        naam="Parkeerterrein",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een parkeerterrein is een open, meestal verharde locatie die speciaal is ingericht
    voor het parkeren van voertuigen.
    """

    parkeervak_auto_binnen = Referentiedata(
        code="VAI",
        naam="Parkeervak auto (binnen)",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een parkeervak auto (binnen) is een specifieke, afgebakende ruimte binnen een
    gebouw, zoals een parkeergarage waarin een voertuig kan worden geparkeerd. Deze
    parkeervakken zijn genummerd of gemarkeerd om een georganiseerde indeling te
    waarborgen. Ze zijn bedoeld voor motorvoertuigen met meer dan twee wielen, zoals
    auto's.
    """

    parkeervak_auto_buiten_niet_overdekt = Referentiedata(
        code="VAU",
        naam="Parkeervak auto (buiten, niet overdekt)",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een parkeervak auto (buiten, niet overdekt) is een specifieke, afgebakende ruimte
    buiten een gebouw, zoals een parkeerterrein waar een voertuig kan worden
    geparkeerd. Deze parkeervakken zijn genummerd of gemarkeerd om een
    georganiseerde indeling te waarborgen. Ze zijn bedoeld voor motorvoertuigen met
    meer dan twee wielen, zoals auto's.
    """

    parkeervak_motorfiets_binnen = Referentiedata(
        code="VMI",
        naam="Parkeervak motorfiets (binnen)",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een parkeervak motorfiets (binnen) is een specifieke, afgebakende ruimte binnen een
    gebouw, zoals een parkeergarage waarin een motorfiets kan worden geparkeerd.
    Deze parkeerplaatsen zijn genummerd of gemarkeerd om een georganiseerde indeling
    te waarborgen. Ze zijn bedoeld voor motorfietsen met twee wielen. Deze
    parkeerplaatsen zijn meestal kleiner dan gewone parkeerplaatsen voor auto's.
    """

    parkeervak_motorfiets_buiten_niet_overdekt = Referentiedata(
        code="VMU",
        naam="Parkeervak motorfiets (buiten, niet overdekt)",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een parkeervak motorfiets (buiten, niet overdekt) is een specifieke, afgebakende
    ruimte buiten een gebouw, zoals een parkeerterrein waar een motorfiets kan
    worden geparkeerd. Deze parkeerplaatsen zijn genummerd of gemarkeerd om een
    georganiseerde indeling te waarborgen. Ze zijn bedoeld voor motorfietsen met
    twee wielen. Deze parkeerplaatsen zijn meestal kleiner dan gewone
    parkeerplaatsen voor auto's.
    """

    parkeervak_scootmobiel_binnen = Referentiedata(
        code="VSI",
        naam="Parkeervak scootmobiel (binnen)",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een parkeervak scootmobiel (binnen) is een specifieke, afgebakende ruimte binnen een
    gebouw, waarin een scootmobiel kan worden geparkeerd. Deze parkeerplaatsen zijn
    genummerd of gemarkeerd om een georganiseerde indeling te waarborgen. Ze zijn
    uitsluitend bedoeld voor het stallen van scootmobiels en bijvoorbeeld dus niet
    voor elektrische fietsen.
    """

    parkeervak_scootmobiel_buiten = Referentiedata(
        code="VSU",
        naam="Parkeervak scootmobiel (buiten)",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een parkeervak scootmobiel (buiten) is een specifieke, afgebakende ruimte buiten een
    gebouw, waarin een scootmobiel kan worden geparkeerd. Deze parkeerplaatsen zijn
    genummerd of gemarkeerd om een georganiseerde indeling te waarborgen. Ze zijn
    uitsluitend bedoeld voor het stallen van scootmobiels en bijvoorbeeld dus niet
    voor elektrische fietsen.
    """

    stalling_extern = Referentiedata(
        code="STE",
        naam="Stalling extern",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een stalling extern is een al dan niet overdekte of afgesloten ruimte buiten het
    hoofdgebouw die bedoeld is voor het parkeren of opslaan van fietsen of
    scootmobielen.
    """

    stalling_intern = Referentiedata(
        code="STI",
        naam="Stalling intern",
        parent=Referentiedata(
            code="PAR",
            naam="Parkeergelegenheid",
        ),
    )
    """
    Een stalling intern is een overdekte en afgesloten ruimte binnen het hoofdgebouw die
    bedoeld is voor het parkeren of opslaan van fietsen of scootmobielen.
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
