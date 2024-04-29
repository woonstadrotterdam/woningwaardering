from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Woningwaarderingstelselgroep(Enum):
    bijzondere_voorzieningen = Referentiedata(
        code="BIJ",
        naam="Bijzondere voorzieningen",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op de aanwezigheid van bijzondere
    voorzieningen, uitsluitend van toepassing bij zorgwoningen (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    beschermd_monument_bmo = Referentiedata(
        code="BMO",
        naam="Beschermd monument",
        parent=Referentiedata(
            code="ONZ",
            naam="Onzelfstandige woonruimten",
        ),
    )
    """
    De extra punten die worden toegekend als de woonruimte bestaat uit of deel uitmaakt
    van een rijksmonument (Beleidsboek Waarderingsstelsel onzelfstandige woonruimte)
    """

    beschermd_monument_bmz = Referentiedata(
        code="BMZ",
        naam="Beschermd monument",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    De extra punten die worden toegekend als de woonruimte bestaat uit of deel uitmaakt
    van een rijksmonument (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    berging = Referentiedata(
        code="BWN",
        naam="Berging",
        parent=Referentiedata(
            code="WOO",
            naam="Woonwagens",
        ),
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op de aanwezigheid
    van een berging (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    energieprestatie = Referentiedata(
        code="ENE",
        naam="Energieprestatie",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op de energieprestaties (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    extra_punten_woonoppervlakte_standplaats = Referentiedata(
        code="EOS",
        naam="Extra punten woonoppervlakte standplaats",
        parent=Referentiedata(
            code="STA",
            naam="Standplaatsen",
        ),
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de woonoppervlakte als die
    meer dan 200m2 bedraagt (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    woonvoorzieningen_voor_gehandicapten = Referentiedata(
        code="GEH",
        naam="Woonvoorzieningen voor gehandicapten",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op ingrepen die zijn gedaan ten behoeve van
    een gehandicapte (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    voorzieningen_gehandicapten_standplaats = Referentiedata(
        code="GST",
        naam="Voorzieningen gehandicapten standplaats",
        parent=Referentiedata(
            code="STA",
            naam="Standplaatsen",
        ),
    )
    """
    Standplaats: De groep criteria die betrekking heeft op (gedeeltelijk) vanuit de WMO
    gesubsidieerde voorzieningen voor gehandicapten (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    voorzieningen_gehandicapten_niet_standaardwoonwagen = Referentiedata(
        code="GWN",
        naam="Voorzieningen gehandicapten niet-standaardwoonwagen",
        parent=Referentiedata(
            code="WOO",
            naam="Woonwagens",
        ),
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op (gedeeltelijk)
    vanuit de WMO gesubsidieerde voorzieningen voor gehandicapten (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    voorzieningen_gehandicapten_standaardwoonwagen = Referentiedata(
        code="GWS",
        naam="Voorzieningen gehandicapten standaardwoonwagen",
        parent=Referentiedata(
            code="WOO",
            naam="Woonwagens",
        ),
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op (gedeeltelijk) vanuit
    de WMO gesubsidieerde voorzieningen voor gehandicapten (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    keuken = Referentiedata(
        code="KEU",
        naam="Keuken",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op de keuken (Beleidsboek Waarderingsstelsel
    zelfstandige woonruimte)
    """

    kookgelegenheid = Referentiedata(
        code="KOO",
        naam="Kookgelegenheid",
        parent=Referentiedata(
            code="ONZ",
            naam="Onzelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op de kookgelegenheid (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    extra_kwaliteit_keuken_en_sanitair_standplaats = Referentiedata(
        code="KST",
        naam="Extra kwaliteit keuken en sanitair standplaats",
        parent=Referentiedata(
            code="STA",
            naam="Standplaatsen",
        ),
    )
    """
    Standplaats: De groep criteria die betrekking heeft op extra kwaliteit van keuken en
    sanitair  (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    kwaliteitsfactoren = Referentiedata(
        code="KWA",
        naam="Kwaliteitsfactoren",
        parent=Referentiedata(
            code="ONZ",
            naam="Onzelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op aanvullende kwaliteitsfactoren
    (Beleidsboek Waarderingsstelsel onzelfstandige woonruimte)
    """

    keuken_en_sanitair_niet_standaardwoonwagen = Referentiedata(
        code="KWN",
        naam="Keuken en sanitair niet-standaardwoonwagen",
        parent=Referentiedata(
            code="WOO",
            naam="Woonwagens",
        ),
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op keuken en
    sanitair  (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    extra_kwaliteit_keuken_en_sanitair_standaardwoonwagen = Referentiedata(
        code="KWS",
        naam="Extra kwaliteit keuken en sanitair standaardwoonwagen",
        parent=Referentiedata(
            code="WOO",
            naam="Woonwagens",
        ),
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op extra kwaliteit van
    keuken en sanitair  (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    minpunten_woonomgeving_standplaats = Referentiedata(
        code="MWS",
        naam="Minpunten woonomgeving standplaats",
        parent=Referentiedata(
            code="STA",
            naam="Standplaatsen",
        ),
    )
    """
    Standplaats: De groep criteria die betrekking heeft op hinderlijke situaties in de
    woonomgeving (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    oppervlakte_van_overige_ruimten = Referentiedata(
        code="OOZ",
        naam="Oppervlakte van overige ruimten",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    Tot deze ruimten worden gerekend: bijkeukens, bergingen, wasruimten, schuren,
    garages, zolders en kelders (Beleidsboek Waarderingsstelsel zelfstandige
    woonruimte)
    """

    oppervlakte_onzelfstandige_woonruimte = Referentiedata(
        code="OPO",
        naam="Oppervlakte onzelfstandige woonruimte",
        parent=Referentiedata(
            code="ONZ",
            naam="Onzelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op de oppervlakte van kamers en keukens, en
    van verwarmde gemeenschappelijke verblijfsruimten (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    oppervlakte_standplaats = Referentiedata(
        code="OST",
        naam="Oppervlakte standplaats",
        parent=Referentiedata(
            code="STA",
            naam="Standplaatsen",
        ),
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de oppervlakte
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    oppervlakte_van_vertrekken = Referentiedata(
        code="OVZ",
        naam="Oppervlakte van vertrekken",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    Onder vertrekken worden verstaan: woonkamer, andere kamers, keuken, badkamer en
    doucheruimte (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    oppervlakte_niet_standaardwoonwagen = Referentiedata(
        code="OWN",
        naam="Oppervlakte niet-standaardwoonwagen",
        parent=Referentiedata(
            code="WOO",
            naam="Woonwagens",
        ),
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op de oppervlakte
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    oppervlakte_standaardwoonwagen = Referentiedata(
        code="OWS",
        naam="Oppervlakte standaardwoonwagen",
        parent=Referentiedata(
            code="WOO",
            naam="Woonwagens",
        ),
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op de oppervlakte
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    prive_buitenruimten = Referentiedata(
        code="PRI",
        naam="Privé-buitenruimten",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    Privé-buitenruimten zijn tot de woning behorende buitenruimten, waarvan de bewoners
    van de desbetreffende woning krachtens de huurovereenkomst het exclusieve
    gebruiksrecht hebben. Dit kunnen onder meer voor-, zij- of achtertuinen,
    balkons, platjes of terrassen zijn (Beleidsboek Waarderingsstelsel zelfstandige
    woonruimte)
    """

    renovatie = Referentiedata(
        code="REN",
        naam="Renovatie",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op renovatie van de woonruimte (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    sanitair = Referentiedata(
        code="SAN",
        naam="Sanitair",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op het sanitair (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    toilet = Referentiedata(
        code="TOI",
        naam="Toilet",
        parent=Referentiedata(
            code="ONZ",
            naam="Onzelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op de w.c. (Beleidsboek Waarderingsstelsel
    onzelfstandige woonruimte)
    """

    verwarmingsmogelijkheden = Referentiedata(
        code="VON",
        naam="Verwarmingsmogelijkheden",
        parent=Referentiedata(
            code="ONZ",
            naam="Onzelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op de verwarmingsmogelijkheden (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    verwarming_standplaats = Referentiedata(
        code="VST",
        naam="Verwarming standplaats",
        parent=Referentiedata(
            code="STA",
            naam="Standplaatsen",
        ),
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de verwarming (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    verwarming_niet_standaardwoonwagen = Referentiedata(
        code="VWN",
        naam="Verwarming niet-standaardwoonwagen",
        parent=Referentiedata(
            code="WOO",
            naam="Woonwagens",
        ),
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op de verwarming
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    verwarming_standaardwoonwagen = Referentiedata(
        code="VWS",
        naam="Verwarming standaardwoonwagen",
        parent=Referentiedata(
            code="WOO",
            naam="Woonwagens",
        ),
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op de verwarming
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    verwarming = Referentiedata(
        code="VZE",
        naam="Verwarming",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    Vertrekken, die met punten als vertrek zijn gewaardeerd, en die verwarmd zijn. Open
    keukens, of vertrekken die met een schuifwand met elkaar in verbinding staan,
    worden als afzonderlijk vertrek geteld (Beleidsboek Waarderingsstelsel
    zelfstandige woonruimte)
    """

    wasgelegenheid = Referentiedata(
        code="WAS",
        naam="Wasgelegenheid",
        parent=Referentiedata(
            code="ONZ",
            naam="Onzelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op douche, bad en wastafel (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    punten_voor_de_woz_waarde = Referentiedata(
        code="WOZ",
        naam="Punten voor de WOZ-waarde",
        parent=Referentiedata(
            code="ZEL",
            naam="Zelfstandige woonruimten",
        ),
    )
    """
    De groep criteria die betrekking heeft op de vastgestelde WOZ-waarde (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    woonomgeving_standplaats = Referentiedata(
        code="WST",
        naam="Woonomgeving standplaats",
        parent=Referentiedata(
            code="STA",
            naam="Standplaatsen",
        ),
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de woonomgeving
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
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
