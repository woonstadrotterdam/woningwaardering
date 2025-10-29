from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.eenheidsoort import (
    Eenheidsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheiddetailsoortReferentiedata(Referentiedata):
    pass


class Eenheiddetailsoort(Referentiedatasoort):
    antenne_opstelplaats = EenheiddetailsoortReferentiedata(
        code="ANT",
        naam="Antenne-opstelplaats",
        parent=Eenheidsoort.overig,
    )

    atelierruimte = EenheiddetailsoortReferentiedata(
        code="ATE",
        naam="Atelierruimte",
        parent=Eenheidsoort.bedrijfsruimte,
    )
    """
    Een atelier is een werkplaats, in het bijzonder die van een beeldend kunstenaar.
    """

    basisschool = EenheiddetailsoortReferentiedata(
        code="BAS",
        naam="Basisschool",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Basisschool conform: art. 49 lid 2a
    """

    benedenwoning = EenheiddetailsoortReferentiedata(
        code="BEN",
        naam="Benedenwoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een benedenwoning is een etagewoning of flatwoning op de begane grond met een
    voordeur die op straat uitkomt. De benedenwoning bestaat uit één of meerdere
    bouwlagen. (Voor marktwaarde bepaling: MGW-meergezinswoning)
    """

    berging = EenheiddetailsoortReferentiedata(
        code="BER",
        naam="Berging",
        parent=Eenheidsoort.overig,
    )
    """
    Een berging is een bergruimte of bijgebouw met een algemene bergfunctie op een apart
    perceel of met een eigen adres, vaak in een aaneengesloten rij met andere
    berghokken of bijgebouwen.
    """

    bibliotheek = EenheiddetailsoortReferentiedata(
        code="BIB",
        naam="Bibliotheek",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Dorps- of wijkbibliotheek
    """

    bijeenkomstruimte = EenheiddetailsoortReferentiedata(
        code="BIJ",
        naam="Bijeenkomstruimte",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Ruimte voor het samenkomen van personen voor kunst, cultuur, godsdienst,
    communicatie, het verstrekken van consumpties voor het gebruik ter plaatse of
    het aanschouwen van sport (bewerking van defintie Bouwbesluit). Let op: Voor
    kinderopvang kan de eenheiddetailsoort Kinderopvanglocatie worden gebruikt.
    """

    bouwkavel = EenheiddetailsoortReferentiedata(
        code="BOU",
        naam="Bouwkavel",
        parent=Eenheidsoort.overig,
    )
    """
    Een aaneengesloten terreinoppervlak, waarop krachtens het bestemmingsplan een
    zelfstandige, bij elkaar behorende bebouwing is toegestaan.
    """

    bovenwoning = EenheiddetailsoortReferentiedata(
        code="BOV",
        naam="Bovenwoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een bovenwoning is een etagewoning of flatwoning op een etage die bereikbaar is via
    een binnentrap met een mogelijk gemeenschappelijke voordeur die op straat
    uitkomt of een eigen voordeur heeft die niet in een portiek uitkomt. De
    bovenwoning bestaat uit één of meerdere bouwlagen. De flat-bovenwoning (ook wel:
    repeterende bovenwoning) is geen galerijflat. (Voor marktwaarde bepaling:
    MGW-meergezinswoning)
    """

    brede_school = EenheiddetailsoortReferentiedata(
        code="BRE",
        naam="Brede school",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Brede school met bijv. peuterzaal, kinderopvang, voor-, tussen- en naschoolse
    opvang, buurtsporthal, en -complex (zogeheten multifunctionele accommodaties)
    """

    buurthuis = EenheiddetailsoortReferentiedata(
        code="BUU",
        naam="Buurthuis",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Openbaar gebouw in een woonkern dat dienst doet als centrum voor maatschappelijk
    werk in en voor de buurt
    """

    centrum_voor_jeugd_en_gezin = EenheiddetailsoortReferentiedata(
        code="CJG",
        naam="Centrum voor Jeugd en Gezin",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Centrum voor jeugd en gezin conform: art. 49 lid 2a
    """

    corridorflat = EenheiddetailsoortReferentiedata(
        code="COR",
        naam="Corridorflat",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een corridorflat is een flatwoning waarbij de voordeur uitkomt op een centraal
    binnen de bouwmassa per etage gelegen loopgang dan wel op een centrale hal op de
    etage. (Voor marktwaarde bepaling: MGW-meergezinswoning)
    """

    cultuur_ruimte = EenheiddetailsoortReferentiedata(
        code="CUL",
        naam="Cultuur ruimte",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Ruimten voor kleinschalige culturele activiteiten
    """

    dagbestedingsruimte = EenheiddetailsoortReferentiedata(
        code="DAG",
        naam="Dagbestedingsruimte",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Ruimte voor dagbesteding van gehandicapten of ouderen, incl. enige
    zorginfrastructuur, die inpandig in een woonzorggebouw zijn gelegen
    """

    eindwoning = EenheiddetailsoortReferentiedata(
        code="EIN",
        naam="Eindwoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een eindwoning is een eengezinswoning die grenst aan een aanliggende woning. De
    eindwoning ligt op het begin of einde van de reeks woningen en heeft geen
    (extra) bij de woning behorende grond aan de zijkant van de woning. (Voor
    marktwaarde bepaling: EGW-eengezinswoning)
    """

    erfpachtkavel = EenheiddetailsoortReferentiedata(
        code="EPK",
        naam="Erfpachtkavel",
        parent=Eenheidsoort.overig,
    )
    """
    Kavels die gepacht zijn danwel verpacht worden
    """

    fietsparkeerplaats_en_of_stalling = EenheiddetailsoortReferentiedata(
        code="FIE",
        naam="Fietsparkeerplaats/stalling",
        parent=Eenheidsoort.overig,
    )

    galerijflat = EenheiddetailsoortReferentiedata(
        code="GAL",
        naam="Galerijflat",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een galerijflat is een flatwoning waarbij de voordeur uitkomt op een aan de
    buitenkant gelegen loopgang. Een galerijflat heeft meerdere bouwlagen met
    woningen boven elkaar. (Voor marktwaarde bepaling: MGW-meergezinswoning)
    """

    garage = EenheiddetailsoortReferentiedata(
        code="GAR",
        naam="Garage",
        parent=Eenheidsoort.parkeergelegenheid,
    )
    """
    Een garage is een overdekte stallingruimte bestemd en geschikt voor motorvoertuigen
    op meer dan twee wielen.
    """

    gemeenschapscentrum = EenheiddetailsoortReferentiedata(
        code="GEM",
        naam="Gemeenschapscentrum",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Culturele infrastructuur door de gemeente beheerd met het oog op
    cultuurparticipatie, gemeenschapsvorming en cultuurspreiding ten behoeve van de
    lokale bevolking en met bijzondere aandacht voor de culturele diversiteit.
    """

    geschakelde_twee_onder_een_kapwoning = EenheiddetailsoortReferentiedata(
        code="GTW",
        naam="Geschakelde Twee-onder-een-kapwoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een geschakelde 2-onder-1-kapwoning is een 2-onder-1-kapwoning waarbij de muren van
    aanbouwen gedeeltelijk aan (aanbouwen van) andere woningen grenzen. Ook wanneer
    de woningen elk een afzonderlijke dakconstructie hebben, vallen deze onder de
    definitie van de geschakelde 2-onder-1-kapwoning. (Voor marktwaarde bepaling:
    EGW-eengezinswoning)
    """

    geschakelde_woning = EenheiddetailsoortReferentiedata(
        code="GWO",
        naam="Geschakelde woning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een geschakelde woning is een eengezinswoning waarbij de muren of muren van
    aanbouwen gedeeltelijk aan (aanbouwen van) andere woningen grenzen. (Voor
    marktwaarde bepaling: EGW-eengezinswoning)
    """

    half_vrijstaande_woning = EenheiddetailsoortReferentiedata(
        code="HAL",
        naam="Half vrijstaande woning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een halfvrijstaande woning is een eengezinswoning waarvan het hoofdgebouw verbonden
    is met het hoofdgebouw van één ander object dat geen woning is: óf waarvan het
    hoofdgebouw verbonden is met het hoofdgebouw van één andere niet gelijksoortige
    en -vormige woning (niet zijnde tussenwoning en niet zijnde een
    2-onder-1-kapwoning). (Voor marktwaarde bepaling: EGW-eengezinswoning)
    """

    herenhuis = EenheiddetailsoortReferentiedata(
        code="HER",
        naam="Herenhuis",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een herenhuis is een relatief grote eengezinswoning gesitueerd binnen de bebouwde
    kom, met een nadrukkelijke architectonische uitstraling in het straatbeeld via
    een opvallende (gevel)presentatie. Oorspronkelijk betrof het een statig, hoog en
    tamelijk oud pand, maar tegenwoordig wordt hiermee ook de duurdere, kwalitatief
    beter uitgevoerde nieuwbouwwoning aangeduid.
    """

    hoekwoning = EenheiddetailsoortReferentiedata(
        code="HOE",
        naam="Hoekwoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een hoekwoning is een eengezinswoning die grenst aan een aanliggende woning. De
    hoekwoning ligt op het begin of einde van de reeks woningen en heeft (extra) bij
    de woning behorende grond aan de zijkant van de woning. (Voor marktwaarde
    bepaling: EGW-eengezinswoning)
    """

    horeca = EenheiddetailsoortReferentiedata(
        code="HOR",
        naam="Horeca",
        parent=Eenheidsoort.bedrijfsruimte,
    )

    hospice = EenheiddetailsoortReferentiedata(
        code="HOS",
        naam="Hospice",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Woongelegenheid voor personen die niet meer kunnen genezen.
    """

    jongerencentrum = EenheiddetailsoortReferentiedata(
        code="JON",
        naam="Jongerencentrum",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Jongerencentrum, mits zonder horecavoorziening
    """

    kamer = EenheiddetailsoortReferentiedata(
        code="KAM",
        naam="Kamer",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Onzelfstandige woonruimte. Een kamer heeft geen eigen toegang of deelt de keuken of
    toilet met de bewoners van andere woningen/kamers.
    """

    kantoorruimte = EenheiddetailsoortReferentiedata(
        code="KAN",
        naam="Kantoorruimte",
        parent=Eenheidsoort.bedrijfsruimte,
    )
    """
    Kantoorruimte, vallend onder Bedrijfsmatig vastgoed. Let op: gebruik voor
    kantoorruimte van een toegelaten instelling eenheiddetailssoort KTI.
    """

    kangoeroewoning = EenheiddetailsoortReferentiedata(
        code="KNG",
        naam="Kangoeroewoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een kangoeroewoning is een type huisvesting dat is ontworpen om twee of meer
    generaties van een familie samen te laten wonen, maar wel met behoud van privacy
    en onafhankelijkheid. In een kangoeroewoning heeft elke generatie of familie een
    aparte woonruimte binnen hetzelfde huis, maar ze delen wel bepaalde
    gemeenschappelijke ruimten zoals de keuken, eetkamer, tuin, en soms zelfs een
    woonkamer.
    """

    kinderopvanglocatie = EenheiddetailsoortReferentiedata(
        code="KIN",
        naam="Kinderopvanglocatie",
        parent=Eenheidsoort.bedrijfsruimte,
    )
    """
    Hieronder vallen kinderdagverblijven, peuterspeelzalen, buitenschoolse of
    24-uursopvang (Bouwbesluit 2012)
    """

    kantoorruimte_van_toegelaten_instelling = EenheiddetailsoortReferentiedata(
        code="KTI",
        naam="Kantoorruimte van toegelaten instelling",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Kantoorruimte van toegelaten instelling, als zodanig vallend onder Maatschappelijk
    vastgoed (MOG).
    """

    lichamelijk_beperkten_instelling = EenheiddetailsoortReferentiedata(
        code="LGI",
        naam="Lichamelijk beperkten instelling",
        parent=Eenheidsoort.intramuraal_zorgvastgoed,
    )
    """
    Instelling voor mensen met een lichamelijke beperking.
    """

    ligplaats = EenheiddetailsoortReferentiedata(
        code="LIG",
        naam="Ligplaats",
        parent=Eenheidsoort.overig,
    )
    """
    Een ligplaats is een formeel door de gemeente als zodanig aangewezen plaats in het
    water, al dan niet aangevuld met een op de oever aanwezig terrein of een
    gedeelte daarvan, dat bestemd is voor het permanent afmeren van een voor woon,
    bedrijfsmatige of recreatieve doeleinden geschikt vaartuig.
    """

    lichamelijk_en_geestelijk_beperkten_instelling = EenheiddetailsoortReferentiedata(
        code="LVG",
        naam="Lichamelijk en geestelijk beperkten instelling",
        parent=Eenheidsoort.intramuraal_zorgvastgoed,
    )
    """
    Instelling voor mensen met een lichamelijke en/of verstandelijke beperking.
    """

    maatschappelijk_werkruimte_wijk_en_of_buurtgericht = (
        EenheiddetailsoortReferentiedata(
            code="MAA",
            naam="Maatschappelijk werkruimte wijk-/buurtgericht",
            parent=Eenheidsoort.maatschappelijk_vastgoed,
        )
    )
    """
    Ruimte voor op de buurt of wijk gericht maatschappelijk werk door stichtingen of
    verenigingen
    """

    maisonette = EenheiddetailsoortReferentiedata(
        code="MAI",
        naam="Maisonette",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een maisonnette is een specifiek type flatwoning waarbij de woning zelf twee of meer
    bouwlagen heeft. De voordeur komt uit op een gemeenschappelijke loopgang, op een
    gemeenschappelijk afsluitbaar trappenhuis, een centrale hal of gesloten portiek.
    (Voor marktwaarde bepaling: MGW-meergezinswoning)
    """

    multifunctionele_centrum = EenheiddetailsoortReferentiedata(
        code="MUL",
        naam="Multifunctionele centrum",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Multifunctionele centrum voor maatschappelijke dienstverlening
    """

    maatschappelijk_werkruimte_niet_wijk_of_buurtgericht = (
        EenheiddetailsoortReferentiedata(
            code="MWR",
            naam="Maatschappelijk werkruimte niet-wijk- of buurtgericht",
            parent=Eenheidsoort.maatschappelijk_vastgoed,
        )
    )
    """
    Ruimten voor niet op de buurt of wijk gericht maatschappelijk werk door stichtingen
    of verenigingen
    """

    opvangcentrum = EenheiddetailsoortReferentiedata(
        code="OPV",
        naam="Opvangcentrum",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Opvangcentrum (blijf-van-mijn-lijfhuizen, dag- en nachtopvang voor dak- en
    thuislozen en verslaafden)
    """

    parkeerplaats_motor = EenheiddetailsoortReferentiedata(
        code="PAM",
        naam="Parkeerplaats motor",
        parent=Eenheidsoort.parkeergelegenheid,
    )
    """
    Een parkeerplaats die dienstbaar is aan wonen, waarbij de parkeerplaats een
    zelfstandig object is. Een parkeerplaats in een publieke parkeergarage
    (abonnement e.d.) valt niet onder de definitie.
    """

    parkeerplaats_overdekt = EenheiddetailsoortReferentiedata(
        code="PAO",
        naam="Parkeerplaats overdekt",
        parent=Eenheidsoort.parkeergelegenheid,
    )

    parkeerplaats_auto = EenheiddetailsoortReferentiedata(
        code="PAR",
        naam="Parkeerplaats auto",
        parent=Eenheidsoort.parkeergelegenheid,
    )
    """
    Een parkeerplaats die dienstbaar is aan wonen, waarbij de parkeerplaats een
    zelfstandig object is. Een parkeerplaats in een publieke parkeergarage
    (abonnement e.d.) valt niet onder de definitie.
    """

    portiekflat = EenheiddetailsoortReferentiedata(
        code="POF",
        naam="Portiekflat",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een portiekflat is een flatwoning waarbij de voordeur uitkomt op een
    gemeenschappelijk afsluitbaar trappenhuis, een centrale hal of een gesloten
    portiek. (Voor marktwaarde bepaling: MGW-meergezinswoning)
    """

    portiekwoning = EenheiddetailsoortReferentiedata(
        code="POW",
        naam="Portiekwoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een portiekwoning is een etagewoning waarbij de voordeur uitkomt in een open
    portiek. Een portiek is een toegangsportaal gelegen achter de voorgevel van een
    meergezinsgebouw en grenzend aan de openbare weg, van waaruit de afzonderlijke
    woningen direct worden ontsloten via een gemeenschappelijk te gebruiken trap en
    bordessen. (Voor marktwaarde bepaling: MGW-meergezinswoning )
    """

    praktijkruimte = EenheiddetailsoortReferentiedata(
        code="PRA",
        naam="Praktijkruimte",
        parent=Eenheidsoort.bedrijfsruimte,
    )
    """
    Een praktijkruimte of therapieruimte bestaat minimaal uit een wachtruimte (met
    toilet) en behandelkamer.
    """

    praktijkwoning = EenheiddetailsoortReferentiedata(
        code="PRW",
        naam="Praktijkwoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een woning waarvan een deel bestemd en in gebruik is voor het uitoefenen van een
    beroep aan huis (tandarts, huisarts, fysio, atelier, e.d.).
    """

    psychische_zorginstelling = EenheiddetailsoortReferentiedata(
        code="PZI",
        naam="Psychische zorginstelling",
        parent=Eenheidsoort.intramuraal_zorgvastgoed,
    )
    """
    Instelling voor psychische zorg
    """

    recreatiewoning = EenheiddetailsoortReferentiedata(
        code="REC",
        naam="Recreatiewoning",
        parent=Eenheidsoort.recreatiebestemming,
    )
    """
    Woning met een recreatiebestemming en niet bedoeld voor permanente bewoning.
    """

    recreatiezaal = EenheiddetailsoortReferentiedata(
        code="REZ",
        naam="Recreatiezaal",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Ruimte bestemd voor ontmoeting, recreatie en informeel amusement, binnen een
    wooncomplex.
    """

    schoolgebouw = EenheiddetailsoortReferentiedata(
        code="SCH",
        naam="Schoolgebouw",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Vmbo-mbo-scholen, vwo-scholen, schoolgebouwen voor speciaal onderwijs.
    """

    scootmobielplek = EenheiddetailsoortReferentiedata(
        code="SCO",
        naam="Scootmobielplek",
        parent=Eenheidsoort.parkeergelegenheid,
    )

    steunpunt = EenheiddetailsoortReferentiedata(
        code="STP",
        naam="Steunpunt",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Steunpunten voor schuldsanering en budgetbeheeradvies voor huishoudens in financiële
    problemen
    """

    tijdelijke_woning = EenheiddetailsoortReferentiedata(
        code="TIJ",
        naam="Tijdelijke woning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een tijdelijke woning is een woning met een tijdelijke instandhoudingstermijn (van
    meestal 10 jaar). Voorbeelden van tijdelijke woningen zijn containerwoningen,
    duplexwoningen.
    """

    tiny_house = EenheiddetailsoortReferentiedata(
        code="TIN",
        naam="Tiny house",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een tiny house is een kleine volwaardige (vrijstaande) woningen van maximaal 50 m2
    vloeroppervlak met een zo klein mogelijke ecologische voetafdruk. ze staan op
    een (tijdelijke) fundering of op wielen.
    """

    tussenwoning = EenheiddetailsoortReferentiedata(
        code="TUS",
        naam="Tussenwoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een tussenwoning is een eengezinswoning waarbij de tussenmuren aan andere panden
    grenzen en waarbij de woningen ten opzichte van elkaar in een gelijk vlak of
    lijn liggen. Ook de woning die de hoek vormt van een gesloten bouwblok (twee
    reeksen woningen zijn verbonden met elkaar) is een tussenwoning. (Voor
    marktwaarde bepaling: EGW-eengezinswoning)
    """

    twee_onder_een_kapwoning = EenheiddetailsoortReferentiedata(
        code="TWE",
        naam="Twee-onder-een-kapwoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een 2-onder-1-kapwoning is een eengezinswoning waarvan het hoofdgebouw is verbonden
    met het hoofdgebouw van één andere gelijksoortige en gelijkvormige woning (niet
    zijnde een tussenwoning). Ook wanneer de woningen elk een afzonderlijke
    dakconstructie hebben, vallen deze onder de definitie van de
    2-onder-1-kapwoning. 2- onder-1-kapwoningen worden ook wel aangeduid als “helft
    van een dubbel”, welk begrip als synoniem gebruikt mag worden. (Voor marktwaarde
    bepaling: EGW-eengezinswoning).
    """

    veiligheidshuis = EenheiddetailsoortReferentiedata(
        code="VEI",
        naam="Veiligheidshuis",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Een veiligheidshuis is een fysieke locatie waar verschillende instellingen in een
    regio of gemeente in Nederland samenwerken aan het terugdringen van overlast,
    huiselijk geweld en criminaliteit.
    """

    verstandelijk_gehandicapten_instelling = EenheiddetailsoortReferentiedata(
        code="VGI",
        naam="Verstandelijk gehandicapten instelling",
        parent=Eenheidsoort.intramuraal_zorgvastgoed,
    )
    """
    Instelling voor mensen met een verstandelijke beperking.
    """

    volkstuin = EenheiddetailsoortReferentiedata(
        code="VOL",
        naam="Volkstuin",
        parent=Eenheidsoort.overig,
    )
    """
    Gehuurd stukje grond waarop je planten, groenten en fruit kunt laten groeien
    """

    verpleeghuis = EenheiddetailsoortReferentiedata(
        code="VPL",
        naam="Verpleeghuis",
        parent=Eenheidsoort.intramuraal_zorgvastgoed,
    )
    """
    Een verpleeghuis is een instelling waar mensen met gezondheidsproblemen kunnen
    verblijven die (meer) zorg en medische begeleiding nodig hebben die ze thuis of
    in het verzorgingshuis niet (voldoende) kunnen krijgen
    """

    vrijstaande_woning = EenheiddetailsoortReferentiedata(
        code="VRI",
        naam="Vrijstaande woning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een vrijstaande woning is een eengezinswoning die los staat van (eventueel)
    aanwezige andere objecten. (Voor marktwaarde bepaling: EGW-eengezinswoning)
    """

    verzorgingshuis = EenheiddetailsoortReferentiedata(
        code="VZO",
        naam="Verzorgingshuis",
        parent=Eenheidsoort.intramuraal_zorgvastgoed,
    )
    """
    Een verzorgingshuis biedt uitgebreide zorg, ondersteuning en een beschutte
    woonomgeving, als u door ouderdom of ziekte niet meer zelfstandig kunt wonen,
    ook niet met hulp van naasten, mantelzorg of thuiszorg.
    """

    waterwoning = EenheiddetailsoortReferentiedata(
        code="WAT",
        naam="Waterwoning",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een waterwoning is een woning voorzien van een draagconstructie met een groot
    drijfvermogen en verbonden met in de grond verankerde geleiders waardoor de
    woning afhankelijk van het waterniveau kan stijgen of dalen. (Voor marktwaarde
    bepaling: EGW-eengezinswoning)
    """

    welzijnswerkruimte_wijk_en_of_buurtgericht = EenheiddetailsoortReferentiedata(
        code="WEL",
        naam="Welzijnswerkruimte wijk-/buurtgericht",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Ruimte voor op de buurt of wijk gerichte activiteiten op het gebied van welzijnswerk
    door stichtingen of verenigingen
    """

    centrum_voor_werk = EenheiddetailsoortReferentiedata(
        code="WER",
        naam="Centrum voor werk",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Centrum voor werk(gelegenheid) en/of bevordering van bedrijvigheid in de wijk
    """

    wijksportvoorziening = EenheiddetailsoortReferentiedata(
        code="WIJ",
        naam="Wijksportvoorziening",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )

    winkelruimte = EenheiddetailsoortReferentiedata(
        code="WIR",
        naam="Winkelruimte",
        parent=Eenheidsoort.bedrijfsruimte,
    )

    woonboot = EenheiddetailsoortReferentiedata(
        code="WOB",
        naam="Woonboot",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een woonboot is een verblijfsobject dat bestemd is voor permanente danwel
    recreatieve bewoning en dat op of in het water is gelegen, met vaste ligplaats
    met walaansluiting en niet direct geschikt om als vervoermiddel te gebruiken.
    """

    woonwagen = EenheiddetailsoortReferentiedata(
        code="WOW",
        naam="Woonwagen",
        parent=Eenheidsoort.woonruimte,
    )
    """
    Een woonwagen respectievelijk stacaravan is een voor permanente respectievelijk
    recreatieve bewoning bestemd verblijfsobject dat is geplaatst op een standplaats
    en in zijn geheel of in delen kan worden verplaatst, met uitzondering van wagens
    die een eigen aandrijving hebben en wagens waarvoor voor het voortbewegen ervan
    over een weg geen ontheffing ingevolge de Wegenverkeerswet en het Reglement
    verkeersregels en verkeerstekens is vereist.
    """

    woon_en_of_winkelpand = EenheiddetailsoortReferentiedata(
        code="WWI",
        naam="Woon-/Winkelpand",
        parent=Eenheidsoort.bedrijfsruimte,
    )
    """
    Een gebouw in de zin van art. 7:290 BW met een binnen de contouren van de
    buitenmuren van het gebouw een al dan niet zelfstandige woonruimte. De
    bedrijfsruimte heeft doorgaans een maximale verhuurbaar vloeroppervlakte (vvo)
    van circa 200 m2 en is bestemd voor of biedt de mogelijkheid tot detailhandel of
    een daaraan vergelijkbare bestemming (kantoor, atelier, showroom e.d.). Verder
    is wonen in een deel van het object toegestaan (veelal bewoond door de eigenaar
    of diens personeel). De bedrijfs- en woonruimte zijn aan de binnenzijde
    onderling bereikbaar.
    """

    woonwagenstandplaats = EenheiddetailsoortReferentiedata(
        code="WWP",
        naam="Woonwagenstandplaats",
        parent=Eenheidsoort.overig,
    )
    """
    Een standplaats is een formeel door de gemeente als zodanig aangewezen terrein of
    een gedeelte daarvan, dat bestemd is voor het permanent plaatsen van een niet
    direct en duurzaam met de aarde verbonden en voor woon, bedrijfsmatige of
    recreatieve doeleinden geschikte ruimte.Binnen de grenzen van een
    recreatieterrein kan ook sprake zijn van uitsluitend een aanwijzing van de
    recreatieve standplaats door de eigenaar van het terrein.
    """

    welzijnswerkruimte_niet_wijk_of_buurtgericht = EenheiddetailsoortReferentiedata(
        code="WWR",
        naam="Welzijnswerkruimte niet-wijk- of buurtgericht",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Ruimten voor niet op de buurt of wijk gerichte activiteiten op het gebied van
    welzijnswerk door stichtingen of verenigingen
    """

    ziekenhuis = EenheiddetailsoortReferentiedata(
        code="ZIE",
        naam="Ziekenhuis",
        parent=Eenheidsoort.intramuraal_zorgvastgoed,
    )

    zorgsteunpunt = EenheiddetailsoortReferentiedata(
        code="ZST",
        naam="Zorgsteunpunt",
        parent=Eenheidsoort.maatschappelijk_vastgoed,
    )
    """
    Zorgsteunpunten die inpandig in een woonzorggebouw zijn gevestigd
    """
