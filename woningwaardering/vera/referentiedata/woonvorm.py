from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class WoonvormReferentiedata(Referentiedata):
    pass


class Woonvorm(Referentiedatasoort):
    adl_clusterwoning = WoonvormReferentiedata(
        code="ADL",
        naam="ADL-clusterwoning",
    )
    """
    Cluster van woningen met een centrale hulppost  (soms ook FOKUS woning genoemd) Met
    ADL kan 24 uur per dag hulp opgeroepen worden bij de algemene dagelijkse
    levensverrichtingen (ADL) in en om de woning
    """

    begeleid_wonen = WoonvormReferentiedata(
        code="BEG",
        naam="Begeleid wonen",
    )

    geclusterde_woonvorm = WoonvormReferentiedata(
        code="GEC",
        naam="Geclusterde woonvorm",
    )
    """
    Deze woning is een zelfstandige wooneenheid binnen een gebouw dat voldoet aan
    specifieke criteria voor geclusterde woonvormen. Dit omvat minimaal 12
    zelfstandige wooneenheden voor bewoners van 55 jaar en ouder, met een aanwezige
    ontmoetingsruimte in het gebouw of grenzend aan het gebouw. Deze woningen
    voldoen aan de uitgangspunten voor nultredenwoningen.
    """

    groepswonen = WoonvormReferentiedata(
        code="GRO",
        naam="Groepswonen",
    )
    """
    Een aantal privé-woningen of appartementen die samen een architecturale eenheid
    vormen met gemeenschappelijke voorzieningen, die zich beperken tot een
    gemeenschappelijke tuin, binnenplaats of bijvoorbeeld een logeerruimte. Een
    samenwoningsgroep kan bestaan uit gelijkgezinden, mensen met een specifieke
    leeftijd, etc. Ook wel geclusterd wonen genoemd.
    """

    grote_woonvorm = WoonvormReferentiedata(
        code="GRW",
        naam="Grote woonvorm",
    )
    """
    In een grote woonvorm wonen veel mensen met lichamelijke of meervoudige beperkingen
    bij elkaar. Deze mensen wonen zo zelfstandig mogelijk.
    """

    hat_eenheid = WoonvormReferentiedata(
        code="HAT",
        naam="HAT-eenheid",
    )
    """
    eenheden voor 1 of twee persoonshuishoudens met gezamelijke keuken, badkamer etc.
    """

    kleine_woonvorm = WoonvormReferentiedata(
        code="KLE",
        naam="Kleine woonvorm",
    )
    """
    gezinsvervangende tehuizen voor lichamelijk gehandicapten
    """

    seniorenwoning_met_zorg = WoonvormReferentiedata(
        code="SEN",
        naam="Seniorenwoning met zorg",
    )
    """
    Senioren woningen met zorg (voorheen Wibo-wonen in beschermde omgeving) zijn bij
    elkaar gelegen zelfstandige (aanleun)woningen met een dienstencentrum met
    allerlei voorzieningen dichtbij.
    """

    thomashuis = WoonvormReferentiedata(
        code="THO",
        naam="Thomashuis",
    )
    """
    Een Thomashuis is een kleinschalige woonvoorziening voor zes à acht mensen met een
    verstandelijke beperking
    """

    zorggeschikte_woning = WoonvormReferentiedata(
        code="ZWO",
        naam="Zorggeschikte woning",
    )
    """
    Woning die voldoet aan de criteria van Geclusterde woonvorm, maar met aanvullende
    voorzieningen om de woning beter geschikt te maken voor mensen met een beperking
    of voor zorgverlening. Bij nieuwbouw en getransformeerde woningen moet de
    woonvorm en woning rolstoelgeschikt zijn en bij verbouw moet de woonvorm
    rolstoelgeschikt zijn en de woning minimaal rollator-geschikt. Daarnaast moet de
    entree van de woning minimaal 90 centimeter breed zijn, moeten alle deuren
    automatisch kunnen openen en moeten woningen die niet op de begane grond zijn,
    bereikbaar zijn met een rolstoeltoegankelijke personenlift.
    """
