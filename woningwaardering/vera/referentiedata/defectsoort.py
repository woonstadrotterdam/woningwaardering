from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class DefectsoortReferentiedata(Referentiedata):
    pass


class Defectsoort(Referentiedatasoort):
    beklad = DefectsoortReferentiedata(
        code="BEK",
        naam="Beklad",
    )

    betonrot = DefectsoortReferentiedata(
        code="BET",
        naam="Betonrot",
    )

    bevroren = DefectsoortReferentiedata(
        code="BEV",
        naam="Bevroren",
    )

    bijen = DefectsoortReferentiedata(
        code="BIJ",
        naam="Bijen",
    )

    blijft_branden = DefectsoortReferentiedata(
        code="BLI",
        naam="Blijft branden",
    )

    boktorren = DefectsoortReferentiedata(
        code="BOK",
        naam="Boktorren",
    )

    breuk_en_of_scheur = DefectsoortReferentiedata(
        code="BRE",
        naam="Breuk / scheur",
    )
    """
    Voor glasbruik: gebruik GLA
    """

    beschadigd_omvang_onbenoemd = DefectsoortReferentiedata(
        code="BS0",
        naam="Beschadigd (omvang onbenoemd)",
    )

    beschadigd_1m2 = DefectsoortReferentiedata(
        code="BS1",
        naam="Beschadigd < 1m2",
    )

    beschadigd_1_5_m2 = DefectsoortReferentiedata(
        code="BS2",
        naam="Beschadigd 1-5 m2",
    )

    beschadigd_5_m2 = DefectsoortReferentiedata(
        code="BS3",
        naam="Beschadigd >5 m2",
    )

    defect_en_of_onderdeel_defect = DefectsoortReferentiedata(
        code="DEF",
        naam="Defect / onderdeel defect",
    )

    doorboord = DefectsoortReferentiedata(
        code="DOO",
        naam="Doorboord",
    )

    druppelt = DefectsoortReferentiedata(
        code="DRP",
        naam="Druppelt",
    )

    waterdruk_te_laag = DefectsoortReferentiedata(
        code="DRU",
        naam="Waterdruk te laag",
    )
    """
    Installatie moet worden bijgevuld/ontlucht
    """

    gaslucht_en_of_gaslek = DefectsoortReferentiedata(
        code="GAS",
        naam="Gaslucht/gaslek",
    )

    maakt_vreemd_geluid = DefectsoortReferentiedata(
        code="GEL",
        naam="Maakt vreemd geluid",
    )

    gezwollen = DefectsoortReferentiedata(
        code="GEZ",
        naam="Gezwollen",
    )

    glasbreuk = DefectsoortReferentiedata(
        code="GLA",
        naam="Glasbreuk",
    )

    houtrot = DefectsoortReferentiedata(
        code="HOR",
        naam="Houtrot",
    )

    houtwormen = DefectsoortReferentiedata(
        code="HOW",
        naam="Houtwormen",
    )

    inbraakschade = DefectsoortReferentiedata(
        code="INB",
        naam="Inbraakschade",
    )

    verkalkt = DefectsoortReferentiedata(
        code="KAL",
        naam="Verkalkt",
    )

    kevers = DefectsoortReferentiedata(
        code="KEV",
        naam="Kevers",
    )

    kakkerlakken = DefectsoortReferentiedata(
        code="KKL",
        naam="Kakkerlakken",
    )

    klemt_en_of_opent_niet = DefectsoortReferentiedata(
        code="KLE",
        naam="Klemt / opent niet",
    )

    knippert = DefectsoortReferentiedata(
        code="KNI",
        naam="Knippert",
    )

    lekt = DefectsoortReferentiedata(
        code="LEK",
        naam="Lekt",
    )

    loopt_door = DefectsoortReferentiedata(
        code="LOO",
        naam="Loopt door",
    )

    zit_los_en_of_onderdeel_zit_los = DefectsoortReferentiedata(
        code="LOS",
        naam="Zit los / onderdeel zit los",
    )

    mieren = DefectsoortReferentiedata(
        code="MIE",
        naam="Mieren",
    )

    muizen = DefectsoortReferentiedata(
        code="MUI",
        naam="Muizen",
    )

    onvoldoende_afzuiging = DefectsoortReferentiedata(
        code="ONA",
        naam="Onvoldoende afzuiging",
    )

    onvoldoende_kracht = DefectsoortReferentiedata(
        code="ONK",
        naam="Onvoldoende kracht",
    )

    ontbreekt_en_of_onderdeel_ontbreekt = DefectsoortReferentiedata(
        code="ONT",
        naam="Ontbreekt / onderdeel ontbreekt",
    )

    ontzet = DefectsoortReferentiedata(
        code="ONZ",
        naam="Ontzet",
    )

    overig = DefectsoortReferentiedata(
        code="OVE",
        naam="Overig",
    )
    """
    Overige soorten die niet onder één van de andere defectsoorten vallen
    """

    personen_ingesloten = DefectsoortReferentiedata(
        code="PER",
        naam="Personen ingesloten",
    )

    ratten = DefectsoortReferentiedata(
        code="RAT",
        naam="Ratten",
    )

    roest = DefectsoortReferentiedata(
        code="ROE",
        naam="Roest",
    )

    sleutel_afgebroken = DefectsoortReferentiedata(
        code="SAF",
        naam="Sleutel afgebroken",
    )

    schimmel = DefectsoortReferentiedata(
        code="SCH",
        naam="Schimmel",
    )

    slot_defect = DefectsoortReferentiedata(
        code="SDE",
        naam="Slot defect",
    )

    sleutel_kwijt = DefectsoortReferentiedata(
        code="SKW",
        naam="Sleutel kwijt",
    )

    sluit_niet = DefectsoortReferentiedata(
        code="SLU",
        naam="Sluit niet",
    )

    spraak_en_of_video_slecht = DefectsoortReferentiedata(
        code="SPR",
        naam="Spraak/video slecht",
    )

    staat_stil = DefectsoortReferentiedata(
        code="STA",
        naam="Staat stil",
    )

    stinkt = DefectsoortReferentiedata(
        code="STI",
        naam="Stinkt",
    )

    storing = DefectsoortReferentiedata(
        code="STO",
        naam="Storing",
    )

    onjuiste_temperatuur = DefectsoortReferentiedata(
        code="TEM",
        naam="Onjuiste temperatuur",
    )

    tijdschakelklok_werkt_niet = DefectsoortReferentiedata(
        code="TIJ",
        naam="Tijdschakelklok werkt niet",
    )

    tocht = DefectsoortReferentiedata(
        code="TOC",
        naam="Tocht",
    )

    verf_laat_los_binnen = DefectsoortReferentiedata(
        code="VBI",
        naam="Verf laat los (binnen)",
    )

    verf_laat_los_buiten = DefectsoortReferentiedata(
        code="VBU",
        naam="Verf laat los (buiten)",
    )

    vlooien = DefectsoortReferentiedata(
        code="VLO",
        naam="Vlooien",
    )

    vochtig_en_of_nat = DefectsoortReferentiedata(
        code="VOC",
        naam="Vochtig / nat",
    )

    vogelnest = DefectsoortReferentiedata(
        code="VOG",
        naam="Vogelnest",
    )

    is_vol = DefectsoortReferentiedata(
        code="VOL",
        naam="Is vol",
    )

    verstopt_hoogte_onbenoemd = DefectsoortReferentiedata(
        code="VS0",
        naam="Verstopt (hoogte onbenoemd)",
    )

    verstopt_lager_dan_7_5_meter = DefectsoortReferentiedata(
        code="VS1",
        naam="Verstopt (lager dan 7,5 meter)",
    )

    verstopt_hoger_dan_7_5_meter = DefectsoortReferentiedata(
        code="VS2",
        naam="Verstopt (hoger dan 7,5 meter)",
    )

    verschoven = DefectsoortReferentiedata(
        code="VSC",
        naam="Verschoven",
    )

    verlichting_werkt_niet = DefectsoortReferentiedata(
        code="VWE",
        naam="Verlichting werkt niet",
    )

    verzakt = DefectsoortReferentiedata(
        code="VZT",
        naam="Verzakt",
    )

    wandluizen = DefectsoortReferentiedata(
        code="WAN",
        naam="Wandluizen",
    )

    wespen = DefectsoortReferentiedata(
        code="WES",
        naam="Wespen",
    )

    zilvervisjes = DefectsoortReferentiedata(
        code="ZIL",
        naam="Zilvervisjes",
    )
