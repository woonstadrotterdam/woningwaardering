
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class DEFECTSOORT:

    beklad = Referentiedata(
        code="BEK",
        naam="Beklad",
    )
    # beklad = ("BEK", "Beklad")

    betonrot = Referentiedata(
        code="BET",
        naam="Betonrot",
    )
    # betonrot = ("BET", "Betonrot")

    bevroren = Referentiedata(
        code="BEV",
        naam="Bevroren",
    )
    # bevroren = ("BEV", "Bevroren")

    bijen = Referentiedata(
        code="BIJ",
        naam="Bijen",
    )
    # bijen = ("BIJ", "Bijen")

    blijft_branden = Referentiedata(
        code="BLI",
        naam="Blijft branden",
    )
    # blijft_branden = ("BLI", "Blijft branden")

    boktorren = Referentiedata(
        code="BOK",
        naam="Boktorren",
    )
    # boktorren = ("BOK", "Boktorren")

    breuk_of_scheur = Referentiedata(
        code="BRE",
        naam="Breuk / scheur",
    )
    # breuk_of_scheur = ("BRE", "Breuk / scheur")
    """
    Voor glasbruik: gebruik GLA
    """

    beschadigd_omvang_onbenoemd = Referentiedata(
        code="BS0",
        naam="Beschadigd (omvang onbenoemd)",
    )
    # beschadigd_omvang_onbenoemd = ("BS0", "Beschadigd (omvang onbenoemd)")

    beschadigd_1m2 = Referentiedata(
        code="BS1",
        naam="Beschadigd < 1m2",
    )
    # beschadigd_1m2 = ("BS1", "Beschadigd < 1m2")

    beschadigd_1_5_m2 = Referentiedata(
        code="BS2",
        naam="Beschadigd 1-5 m2",
    )
    # beschadigd_1_5_m2 = ("BS2", "Beschadigd 1-5 m2")

    beschadigd_5_m2 = Referentiedata(
        code="BS3",
        naam="Beschadigd >5 m2",
    )
    # beschadigd_5_m2 = ("BS3", "Beschadigd >5 m2")

    defect_of_onderdeel_defect = Referentiedata(
        code="DEF",
        naam="Defect / onderdeel defect",
    )
    # defect_of_onderdeel_defect = ("DEF", "Defect / onderdeel defect")

    doorboord = Referentiedata(
        code="DOO",
        naam="Doorboord",
    )
    # doorboord = ("DOO", "Doorboord")

    druppelt = Referentiedata(
        code="DRP",
        naam="Druppelt",
    )
    # druppelt = ("DRP", "Druppelt")

    waterdruk_te_laag = Referentiedata(
        code="DRU",
        naam="Waterdruk te laag",
    )
    # waterdruk_te_laag = ("DRU", "Waterdruk te laag")
    """
    Installatie moet worden bijgevuld/ontlucht
    """

    gaslucht_of_gaslek = Referentiedata(
        code="GAS",
        naam="Gaslucht/gaslek",
    )
    # gaslucht_of_gaslek = ("GAS", "Gaslucht/gaslek")

    maakt_vreemd_geluid = Referentiedata(
        code="GEL",
        naam="Maakt vreemd geluid",
    )
    # maakt_vreemd_geluid = ("GEL", "Maakt vreemd geluid")

    gezwollen = Referentiedata(
        code="GEZ",
        naam="Gezwollen",
    )
    # gezwollen = ("GEZ", "Gezwollen")

    glasbreuk = Referentiedata(
        code="GLA",
        naam="Glasbreuk",
    )
    # glasbreuk = ("GLA", "Glasbreuk")

    houtrot = Referentiedata(
        code="HOR",
        naam="Houtrot",
    )
    # houtrot = ("HOR", "Houtrot")

    houtwormen = Referentiedata(
        code="HOW",
        naam="Houtwormen",
    )
    # houtwormen = ("HOW", "Houtwormen")

    inbraakschade = Referentiedata(
        code="INB",
        naam="Inbraakschade",
    )
    # inbraakschade = ("INB", "Inbraakschade")

    verkalkt = Referentiedata(
        code="KAL",
        naam="Verkalkt",
    )
    # verkalkt = ("KAL", "Verkalkt")

    kevers = Referentiedata(
        code="KEV",
        naam="Kevers",
    )
    # kevers = ("KEV", "Kevers")

    kakkerlakken = Referentiedata(
        code="KKL",
        naam="Kakkerlakken",
    )
    # kakkerlakken = ("KKL", "Kakkerlakken")

    klemt_of_opent_niet = Referentiedata(
        code="KLE",
        naam="Klemt / opent niet",
    )
    # klemt_of_opent_niet = ("KLE", "Klemt / opent niet")

    knippert = Referentiedata(
        code="KNI",
        naam="Knippert",
    )
    # knippert = ("KNI", "Knippert")

    lekt = Referentiedata(
        code="LEK",
        naam="Lekt",
    )
    # lekt = ("LEK", "Lekt")

    loopt_door = Referentiedata(
        code="LOO",
        naam="Loopt door",
    )
    # loopt_door = ("LOO", "Loopt door")

    zit_los_of_onderdeel_zit_los = Referentiedata(
        code="LOS",
        naam="Zit los / onderdeel zit los",
    )
    # zit_los_of_onderdeel_zit_los = ("LOS", "Zit los / onderdeel zit los")

    mieren = Referentiedata(
        code="MIE",
        naam="Mieren",
    )
    # mieren = ("MIE", "Mieren")

    muizen = Referentiedata(
        code="MUI",
        naam="Muizen",
    )
    # muizen = ("MUI", "Muizen")

    onvoldoende_afzuiging = Referentiedata(
        code="ONA",
        naam="Onvoldoende afzuiging",
    )
    # onvoldoende_afzuiging = ("ONA", "Onvoldoende afzuiging")

    onvoldoende_kracht = Referentiedata(
        code="ONK",
        naam="Onvoldoende kracht",
    )
    # onvoldoende_kracht = ("ONK", "Onvoldoende kracht")

    ontbreekt_of_onderdeel_ontbreekt = Referentiedata(
        code="ONT",
        naam="Ontbreekt / onderdeel ontbreekt",
    )
    # ontbreekt_of_onderdeel_ontbreekt = ("ONT", "Ontbreekt / onderdeel ontbreekt")

    ontzet = Referentiedata(
        code="ONZ",
        naam="Ontzet",
    )
    # ontzet = ("ONZ", "Ontzet")

    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )
    # overig = ("OVE", "Overig")
    """
    Overige soorten die niet onder één van de andere defectsoorten vallen
    """

    personen_ingesloten = Referentiedata(
        code="PER",
        naam="Personen ingesloten",
    )
    # personen_ingesloten = ("PER", "Personen ingesloten")

    ratten = Referentiedata(
        code="RAT",
        naam="Ratten",
    )
    # ratten = ("RAT", "Ratten")

    roest = Referentiedata(
        code="ROE",
        naam="Roest",
    )
    # roest = ("ROE", "Roest")

    sleutel_afgebroken = Referentiedata(
        code="SAF",
        naam="Sleutel afgebroken",
    )
    # sleutel_afgebroken = ("SAF", "Sleutel afgebroken")

    schimmel = Referentiedata(
        code="SCH",
        naam="Schimmel",
    )
    # schimmel = ("SCH", "Schimmel")

    slot_defect = Referentiedata(
        code="SDE",
        naam="Slot defect",
    )
    # slot_defect = ("SDE", "Slot defect")

    sleutel_kwijt = Referentiedata(
        code="SKW",
        naam="Sleutel kwijt",
    )
    # sleutel_kwijt = ("SKW", "Sleutel kwijt")

    sluit_niet = Referentiedata(
        code="SLU",
        naam="Sluit niet",
    )
    # sluit_niet = ("SLU", "Sluit niet")

    spraak_of_video_slecht = Referentiedata(
        code="SPR",
        naam="Spraak/video slecht",
    )
    # spraak_of_video_slecht = ("SPR", "Spraak/video slecht")

    staat_stil = Referentiedata(
        code="STA",
        naam="Staat stil",
    )
    # staat_stil = ("STA", "Staat stil")

    stinkt = Referentiedata(
        code="STI",
        naam="Stinkt",
    )
    # stinkt = ("STI", "Stinkt")

    storing = Referentiedata(
        code="STO",
        naam="Storing",
    )
    # storing = ("STO", "Storing")

    onjuiste_temperatuur = Referentiedata(
        code="TEM",
        naam="Onjuiste temperatuur",
    )
    # onjuiste_temperatuur = ("TEM", "Onjuiste temperatuur")

    tijdschakelklok_werkt_niet = Referentiedata(
        code="TIJ",
        naam="Tijdschakelklok werkt niet",
    )
    # tijdschakelklok_werkt_niet = ("TIJ", "Tijdschakelklok werkt niet")

    tocht = Referentiedata(
        code="TOC",
        naam="Tocht",
    )
    # tocht = ("TOC", "Tocht")

    verf_laat_los_binnen = Referentiedata(
        code="VBI",
        naam="Verf laat los (binnen)",
    )
    # verf_laat_los_binnen = ("VBI", "Verf laat los (binnen)")

    verf_laat_los_buiten = Referentiedata(
        code="VBU",
        naam="Verf laat los (buiten)",
    )
    # verf_laat_los_buiten = ("VBU", "Verf laat los (buiten)")

    vlooien = Referentiedata(
        code="VLO",
        naam="Vlooien",
    )
    # vlooien = ("VLO", "Vlooien")

    vochtig_of_nat = Referentiedata(
        code="VOC",
        naam="Vochtig / nat",
    )
    # vochtig_of_nat = ("VOC", "Vochtig / nat")

    vogelnest = Referentiedata(
        code="VOG",
        naam="Vogelnest",
    )
    # vogelnest = ("VOG", "Vogelnest")

    is_vol = Referentiedata(
        code="VOL",
        naam="Is vol",
    )
    # is_vol = ("VOL", "Is vol")

    verstopt_hoogte_onbenoemd = Referentiedata(
        code="VS0",
        naam="Verstopt (hoogte onbenoemd)",
    )
    # verstopt_hoogte_onbenoemd = ("VS0", "Verstopt (hoogte onbenoemd)")

    verstopt_lager_dan_7_5_meter = Referentiedata(
        code="VS1",
        naam="Verstopt (lager dan 7,5 meter)",
    )
    # verstopt_lager_dan_7_5_meter = ("VS1", "Verstopt (lager dan 7,5 meter)")

    verstopt_hoger_dan_7_5_meter = Referentiedata(
        code="VS2",
        naam="Verstopt (hoger dan 7,5 meter)",
    )
    # verstopt_hoger_dan_7_5_meter = ("VS2", "Verstopt (hoger dan 7,5 meter)")

    verschoven = Referentiedata(
        code="VSC",
        naam="Verschoven",
    )
    # verschoven = ("VSC", "Verschoven")

    verlichting_werkt_niet = Referentiedata(
        code="VWE",
        naam="Verlichting werkt niet",
    )
    # verlichting_werkt_niet = ("VWE", "Verlichting werkt niet")

    verzakt = Referentiedata(
        code="VZT",
        naam="Verzakt",
    )
    # verzakt = ("VZT", "Verzakt")

    wandluizen = Referentiedata(
        code="WAN",
        naam="Wandluizen",
    )
    # wandluizen = ("WAN", "Wandluizen")

    wespen = Referentiedata(
        code="WES",
        naam="Wespen",
    )
    # wespen = ("WES", "Wespen")

    zilvervisjes = Referentiedata(
        code="ZIL",
        naam="Zilvervisjes",
    )
    # zilvervisjes = ("ZIL", "Zilvervisjes")
