from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class WoonvormReferentiedata(Referentiedata):
    pass


class Woonvorm(Referentiedatasoort):
    adl_clusterwoning = WoonvormReferentiedata(
        code="ADL",
        naam="ADL-clusterwoning",
    )
    """
    Cluster van woningen met een centrale hulppost  (soms ook FOKUS-woning genoemd) Met
    ADL kan 24 uur per dag hulp opgeroepen worden bij de algemene dagelijkse
    levensverrichtingen (ADL) in en om de woning. Een ADL-clusterwoning is een
    speciale woonvorm voor mensen met een lichamelijke beperking die zelfstandig
    willen wonen, maar wel ondersteuning nodig hebben bij algemene dagelijkse
    levensverrichtingen (ADL), zoals: opstaan en naar bed gaan, wassen en aankleden,
    eten en drinken, naar het toilet gaan, verplaatsen (bijv. in en uit een
    rolstoel). Zelfstandige woning: de woning is een reguliere zelfstandige woning
    (met eigen keuken, badkamer en woonkamer). Aangepast voor rolstoelgebruikers:
    bijvoorbeeld brede deuropeningen, drempelloze vloeren en automatische deuren.
    Aansluiting op een ADL-centrale: de woning maakt deel uit van een cluster rond
    een centrale post waar 24 uur per dag zorgverleners aanwezig zijn. Hulp op
    afroep: bewoners kunnen met een alarmknop of intercom direct contact maken met
    de centrale om hulp in te roepen. Doelgroep: mensen met een ernstige
    lichamelijke beperking, die wilsbekwaam zijn en regie over hun eigen leven
    willen houden en niet in een verpleeghuis of instelling willen wonen en wel
    24-uurs assistentie nodig hebben.
    """

    begeleid_wonen = WoonvormReferentiedata(
        code="BEG",
        naam="Begeleid wonen",
    )
    """
    Woonvorm voor mensen die (tijdelijk) niet volledig zelfstandig kunnen wonen, maar
    geen 24-uurs zorg nodig hebben. Het combineert zelfstandig wonen met begeleiding
    op maat, praktisch, sociaal of psychisch. Bewoners hebben eigen woonruimte (soms
    een zelfstandige studio, soms een kamer met gedeelde voorzieningen) en krijgen
    structurele begeleiding van professionele hulpverleners. De begeleiding richt
    zich op het vergroten van zelfredzaamheid en maatschappelijke participatie.
    Begeleid wonen is bedoeld voor mensen die ondersteuning nodig hebben bij wonen
    of leven. Bijvoorbeeld mensen met een verstandelijke beperking, mensen met
    psychische problemen of verslavingsproblematiek,  jongvolwassenen die uit
    jeugdzorg of pleegzorg komen, mensen met niet-aangeboren hersenletsel (NAH),
    mensen die dakloos zijn geweest of schulden hebben.
    """

    geclusterde_woonvorm = WoonvormReferentiedata(
        code="GEC",
        naam="Geclusterde woonvorm",
    )
    """
    Deze woning is een zelfstandige wooneenheid binnen een gebouw dat voldoet aan
    specifieke criteria voor geclusterde woonvormen. Dit omvat minimaal 12
    zelfstandige wooneenheden voor bewoners van 55 jaar en ouder, met een aanwezige
    ontmoetingsruimte in het gebouw of grenzend aan het gebouw. Deze woningen
    voldoen aan de uitgangspunten voor nultredenwoningen.
    """

    groepswonen = WoonvormReferentiedata(
        code="GRO",
        naam="Groepswonen",
    )
    """
    Woonvorm waarbij meerdere mensen samen wonen in één huis of wooncomplex en bewust
    een woongemeenschap vormen. Iedere bewoner heeft meestal een eigen kamer of
    appartement, maar er zijn ook gedeelde ruimtes (zoals keuken, woonkamer of tuin)
    en vaak wordt er iets samen georganiseerd of ondernomen. Bewoners wonen bewust
    samen en kiezen voor meer contact en wederzijdse steun. Er is een balans tussen
    privacy en gezamenlijkheid: je hebt je eigen plek, maar ook gedeelde
    leefruimtes. Ook wel geclusterd wonen genoemd.
    """

    grote_woonvorm = WoonvormReferentiedata(
        code="GRW",
        naam="Grote woonvorm",
    )
    """
    Woonlocatie met meerdere bewoners die zorg of begeleiding ontvangen, vaak met
    gemeenschappelijke voorzieningen en professionele ondersteuning op locatie. Het
    is in feite het tegenovergestelde van kleinschalig wonen. Veel bewoners: meestal
    meer dan 20, soms tientallen of zelfs honderden bewoners. Gemeenschappelijke
    voorzieningen: gezamenlijke woonkamers, eetruimtes, activiteitenruimtes of
    tuinen. Professionele aanwezigheid: er is structurele of 24-uurs zorg of
    begeleiding aanwezig. Eigen of gedeelde woonruimte: bewoners hebben een eigen
    kamer, studio of appartement, maar niet altijd volledige zelfstandigheid (keuken
    of sanitair kan gedeeld zijn). Centraal georganiseerd: vaak beheerd door een
    zorginstelling of woningcorporatie.Een grote woonvorm komt vaak voor bij:
    Ouderen met intensieve zorg (verpleeghuis, verzorgingshuis), Mensen met een
    verstandelijke beperking (instellingsterrein of groot wooncomplex), Mensen met
    psychiatrische problematiek of verslavingszorg (beschermd wonen in
    groepsverband), Studenten of arbeidsmigranten (in niet-zorgcontext:
    grootschalige huisvesting).
    """

    hat_eenheid = WoonvormReferentiedata(
        code="HAT",
        naam="HAT-eenheid",
    )
    """
    Eenheden voor 1 of twee persoonshuishoudens met gezamenlijke keuken, badkamer
    etc.een kleine zelfstandige woning bedoeld voor alleenstaanden of
    twee­persoonshuishoudens, meestal jongvolwassenen of starters. De term HAT staat
    voor Herstart Arbeid en Training – een beleidsbegrip uit de jaren ’80, toen deze
    woonvorm werd ontwikkeld om jonge mensen met werk of opleiding een zelfstandige,
    betaalbare woonruimte te bieden. Klein zelfstandig appartement (ongeveer 25–45
    m²). Eigen voorzieningen: keuken, douche en toilet (dus geen kamerbewoning).
    Doelgroep: alleenstaanden, starters of jongeren die beginnen met werk of studie.
    Betaalbaar segment: vaak sociale huur, soms tijdelijke contracten. Complexgewijs
    gebouwd: meerdere HAT-eenheden in één gebouw met gedeelde voorzieningen zoals
    wasruimte of fietsenstalling. De HAT-eenheid werd geïntroduceerd in de jaren
    1980 om het tekort aan betaalbare starterswoningen tegen te gaan, jongeren te
    helpen zelfstandig te worden (de “herstart” in werk en opleiding) en
    doorstroming in de woningmarkt te bevorderen.
    """

    kleine_woonvorm = WoonvormReferentiedata(
        code="KLE",
        naam="Kleine woonvorm",
    )
    """
    Kleinschalig wonen, meestal bedoeld voor mensen die zorg of begeleiding nodig
    hebben, maar in een huiselijke, persoonlijke omgeving willen wonen in plaats van
    een instelling. Weinig bewoners: meestal 6 tot 12 personen per huis of
    woongroep. Huiskamermodel: bewoners delen gemeenschappelijke ruimtes (woonkamer,
    keuken, tuin). Persoonlijke begeleiding of zorg: vaak 24-uurs aanwezigheid, maar
    in een kleine vaste groep. Veel aandacht voor individuele zorg en sociale
    interactie. Kleine woonvormen komen voor bij verschillende doelgroepen. Ouderen
    met dementie: Kleinschalige woonvoorziening binnen een verpleeghuis (8 bewoners
    per woning). Mensen met verstandelijke beperking: Woonhuis in de wijk met 6
    bewoners en begeleider. Mensen met psychische kwetsbaarheid: Kleinschalig
    beschermd wonen met nabijheid van begeleiding. Jeugd / jongvolwassenen met
    zorgvraag: Groepswoning met vaste mentor en gezamenlijke dagbesteding.
    """

    levensloopbestendig_woning = WoonvormReferentiedata(
        code="LEV",
        naam="Levensloopbestendig woning",
    )
    """
    Een levensloopbestendige woning is een woning die geschikt is voor bewoning in elke
    levensfase, inclusief op latere leeftijd of bij een fysieke beperking.
    Kenmerkend zijn gelijkvloerse voorzieningen zoals slapen en baden op de begane
    grond, brede doorgangen en een drempelloze, toegankelijke indeling.
    """

    seniorenwoning_met_zorg = WoonvormReferentiedata(
        code="SEN",
        naam="Seniorenwoning met zorg",
    )
    """
    Senioren woningen met zorg (voorheen Wibo-wonen in beschermde omgeving) zijn bij
    elkaar gelegen zelfstandige (aanleun)woningen met een dienstencentrum met
    allerlei voorzieningen dichtbij.
    """

    thomashuis = WoonvormReferentiedata(
        code="THO",
        naam="Thomashuis",
    )
    """
    Een Thomashuis is een kleinschalige woonvoorziening voor zes à acht mensen met een
    verstandelijke beperking
    """

    zorggeschikte_woning = WoonvormReferentiedata(
        code="ZWO",
        naam="Zorggeschikte woning",
    )
    """
    Woning die voldoet aan de criteria van Geclusterde woonvorm, maar met aanvullende
    voorzieningen om de woning beter geschikt te maken voor mensen met een beperking
    of voor zorgverlening. Bij nieuwbouw en getransformeerde woningen moet de
    woonvorm en woning rolstoelgeschikt zijn en bij verbouw moet de woonvorm
    rolstoelgeschikt zijn en de woning minimaal rollator-geschikt. Daarnaast moet de
    entree van de woning minimaal 90 centimeter breed zijn, moeten alle deuren
    automatisch kunnen openen en moeten woningen die niet op de begane grond zijn,
    bereikbaar zijn met een rolstoeltoegankelijke personenlift.
    """
