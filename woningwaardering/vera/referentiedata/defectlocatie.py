from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Defectlocatie(Enum):
    airco_en_of_koelinstallatie = Referentiedata(
        code="AIR",
        naam="Airco/koelinstallatie",
    )

    badkamer_en_of_doucheruimte = Referentiedata(
        code="BAD",
        naam="Badkamer / doucheruimte",
    )

    balkon = Referentiedata(
        code="BAL",
        naam="Balkon",
    )

    bergingsruimte = Referentiedata(
        code="BER",
        naam="Bergingsruimte",
    )

    bijkeuken = Referentiedata(
        code="BIJ",
        naam="Bijkeuken",
    )

    buitengevel = Referentiedata(
        code="BUI",
        naam="Buitengevel",
    )

    containerruimte = Referentiedata(
        code="CON",
        naam="Containerruimte",
    )

    dak = Referentiedata(
        code="DAK",
        naam="Dak",
    )

    dakterras = Referentiedata(
        code="DTE",
        naam="Dakterras",
    )

    entreehal_en_of_ingang = Referentiedata(
        code="ENT",
        naam="Entreehal / Ingang",
    )

    fietsenstalling = Referentiedata(
        code="FIE",
        naam="Fietsenstalling",
    )

    galerij_en_of_galerijgang = Referentiedata(
        code="GAL",
        naam="Galerij / galerijgang",
    )

    gangkast_en_of_trapkast = Referentiedata(
        code="GAN",
        naam="Gangkast / trapkast",
    )

    garage_perceelgebonden_en_of_carport = Referentiedata(
        code="GAR",
        naam="Garage (perceelgebonden) / carport",
    )

    hal_en_of_gang_individueel = Referentiedata(
        code="HAL",
        naam="Hal / gang individueel",
    )

    kelder = Referentiedata(
        code="KEL",
        naam="Kelder",
    )

    keuken = Referentiedata(
        code="KEU",
        naam="Keuken",
    )

    kruipruimte = Referentiedata(
        code="KRU",
        naam="Kruipruimte",
    )

    lift = Referentiedata(
        code="LIF",
        naam="Lift",
    )

    overige_ruimte = Referentiedata(
        code="OVE",
        naam="Overige ruimte",
    )
    """
    Overige locaties die niet onder één van de andere defectlocaties vallen
    """

    overloop = Referentiedata(
        code="OVL",
        naam="Overloop",
    )

    pad_en_of_brandgang = Referentiedata(
        code="PAD",
        naam="Pad / brandgang",
    )

    pantry = Referentiedata(
        code="PAN",
        naam="Pantry",
    )

    parkeerplaats = Referentiedata(
        code="PAR",
        naam="Parkeerplaats",
    )

    trappenhuis_en_of_portiek = Referentiedata(
        code="POR",
        naam="Trappenhuis / Portiek",
    )

    schuur = Referentiedata(
        code="SCH",
        naam="Schuur",
    )

    scootmobielruimte = Referentiedata(
        code="SCO",
        naam="Scootmobielruimte",
    )

    slaapkamer = Referentiedata(
        code="SLA",
        naam="Slaapkamer",
    )

    toiletruimte = Referentiedata(
        code="TOI",
        naam="Toiletruimte",
    )

    trap = Referentiedata(
        code="TRA",
        naam="Trap",
    )

    technische_ruimte_collectief = Referentiedata(
        code="TRC",
        naam="Technische ruimte (collectief)",
    )

    technische_ruimte_individueel = Referentiedata(
        code="TRI",
        naam="Technische ruimte (individueel)",
    )

    tuin = Referentiedata(
        code="TUI",
        naam="Tuin",
    )

    voertuigingang = Referentiedata(
        code="VOE",
        naam="Voertuigingang",
    )

    woonkamer = Referentiedata(
        code="WOO",
        naam="Woonkamer",
    )

    wasruimte_collectief = Referentiedata(
        code="WRC",
        naam="Wasruimte collectief",
    )

    wasruimte_individueel = Referentiedata(
        code="WRI",
        naam="Wasruimte individueel",
    )

    zolder_en_of_vliering = Referentiedata(
        code="ZOL",
        naam="Zolder / vliering",
    )

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
