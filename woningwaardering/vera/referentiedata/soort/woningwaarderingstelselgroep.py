from woningwaardering.vera.bvg.generated import Referentiedata


class Woningwaarderingstelselgroep:
    bijzondere_voorzieningen = Referentiedata(
        code="BIJ",
        naam="Bijzondere voorzieningen",
    )
    """
    De groep criteria die betrekking heeft op de aanwezigheid van bijzondere
    voorzieningen, uitsluitend van toepassing bij zorgwoningen (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    beschermd_monument_bmo = Referentiedata(
        code="BMO",
        naam="Beschermd monument",
    )
    """
    De extra punten die worden toegekend als de woonruimte bestaat uit of deel uitmaakt
    van een rijksmonument (Beleidsboek Waarderingsstelsel onzelfstandige woonruimte)
    """

    beschermd_monument_bmz = Referentiedata(
        code="BMZ",
        naam="Beschermd monument",
    )
    """
    De extra punten die worden toegekend als de woonruimte bestaat uit of deel uitmaakt
    van een rijksmonument (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    berging = Referentiedata(
        code="BWN",
        naam="Berging",
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op de aanwezigheid
    van een berging (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    energieprestatie = Referentiedata(
        code="ENE",
        naam="Energieprestatie",
    )
    """
    De groep criteria die betrekking heeft op de energieprestaties (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    extra_punten_woonoppervlakte_standplaats = Referentiedata(
        code="EOS",
        naam="Extra punten woonoppervlakte standplaats",
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de woonoppervlakte als die
    meer dan 200m2 bedraagt (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    woonvoorzieningen_voor_gehandicapten = Referentiedata(
        code="GEH",
        naam="Woonvoorzieningen voor gehandicapten",
    )
    """
    De groep criteria die betrekking heeft op ingrepen die zijn gedaan ten behoeve van
    een gehandicapte (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    voorzieningen_gehandicapten_standplaats = Referentiedata(
        code="GST",
        naam="Voorzieningen gehandicapten standplaats",
    )
    """
    Standplaats: De groep criteria die betrekking heeft op (gedeeltelijk) vanuit de WMO
    gesubsidieerde voorzieningen voor gehandicapten (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    voorzieningen_gehandicapten_niet_standaardwoonwagen = Referentiedata(
        code="GWN",
        naam="Voorzieningen gehandicapten niet-standaardwoonwagen",
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op (gedeeltelijk)
    vanuit de WMO gesubsidieerde voorzieningen voor gehandicapten (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    voorzieningen_gehandicapten_standaardwoonwagen = Referentiedata(
        code="GWS",
        naam="Voorzieningen gehandicapten standaardwoonwagen",
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op (gedeeltelijk) vanuit
    de WMO gesubsidieerde voorzieningen voor gehandicapten (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    keuken = Referentiedata(
        code="KEU",
        naam="Keuken",
    )
    """
    De groep criteria die betrekking heeft op de keuken (Beleidsboek Waarderingsstelsel
    zelfstandige woonruimte)
    """

    kookgelegenheid = Referentiedata(
        code="KOO",
        naam="Kookgelegenheid",
    )
    """
    De groep criteria die betrekking heeft op de kookgelegenheid (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    extra_kwaliteit_keuken_en_sanitair_standplaats = Referentiedata(
        code="KST",
        naam="Extra kwaliteit keuken en sanitair standplaats",
    )
    """
    Standplaats: De groep criteria die betrekking heeft op extra kwaliteit van keuken en
    sanitair  (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    kwaliteitsfactoren = Referentiedata(
        code="KWA",
        naam="Kwaliteitsfactoren",
    )
    """
    De groep criteria die betrekking heeft op aanvullende kwaliteitsfactoren
    (Beleidsboek Waarderingsstelsel onzelfstandige woonruimte)
    """

    keuken_en_sanitair_niet_standaardwoonwagen = Referentiedata(
        code="KWN",
        naam="Keuken en sanitair niet-standaardwoonwagen",
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op keuken en
    sanitair  (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    extra_kwaliteit_keuken_en_sanitair_standaardwoonwagen = Referentiedata(
        code="KWS",
        naam="Extra kwaliteit keuken en sanitair standaardwoonwagen",
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op extra kwaliteit van
    keuken en sanitair  (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    minpunten_woonomgeving_standplaats = Referentiedata(
        code="MWS",
        naam="Minpunten woonomgeving standplaats",
    )
    """
    Standplaats: De groep criteria die betrekking heeft op hinderlijke situaties in de
    woonomgeving (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    oppervlakte_van_overige_ruimten = Referentiedata(
        code="OOZ",
        naam="Oppervlakte van overige ruimten",
    )
    """
    Tot deze ruimten worden gerekend: bijkeukens, bergingen, wasruimten, schuren,
    garages, zolders en kelders (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    oppervlakte_onzelfstandige_woonruimte = Referentiedata(
        code="OPO",
        naam="Oppervlakte onzelfstandige woonruimte",
    )
    """
    De groep criteria die betrekking heeft op de oppervlakte van kamers en keukens, en
    van verwarmde gemeenschappelijke verblijfsruimten (Beleidsboek Waarderingsstelsel
    onzelfstandige woonruimte)
    """

    oppervlakte_standplaats = Referentiedata(
        code="OST",
        naam="Oppervlakte standplaats",
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de oppervlakte
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    oppervlakte_van_vertrekken = Referentiedata(
        code="OVZ",
        naam="Oppervlakte van vertrekken",
    )
    """
    Onder vertrekken worden verstaan: woonkamer, andere kamers, keuken, badkamer en
    doucheruimte (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    oppervlakte_niet_standaardwoonwagen = Referentiedata(
        code="OWN",
        naam="Oppervlakte niet-standaardwoonwagen",
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op de oppervlakte
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    oppervlakte_standaardwoonwagen = Referentiedata(
        code="OWS",
        naam="Oppervlakte standaardwoonwagen",
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op de oppervlakte
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    prive_buitenruimten = Referentiedata(
        code="PRI",
        naam="Privé-buitenruimten",
    )
    """
    Privé-buitenruimten zijn tot de woning behorende buitenruimten, waarvan de bewoners
    van de desbetreffende woning krachtens de huurovereenkomst het exclusieve
    gebruiksrecht hebben. Dit kunnen onder meer voor-, zij- of achtertuinen, balkons,
    platjes of terrassen zijn (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    renovatie = Referentiedata(
        code="REN",
        naam="Renovatie",
    )
    """
    De groep criteria die betrekking heeft op renovatie van de woonruimte (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    sanitair = Referentiedata(
        code="SAN",
        naam="Sanitair",
    )
    """
    De groep criteria die betrekking heeft op het sanitair (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    toilet = Referentiedata(
        code="TOI",
        naam="Toilet",
    )
    """
    De groep criteria die betrekking heeft op de w.c. (Beleidsboek Waarderingsstelsel
    onzelfstandige woonruimte)
    """

    verwarmingsmogelijkheden = Referentiedata(
        code="VON",
        naam="Verwarmingsmogelijkheden",
    )
    """
    De groep criteria die betrekking heeft op de verwarmingsmogelijkheden (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    verwarming_standplaats = Referentiedata(
        code="VST",
        naam="Verwarming standplaats",
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de verwarming (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    verwarming_niet_standaardwoonwagen = Referentiedata(
        code="VWN",
        naam="Verwarming niet-standaardwoonwagen",
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op de verwarming
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    verwarming_standaardwoonwagen = Referentiedata(
        code="VWS",
        naam="Verwarming standaardwoonwagen",
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op de verwarming
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    verwarming = Referentiedata(
        code="VZE",
        naam="Verwarming",
    )
    """
    Vertrekken, die met punten als vertrek zijn gewaardeerd, en die verwarmd zijn. Open
    keukens, of vertrekken die met een schuifwand met elkaar in verbinding staan, worden
    als afzonderlijk vertrek geteld (Beleidsboek Waarderingsstelsel zelfstandige
    woonruimte)
    """

    wasgelegenheid = Referentiedata(
        code="WAS",
        naam="Wasgelegenheid",
    )
    """
    De groep criteria die betrekking heeft op douche, bad en wastafel (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    punten_voor_de_woz_waarde = Referentiedata(
        code="WOZ",
        naam="Punten voor de WOZ-waarde",
    )
    """
    De groep criteria die betrekking heeft op de vastgestelde WOZ-waarde (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    woonomgeving_standplaats = Referentiedata(
        code="WST",
        naam="Woonomgeving standplaats",
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de woonomgeving
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """
