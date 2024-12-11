from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OnderhoudspecialismeReferentiedata(Referentiedata):
    pass


class Onderhoudspecialisme(Referentiedatasoort):
    specialist_alarminstallaties = OnderhoudspecialismeReferentiedata(
        code="ALA",
        naam="Specialist Alarminstallaties",
    )
    """
    Specialisme die zich bezig houdt met de installatie en onderhoud van
    alarminstallaties en andere beveiligingsystemen
    """

    specialist_asbestsanering = OnderhoudspecialismeReferentiedata(
        code="ASB",
        naam="Specialist Asbestsanering",
    )
    """
    Inventarisatie en sanering van asbest
    """

    specialist_bliksemgeleider = OnderhoudspecialismeReferentiedata(
        code="BLI",
        naam="Specialist Bliksemgeleider",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_blusmiddelen = OnderhoudspecialismeReferentiedata(
        code="BLU",
        naam="Specialist Blusmiddelen",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_brandmeldinstallatie = OnderhoudspecialismeReferentiedata(
        code="BRA",
        naam="Specialist Brandmeldinstallatie",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    cv_installateur = OnderhoudspecialismeReferentiedata(
        code="CVI",
        naam="CV Installateur",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    dakdekker = OnderhoudspecialismeReferentiedata(
        code="DAK",
        naam="Dakdekker",
    )
    """
    Specialist die dakbedekking aanbrengt op platte en licht hellende daken.
    Gespecialiseerd in het toepassen en verwerken van diverse materialen die
    gebruikt worden om deze daken waterdicht en bestand te maken tegen verschillende
    weersinvloeden
    """

    specialist_domotica = OnderhoudspecialismeReferentiedata(
        code="DOM",
        naam="Specialist Domotica",
    )
    """
    Specialist op het gebied van installatie en onderhoud van domotica-systemen
    """

    elektricien_allrounder = OnderhoudspecialismeReferentiedata(
        code="ELA",
        naam="Elektriciën allrounder",
    )
    """
    De allrounder elektricien kan kleine elektra-werkzaamheden uitvoeren.Relatie met
    Ketenstandaard: competentiecode ELE - Electra
    """

    elektricien = OnderhoudspecialismeReferentiedata(
        code="ELE",
        naam="Elektriciën",
    )
    """
    Een volwaardige elektriciënRelatie met Ketenstandaard: competentiecode ELE - Electra
    """

    specialist_elektrische_toegangsdeuren = OnderhoudspecialismeReferentiedata(
        code="ELT",
        naam="Specialist Elektrische Toegangsdeuren",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_geiser = OnderhoudspecialismeReferentiedata(
        code="GEI",
        naam="Specialist Geiser",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    glaszetter = OnderhoudspecialismeReferentiedata(
        code="GLA",
        naam="Glaszetter",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    hovenier = OnderhoudspecialismeReferentiedata(
        code="HOV",
        naam="Hovenier",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_hydrofoor = OnderhoudspecialismeReferentiedata(
        code="HYD",
        naam="Specialist Hydrofoor",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    inspecteur = OnderhoudspecialismeReferentiedata(
        code="INS",
        naam="Inspecteur",
    )
    """
    Medewerker die een inspectie uit gaat voeren. Dit kan voorafgaand aan de opdracht
    zijn (bijvoorbeeld bij mutatie of reparatie) maar ook achteraf
    (steekproef-controle)Binnen Ketenstandaard is hier op dit moment geen specifieke
    codering voor beschikbaar
    """

    specialist_lift = OnderhoudspecialismeReferentiedata(
        code="LIF",
        naam="Specialist Lift",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    loodgieter_allrounder = OnderhoudspecialismeReferentiedata(
        code="LOA",
        naam="Loodgieter allrounder",
    )
    """
    De allrounder loodgieter kan kleine loodgieter-werkzaamheden uitvoeren.Relatie met
    Ketenstandaard: competentiecode LOO  - Loodgieter
    """

    loodgieter = OnderhoudspecialismeReferentiedata(
        code="LOO",
        naam="Loodgieter",
    )
    """
    Een volwaardige loodgieter. Relatie met Ketenstandaard: competentiecode LOO  -
    Loodgieter
    """

    ongediertebestrijder = OnderhoudspecialismeReferentiedata(
        code="ONG",
        naam="Ongediertebestrijder",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    ontstopper = OnderhoudspecialismeReferentiedata(
        code="ONT",
        naam="Ontstopper",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    overig = OnderhoudspecialismeReferentiedata(
        code="OVE",
        naam="Overig",
    )
    """
    Overige specialismen die niet onder één van de andere onderhoudspecialismen vallen
    """

    schilder = OnderhoudspecialismeReferentiedata(
        code="SCH",
        naam="Schilder",
    )
    """
    Een volwaardige schilder
    """

    schoonmaker = OnderhoudspecialismeReferentiedata(
        code="SCM",
        naam="Schoonmaker",
    )
    """
    Algemene specialisme voor schoonmaken, onder andere in de woning maar ook zaken als
    dakgoot schoonmaken en graffiti verwijderen
    """

    stucadoor = OnderhoudspecialismeReferentiedata(
        code="STU",
        naam="Stucadoor",
    )
    """
    Een volwaardige stucadoor. Relatie met Ketenstandaard: competentiecode STU - Stucen
    """

    timmerman_allrounder = OnderhoudspecialismeReferentiedata(
        code="TAL",
        naam="Timmerman allrounder",
    )
    """
    De allrounder timmerman kan kleine timmer-werkzaamheden uitvoeren.Relatie met
    Ketenstandaard: competentiecode TIM - Timmerman
    """

    tegelzetter = OnderhoudspecialismeReferentiedata(
        code="TEG",
        naam="Tegelzetter",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    timmerman = OnderhoudspecialismeReferentiedata(
        code="TIM",
        naam="Timmerman",
    )
    """
    Een volwaardige timmermanRelatie met Ketenstandaard: competentiecode TIM - Timmerman
    """

    specialist_vochtwering = OnderhoudspecialismeReferentiedata(
        code="VOC",
        naam="Specialist Vochtwering",
    )
    """
    Specialist voor schimmel en vocht bestrijding
    """

    specialist_witgoed = OnderhoudspecialismeReferentiedata(
        code="WIT",
        naam="Specialist Witgoed",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_mv_en_of_wtw = OnderhoudspecialismeReferentiedata(
        code="WTW",
        naam="Specialist MV/WTW",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_zonnepanelen = OnderhoudspecialismeReferentiedata(
        code="ZON",
        naam="Specialist Zonnepanelen",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_zonwering = OnderhoudspecialismeReferentiedata(
        code="ZWE",
        naam="Specialist Zonwering",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """
