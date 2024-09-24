from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Defectsoort(Enum):
    beklad = Referentiedata(
        code="BEK",
        naam="Beklad",
    )

    betonrot = Referentiedata(
        code="BET",
        naam="Betonrot",
    )

    bevroren = Referentiedata(
        code="BEV",
        naam="Bevroren",
    )

    bijen = Referentiedata(
        code="BIJ",
        naam="Bijen",
    )

    blijft_branden = Referentiedata(
        code="BLI",
        naam="Blijft branden",
    )

    boktorren = Referentiedata(
        code="BOK",
        naam="Boktorren",
    )

    breuk_en_of_scheur = Referentiedata(
        code="BRE",
        naam="Breuk / scheur",
    )
    """
    Voor glasbruik: gebruik GLA
    """

    beschadigd_omvang_onbenoemd = Referentiedata(
        code="BS0",
        naam="Beschadigd (omvang onbenoemd)",
    )

    beschadigd_1m2 = Referentiedata(
        code="BS1",
        naam="Beschadigd < 1m2",
    )

    beschadigd_1_5_m2 = Referentiedata(
        code="BS2",
        naam="Beschadigd 1-5 m2",
    )

    beschadigd_5_m2 = Referentiedata(
        code="BS3",
        naam="Beschadigd >5 m2",
    )

    defect_en_of_onderdeel_defect = Referentiedata(
        code="DEF",
        naam="Defect / onderdeel defect",
    )

    doorboord = Referentiedata(
        code="DOO",
        naam="Doorboord",
    )

    druppelt = Referentiedata(
        code="DRP",
        naam="Druppelt",
    )

    waterdruk_te_laag = Referentiedata(
        code="DRU",
        naam="Waterdruk te laag",
    )
    """
    Installatie moet worden bijgevuld/ontlucht
    """

    gaslucht_en_of_gaslek = Referentiedata(
        code="GAS",
        naam="Gaslucht/gaslek",
    )

    maakt_vreemd_geluid = Referentiedata(
        code="GEL",
        naam="Maakt vreemd geluid",
    )

    gezwollen = Referentiedata(
        code="GEZ",
        naam="Gezwollen",
    )

    glasbreuk = Referentiedata(
        code="GLA",
        naam="Glasbreuk",
    )

    houtrot = Referentiedata(
        code="HOR",
        naam="Houtrot",
    )

    houtwormen = Referentiedata(
        code="HOW",
        naam="Houtwormen",
    )

    inbraakschade = Referentiedata(
        code="INB",
        naam="Inbraakschade",
    )

    verkalkt = Referentiedata(
        code="KAL",
        naam="Verkalkt",
    )

    kevers = Referentiedata(
        code="KEV",
        naam="Kevers",
    )

    kakkerlakken = Referentiedata(
        code="KKL",
        naam="Kakkerlakken",
    )

    klemt_en_of_opent_niet = Referentiedata(
        code="KLE",
        naam="Klemt / opent niet",
    )

    knippert = Referentiedata(
        code="KNI",
        naam="Knippert",
    )

    lekt = Referentiedata(
        code="LEK",
        naam="Lekt",
    )

    loopt_door = Referentiedata(
        code="LOO",
        naam="Loopt door",
    )

    zit_los_en_of_onderdeel_zit_los = Referentiedata(
        code="LOS",
        naam="Zit los / onderdeel zit los",
    )

    mieren = Referentiedata(
        code="MIE",
        naam="Mieren",
    )

    muizen = Referentiedata(
        code="MUI",
        naam="Muizen",
    )

    onvoldoende_afzuiging = Referentiedata(
        code="ONA",
        naam="Onvoldoende afzuiging",
    )

    onvoldoende_kracht = Referentiedata(
        code="ONK",
        naam="Onvoldoende kracht",
    )

    ontbreekt_en_of_onderdeel_ontbreekt = Referentiedata(
        code="ONT",
        naam="Ontbreekt / onderdeel ontbreekt",
    )

    ontzet = Referentiedata(
        code="ONZ",
        naam="Ontzet",
    )

    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )
    """
    Overige soorten die niet onder één van de andere defectsoorten vallen
    """

    personen_ingesloten = Referentiedata(
        code="PER",
        naam="Personen ingesloten",
    )

    ratten = Referentiedata(
        code="RAT",
        naam="Ratten",
    )

    roest = Referentiedata(
        code="ROE",
        naam="Roest",
    )

    sleutel_afgebroken = Referentiedata(
        code="SAF",
        naam="Sleutel afgebroken",
    )

    schimmel = Referentiedata(
        code="SCH",
        naam="Schimmel",
    )

    slot_defect = Referentiedata(
        code="SDE",
        naam="Slot defect",
    )

    sleutel_kwijt = Referentiedata(
        code="SKW",
        naam="Sleutel kwijt",
    )

    sluit_niet = Referentiedata(
        code="SLU",
        naam="Sluit niet",
    )

    spraak_en_of_video_slecht = Referentiedata(
        code="SPR",
        naam="Spraak/video slecht",
    )

    staat_stil = Referentiedata(
        code="STA",
        naam="Staat stil",
    )

    stinkt = Referentiedata(
        code="STI",
        naam="Stinkt",
    )

    storing = Referentiedata(
        code="STO",
        naam="Storing",
    )

    onjuiste_temperatuur = Referentiedata(
        code="TEM",
        naam="Onjuiste temperatuur",
    )

    tijdschakelklok_werkt_niet = Referentiedata(
        code="TIJ",
        naam="Tijdschakelklok werkt niet",
    )

    tocht = Referentiedata(
        code="TOC",
        naam="Tocht",
    )

    verf_laat_los_binnen = Referentiedata(
        code="VBI",
        naam="Verf laat los (binnen)",
    )

    verf_laat_los_buiten = Referentiedata(
        code="VBU",
        naam="Verf laat los (buiten)",
    )

    vlooien = Referentiedata(
        code="VLO",
        naam="Vlooien",
    )

    vochtig_en_of_nat = Referentiedata(
        code="VOC",
        naam="Vochtig / nat",
    )

    vogelnest = Referentiedata(
        code="VOG",
        naam="Vogelnest",
    )

    is_vol = Referentiedata(
        code="VOL",
        naam="Is vol",
    )

    verstopt_hoogte_onbenoemd = Referentiedata(
        code="VS0",
        naam="Verstopt (hoogte onbenoemd)",
    )

    verstopt_lager_dan_7_5_meter = Referentiedata(
        code="VS1",
        naam="Verstopt (lager dan 7,5 meter)",
    )

    verstopt_hoger_dan_7_5_meter = Referentiedata(
        code="VS2",
        naam="Verstopt (hoger dan 7,5 meter)",
    )

    verschoven = Referentiedata(
        code="VSC",
        naam="Verschoven",
    )

    verlichting_werkt_niet = Referentiedata(
        code="VWE",
        naam="Verlichting werkt niet",
    )

    verzakt = Referentiedata(
        code="VZT",
        naam="Verzakt",
    )

    wandluizen = Referentiedata(
        code="WAN",
        naam="Wandluizen",
    )

    wespen = Referentiedata(
        code="WES",
        naam="Wespen",
    )

    zilvervisjes = Referentiedata(
        code="ZIL",
        naam="Zilvervisjes",
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
