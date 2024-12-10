from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ProjectsoortReferentiedata(Referentiedata):
    pass


class Projectsoort(Referentiedatasoort):
    grondexploitatie = ProjectsoortReferentiedata(
        code="GRX",
        naam="Grondexploitatie",
    )
    """
    Een project dat tot doel heeft een stuk grond te exploiteren, van het moment van
    verwerving tot het moment van ontwikkeling of verkoop. Aan de basis van een
    grondexploitatie project (soms afgekort tot grex) ligt een begroting die wordt
    opgesteld om grondkosten en grondopbrengsten van een ruimtelijk
    ontwikkelingsplan in beeld te brengen. De begroting dient als kader voor
    onderhandelingen over mogelijke aan- en verkoop van gronden (en/of opstallen) en
    wordt als basis gebruikt om een exploitatieovereenkomst of exploitatieplan op te
    stellen. (Bron: vrij naar Wikipedia)
    """

    modulaire_bouw = ProjectsoortReferentiedata(
        code="MOD",
        naam="Modulaire bouw",
    )
    """
    Bouwtechniek waarbij modules worden gekoppeld of gestapeld om een gebouw te creëren.
    De modules worden gebruiksklaar in een fabriek geproduceerd en worden met behulp
    van een hijskraan geplaatst op locatie. Daarna moeten modules alleen worden
    geïnstalleerd en aangesloten (Bron: Portakabin)
    """

    nieuwbouw = ProjectsoortReferentiedata(
        code="NIU",
        naam="Nieuwbouw",
    )
    """
    Project waarbij een of meer eenheden aan de voorraad worden toegevoegd door
    nieuwbouw, zonder dat daarvoor op het(/de)zelde perce(e)l(en) eerst een of meer
    eenheden zijn gesloopt
    """

    renovatie_bewoond = ProjectsoortReferentiedata(
        code="REB",
        naam="Renovatie bewoond",
    )
    """
    Renovatieproject waarbij (een deel van) de bewoners in hun woning blijven.Er is
    sprake van een renovatie (of: ‘ingrijpende verbouwing’) als een onroerende zaak
    technisch en economisch gezien hoogst verouderd is, of als van een onroerende
    zaak een gedeelte bouwvallig is, welk gedeelte wordt afgebroken, en in het
    overblijvende gedeelte een groot aantal veranderingen en vernieuwingen wordt
    aangebracht.Een renovatieproject is erop gericht bij de verhuurbare eenheid,
    danwel het complex een hedendaagse kwaliteit tot stand te brengen waar dit in de
    bestaande situatie niet het geval was (Bron: SBR-Wonen).
    """

    renovatie_onbewoond = ProjectsoortReferentiedata(
        code="REO",
        naam="Renovatie onbewoond",
    )
    """
    Renovatieproject waarbij alle bewoners (tijdelijk) hun woningen verlaten.Er is
    sprake van een renovatie (of: ‘ingrijpende verbouwing’) als een onroerende zaak
    technisch en economisch gezien hoogst verouderd is, of als van een onroerende
    zaak een gedeelte bouwvallig is, welk gedeelte wordt afgebroken, en in het
    overblijvende gedeelte een groot aantal veranderingen en vernieuwingen wordt
    aangebracht.Een renovatieproject is erop gericht bij de verhuurbare eenheid,
    danwel het complex een hedendaagse kwaliteit tot stand te brengen waar dit in de
    bestaande situatie niet het geval was (Bron: SBR-Wonen).
    """

    sloop_en_nieuwbouw = ProjectsoortReferentiedata(
        code="SLN",
        naam="Sloop- en Nieuwbouw",
    )
    """
    Project waarbij een of meer eenheden aan de voorraad worden onttrokken door sloop,
    waarna een of meer nieuwe eenheden aan de voorraad worden toegevoegd door
    nieuwbouw op het(/de)zelde perce(e)l(en)
    """

    sloop = ProjectsoortReferentiedata(
        code="SLO",
        naam="Sloop",
    )
    """
    Project waarbij een of meer eenheden aan de voorraad worden onttrokken door sloop,
    zonder dat daar nieuwbouw op het(/de)zelde perce(e)l(en) tegenover staat
    """

    transformatie = ProjectsoortReferentiedata(
        code="TRA",
        naam="Transformatie",
    )
    """
    Een transformatieproject beoogt “het hergebruik van bestaande panden waarbij
    hetgebruik van het pand (deels) wordt omgezet van een niet-woonfunctie naar een
    woonfunctie” (bron: CBS).Let op: Het splitsen van woningen in meerdere eenheden
    valt niet onder deze definitie, om dat er geen herbestemming van de functie van
    het pand plaatsvindt.
    """
