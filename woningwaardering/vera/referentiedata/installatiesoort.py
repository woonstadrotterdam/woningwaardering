from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InstallatiesoortReferentiedata(Referentiedata):
    pass


class Installatiesoort(Referentiedatasoort):
    aanbelfunctie_met_video_en_audioverbinding = InstallatiesoortReferentiedata(
        code="ABF",
        naam="Aanbelfunctie met video- en audioverbinding",
    )
    """
    Een aanbelfunctie met video- en audioverbinding waarbij de voordeur automatisch kan
    worden geopend vanuit de woning wordt gewaardeerd met 0,25 punt. Hieronder wordt
    een systeem verstaan dat tweewegcommunicatie mogelijk maakt met beeld en geluid
    tussen degene die aanbelt en een aanwezige in de woonruimte. Daarbij dient er
    tevens sprake te zijn van de mogelijkheid tot het openen van de
    (gemeenschappelijke) voordeur vanuit de woonruimte (op afstand) die toegang
    geeft tot het complex waarvan de woning onderdeel uitmaakt.
    """

    elektrische_gordijnen = InstallatiesoortReferentiedata(
        code="EGV",
        naam="Elektrische gordijnen",
    )
    """
    Installatie van domotica voor elektrische gordijnen.
    """

    spraakgestuurde_apparaten = InstallatiesoortReferentiedata(
        code="SPR",
        naam="Spraakgestuurde apparaten",
    )
    """
    Installatie van domotica voor spraakgestuurde apparaten (licht,verwarming,deuren).
    """

    noodoproepsysteem = InstallatiesoortReferentiedata(
        code="NPS",
        naam="Noodoproepsysteem",
    )
    """
    Installatie voor noodoproepen
    """

    inbouw_afzuiginstallatie = InstallatiesoortReferentiedata(
        code="IAF",
        naam="Inbouw afzuiginstallatie",
    )
    """
    Bij een afzuiginstallatie gaat het om een luchtafvoer met afzuiging naar buiten de
    woning of op basis van recirculatie met actieve koolstof- en vetfilters. Een
    afzuiginstallatie kan zowel een afzuig- of recirculatiekap boven de
    kookinstallatie zijn, als een in het aanrecht geïntegreerd afzuigsysteem.
    """

    inbouw_kookplaat_inductie = InstallatiesoortReferentiedata(
        code="IKI",
        naam="Inbouw kookplaat inductie",
    )
    """
    Een inbouw inductiekookplaat is een keukenapparaat dat in het werkblad wordt
    geïntegreerd. Het gebruikt magnetische velden om pannen direct te verwarmen, wat
    resulteert in snelle opwarming, nauwkeurige temperatuurcontrole, en verhoogde
    energie-efficiëntie in vergelijking met traditionele kookplaten.
    """

    inbouw_kookplaat_keramisch = InstallatiesoortReferentiedata(
        code="IKK",
        naam="Inbouw kookplaat keramisch",
    )
    """
    Een inbouw keramische kookplaat is een keukenapparaat dat in het werkblad wordt
    geïntegreerd. Het verwarmt door elektrische spiralen onder een glad glazen
    oppervlak, waardoor het een gelijkmatige warmteverdeling biedt en gemakkelijk
    schoon te maken is, maar trager opwarmt dan inductie.
    """

    inbouw_kookplaat_gas = InstallatiesoortReferentiedata(
        code="IKG",
        naam="Inbouw kookplaat gas",
    )
    """
    Een inbouw gaskookplaat is een keukenapparaat dat in het werkblad wordt
    geïntegreerd. Het maakt gebruik van open gasvlammen voor directe hitte, biedt
    snelle temperatuurregeling, visuele feedback, en is compatibel met alle soorten
    kookgerei, maar vereist gasaanvoer en ventilatie.
    """

    onderrijdbare_kookplaat = InstallatiesoortReferentiedata(
        code="ORK",
        naam="Onderrijdbare kookplaat",
    )
    """
    Type kookplaat dat voldoende vrije ruimte onder het kookgedeelte biedt, zodat een
    gebruiker met een rolstoel er eenvouding onder kan rijden.
    """

    oplaadpunt = InstallatiesoortReferentiedata(
        code="OPL",
        naam="Oplaadpunt",
    )
    """
    Oplaadpunt waar een auto aan gekoppeld kan worden om te op te laden. Het betreft
    hier niet de laadpaal maar het oplaadpunt (er kunnen meerdere oplaadpunten
    beschikbaar zijn op een laadpaal
    """

    inbouw_koelkast = InstallatiesoortReferentiedata(
        code="IKO",
        naam="Inbouw koelkast",
    )
    """
    Een inbouwkoelkast is een keukenapparaat dat naadloos in de keukeninrichting wordt
    geïntegreerd. Het is ontworpen om achter een keukenkastdeur te worden geplaatst,
    biedt voedselkoeling en -opslag, en zorgt voor een gestroomlijnde en uniforme
    uitstraling in de keuken.
    """

    inbouw_vrieskast = InstallatiesoortReferentiedata(
        code="IVR",
        naam="Inbouw vrieskast",
    )
    """
    Een inbouwvrieskast is een keukenapparaat dat naadloos in de keukeninrichting wordt
    geïntegreerd. Het wordt achter een keukenkastdeur geplaatst, biedt
    vriescapaciteit voor langdurige voedselopslag, en behoudt een gestroomlijnde,
    uniforme uitstraling in de keuken.
    """

    inbouw_koelvriescombinatie = InstallatiesoortReferentiedata(
        code="IKV",
        naam="Inbouw koelvriescombinatie",
    )
    """
    Een inbouw koelvriescombinatie is een keukenapparaat dat zowel een koelkast als een
    vriesgedeelte combineert. Het wordt achter een keukenkastdeur geplaatst, zorgt
    voor efficiënte voedselkoeling en -opslag en biedt een gestroomlijnde, uniforme
    uitstraling in de keuken.
    """

    inbouw_oven_elektrisch = InstallatiesoortReferentiedata(
        code="IOE",
        naam="Inbouw oven elektrisch",
    )
    """
    Een inbouw elektrische oven is een keukenapparaat dat naadloos in een keukenkast
    wordt geïntegreerd. Het gebruikt elektriciteit om gerechten gelijkmatig te
    bakken en braden, biedt nauwkeurige temperatuurregeling, en heeft verschillende
    programma's voor diverse kookmethoden.
    """

    inbouw_oven_gas = InstallatiesoortReferentiedata(
        code="IOG",
        naam="Inbouw oven gas",
    )
    """
    Een inbouw gasoven is een keukenapparaat dat naadloos in een keukenkast wordt
    geïntegreerd. Het gebruikt gas als energiebron om gerechten te bakken en te
    braden, biedt snelle temperatuurstijging en gelijkmatige warmteverdeling, maar
    vereist gasaanvoer.
    """

    inbouw_magnetron = InstallatiesoortReferentiedata(
        code="IMA",
        naam="Inbouw magnetron",
    )
    """
    Een inbouwmagnetron is een keukenapparaat dat naadloos in een keukenkast wordt
    geïntegreerd. Het gebruikt magnetronstraling om voedsel snel te verwarmen en te
    ontdooien, bespaart ruimte op het aanrecht en biedt een gestroomlijnde, uniforme
    uitstraling in de keuken.
    """

    inbouw_combi_magnetron_en_of_oven = InstallatiesoortReferentiedata(
        code="ICM",
        naam="Inbouw combi magnetron/oven",
    )
    """
    Een inbouw combimagnetron/oven is een keukenapparaat dat zowel magnetron- als
    ovenfuncties combineert. Het is ontworpen om naadloos in een keukenkast te
    worden geïntegreerd en biedt veelzijdigheid voor bakken, braden, grillen en snel
    opwarmen. Dit bespaart ruimte en biedt flexibiliteit in de keuken.
    """

    inbouw_vaatwasmachine = InstallatiesoortReferentiedata(
        code="IVA",
        naam="Inbouw vaatwasmachine",
    )
    """
    Een inbouwvaatwasmachine is een keukenapparaat dat naadloos in een keukenkast wordt
    geïntegreerd. Het reinigt en droogt vaatwerk automatisch, bespaart ruimte op het
    aanrecht, vermindert handmatig afwassen en past bij de gestroomlijnde, uniforme
    uitstraling van de keuken.
    """

    extra_keukenkastruimte_boven_het_minimum = InstallatiesoortReferentiedata(
        code="EKA",
        naam="Extra keukenkastruimte boven het minimum",
    )
    """
    per 60 cm breedte, met een minimum van 60 cm hoogte.
    """

    verlaagde_keuken = InstallatiesoortReferentiedata(
        code="VKE",
        naam="Verlaagde keuken",
    )
    """
    Een keuken met werkbladen en kastjes op een hoogte van 85 cm voor
    rolstoelgebruikers.
    """

    verhoogde_keuken = InstallatiesoortReferentiedata(
        code="VHK",
        naam="Verhoogde keuken",
    )
    """
    Keuken waarvan het werkblad en/of de keukenkasten hoger zijn geplaatst dan de
    standaardhoogte De werkbladen en kastjes zijn hoger dan 95 cm.
    """

    onderrijdbare_spoelbak = InstallatiesoortReferentiedata(
        code="KSP",
        naam="Onderrijdbare spoelbak",
    )
    """
    Type spoelbak dat voldoende vrije ruimte onder de spoelbak biedt, waardoor een
    gebruiker met een rolstoel of ander hulpmiddel er gemakkelijjk onder kan rijden.
    """

    uitschuifbare_of_kantelbare_keukenkastjes = InstallatiesoortReferentiedata(
        code="UKK",
        naam="Uitschuifbare of kantelbare keukenkastjes",
    )
    """
    Uitschuifbare of kantelbare keukenkastjes t.b.v. rolstoelgebruikers.
    """

    eenhandsmengkraan = InstallatiesoortReferentiedata(
        code="EHM",
        naam="Éénhandsmengkraan",
    )
    """
    Een ééngreepsmengkraan is een kraan met één hendel waarmee de watertemperatuur en
    -stroom eenvoudig worden geregeld. Het combineert warm en koud water tot de
    gewenste temperatuur, is gebruiksvriendelijk en biedt een modern ontwerp voor
    elke keuken of badkamer.
    """

    thermostatische_mengkraan = InstallatiesoortReferentiedata(
        code="TME",
        naam="Thermostatische mengkraan",
    )
    """
    Een thermostatische mengkraan regelt automatisch de watertemperatuur door warm en
    koud water te mengen. Het handhaaft een constante temperatuur, voorkomt
    temperatuurfluctuaties, en verhoogt het comfort en de veiligheid in de badkamer
    of keuken.
    """

    kokend_waterfunctie = InstallatiesoortReferentiedata(
        code="KWA",
        naam="Kokend waterfunctie",
    )
    """
    De kokend waterfunctie levert direct kokend water uit een kraan, zonder koken op het
    fornuis. Het biedt gemak en tijdsbesparing voor het bereiden van thee, koffie,
    en andere warme dranken, en verhoogt de efficiëntie in de keuken. Al dan niet
    apart of in aanvulling op de kraan.
    """

    staand_toilet = InstallatiesoortReferentiedata(
        code="STO",
        naam="Staand Toilet",
    )
    """
    Een toilet met waterspoeling als het toilet is geplaatst in een daartoe bestemde
    ruimte en als het toilet binnen het woongebouw is gelegen. Wanneer sprake is van
    een toilet dat buiten de woning maar binnen het woongebouw is gelegen, dan geldt
    dat het toilet in de waardering wordt meegenomen als het gebruik van het toilet
    door derden is uit te sluiten. Toiletten buiten toiletruimten en badkamers komen
    niet in aanmerking voor waardering.
    """

    hangend_toilet = InstallatiesoortReferentiedata(
        code="HTO",
        naam="Hangend toilet",
    )
    """
    een hangend toilet met waterspoeling als het toilet is geplaatst in een daartoe
    bestemde ruimte en als het toilet binnen het woongebouw is gelegen. Wanneer
    sprake is van een toilet dat buiten de woning maar binnen het woongebouw is
    gelegen, dan geldt dat het toilet in de waardering wordt meegenomen als het
    gebruik van het toilet door derden is uit te sluiten. Toiletten buiten
    toiletruimten en badkamers komen niet in aanmerking voor waardering.
    """

    verhoogd_toilet = InstallatiesoortReferentiedata(
        code="VTI",
        naam="Verhoogd toilet",
    )
    """
    Een toilet dat hoger is geplaatst dan de standaardtoiletten. Dit maakt het zitten en
    opstaan gemakkelijker, vooral voor ouderen, lange mensen, mensen met beperkte
    mobiliteit or lichamelijke beperking.
    """

    wastafel = InstallatiesoortReferentiedata(
        code="WAS",
        naam="Wastafel",
    )
    """
    Een wastafel is een sanitair element met een ingebouwde afvoer voor het wassen van
    handen, gezichten, of voor andere doeleinden. Het wordt vaak geïnstalleerd in
    keukens of badkamers en kan variëren in materiaal, vorm en grootte. Als
    wastafels worden alle bakken geteld voor wassen en spoelen die op de
    waterleiding én op het huisriool zijn aangesloten. Een dergelijke bak wordt niet
    als wastafel gewaardeerd indien boven de bak een douche is aangebracht. Een bad
    of spoelbakken in een keukenaanrecht, bidet of lavet wordt niet als wastafel,
    douche of bad gewaardeerd. Wastafels worden gewaardeerd tot een maximum van 1
    keer per vertrek of overige ruimte, m.u.v. de badkamer.
    """

    meerpersoonswastafel = InstallatiesoortReferentiedata(
        code="MPW",
        naam="Meerpersoonswastafel",
    )
    """
    Een meerpersoonswastafel is een grotere wastafel met meerdere kranen of secties,
    ontworpen om gelijktijdig door meerdere personen te worden gebruikt. Ideaal voor
    drukke gezinnen of gedeelde badkamers, biedt het extra ruimte en comfort. Van
    een meerpersoonswastafel is sprake bij een wastafel met een minimale breedte van
    70 cm, voorzien van twee kranen. Deze wastafels worden tot maximaal 1 keer per
    vertrek of overige ruimte, m.u.v. de badkamer, gewaardeerd. De kranen worden
    afzonderlijk gewaardeerd.
    """

    douche = InstallatiesoortReferentiedata(
        code="DOU",
        naam="Douche",
    )
    """
    Een douche is een sanitair apparaat voor het snel en efficiënt wassen van het
    lichaam met stromend water. Het bestaat uit een douchekop, een afvoer en vaak
    een cabine of omheining om water te beheersen en spatten te voorkomen. Er is
    alleen een douche en geen bad in de ruimte. Als douche wordt meegeteld iedere
    door de verhuurder aangebrachte installatie voor het nemen van een stortbad.
    Hieronder valt eveneens een zogenaamde douchecabine, die voldoet aan
    bovengenoemde voorwaarden, als de douchecabine in een vertrek (anders dan bad-
    of doucheruimte) of overige ruimte is geplaatst. De oppervlakte van dat vertrek
    of van die overige ruimte wordt in dat geval niet verminderd met de door de
    douchecabine ingenomen oppervlakte.
    """

    bad = InstallatiesoortReferentiedata(
        code="BAD",
        naam="Bad",
    )
    """
    Een bad is een sanitair apparaat waarin men kan liggen om te baden. Het bevat een
    waterdichte kuip, vaak met een afvoer en een kraan voor het in- en uitlaten van
    water, en biedt een ontspannende en volledige onderdompeling. Er is alleen een
    bad en geen doude in de ruimte. Aan baden worden punten toegekend, ongeacht de
    lengte van het bad, als een volwassen persoon er in een normale zithouding in
    kan plaatsnemen. Indien een bad is voorzien van een (hand)douche, dan wordt het
    douchegarnituur niet afzonderlijk geteld.
    """

    bad_en_douche = InstallatiesoortReferentiedata(
        code="BDO",
        naam="Bad en douche",
    )
    """
    Indien in de badruimte behalve het bad tevens een afzonderlijke douche is
    aangebracht, geldt een afwijkende waardering.
    """

    bubbelfunctie_van_het_bad = InstallatiesoortReferentiedata(
        code="BUB",
        naam="Bubbelfunctie van het bad",
    )
    """
    De bubbelfunctie van het bad genereert luchtbellen door lucht in het water te
    pompen, wat zorgt voor een ontspannende en masserende werking. Het verhoogt het
    comfort en de ontspanning tijdens het baden door een verfrissend bubbeleffect te
    bieden.
    """

    steunbeugels_voor_sanitaire_ruimtes = InstallatiesoortReferentiedata(
        code="SSR",
        naam="Steunbeugels voor sanitaire ruimtes",
    )
    """
    Steunbeugels die in sanitaire ruimtes, zoals badkamers en toiletten, zijn
    geïnstalleerd om extra ondersteuning te bieden voor mensen met een beperking of
    mobiliteitsproblemen.
    """

    drempelloze_inrijdouche = InstallatiesoortReferentiedata(
        code="DRD",
        naam="Drempelloze inrijdouche",
    )
    """
    Een drempelloze, ruime inrijdouche t.b.v. rolstoelgebruikers.
    """

    douchewand = InstallatiesoortReferentiedata(
        code="DOW",
        naam="Douchewand",
    )
    """
    Gemonteerde volledige afscheiding van de douche. In het geval van een gemonteerde
    volledige afscheiding van de douche vindt de waardering plaats wanneer de
    doucheruimte beschikt over een onroerend aanhorige afscheiding met een
    waterdichte afwerking aan alle zijden van de douche. Ter illustratie: glazen
    deuren vallen hier wel onder, maar een douchegordijn (dat snel weggenomen kan
    worden) niet.
    """

    handdoekenradiator = InstallatiesoortReferentiedata(
        code="HRA",
        naam="Handdoekenradiator",
    )
    """
    Een handdoekenradiator is een verwarmingspaneel dat speciaal is ontworpen om
    handdoeken te drogen en te verwarmen. Het biedt extra comfort in de badkamer
    door handdoeken warm en klaar voor gebruik te houden, en zorgt tegelijkertijd
    voor een aangename temperatuur.
    """

    ingebouwd_kastje_met_in_of_opgebouwde_wastafel = InstallatiesoortReferentiedata(
        code="IKW",
        naam="Ingebouwd kastje met in- of opgebouwde wastafel",
    )
    """
    Een ingebouwd kastje met wastafel is een geïntegreerde opberg- en wastafeloplossing
    die een wastafel combineert met een kastje voor extra opbergruimte. Het biedt
    een gestroomlijnde uitstraling en praktische opslag in badkamers of keukens.
    """

    kastruimte = InstallatiesoortReferentiedata(
        code="KAS",
        naam="Kastruimte",
    )
    """
    Kastruimte met een minimale breedte van 40cm, en minimale hoogte van 40cm.
    """

    stopcontact_bij_wastafel = InstallatiesoortReferentiedata(
        code="STW",
        naam="Stopcontact bij wastafel",
    )
    """
    Stopcontact bij de wastafel. Maximaal twee per wastafel worden meegeteld in de
    waardering.
    """
