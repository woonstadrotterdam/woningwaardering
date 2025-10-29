from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RelatierolsoortReferentiedata(Referentiedata):
    pass


class Relatierolsoort(Referentiedatasoort):
    aankopende_makelaar = RelatierolsoortReferentiedata(
        code="AMA",
        naam="Aankopende makelaar",
    )
    """
    Makelaar die namens de aankopende partij optreedt
    """

    ambulante_begeleider = RelatierolsoortReferentiedata(
        code="AMB",
        naam="Ambulante begeleider",
    )
    """
    De ambulant begeleider helpt mensen om regie te voeren over hun eigen leven en zo
    veel mogelijk zelfstandig te functioneren.
    """

    assetmanager = RelatierolsoortReferentiedata(
        code="ASS",
        naam="Assetmanager",
    )
    """
    De assetmanager voor het betreffende vastgoed
    """

    behandelaar = RelatierolsoortReferentiedata(
        code="BED",
        naam="Behandelaar",
    )
    """
    De behandelaar (van een specifieke actie, zaak of taak). Dit is meestal een
    medewerker van de corporatie maar kan ook een externe behandelaar zijn
    """

    beheerder = RelatierolsoortReferentiedata(
        code="BEH",
        naam="Beheerder",
    )
    """
    De beheerder van een eenheid of cluster
    """

    betaler = RelatierolsoortReferentiedata(
        code="BET",
        naam="Betaler",
    )
    """
    Betaler, vooral van belang als de betaler een andere relatie is dan de huurder of
    contractant. Iemand anders betaalt dan namens de huurder, vanaf een eigen
    bankrekening. Zie ook Bewindvoerder (die vanaf de rekening van de huurder
    betaalt).
    """

    bewoner = RelatierolsoortReferentiedata(
        code="BEW",
        naam="Bewoner",
    )
    """
    Persoon die volgens het GBA een verblijfseenheid/woning stelselmatig bewoont (CORA).
    Als de bewoner ook de huurder is, dan ook ook Huurder worden gebruikt.Zie ook
    Gebruiker.
    """

    bestuurslid = RelatierolsoortReferentiedata(
        code="BSL",
        naam="Bestuurslid",
    )
    """
    Iemand die deel uitmaakt van een bestuur, bijvoorbeeld van een VvE of
    bewonersvereniging, en daarin de rol van Algemeen bestuurslid heeft. Voor
    bestuursleden met de rol van Voorzitter, Secretaris en Penningmeester zijn
    afzonderlijke relatierolsoorten beschikbaar
    """

    budgetcoach = RelatierolsoortReferentiedata(
        code="BUD",
        naam="Budgetcoach",
    )
    """
    Synoniem: budgetbeheerder. De relatie is budgetcoach van een andere relatie zonder
    rechterlijke beschikking en voert financieel beheer voor deze relatie uit. Voor
    het financieel beheer wordt een aparte beheerrekening geopend waarvan betalingen
    voor de vaste lasten worden uitgevoerd door budgetcoach.
    """

    bewindvoerder = RelatierolsoortReferentiedata(
        code="BWI",
        naam="Bewindvoerder",
    )
    """
    De relatie is bewindvoerder van een andere relatie, bijvoorbeeld in het kader van de
    WSNP (Huurder Jansen staat onder bewindvoering van meneer Karelse). De
    bewindvoerder betaalt vanaf de bankrekening van de huurder. Zie ook Betaler
    (namens een huurder betaalt, maar vanaf een eigen bankrekening)
    """

    wooncooperatie_lid = RelatierolsoortReferentiedata(
        code="COL",
        naam="Wooncoöperatie-lid",
    )
    """
    Lid van een wooncoöperatie. Niet te verwarren met de relatierolsoort Wooncoöperatie
    (rechtspersoon). Let op dat voor bestuursleden afzonderlijke relatierolsoorten
    beschikbaar zijn: Bestuurslid, Voorzitter, Penningmeester, Secretaris.
    """

    wooncooperatie = RelatierolsoortReferentiedata(
        code="COO",
        naam="Wooncoöperatie",
    )
    """
    Een wooncoöperatie is een vereniging waarvan de leden tevens eigenaren zijn en die
    voorziet in bepaalde materiële behoefte van de deelnemers.De wooncoöperatie is
    de meest verregaande vorm van zelforganisatie waarin bewoners voor het onderhoud
    en beheer van hun woningen zelf verantwoordelijk zijn. Sinds 1 juli 2015 maakt
    de wooncoöperatie deel uit van de Woningwet: Groepen met interesse kunnen
    ondersteuning krijgen bij het opstellen van een plan en dat indienen bij hun
    corporatie. Er zijn daarnaast steeds meer groepen die zelf een stuk grond willen
    bebouwen en de woningen aan hun leden willen verhure (CORA).  Niet te verwarren
    met de relatierolsoort Wooncoöperatie-lid
    """

    contactpersoon = RelatierolsoortReferentiedata(
        code="CPE",
        naam="Contactpersoon",
    )
    """
    Een contactpersoon is een natuurlijke persoon die één of meer relaties, eenheden, of
    clusters vertegenwoordigt
    """

    deurwaarder = RelatierolsoortReferentiedata(
        code="DEU",
        naam="Deurwaarder",
    )
    """
    De relatie is de deurwaarder van een andere relatie.  (Huurder Jansen heeft een
    huurschuld en wordt extern geincasseerd door deurwaarder Karelse)
    """

    eigenaar = RelatierolsoortReferentiedata(
        code="EIG",
        naam="Eigenaar",
    )
    """
    Een eigenaar van vastgoed kan een VVE-lid zijn indien het eigendom een
    appartementsrecht betreft. Indien sprake is van bloot eigendom, dan is de
    eigenaar geen VVE-lid. De eigenaar kan het appartementsrecht of bloot eigendom
    hebben gekocht van de woningcorporatie (CORA). Bij een koop-/verkooptransactie
    heeft de eigenaar tevens de rol van verkoper.
    """

    erfpachter = RelatierolsoortReferentiedata(
        code="ERF",
        naam="Erfpachter",
    )
    """
    De erfpachter is de persoon of organisatie die eigenaar is van het object waarop de
    erfpacht rust. De erfpachter betaalt de canon. Erfpacht is overdraagbaar en gaat
    over met de verkoop van de woning, het appartement of ander onroerend goed
    (CORA)
    """

    fiatteur = RelatierolsoortReferentiedata(
        code="FIA",
        naam="Fiatteur",
    )
    """
    De medewerker die verantwoordelijk is voor het goedkeuren van een financiële
    activiteit
    """

    garantiegever = RelatierolsoortReferentiedata(
        code="GAR",
        naam="Garantiegever",
    )
    """
    De garantiegever bij een lening
    """

    gebruiker = RelatierolsoortReferentiedata(
        code="GEB",
        naam="Gebruiker",
    )
    """
    Persoon die een eenheid gebruikt, maar niet zozeer bewoont. Vooral van toepassing
    bij niet-woongelegenheden, zoals BOG en MOG. Als de gebruiker ook de huurder is,
    dan ook ook Huurder worden gebruikt. Zie ook Bewoner.
    """

    geldnemer = RelatierolsoortReferentiedata(
        code="GEL",
        naam="Geldnemer",
    )
    """
    De geldnemer van de lening
    """

    huismeester = RelatierolsoortReferentiedata(
        code="HME",
        naam="Huismeester",
    )
    """
    De huismeester voor het betreffende vastgoed
    """

    huurder = RelatierolsoortReferentiedata(
        code="HUU",
        naam="Huurder",
    )
    """
    De huurder is een de (rechts)persoon die met de woningcorporatie een
    huurovereenkomst heeft gesloten en daarmee het exclusief gebruiksrecht heeft
    verkregen van het vastgoed dat aan de huurder wordt verhuurd en waarvoor de
    huurder een netto huur betaald (CORA). Synoniem aan het begrip Hoofdhuurder
    """

    inspecteur = RelatierolsoortReferentiedata(
        code="INS",
        naam="Inspecteur",
    )
    """
    Medewerker die de inspectie uitvoert
    """

    koper = RelatierolsoortReferentiedata(
        code="KOP",
        naam="Koper",
    )
    """
    De koper verkrijgt het bloot eigendom van de opstal (evt. in combinatie met het
    bloot eigendom of het pachtrecht van het onderliggende perceel respectievelijk
    het appartementsrecht) en kan afhankelijk van de regeling op termijn verkoper
    zijn van de opstal (met verzoek beeindiging van vigerende erfpachtregeling) of
    het appartementsrecht. Koper wordt dus verkoper indien sprake is van het proces
    terugkopen eenheid. (CORA). De verkoper is de eigenaar van de eenheid, op het
    moment van verkoop
    """

    leverancier = RelatierolsoortReferentiedata(
        code="LEV",
        naam="Leverancier",
    )
    """
    Een leverancier is een relatie die diensten of goederen levert, zou kunnen gaan
    leveren of heeft geleverd aan de woningcorporatie (CORA)
    """

    medebewoner = RelatierolsoortReferentiedata(
        code="MBW",
        naam="Medebewoner",
    )
    """
    Kinderen of volwassenen die met de hoofdbewoner of hoofdaanvrager een huishouden
    (willen) vormen.
    """

    medehuurder = RelatierolsoortReferentiedata(
        code="MDH",
        naam="Medehuurder",
    )
    """
    Op de huurovereenkomst vermelde medehuurder
    """

    medewerker = RelatierolsoortReferentiedata(
        code="MDW",
        naam="Medewerker",
    )
    """
    Werknemers ingehuurd of in vaste dienst van een woningcorporatie (CORA)
    """

    mede_aanvrager = RelatierolsoortReferentiedata(
        code="MED",
        naam="Mede aanvrager",
    )
    """
    Een woningzoekende die samen met een andere woningzoekende (de (hoofd)aanvrager) een
    woning (of ander vastgoed)zoekt.
    """

    melder = RelatierolsoortReferentiedata(
        code="MEL",
        naam="Melder",
    )
    """
    De melder van een verzoek of incident. Vaak de initiator van een (werk-)proces.
    """

    notaris = RelatierolsoortReferentiedata(
        code="NOT",
        naam="Notaris",
    )
    """
    Notaris die een koop-/verkooptransactie formeel bekrachtigt
    """

    opdrachtgever = RelatierolsoortReferentiedata(
        code="OPD",
        naam="Opdrachtgever",
    )
    """
    Opdrachtgevende partij
    """

    opdrachtnemer = RelatierolsoortReferentiedata(
        code="OPN",
        naam="Opdrachtnemer",
    )
    """
    Opdrachtnemende partij
    """

    opzichter = RelatierolsoortReferentiedata(
        code="OPZ",
        naam="Opzichter",
    )
    """
    De opzichter voor het betreffende vastgoed
    """

    onderwijsinstelling = RelatierolsoortReferentiedata(
        code="OWI",
        naam="Onderwijsinstelling",
    )

    penningmeester = RelatierolsoortReferentiedata(
        code="PEN",
        naam="Penningmeester",
    )
    """
    Iemand die deel uitmaakt van een bestuur, bijvoorbeeld van een VvE of
    bewonersvereniging, en daarin de rol van Penningmeester heeft
    """

    prospect = RelatierolsoortReferentiedata(
        code="PRO",
        naam="Prospect",
    )
    """
    Een prospect is een relatie die belangstelling heeft om een dienst of product van de
    woningcorporatie af te nemen. Gebruik eventueel Woningzoekende om meer concreet
    te zijn.
    """

    secretaris = RelatierolsoortReferentiedata(
        code="SEC",
        naam="Secretaris",
    )
    """
    Iemand die deel uitmaakt van een bestuur, bijvoorbeeld van een VvE of
    bewonersvereniging, en daarin de rol van Secretaris heeft
    """

    verkoper = RelatierolsoortReferentiedata(
        code="VER",
        naam="Verkoper",
    )
    """
    Verkopende partij
    """

    verkopende_makelaar = RelatierolsoortReferentiedata(
        code="VMA",
        naam="Verkopende makelaar",
    )
    """
    Makelaar die namens de verkopende partij optreedt
    """

    voorzitter = RelatierolsoortReferentiedata(
        code="VOO",
        naam="Voorzitter",
    )
    """
    Iemand die deel uitmaakt van een bestuur, bijvoorbeeld van een VvE of
    bewonersvereniging, en daarin de rol van Voorzitter heeft
    """

    vereniging_van_eigenaren = RelatierolsoortReferentiedata(
        code="VVE",
        naam="Vereniging van Eigenaren",
    )
    """
    Dit is de vereniging die is ontstaan na een (onder)splitsing en als vereniging
    verantwoordelijk is voor het beheer van de collectieve delen van het vastgoed
    zoals die in de splitsingsakte zijn beschreven. Een vereniging van Eigenaren kan
    weer zelf lid zijn van een andere vereniging van Eigenaren indien sprake is van
    een hoofd- en ondersplitsing (CORA).Niet te verwarren met de relatierolsoort
    VvE-lid
    """

    vve_lid = RelatierolsoortReferentiedata(
        code="VVL",
        naam="VvE-lid",
    )
    """
    Een eigenaar van een appartementsrecht is vanuit die hoedanigheid altijd lid van de
    rechtspersoon VvE. Een VvE-lid kan een natuurlijk persoon of een rechtspersoon
    zijn.  (CORA). Niet te verwarren met de relatierolsoort VvE (rechtspersoon). Let
    op dat voor bestuursleden afzonderlijke relatierolsoorten beschikbaar zijn:
    Bestuurslid, Voorzitter, Penningmeester, Secretaris.
    """

    woningzoekende = RelatierolsoortReferentiedata(
        code="WON",
        naam="Woningzoekende",
    )
    """
    Een woningzoekende is een persoon die zich heeft gemeld/ingeschreven met de intentie
    (met het nog te vormen) huishouden te verhuizen naar een andere woning en
    daarvoor woonwensen kenbaar heeft gemaakt en graag in aanmerking komt voor
    passend vrijkomend woningaanbod. Zodra de woningzoekende dient te betalen voor
    de inschrijving, is sprake van een klantrelatie. Synoniem aan Hoofdaanvrager
    """

    woonconsulent = RelatierolsoortReferentiedata(
        code="WOO",
        naam="Woonconsulent",
    )
    """
    De woonconsulent voor het betreffende vastgoed
    """

    zekerheidsnemer = RelatierolsoortReferentiedata(
        code="ZEK",
        naam="Zekerheidsnemer",
    )
    """
    De relatie aan wie de zekerheid op de eenheid is verleend bij een eventuele
    zekerheidsverpanding
    """
