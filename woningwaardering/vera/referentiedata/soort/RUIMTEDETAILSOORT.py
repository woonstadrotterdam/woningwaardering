
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class RUIMTEDETAILSOORT:

    atrium_of_patio = Referentiedata(
        code="ATR",
        naam="Atrium / Patio",
    )
    # atrium_of_patio = ("ATR", "Atrium / Patio")
    """
    Niet overdekt atrium of patio
    """

    achtertuin = Referentiedata(
        code="ATU",
        naam="Achtertuin",
    )
    # achtertuin = ("ATU", "Achtertuin")

    badkamer = Referentiedata(
        code="BAD",
        naam="Badkamer",
    )
    # badkamer = ("BAD", "Badkamer")
    """
    Vertrek: voor een sanitaire ruimte in een woning, dat wil zeggen een ruimte die
    speciaal is ingericht voor lichaamsverzorging.
    """

    balkon = Referentiedata(
        code="BAL",
        naam="Balkon",
    )
    # balkon = ("BAL", "Balkon")
    """
    Een balkon.
    """

    badkamer_of_toilet = Referentiedata(
        code="BAT",
        naam="Badkamer/toilet",
    )
    # badkamer_of_toilet = ("BAT", "Badkamer/toilet")
    """
    Gecombineerde badkamer/toilet
    """

    berging = Referentiedata(
        code="BER",
        naam="Berging",
    )
    # berging = ("BER", "Berging")
    """
    Berging voor eigen gebruik, overige ruimte
    """

    bijkeuken = Referentiedata(
        code="BIJ",
        naam="Bijkeuken",
    )
    # bijkeuken = ("BIJ", "Bijkeuken")
    """
    Overige ruimte: grenzend aan de eigenlijke keuken die voor ondersteunende
    huishoudelijke handelingen gebruikt wordt, zoals wassen, drogen en strijken, maar
    ook voor het opbergen en bewaren van (etens)voorraden en schoonmaakspullen.
    """

    carport = Referentiedata(
        code="CAR",
        naam="Carport",
    )
    # carport = ("CAR", "Carport")

    dakterras = Referentiedata(
        code="DAK",
        naam="Dakterras",
    )
    # dakterras = ("DAK", "Dakterras")
    """
    Een dakterras.
    """

    gemeenschappelijk_dakterras = Referentiedata(
        code="GAK",
        naam="Gemeenschappelijk dakterras",
    )
    # gemeenschappelijk_dakterras = ("GAK", "Gemeenschappelijk dakterras")
    """
    Buitenruimte: een gemeenschappelijk dakterras
    """

    doucheruimte = Referentiedata(
        code="DOU",
        naam="Doucheruimte",
    )
    # doucheruimte = ("DOU", "Doucheruimte")
    """
    Vertrek: sanitaire ruimte met een douche.
    """

    gang = Referentiedata(
        code="GAN",
        naam="Gang",
    )
    # gang = ("GAN", "Gang")
    """
    Ruimte : is een betrekkelijk smalle en lange ruimte omgeven door muren en afgedekt
    door een plafond of zoldering, in een gebouw, als verbinding van vertrekken waarvan
    de deuren erop uitkomen.
    """

    garage = Referentiedata(
        code="GAR",
        naam="Garage",
    )
    # garage = ("GAR", "Garage")
    """
    Overige ruimte: een overdekte en afsluitbare ruimte om voertuigen in te stallen.
    """

    gemeenschappelijke_tuin = Referentiedata(
        code="GTU",
        naam="Gemeenschappelijke tuin",
    )
    # gemeenschappelijke_tuin = ("GTU", "Gemeenschappelijke tuin")

    gemeenschappelijk_dakterras = Referentiedata(
        code="GTU",
        naam="Gemeenschappelijk dakterras",
    )
    # gemeenschappelijk_dakterras = ("GTU", "Gemeenschappelijk dakterras")

    hal = Referentiedata(
        code="HAL",
        naam="Hal",
    )
    # hal = ("HAL", "Hal")
    """
    Verkeersruimte bijv. entree, Hal, overloop, speelhal etc.
    """

    kelder = Referentiedata(
        code="KEL",
        naam="Kelder",
    )
    # kelder = ("KEL", "Kelder")
    """
    Overige ruimte: dat gedeelte van een gebouw dat onder de grond (onder het maaiveld)
    is gelegen.
    """

    keuken = Referentiedata(
        code="KEU",
        naam="Keuken",
    )
    # keuken = ("KEU", "Keuken")
    """
    Vertrek of plaats in een gebouw waarin mensen hun voedsel bereiden of laten bereiden
    """

    loggia = Referentiedata(
        code="LOG",
        naam="Loggia",
    )
    # loggia = ("LOG", "Loggia")

    overige_ruimte = Referentiedata(
        code="OBR",
        naam="Overige ruimte",
    )
    # overige_ruimte = ("OBR", "Overige ruimte")
    """
    Buitenruimte die niet nader is gespecifeerd als ruimtedetailsoort. Bijvoorbeeld een
    platje.
    """

    overige_gemeenschappelijke_ruimte_of_voorziening = Referentiedata(
        code="OGR",
        naam="Overige gemeenschappelijke ruimte of voorziening",
    )
    # overige_gemeenschappelijke_ruimte_of_voorziening = ("OGR", "Overige gemeenschappelijke ruimte of voorziening")
    """
    Gemeenschappelijke ruimte of voorziening die niet nader is gespecifeerd als
    ruimtedetailsoort. Bijvoorbeeld gemeenschappelijke hobbyruimte, wasruimte.
    """

    overig_vertrek = Referentiedata(
        code="OVT",
        naam="Overig vertrek",
    )
    # overig_vertrek = ("OVT", "Overig vertrek")
    """
    Vertrek dat niet nader gespecifeerd is als ruimtedetailsoort. Bijvoorbeeld eetkamer,
    hobbykamer, studeerkamer etc.
    """

    parkeerkelder = Referentiedata(
        code="PAK",
        naam="Parkeerkelder",
    )
    # parkeerkelder = ("PAK", "Parkeerkelder")
    """
    Eigen parkeerplaats in parkeerkelder
    """

    parkeerplaats = Referentiedata(
        code="PAR",
        naam="Parkeerplaats",
    )
    # parkeerplaats = ("PAR", "Parkeerplaats")
    """
    Eigen parkeerplaats of oprit bij de woning
    """

    recreatieruimte = Referentiedata(
        code="REC",
        naam="Recreatieruimte",
    )
    # recreatieruimte = ("REC", "Recreatieruimte")
    """
    Een ruimte binnen de eenheid die recreatie als gebruiksdoel heeft. Bijvoorbeeld
    binnen een zorginstelling.
    """

    tuin_rondom = Referentiedata(
        code="RON",
        naam="Tuin Rondom",
    )
    # tuin_rondom = ("RON", "Tuin Rondom")
    """
    Buitenruimte: tuin gelegen rondom de eenheid
    """

    schuur = Referentiedata(
        code="SCH",
        naam="Schuur",
    )
    # schuur = ("SCH", "Schuur")
    """
    Buitenruimte: veelal vrijstaand gebouw, dat gebruikt wordt om goederen of voedsel in
    op te slaan, en ook als werkruimte kan dienen, maar niet als woning bedoeld is.
    """

    serre = Referentiedata(
        code="SER",
        naam="Serre",
    )
    # serre = ("SER", "Serre")
    """
    Vertrek: glazen veranda verbonden aan een woning.
    """

    slaapkamer = Referentiedata(
        code="SLA",
        naam="Slaapkamer",
    )
    # slaapkamer = ("SLA", "Slaapkamer")
    """
    Vertrek: ruimte in een woning waarin men kan slapen.
    """

    terras = Referentiedata(
        code="TER",
        naam="Terras",
    )
    # terras = ("TER", "Terras")
    """
    Buitenruimte: deel van een buitenruimte met een vlakke oppervlakte die wordt
    gebruikt om op te zitten, te eten, te drinken of andere activiteiten te doen.
    """

    toiletruimte = Referentiedata(
        code="TOI",
        naam="Toiletruimte",
    )
    # toiletruimte = ("TOI", "Toiletruimte")
    """
    Overige ruimte: Sanitaire ruimte met een toilet.
    """

    tussenkamer = Referentiedata(
        code="TUS",
        naam="Tussenkamer",
    )
    # tussenkamer = ("TUS", "Tussenkamer")
    """
    Vertrek: ruimte gelegen tussen en verbonden met twee andere kamers.
    """

    vliering = Referentiedata(
        code="VLI",
        naam="Vliering",
    )
    # vliering = ("VLI", "Vliering")
    """
    Overige ruimte: een meestal niet of beperkt afgewerkte opslagruimte onder het dak,
    die alleen bereikbaar is met een vlizotrap en die niet altijd hoog genoeg is om
    rechtop te kunnen staan.
    """

    voortuin = Referentiedata(
        code="VTU",
        naam="Voortuin",
    )
    # voortuin = ("VTU", "Voortuin")
    """
    Buitenruimte: tuin gelegen voor de voorgevellijn, waar meestal de voordeur van een
    woning is gelegen.
    """

    wasruimte = Referentiedata(
        code="WAS",
        naam="Wasruimte",
    )
    # wasruimte = ("WAS", "Wasruimte")
    """
    Overige ruimte: Specifieke ruimte voor wasmachine, droger, strijken, voor eigen
    gebruik.
    """

    woonkamer_of_keuken = Referentiedata(
        code="WOK",
        naam="Woonkamer/keuken",
    )
    # woonkamer_of_keuken = ("WOK", "Woonkamer/keuken")
    """
    Vertrek: ruimte met een gecombineerde functie van keuken en woonkamer
    """

    woonkamer = Referentiedata(
        code="WOO",
        naam="Woonkamer",
    )
    # woonkamer = ("WOO", "Woonkamer")
    """
    Vertrek: de kamer in een huis waar het dagelijkse gezinsleven zich afspeelt. Het is
    een van de grootste vertrekken en bevindt zich meestal op de begane grond, voor
    zover het niet gaat om een appartement in een flat.
    """

    woon_of_slaapkamer = Referentiedata(
        code="WSL",
        naam="Woon-/slaapkamer",
    )
    # woon_of_slaapkamer = ("WSL", "Woon-/slaapkamer")
    """
    Vertrek: ruimte met een gecombineerde functie van woonkamer en slaapkamer.
    """

    zijtuin = Referentiedata(
        code="ZIJ",
        naam="Zijtuin",
    )
    # zijtuin = ("ZIJ", "Zijtuin")
    """
    Buitenruimte: tuin gelegen aan de zijkant van een woning.
    """

    loggia = Referentiedata(
        code="LOG",
        naam="Loggia",
    )
    # loggia = ("LOG", "Loggia")
    """
    Buitenruimte: een inpandig balkon.
    """

    zolder = Referentiedata(
        code="ZOL",
        naam="Zolder",
    )
    # zolder = ("ZOL", "Zolder")
    """
    Overige ruimte: is de bovenste verdieping direct onder het dak van een gebouw met
    een vaste trap zoals gedefinieerd voor het bepalen van de woningwaardering. De term
    wordt vooral gebruikt bij gebouwen met een puntdak. De bovenste verdieping van een
    gebouw met plat dak wordt meestal geen zolder genoemd. Een ruimte mag als vertrek
    worden gezien indien deze een vast trap heeft, de vloer begaanbaar en het dak
    beschoten is. Zolders zonder vaste trap leggen we niet vast als vertrek. Indien een
    woning een zolder heeft met een vlizotrap kan dit in de advertentietekst worden
    gemeld.
    """
