from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Onderhoudspecialisme(Enum):
    specialist_alarminstallaties = Referentiedata(
        code="ALA",
        naam="Specialist Alarminstallaties",
    )
    """
    Specialisme die zich bezig houdt met de installatie en onderhoud van
    alarminstallaties en andere beveiligingsystemen
    """

    specialist_asbestsanering = Referentiedata(
        code="ASB",
        naam="Specialist Asbestsanering",
    )
    """
    Inventarisatie en sanering van asbest
    """

    specialist_bliksemgeleider = Referentiedata(
        code="BLI",
        naam="Specialist Bliksemgeleider",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_blusmiddelen = Referentiedata(
        code="BLU",
        naam="Specialist Blusmiddelen",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_brandmeldinstallatie = Referentiedata(
        code="BRA",
        naam="Specialist Brandmeldinstallatie",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    cv_installateur = Referentiedata(
        code="CVI",
        naam="CV Installateur",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    dakdekker = Referentiedata(
        code="DAK",
        naam="Dakdekker",
    )
    """
    Specialist die dakbedekking aanbrengt op platte en licht hellende daken.
    Gespecialiseerd in het toepassen en verwerken van diverse materialen die
    gebruikt worden om deze daken waterdicht en bestand te maken tegen verschillende
    weersinvloeden
    """

    specialist_domotica = Referentiedata(
        code="DOM",
        naam="Specialist Domotica",
    )
    """
    Specialist op het gebied van installatie en onderhoud van domotica-systemen
    """

    elektricien_allrounder = Referentiedata(
        code="ELA",
        naam="Elektriciën allrounder",
    )
    """
    De allrounder elektricien kan kleine elektra-werkzaamheden uitvoeren.Relatie met
    Ketenstandaard: competentiecode ELE - Electra
    """

    elektricien = Referentiedata(
        code="ELE",
        naam="Elektriciën",
    )
    """
    Een volwaardige elektriciënRelatie met Ketenstandaard: competentiecode ELE - Electra
    """

    specialist_elektrische_toegangsdeuren = Referentiedata(
        code="ELT",
        naam="Specialist Elektrische Toegangsdeuren",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_geiser = Referentiedata(
        code="GEI",
        naam="Specialist Geiser",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    glaszetter = Referentiedata(
        code="GLA",
        naam="Glaszetter",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    hovenier = Referentiedata(
        code="HOV",
        naam="Hovenier",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_hydrofoor = Referentiedata(
        code="HYD",
        naam="Specialist Hydrofoor",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    inspecteur = Referentiedata(
        code="INS",
        naam="Inspecteur",
    )
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
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    loodgieter_allrounder = Referentiedata(
        code="LOA",
        naam="Loodgieter allrounder",
    )
    """
    De allrounder loodgieter kan kleine loodgieter-werkzaamheden uitvoeren.Relatie met
    Ketenstandaard: competentiecode LOO  - Loodgieter
    """

    loodgieter = Referentiedata(
        code="LOO",
        naam="Loodgieter",
    )
    """
    Een volwaardige loodgieter. Relatie met Ketenstandaard: competentiecode LOO  -
    Loodgieter
    """

    ongediertebestrijder = Referentiedata(
        code="ONG",
        naam="Ongediertebestrijder",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    ontstopper = Referentiedata(
        code="ONT",
        naam="Ontstopper",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )
    """
    Overige specialismen die niet onder één van de andere onderhoudspecialismen vallen
    """

    schilder = Referentiedata(
        code="SCH",
        naam="Schilder",
    )
    """
    Een volwaardige schilder
    """

    schoonmaker = Referentiedata(
        code="SCM",
        naam="Schoonmaker",
    )
    """
    Algemene specialisme voor schoonmaken, onder andere in de woning maar ook zaken als
    dakgoot schoonmaken en graffiti verwijderen
    """

    stucadoor = Referentiedata(
        code="STU",
        naam="Stucadoor",
    )
    """
    Een volwaardige stucadoor. Relatie met Ketenstandaard: competentiecode STU - Stucen
    """

    timmerman_allrounder = Referentiedata(
        code="TAL",
        naam="Timmerman allrounder",
    )
    """
    De allrounder timmerman kan kleine timmer-werkzaamheden uitvoeren.Relatie met
    Ketenstandaard: competentiecode TIM - Timmerman
    """

    tegelzetter = Referentiedata(
        code="TEG",
        naam="Tegelzetter",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    timmerman = Referentiedata(
        code="TIM",
        naam="Timmerman",
    )
    """
    Een volwaardige timmermanRelatie met Ketenstandaard: competentiecode TIM - Timmerman
    """

    specialist_vochtwering = Referentiedata(
        code="VOC",
        naam="Specialist Vochtwering",
    )
    """
    Specialist voor schimmel en vocht bestrijding
    """

    specialist_witgoed = Referentiedata(
        code="WIT",
        naam="Specialist Witgoed",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_mv_en_of_wtw = Referentiedata(
        code="WTW",
        naam="Specialist MV/WTW",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_zonnepanelen = Referentiedata(
        code="ZON",
        naam="Specialist Zonnepanelen",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
    """

    specialist_zonwering = Referentiedata(
        code="ZWE",
        naam="Specialist Zonwering",
    )
    """
    Binnen Ketenstandaard is hier op dit moment geen specifieke codering voor,
    vooralsnog gebruik maken van competentiecode OVE - Overige
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
