
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PRIJSCOMPONENTDETAILSOORT:

    administratiekosten = Referentiedata(
        code="AKO",
        naam="Administratiekosten",
    )
    # administratiekosten = ("AKO", "Administratiekosten")

    alarm_bewaking = Referentiedata(
        code="ALA",
        naam="Alarm bewaking",
    )
    # alarm_bewaking = ("ALA", "Alarm bewaking")
    """
    Maandelijkse kosten voor het alarm en de bewaking van de woning
    """

    servicekosten_bedrijfsruimten = Referentiedata(
        code="BED",
        naam="Servicekosten bedrijfsruimten",
    )
    # servicekosten_bedrijfsruimten = ("BED", "Servicekosten bedrijfsruimten")
    """
    Maandelijkse kosten voor services m.b.t. bedrijfsruimten
    """

    beheerders = Referentiedata(
        code="BEH",
        naam="Beheerder(s)",
    )
    # beheerders = ("BEH", "Beheerder(s)")
    """
    Maandelijkse kosten voor de beheerder(s) van de eenheid en/of het complex
    """

    borg = Referentiedata(
        code="BOR",
        naam="Borg",
    )
    # borg = ("BOR", "Borg")

    dienst_en_recreatieruimten = Referentiedata(
        code="DIE",
        naam="Dienst- en recreatieruimten",
    )
    # dienst_en_recreatieruimten = ("DIE", "Dienst- en recreatieruimten")
    """
    De maandelijkse kosten voor reparaties en groot onderhoud aan dienstruimten en
    recreatieruimten. Deze kosten komen meestal voor bij senioren- of bejaardenwoningen.
    Het gaat niet om de inventaris, het schoonmaken van de ruimten of onderhoud aan de
    tuin.
    """

    electriciteit = Referentiedata(
        code="ELE",
        naam="Electriciteit",
    )
    # electriciteit = ("ELE", "Electriciteit")

    elektrische_installaties = Referentiedata(
        code="ELI",
        naam="Elektrische installaties",
    )
    # elektrische_installaties = ("ELI", "Elektrische installaties")
    """
    Maandelijkse kosten voor het gebruik van elektrische installaties
    """

    elektra_oplaadpunt = Referentiedata(
        code="ELO",
        naam="Elektra oplaadpunt",
    )
    # elektra_oplaadpunt = ("ELO", "Elektra oplaadpunt")
    """
    Maandelijkse kosten voor het gebruik van een oplaadpunt voor andere elektrische
    apparaten dan een elektrische auto (b.v. scootmobiel)
    """

    energie_voor_gemeenschappelijke_ruimten = Referentiedata(
        code="ENE",
        naam="Energie voor gemeenschappelijke ruimten",
    )
    # energie_voor_gemeenschappelijke_ruimten = ("ENE", "Energie voor gemeenschappelijke ruimten")
    """
    Dit zijn bijvoorbeeld de maandelijkse kosten voor elektriciteit voor bijvoorbeeld:
    lift, verlichting, ventilatie, alarminstallatie. Alleen voor gemeenschappelijke
    ruimten.
    """

    energieprestatievergoeding = Referentiedata(
        code="EPV",
        naam="Energieprestatievergoeding",
    )
    # energieprestatievergoeding = ("EPV", "Energieprestatievergoeding")
    """
    Een vergoeding die verhuurder aan huurder mag vragen voor een huurwoning die zelf
    energie opwekt
    """

    gas = Referentiedata(
        code="GAS",
        naam="Gas",
    )
    # gas = ("GAS", "Gas")

    reparatie_gem_ruimten = Referentiedata(
        code="GEM",
        naam="Reparatie gem. ruimten",
    )
    # reparatie_gem_ruimten = ("GEM", "Reparatie gem. ruimten")
    """
    Maandelijkse kosten voor het repareren van defecten aan gemeenschappelijke ruimten
    """

    gladheidsbestrijding = Referentiedata(
        code="GHB",
        naam="Gladheidsbestrijding",
    )
    # gladheidsbestrijding = ("GHB", "Gladheidsbestrijding")
    """
    Maandelijkse kosten voor het bestrijden van gladheid rondom de eenheid
    """

    glasbewassing = Referentiedata(
        code="GLB",
        naam="Glasbewassing",
    )
    # glasbewassing = ("GLB", "Glasbewassing")
    """
    Maandelijkse kosten voor het wassen van glas van ramen en deuren van de eenheid
    """

    glasfonds = Referentiedata(
        code="GLF",
        naam="Glasfonds",
    )
    # glasfonds = ("GLF", "Glasfonds")
    """
    Maandelijkse kosten voor de voorziening voor repareren van glasschade
    """

    groenvoorziening = Referentiedata(
        code="GRO",
        naam="Groenvoorziening",
    )
    # groenvoorziening = ("GRO", "Groenvoorziening")
    """
    Maandelijkse kosten voor het onderhouden van de groenvoorziening rondom de eenheid
    """

    huismeester = Referentiedata(
        code="HUI",
        naam="Huismeester",
    )
    # huismeester = ("HUI", "Huismeester")
    """
    De maandelijkse kosten voor de diensten die de huismeester, flatwacht, wijkbeheerder
    of conciërge levert.
    """

    huisvuil = Referentiedata(
        code="HUV",
        naam="Huisvuil",
    )
    # huisvuil = ("HUV", "Huisvuil")
    """
    Maandelijkse kosten voor het verwerken van huisvuil
    """

    individuele_garage = Referentiedata(
        code="IGA",
        naam="Individuele garage",
    )
    # individuele_garage = ("IGA", "Individuele garage")
    """
    Inpandige parkeerplek individueel
    """

    installaties = Referentiedata(
        code="INS",
        naam="Installaties",
    )
    # installaties = ("INS", "Installaties")
    """
    Maandelijkse kosten voor het gebruik van andere installaties dan elektrische
    installaties
    """

    inventaris = Referentiedata(
        code="INV",
        naam="Inventaris",
    )
    # inventaris = ("INV", "Inventaris")
    """
    Maandelijkse kosten voor het gebruik van inventaris
    """

    kale_huur = Referentiedata(
        code="KAL",
        naam="Kale huur",
    )
    # kale_huur = ("KAL", "Kale huur")
    """
    Basisbedrag voor het gebruik van de woning
    """

    laadpaal = Referentiedata(
        code="LAA",
        naam="Laadpaal",
    )
    # laadpaal = ("LAA", "Laadpaal")
    """
    Maandelijkse kosten voor het gebruik van een laadpaal voor elektrische auto
    """

    liftkosten = Referentiedata(
        code="LIF",
        naam="Liftkosten",
    )
    # liftkosten = ("LIF", "Liftkosten")
    """
    Maandelijkse kosten voor het gebruik van de lift(en)
    """

    linnenpakket = Referentiedata(
        code="LIN",
        naam="Linnenpakket",
    )
    # linnenpakket = ("LIN", "Linnenpakket")
    """
    Maandelijkse kosten voor het gebruik van linnen
    """

    matiging_huurtoeslag = Referentiedata(
        code="MAT",
        naam="Matiging huurtoeslag",
    )
    # matiging_huurtoeslag = ("MAT", "Matiging huurtoeslag")
    """
    Component voor het matigen van de huurprijs op basis van toegekende huurtoeslag
    conform de wettelijke regeling van vóór 2014. Dit component is alleen bedoeld voor
    het uitwisselen van historische data
    """

    mechanische_ventilatie = Referentiedata(
        code="MVE",
        naam="Mechanische ventilatie",
    )
    # mechanische_ventilatie = ("MVE", "Mechanische ventilatie")
    """
    Maandelijkse kosten voor het gebruik van de mechanische ventilatie
    """

    overnamekosten = Referentiedata(
        code="OKO",
        naam="Overnamekosten",
    )
    # overnamekosten = ("OKO", "Overnamekosten")

    onderhoudsabonnement = Referentiedata(
        code="OND",
        naam="Onderhoudsabonnement",
    )
    # onderhoudsabonnement = ("OND", "Onderhoudsabonnement")
    """
    Maandelijkse kosten voor onderhoudsabonnement. De huurder is zelf verantwoordelijk
    voor het klein onderhoud aan de woning. Als de huurder een onderhoudsabonnement
    afsluit, dan regelt de corporatie het klein onderhoud voor de huurder.
    """

    overige_netto_huur_component = Referentiedata(
        code="ONH",
        naam="Overige netto huur component",
    )
    # overige_netto_huur_component = ("ONH", "Overige netto huur component")
    """
    Een overige netto huur component wordt bijvoorbeeld gebruikt om de extra huur na het
    aanbrengen van (verduurzamings-) verbeteringen te onderscheiden van de basis kale
    huur.
    """

    overige_kosten_gem_ruimten = Referentiedata(
        code="OVE",
        naam="Overige kosten gem. ruimten",
    )
    # overige_kosten_gem_ruimten = ("OVE", "Overige kosten gem. ruimten")
    """
    Maandelijkse kosten voor overige kosten voor gemeenschappelijke ruimten (naast
    schoonmaak, energie en reparatie)
    """

    parkeerplaats_buiten = Referentiedata(
        code="PBU",
        naam="Parkeerplaats buiten",
    )
    # parkeerplaats_buiten = ("PBU", "Parkeerplaats buiten")
    """
    Uitpandige parkeerplek
    """

    parkeergarage = Referentiedata(
        code="PGA",
        naam="Parkeergarage",
    )
    # parkeergarage = ("PGA", "Parkeergarage")
    """
    Inpandige parkeerplek collectief
    """

    rioolfonds = Referentiedata(
        code="RIO",
        naam="Rioolfonds",
    )
    # rioolfonds = ("RIO", "Rioolfonds")
    """
    Maandelijkse kosten voor de voorziening voor het repareren van problemen aan het
    riool
    """

    schoonmaak_eenheid = Referentiedata(
        code="SCE",
        naam="Schoonmaak eenheid",
    )
    # schoonmaak_eenheid = ("SCE", "Schoonmaak eenheid")
    """
    Maandelijkse kosten voor schoonmaak van de eenheid
    """

    schoonmaak_van_gemeenschappelijke_ruimten = Referentiedata(
        code="SCH",
        naam="Schoonmaak van gemeenschappelijke ruimten",
    )
    # schoonmaak_van_gemeenschappelijke_ruimten = ("SCH", "Schoonmaak van gemeenschappelijke ruimten")
    """
    De maandelijkse schoonmaakkosten voor de lift en andere gemeenschappelijke ruimten,
    zoals een galerij, trappenhuis of recreatieruimte
    """

    signaallevering_o_a_cai = Referentiedata(
        code="SIG",
        naam="Signaallevering (o.a. CAI)",
    )
    # signaallevering_o_a_cai = ("SIG", "Signaallevering (o.a. CAI)")
    """
    Maandelijkse kosten voor signaallevering (o.a. CAI)
    """

    schoorsteenvegen = Referentiedata(
        code="STV",
        naam="Schoorsteenvegen",
    )
    # schoorsteenvegen = ("STV", "Schoorsteenvegen")
    """
    Maandelijkse kosten voor het vegen van de schoorsteen
    """

    verenigingskosten = Referentiedata(
        code="VER",
        naam="Verenigingskosten",
    )
    # verenigingskosten = ("VER", "Verenigingskosten")
    """
    Maandelijkse kosten voor lidmaatschap van verenigingen
    """

    volkstuin = Referentiedata(
        code="VOL",
        naam="Volkstuin",
    )
    # volkstuin = ("VOL", "Volkstuin")
    """
    Maandelijkse kosten voor het gebruik van een volkstuin
    """

    vve_kosten = Referentiedata(
        code="VVE",
        naam="VVE kosten",
    )
    # vve_kosten = ("VVE", "VVE kosten")
    """
    Maandelijkse kosten voor VVE-lidmaatschap
    """

    verzekeringskosten = Referentiedata(
        code="VZE",
        naam="Verzekeringskosten",
    )
    # verzekeringskosten = ("VZE", "Verzekeringskosten")
    """
    Maandelijkse kosten voor verzekeringen
    """

    warmte_installaties = Referentiedata(
        code="WAI",
        naam="Warmte-installaties",
    )
    # warmte_installaties = ("WAI", "Warmte-installaties")
    """
    Maandelijkse kosten voor het gebruik van installaties voor verwarming van de
    vertrekken van de eenheid
    """

    warmte = Referentiedata(
        code="WAR",
        naam="Warmte",
    )
    # warmte = ("WAR", "Warmte")
    """
    Centrale verwarming, Stadsverwarming, etc.
    """

    water = Referentiedata(
        code="WAT",
        naam="Water",
    )
    # water = ("WAT", "Water")

    witgoed = Referentiedata(
        code="WIT",
        naam="Witgoed",
    )
    # witgoed = ("WIT", "Witgoed")
    """
    Maandelijkse kosten voor het gebruik van witgoed (bijvoorbeeld wasmachine of droger)
    """

    warmwaterinstallaties = Referentiedata(
        code="WWI",
        naam="Warmwaterinstallaties",
    )
    # warmwaterinstallaties = ("WWI", "Warmwaterinstallaties")
    """
    Maandelijkse kosten voor het gebruik van installaties voor warm water
    """

    zonnepanelen = Referentiedata(
        code="ZON",
        naam="Zonnepanelen",
    )
    # zonnepanelen = ("ZON", "Zonnepanelen")
    """
    Maandelijkse kosten voor het gebruik van zonnepanelen
    """

    zonwering = Referentiedata(
        code="ZWE",
        naam="Zonwering",
    )
    # zonwering = ("ZWE", "Zonwering")
    """
    Maandelijkse kosten voor het gebruik van zonwering
    """
