
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class DEFECTLOCATIE:

    airco_of_koelinstallatie = Referentiedata(
        code="AIR",
        naam="Airco/koelinstallatie",
    )
    # airco_of_koelinstallatie = ("AIR", "Airco/koelinstallatie")

    badkamer_of_doucheruimte = Referentiedata(
        code="BAD",
        naam="Badkamer / doucheruimte",
    )
    # badkamer_of_doucheruimte = ("BAD", "Badkamer / doucheruimte")

    balkon = Referentiedata(
        code="BAL",
        naam="Balkon",
    )
    # balkon = ("BAL", "Balkon")

    bergingsruimte = Referentiedata(
        code="BER",
        naam="Bergingsruimte",
    )
    # bergingsruimte = ("BER", "Bergingsruimte")

    bijkeuken = Referentiedata(
        code="BIJ",
        naam="Bijkeuken",
    )
    # bijkeuken = ("BIJ", "Bijkeuken")

    buitengevel = Referentiedata(
        code="BUI",
        naam="Buitengevel",
    )
    # buitengevel = ("BUI", "Buitengevel")

    containerruimte = Referentiedata(
        code="CON",
        naam="Containerruimte",
    )
    # containerruimte = ("CON", "Containerruimte")

    dak = Referentiedata(
        code="DAK",
        naam="Dak",
    )
    # dak = ("DAK", "Dak")

    dakterras = Referentiedata(
        code="DTE",
        naam="Dakterras",
    )
    # dakterras = ("DTE", "Dakterras")

    entreehal_of_ingang = Referentiedata(
        code="ENT",
        naam="Entreehal / Ingang",
    )
    # entreehal_of_ingang = ("ENT", "Entreehal / Ingang")

    fietsenstalling = Referentiedata(
        code="FIE",
        naam="Fietsenstalling",
    )
    # fietsenstalling = ("FIE", "Fietsenstalling")

    galerij_of_galerijgang = Referentiedata(
        code="GAL",
        naam="Galerij / galerijgang",
    )
    # galerij_of_galerijgang = ("GAL", "Galerij / galerijgang")

    gangkast_of_trapkast = Referentiedata(
        code="GAN",
        naam="Gangkast / trapkast",
    )
    # gangkast_of_trapkast = ("GAN", "Gangkast / trapkast")

    garage_perceelgebonden_of_carport = Referentiedata(
        code="GAR",
        naam="Garage (perceelgebonden) / carport",
    )
    # garage_perceelgebonden_of_carport = ("GAR", "Garage (perceelgebonden) / carport")

    hal_of_gang_individueel = Referentiedata(
        code="HAL",
        naam="Hal / gang individueel",
    )
    # hal_of_gang_individueel = ("HAL", "Hal / gang individueel")

    kelder = Referentiedata(
        code="KEL",
        naam="Kelder",
    )
    # kelder = ("KEL", "Kelder")

    keuken = Referentiedata(
        code="KEU",
        naam="Keuken",
    )
    # keuken = ("KEU", "Keuken")

    kruipruimte = Referentiedata(
        code="KRU",
        naam="Kruipruimte",
    )
    # kruipruimte = ("KRU", "Kruipruimte")

    lift = Referentiedata(
        code="LIF",
        naam="Lift",
    )
    # lift = ("LIF", "Lift")

    overige_ruimte = Referentiedata(
        code="OVE",
        naam="Overige ruimte",
    )
    # overige_ruimte = ("OVE", "Overige ruimte")
    """
    Overige locaties die niet onder één van de andere defectlocaties vallen
    """

    overloop = Referentiedata(
        code="OVL",
        naam="Overloop",
    )
    # overloop = ("OVL", "Overloop")

    pad_of_brandgang = Referentiedata(
        code="PAD",
        naam="Pad / brandgang",
    )
    # pad_of_brandgang = ("PAD", "Pad / brandgang")

    pantry = Referentiedata(
        code="PAN",
        naam="Pantry",
    )
    # pantry = ("PAN", "Pantry")

    parkeerplaats = Referentiedata(
        code="PAR",
        naam="Parkeerplaats",
    )
    # parkeerplaats = ("PAR", "Parkeerplaats")

    trappenhuis_of_portiek = Referentiedata(
        code="POR",
        naam="Trappenhuis / Portiek",
    )
    # trappenhuis_of_portiek = ("POR", "Trappenhuis / Portiek")

    schuur = Referentiedata(
        code="SCH",
        naam="Schuur",
    )
    # schuur = ("SCH", "Schuur")

    scootmobielruimte = Referentiedata(
        code="SCO",
        naam="Scootmobielruimte",
    )
    # scootmobielruimte = ("SCO", "Scootmobielruimte")

    slaapkamer = Referentiedata(
        code="SLA",
        naam="Slaapkamer",
    )
    # slaapkamer = ("SLA", "Slaapkamer")

    toiletruimte = Referentiedata(
        code="TOI",
        naam="Toiletruimte",
    )
    # toiletruimte = ("TOI", "Toiletruimte")

    trap = Referentiedata(
        code="TRA",
        naam="Trap",
    )
    # trap = ("TRA", "Trap")

    technische_ruimte_collectief = Referentiedata(
        code="TRC",
        naam="Technische ruimte (collectief)",
    )
    # technische_ruimte_collectief = ("TRC", "Technische ruimte (collectief)")

    technische_ruimte_individueel = Referentiedata(
        code="TRI",
        naam="Technische ruimte (individueel)",
    )
    # technische_ruimte_individueel = ("TRI", "Technische ruimte (individueel)")

    tuin = Referentiedata(
        code="TUI",
        naam="Tuin",
    )
    # tuin = ("TUI", "Tuin")

    voertuigingang = Referentiedata(
        code="VOE",
        naam="Voertuigingang",
    )
    # voertuigingang = ("VOE", "Voertuigingang")

    woonkamer = Referentiedata(
        code="WOO",
        naam="Woonkamer",
    )
    # woonkamer = ("WOO", "Woonkamer")

    wasruimte_collectief = Referentiedata(
        code="WRC",
        naam="Wasruimte collectief",
    )
    # wasruimte_collectief = ("WRC", "Wasruimte collectief")

    wasruimte_individueel = Referentiedata(
        code="WRI",
        naam="Wasruimte individueel",
    )
    # wasruimte_individueel = ("WRI", "Wasruimte individueel")

    zolder_of_vliering = Referentiedata(
        code="ZOL",
        naam="Zolder / vliering",
    )
    # zolder_of_vliering = ("ZOL", "Zolder / vliering")
