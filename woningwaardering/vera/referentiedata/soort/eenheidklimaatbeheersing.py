from vera.bvg.generated import Referentiedata


class Eenheidklimaatbeheersing:
    airco = Referentiedata(
        code="AIR",
        naam="Airco",
    )
    """
    Een airconditioner (airco) is een apparaat dat de luchttemperatuur en vochtigheid in
    een ruimte regelt voor comfortabele omstandigheden. Het werkt door warme lucht uit
    de ruimte te verwijderen, te koelen via een koelmiddel zoals freon, en vervolgens
    gekoelde lucht terug te blazen om de gewenste temperatuur te handhaven. Dit kan
    zowel individueel als collectief georganiseerd zijn.
    """

    blokverwarming = Referentiedata(
        code="BLO",
        naam="Blokverwarming",
    )
    """
    Blokverwarming is een centraal verwarmingssysteem dat wordt gebruikt in gebouwen met
    meerdere woningen. In plaats van individuele cv-ketels hebben alle woningen een
    gemeenschappelijke warmtebron, meestal een centrale ketelinstallatie. Warm water
    wordt via leidingen naar radiatoren in elke woning gestuurd om de ruimtes te
    verwarmen.
    """

    centrale_verwarming = Referentiedata(
        code="CEV",
        naam="Centrale verwarming",
    )
    """
    Centrale verwarming is een systeem waarbij warmte wordt geproduceerd op één centrale
    locatie, meestal een ketel, en vervolgens via leidingen naar verschillende ruimtes
    in een gebouw wordt verspreid. Dit wordt vaak gedaan door radiatoren,
    vloerverwarming of convectoren, waardoor een gelijkmatige warmteverdeling door het
    hele gebouw wordt bereikt. Dit kan zowel individueel als collectief georganiseerd
    zijn.
    """

    gaskachels = Referentiedata(
        code="GAS",
        naam="Gaskachels",
    )
    """
    Een gaskachel is een verwarmingstoestel dat werkt op aardgas of propaan. Het bevat
    een brander die gas verbrandt om warmte te produceren, waardoor de
    omgevingstemperatuur wordt verhoogd voor comfort in een ruimte.
    """

    houtkachel = Referentiedata(
        code="HKA",
        naam="Houtkachel",
    )
    """
    Een houtkachel is een verwarmingstoestel dat brandt op hout als brandstof. Het heeft
    een vuurhaard waarin hout wordt verbrand om warmte te genereren, waardoor een ruimte
    wordt verwarmd voor comfort.
    """

    muurverwarming = Referentiedata(
        code="MUU",
        naam="Muurverwarming",
    )
    """
    Muurverwarming is een verwarmingssysteem waarbij warmte wordt gegenereerd door
    leidingen die in de muren zijn ingebed. Warm water stroomt door deze leidingen,
    waardoor de muren warmte afgeven en de ruimte gelijkmatig verwarmen.
    """

    mechanische_ventilatie = Referentiedata(
        code="MVE",
        naam="Mechanische ventilatie",
    )
    """
    Mechanische ventilatie is een systeem dat wordt gebruikt om verse lucht in gebouwen
    te brengen en vervuilde lucht af te voeren. Het maakt gebruik van ventilatoren om
    luchtstromen te creëren en te reguleren voor een gezond binnenklimaat. Dit kan zowel
    individueel als collectief georganiseerd zijn.
    """

    open_haard = Referentiedata(
        code="OHA",
        naam="Open haard",
    )
    """
    Een open haard is een vuurplaats in een huis met een opening waarin hout of andere
    brandbare materialen worden verbrand. Het biedt warmte, sfeer en soms ook
    kookmogelijkheden.
    """

    stadsverwarming = Referentiedata(
        code="STV",
        naam="Stadsverwarming",
    )
    """
    Stadsverwarming is een systeem waarbij warmte wordt geproduceerd op één centrale
    locatie, meestal een energiecentrale, en vervolgens via een netwerk van leidingen
    naar huizen en bedrijven in een stad wordt getransporteerd. De warmte wordt gebruikt
    voor ruimteverwarming, tapwaterverwarming en soms ook voor industriële processen,
    wat bijdraagt aan energie-efficiëntie.
    """

    vloerverwarming = Referentiedata(
        code="VLV",
        naam="Vloerverwarming",
    )
    """
    Vloerverwarming is een verwarmingssysteem waarbij warmte wordt afgegeven via
    leidingen onder de vloer. Warm water stroomt door deze leidingen, waardoor de vloer
    wordt verwarmd en de warmte gelijkmatig wordt verspreid in de ruimte.
    """

    volledig_elektrisch = Referentiedata(
        code="VOL",
        naam="Volledig Elektrisch",
    )
    """
    Volledig elektrische klimaatbeheersing
    """

    warmtepomp_cv = Referentiedata(
        code="WAC",
        naam="Warmtepomp CV",
    )
    """
    Warmtepomp i.c.m. CV-ketel voor verwarming en warm water. Ook wel een hybride
    waterpomp genoemd. Dit kan zowel individueel als collectief georganiseerd zijn.
    """

    warmtepomp = Referentiedata(
        code="WAR",
        naam="Warmtepomp",
    )
    """
    Volledig elektrische warmtepomp voor verwarming en warm water. Dit kan zowel
    individueel als collectief georganiseerd zijn.
    """

    warmte_koudeopslaginstallatie = Referentiedata(
        code="WKO",
        naam="Warmte- koudeopslaginstallatie",
    )
    """
    Een warmte-koudeopslaginstallatie (WKO) is een duurzaam verwarmingssysteem dat
    warmte in de zomer uit een gebouw haalt en opslaat in de grond, om het in de winter
    weer te gebruiken voor verwarming. Er is altijd sprake een (bodem-)waterpomp Dit kan
    zowel individueel als collectief georganiseerd zijn.
    """

    warmteterugwinsysteem = Referentiedata(
        code="WTW",
        naam="Warmteterugwinsysteem",
    )
    """
    Een warmteterugwinsysteem (WTW) is een installatie die de warmte uit afgevoerde
    lucht recupereert en gebruikt om de binnenkomende verse lucht te verwarmen, waardoor
    energie wordt bespaard en het binnenklimaat wordt verbeterd. Dit kan zowel
    individueel als collectief georganiseerd zijn.
    """
