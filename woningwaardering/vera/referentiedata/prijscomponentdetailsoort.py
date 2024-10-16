from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.prijscomponentsoort import Prijscomponentsoort


class Prijscomponentdetailsoort(Enum):
    administratiekosten = Referentiedata(
        code="AKO",
        naam="Administratiekosten",
        parent=Prijscomponentsoort.eenmalig.value,
    )

    alarm_bewaking = Referentiedata(
        code="ALA",
        naam="Alarm bewaking",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het alarm en de bewaking van de woning
    """

    servicekosten_bedrijfsruimten = Referentiedata(
        code="BED",
        naam="Servicekosten bedrijfsruimten",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor services m.b.t. bedrijfsruimten
    """

    beheerders = Referentiedata(
        code="BEH",
        naam="Beheerder(s)",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor de beheerder(s) van de eenheid en/of het complex
    """

    borg = Referentiedata(
        code="BOR",
        naam="Borg",
        parent=Prijscomponentsoort.eenmalig.value,
    )

    dienst_en_recreatieruimten = Referentiedata(
        code="DIE",
        naam="Dienst- en recreatieruimten",
        parent=Prijscomponentsoort.service.value,
    )
    """
    De maandelijkse kosten voor reparaties en groot onderhoud aan dienstruimten en
    recreatieruimten. Deze kosten komen meestal voor bij senioren- of
    bejaardenwoningen. Het gaat niet om de inventaris, het schoonmaken van de
    ruimten of onderhoud aan de tuin.
    """

    electriciteit = Referentiedata(
        code="ELE",
        naam="Electriciteit",
        parent=Prijscomponentsoort.verbruik.value,
    )

    elektrische_installaties = Referentiedata(
        code="ELI",
        naam="Elektrische installaties",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van elektrische installaties
    """

    elektra_oplaadpunt = Referentiedata(
        code="ELO",
        naam="Elektra oplaadpunt",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van een oplaadpunt voor andere elektrische
    apparaten dan een elektrische auto (b.v. scootmobiel)
    """

    energie_voor_gemeenschappelijke_ruimten = Referentiedata(
        code="ENE",
        naam="Energie voor gemeenschappelijke ruimten",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Dit zijn bijvoorbeeld de maandelijkse kosten voor elektriciteit voor bijvoorbeeld:
    lift, verlichting, ventilatie, alarminstallatie. Alleen voor gemeenschappelijke
    ruimten.
    """

    energieprestatievergoeding = Referentiedata(
        code="EPV",
        naam="Energieprestatievergoeding",
        parent=Prijscomponentsoort.verbruik.value,
    )
    """
    Een vergoeding die verhuurder aan huurder mag vragen voor een huurwoning die zelf
    energie opwekt
    """

    gas = Referentiedata(
        code="GAS",
        naam="Gas",
        parent=Prijscomponentsoort.verbruik.value,
    )

    reparatie_gem_ruimten = Referentiedata(
        code="GEM",
        naam="Reparatie gem. ruimten",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het repareren van defecten aan gemeenschappelijke ruimten
    """

    gladheidsbestrijding = Referentiedata(
        code="GHB",
        naam="Gladheidsbestrijding",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het bestrijden van gladheid rondom de eenheid
    """

    glasbewassing = Referentiedata(
        code="GLB",
        naam="Glasbewassing",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het wassen van glas van ramen en deuren van de eenheid
    """

    glasfonds = Referentiedata(
        code="GLF",
        naam="Glasfonds",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor de voorziening voor repareren van glasschade
    """

    groenvoorziening = Referentiedata(
        code="GRO",
        naam="Groenvoorziening",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het onderhouden van de groenvoorziening rondom de eenheid
    """

    huismeester = Referentiedata(
        code="HUI",
        naam="Huismeester",
        parent=Prijscomponentsoort.service.value,
    )
    """
    De maandelijkse kosten voor de diensten die de huismeester, flatwacht, wijkbeheerder
    of conciërge levert.
    """

    huisvuil = Referentiedata(
        code="HUV",
        naam="Huisvuil",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het verwerken van huisvuil
    """

    individuele_garage = Referentiedata(
        code="IGA",
        naam="Individuele garage",
        parent=Prijscomponentsoort.parkeren.value,
    )
    """
    Inpandige parkeerplek individueel
    """

    installaties = Referentiedata(
        code="INS",
        naam="Installaties",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van andere installaties dan elektrische
    installaties
    """

    inventaris = Referentiedata(
        code="INV",
        naam="Inventaris",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van inventaris
    """

    kale_huur = Referentiedata(
        code="KAL",
        naam="Kale huur",
        parent=Prijscomponentsoort.netto_huur.value,
    )
    """
    Basisbedrag voor het gebruik van de woning
    """

    laadpaal = Referentiedata(
        code="LAA",
        naam="Laadpaal",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van een laadpaal voor elektrische auto
    """

    liftkosten = Referentiedata(
        code="LIF",
        naam="Liftkosten",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van de lift(en)
    """

    linnenpakket = Referentiedata(
        code="LIN",
        naam="Linnenpakket",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van linnen
    """

    matiging_huurtoeslag = Referentiedata(
        code="MAT",
        naam="Matiging huurtoeslag",
        parent=Prijscomponentsoort.huuraanpassing.value,
    )
    """
    Component voor het matigen van de huurprijs op basis van toegekende huurtoeslag
    conform de wettelijke regeling van vóór 2014. Dit component is alleen bedoeld
    voor het uitwisselen van historische data
    """

    mechanische_ventilatie = Referentiedata(
        code="MVE",
        naam="Mechanische ventilatie",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van de mechanische ventilatie
    """

    overnamekosten = Referentiedata(
        code="OKO",
        naam="Overnamekosten",
        parent=Prijscomponentsoort.eenmalig.value,
    )

    onderhoudsabonnement = Referentiedata(
        code="OND",
        naam="Onderhoudsabonnement",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor onderhoudsabonnement. De huurder is zelf verantwoordelijk
    voor het klein onderhoud aan de woning. Als de huurder een onderhoudsabonnement
    afsluit, dan regelt de corporatie het klein onderhoud voor de huurder.
    """

    overige_netto_huur_component = Referentiedata(
        code="ONH",
        naam="Overige netto huur component",
        parent=Prijscomponentsoort.netto_huur.value,
    )
    """
    Een overige netto huur component wordt bijvoorbeeld gebruikt om de extra huur na het
    aanbrengen van (verduurzamings-) verbeteringen te onderscheiden van de basis
    kale huur.
    """

    overige_kosten_gem_ruimten = Referentiedata(
        code="OVE",
        naam="Overige kosten gem. ruimten",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor overige kosten voor gemeenschappelijke ruimten (naast
    schoonmaak, energie en reparatie)
    """

    parkeerplaats_buiten = Referentiedata(
        code="PBU",
        naam="Parkeerplaats buiten",
        parent=Prijscomponentsoort.parkeren.value,
    )
    """
    Uitpandige parkeerplek
    """

    parkeergarage = Referentiedata(
        code="PGA",
        naam="Parkeergarage",
        parent=Prijscomponentsoort.parkeren.value,
    )
    """
    Inpandige parkeerplek collectief
    """

    rioolfonds = Referentiedata(
        code="RIO",
        naam="Rioolfonds",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor de voorziening voor het repareren van problemen aan het
    riool
    """

    schoonmaak_eenheid = Referentiedata(
        code="SCE",
        naam="Schoonmaak eenheid",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor schoonmaak van de eenheid
    """

    schoonmaak_van_gemeenschappelijke_ruimten = Referentiedata(
        code="SCH",
        naam="Schoonmaak van gemeenschappelijke ruimten",
        parent=Prijscomponentsoort.service.value,
    )
    """
    De maandelijkse schoonmaakkosten voor de lift en andere gemeenschappelijke ruimten,
    zoals een galerij, trappenhuis of recreatieruimte
    """

    signaallevering_o_a_cai = Referentiedata(
        code="SIG",
        naam="Signaallevering (o.a. CAI)",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor signaallevering (o.a. CAI)
    """

    schoorsteenvegen = Referentiedata(
        code="STV",
        naam="Schoorsteenvegen",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het vegen van de schoorsteen
    """

    verenigingskosten = Referentiedata(
        code="VER",
        naam="Verenigingskosten",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor lidmaatschap van  verenigingen
    """

    volkstuin = Referentiedata(
        code="VOL",
        naam="Volkstuin",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van een volkstuin
    """

    vve_kosten = Referentiedata(
        code="VVE",
        naam="VVE kosten",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor VVE-lidmaatschap
    """

    verzekeringskosten = Referentiedata(
        code="VZE",
        naam="Verzekeringskosten",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor verzekeringen
    """

    warmte_installaties = Referentiedata(
        code="WAI",
        naam="Warmte-installaties",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van installaties voor verwarming van de
    vertrekken van de eenheid
    """

    warmte = Referentiedata(
        code="WAR",
        naam="Warmte",
        parent=Prijscomponentsoort.verbruik.value,
    )
    """
    Centrale verwarming, Stadsverwarming, etc.
    """

    water = Referentiedata(
        code="WAT",
        naam="Water",
        parent=Prijscomponentsoort.verbruik.value,
    )

    witgoed = Referentiedata(
        code="WIT",
        naam="Witgoed",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van witgoed (bijvoorbeeld wasmachine of droger)
    """

    warmwaterinstallaties = Referentiedata(
        code="WWI",
        naam="Warmwaterinstallaties",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van installaties voor warm water
    """

    zonnepanelen = Referentiedata(
        code="ZON",
        naam="Zonnepanelen",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van zonnepanelen
    """

    zonwering = Referentiedata(
        code="ZWE",
        naam="Zonwering",
        parent=Prijscomponentsoort.service.value,
    )
    """
    Maandelijkse kosten voor het gebruik van zonwering
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
