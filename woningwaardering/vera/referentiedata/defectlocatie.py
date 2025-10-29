from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class DefectlocatieReferentiedata(Referentiedata):
    pass


class Defectlocatie(Referentiedatasoort):
    airco_en_of_koelinstallatie = DefectlocatieReferentiedata(
        code="AIR",
        naam="Airco/koelinstallatie",
    )

    badkamer_en_of_doucheruimte = DefectlocatieReferentiedata(
        code="BAD",
        naam="Badkamer / doucheruimte",
    )

    balkon = DefectlocatieReferentiedata(
        code="BAL",
        naam="Balkon",
    )

    bergingsruimte = DefectlocatieReferentiedata(
        code="BER",
        naam="Bergingsruimte",
    )

    bijkeuken = DefectlocatieReferentiedata(
        code="BIJ",
        naam="Bijkeuken",
    )

    buitengevel = DefectlocatieReferentiedata(
        code="BUI",
        naam="Buitengevel",
    )

    containerruimte = DefectlocatieReferentiedata(
        code="CON",
        naam="Containerruimte",
    )

    dak = DefectlocatieReferentiedata(
        code="DAK",
        naam="Dak",
    )

    dakterras = DefectlocatieReferentiedata(
        code="DTE",
        naam="Dakterras",
    )

    entreehal_en_of_ingang = DefectlocatieReferentiedata(
        code="ENT",
        naam="Entreehal / Ingang",
    )

    fietsenstalling = DefectlocatieReferentiedata(
        code="FIE",
        naam="Fietsenstalling",
    )

    galerij_en_of_galerijgang = DefectlocatieReferentiedata(
        code="GAL",
        naam="Galerij / galerijgang",
    )

    gangkast_en_of_trapkast = DefectlocatieReferentiedata(
        code="GAN",
        naam="Gangkast / trapkast",
    )

    garage_perceelgebonden_en_of_carport = DefectlocatieReferentiedata(
        code="GAR",
        naam="Garage (perceelgebonden) / carport",
    )

    hal_en_of_gang_individueel = DefectlocatieReferentiedata(
        code="HAL",
        naam="Hal / gang individueel",
    )

    kelder = DefectlocatieReferentiedata(
        code="KEL",
        naam="Kelder",
    )

    keuken = DefectlocatieReferentiedata(
        code="KEU",
        naam="Keuken",
    )

    kruipruimte = DefectlocatieReferentiedata(
        code="KRU",
        naam="Kruipruimte",
    )

    lift = DefectlocatieReferentiedata(
        code="LIF",
        naam="Lift",
    )

    overige_ruimte = DefectlocatieReferentiedata(
        code="OVE",
        naam="Overige ruimte",
    )
    """
    Overige locaties die niet onder één van de andere defectlocaties vallen
    """

    overloop = DefectlocatieReferentiedata(
        code="OVL",
        naam="Overloop",
    )

    pad_en_of_brandgang = DefectlocatieReferentiedata(
        code="PAD",
        naam="Pad / brandgang",
    )

    pantry = DefectlocatieReferentiedata(
        code="PAN",
        naam="Pantry",
    )

    parkeerplaats = DefectlocatieReferentiedata(
        code="PAR",
        naam="Parkeerplaats",
    )

    trappenhuis_en_of_portiek = DefectlocatieReferentiedata(
        code="POR",
        naam="Trappenhuis / Portiek",
    )

    schuur = DefectlocatieReferentiedata(
        code="SCH",
        naam="Schuur",
    )

    scootmobielruimte = DefectlocatieReferentiedata(
        code="SCO",
        naam="Scootmobielruimte",
    )

    slaapkamer = DefectlocatieReferentiedata(
        code="SLA",
        naam="Slaapkamer",
    )

    toiletruimte = DefectlocatieReferentiedata(
        code="TOI",
        naam="Toiletruimte",
    )

    trap = DefectlocatieReferentiedata(
        code="TRA",
        naam="Trap",
    )

    technische_ruimte_collectief = DefectlocatieReferentiedata(
        code="TRC",
        naam="Technische ruimte (collectief)",
    )

    technische_ruimte_individueel = DefectlocatieReferentiedata(
        code="TRI",
        naam="Technische ruimte (individueel)",
    )

    tuin = DefectlocatieReferentiedata(
        code="TUI",
        naam="Tuin",
    )

    voertuigingang = DefectlocatieReferentiedata(
        code="VOE",
        naam="Voertuigingang",
    )

    woonkamer = DefectlocatieReferentiedata(
        code="WOO",
        naam="Woonkamer",
    )

    wasruimte_collectief = DefectlocatieReferentiedata(
        code="WRC",
        naam="Wasruimte collectief",
    )

    wasruimte_individueel = DefectlocatieReferentiedata(
        code="WRI",
        naam="Wasruimte individueel",
    )

    zolder_en_of_vliering = DefectlocatieReferentiedata(
        code="ZOL",
        naam="Zolder / vliering",
    )
