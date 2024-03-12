
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ONDERHOUDSPECIALISME:

    specialist_alarminstallaties = Referentiedata(
        code="ALA",
        naam="Specialist Alarminstallaties",
    )
    # specialist_alarminstallaties = ("ALA", "Specialist Alarminstallaties")
    """
    Specialisme die zich bezig houdt met de installatie en onderhoud van
    alarminstallaties en andere beveiligingsystemen
    """

    specialist_asbestsanering = Referentiedata(
        code="ASB",
        naam="Specialist Asbestsanering",
    )
    # specialist_asbestsanering = ("ASB", "Specialist Asbestsanering")
    """
    Inventarisatie en sanering van asbest
    """

    specialist_bliksemgeleider = Referentiedata(
        code="BLI",
        naam="Specialist Bliksemgeleider",
    )
    # specialist_bliksemgeleider = ("BLI", "Specialist Bliksemgeleider")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_blusmiddelen = Referentiedata(
        code="BLU",
        naam="Specialist Blusmiddelen",
    )
    # specialist_blusmiddelen = ("BLU", "Specialist Blusmiddelen")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_brandmeldinstallatie = Referentiedata(
        code="BRA",
        naam="Specialist Brandmeldinstallatie",
    )
    # specialist_brandmeldinstallatie = ("BRA", "Specialist Brandmeldinstallatie")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    cv_installateur = Referentiedata(
        code="CVI",
        naam="CV Installateur",
    )
    # cv_installateur = ("CVI", "CV Installateur")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    dakdekker = Referentiedata(
        code="DAK",
        naam="Dakdekker",
    )
    # dakdekker = ("DAK", "Dakdekker")
    """
    Specialist die dakbedekking aanbrengt op platte en licht hellende daken.
    Gespecialiseerd in het toepassen en verwerken van diverse materialen die gebruikt
    worden om deze daken waterdicht en bestand te maken tegen verschillende
    weersinvloeden
    """

    specialist_domotica = Referentiedata(
        code="DOM",
        naam="Specialist Domotica",
    )
    # specialist_domotica = ("DOM", "Specialist Domotica")
    """
    Specialist op het gebied van installatie en onderhoud van domotica-systemen
    """

    elektricien_allrounder = Referentiedata(
        code="ELA",
        naam="Elektriciën allrounder",
    )
    # elektricien_allrounder = ("ELA", "Elektriciën allrounder")
    """
    De allrounder elektricien kan kleine elektra-werkzaamheden uitvoeren.Relatie met
    Ketenstandaard: competentiecode ELE - Electra
    """

    elektricien = Referentiedata(
        code="ELE",
        naam="Elektriciën",
    )
    # elektricien = ("ELE", "Elektriciën")
    """
    Een volwaardige elektriciënRelatie met Ketenstandaard: competentiecode ELE - Electra
    """

    specialist_elektrische_toegangsdeuren = Referentiedata(
        code="ELT",
        naam="Specialist Elektrische Toegangsdeuren",
    )
    # specialist_elektrische_toegangsdeuren = ("ELT", "Specialist Elektrische Toegangsdeuren")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_geiser = Referentiedata(
        code="GEI",
        naam="Specialist Geiser",
    )
    # specialist_geiser = ("GEI", "Specialist Geiser")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    glaszetter = Referentiedata(
        code="GLA",
        naam="Glaszetter",
    )
    # glaszetter = ("GLA", "Glaszetter")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    hovenier = Referentiedata(
        code="HOV",
        naam="Hovenier",
    )
    # hovenier = ("HOV", "Hovenier")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_hydrofoor = Referentiedata(
        code="HYD",
        naam="Specialist Hydrofoor",
    )
    # specialist_hydrofoor = ("HYD", "Specialist Hydrofoor")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    inspecteur = Referentiedata(
        code="INS",
        naam="Inspecteur",
    )
    # inspecteur = ("INS", "Inspecteur")
    """
    Medewerker die een inspectie uit gaat voeren. Dit kan voorafgaand aan de opdracht
    zijn (bijvoorbeeld bij mutatie of reparatie) maar ook achteraf
    (steekproef-controle)Binnen Ketenstandaard is hier op dit moment geen specifieke
    codering voor beschikbaar
    """

    specialist_lift = Referentiedata(
        code="LIF",
        naam="Specialist Lift",
    )
    # specialist_lift = ("LIF", "Specialist Lift")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    loodgieter_allrounder = Referentiedata(
        code="LOA",
        naam="Loodgieter allrounder",
    )
    # loodgieter_allrounder = ("LOA", "Loodgieter allrounder")
    """
    De allrounder loodgieter kan kleine loodgieter-werkzaamheden uitvoeren.Relatie met
    Ketenstandaard: competentiecode LOO - Loodgieter
    """

    loodgieter = Referentiedata(
        code="LOO",
        naam="Loodgieter",
    )
    # loodgieter = ("LOO", "Loodgieter")
    """
    Een volwaardige loodgieter. Relatie met Ketenstandaard: competentiecode LOO -
    Loodgieter
    """

    ongediertebestrijder = Referentiedata(
        code="ONG",
        naam="Ongediertebestrijder",
    )
    # ongediertebestrijder = ("ONG", "Ongediertebestrijder")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    ontstopper = Referentiedata(
        code="ONT",
        naam="Ontstopper",
    )
    # ontstopper = ("ONT", "Ontstopper")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )
    # overig = ("OVE", "Overig")
    """
    Overige specialismen die niet onder één van de andere onderhoudspecialismen vallen
    """

    schilder = Referentiedata(
        code="SCH",
        naam="Schilder",
    )
    # schilder = ("SCH", "Schilder")
    """
    Een volwaardige schilder
    """

    schoonmaker = Referentiedata(
        code="SCM",
        naam="Schoonmaker",
    )
    # schoonmaker = ("SCM", "Schoonmaker")
    """
    Algemene specialisme voor schoonmaken, onder andere in de woning maar ook zaken als
    dakgoot schoonmaken en graffiti verwijderen
    """

    stucadoor = Referentiedata(
        code="STU",
        naam="Stucadoor",
    )
    # stucadoor = ("STU", "Stucadoor")
    """
    Een volwaardige stucadoor. Relatie met Ketenstandaard: competentiecode STU - Stucen
    """

    timmerman_allrounder = Referentiedata(
        code="TAL",
        naam="Timmerman allrounder",
    )
    # timmerman_allrounder = ("TAL", "Timmerman allrounder")
    """
    De allrounder timmerman kan kleine timmer-werkzaamheden uitvoeren.Relatie met
    Ketenstandaard: competentiecode TIM - Timmerman
    """

    tegelzetter = Referentiedata(
        code="TEG",
        naam="Tegelzetter",
    )
    # tegelzetter = ("TEG", "Tegelzetter")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    timmerman = Referentiedata(
        code="TIM",
        naam="Timmerman",
    )
    # timmerman = ("TIM", "Timmerman")
    """
    Een volwaardige timmermanRelatie met Ketenstandaard: competentiecode TIM - Timmerman
    """

    specialist_vochtwering = Referentiedata(
        code="VOC",
        naam="Specialist Vochtwering",
    )
    # specialist_vochtwering = ("VOC", "Specialist Vochtwering")
    """
    Specialist voor schimmel en vocht bestrijding
    """

    specialist_witgoed = Referentiedata(
        code="WIT",
        naam="Specialist Witgoed",
    )
    # specialist_witgoed = ("WIT", "Specialist Witgoed")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_mv_of_wtw = Referentiedata(
        code="WTW",
        naam="Specialist MV/WTW",
    )
    # specialist_mv_of_wtw = ("WTW", "Specialist MV/WTW")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_zonnepanelen = Referentiedata(
        code="ZON",
        naam="Specialist Zonnepanelen",
    )
    # specialist_zonnepanelen = ("ZON", "Specialist Zonnepanelen")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_zonwering = Referentiedata(
        code="ZWE",
        naam="Specialist Zonwering",
    )
    # specialist_zonwering = ("ZWE", "Specialist Zonwering")
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """
