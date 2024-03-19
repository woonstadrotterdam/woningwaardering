from vera.bvg.generated import Referentiedata


class Woonvorm:
    adl_clusterwoning = Referentiedata(
        code="ADL",
        naam="ADL-clusterwoning",
    )
    """
    Cluster van woningen met een centrale hulppost  (soms ook FOKUS woning genoemd) Met
    ADL kan 24 uur per dag hulp opgeroepen worden bij de algemene dagelijkse
    levensverrichtingen (ADL) in en om de woning
    """

    begeleid_wonen = Referentiedata(
        code="BEG",
        naam="Begeleid wonen",
    )

    groepswonen = Referentiedata(
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

    grote_woonvorm = Referentiedata(
        code="GRW",
        naam="Grote woonvorm",
    )
    """
    In een grote woonvorm wonen veel mensen met lichamelijke of meervoudige beperkingen
    bij elkaar. Deze mensen wonen zo zelfstandig mogelijk.
    """

    hat_eenheid = Referentiedata(
        code="HAT",
        naam="HAT-eenheid",
    )
    """
    eenheden voor 1 of twee persoonshuishoudens met gezamelijke keuken, badkamer etc.
    """

    kleine_woonvorm = Referentiedata(
        code="KLE",
        naam="Kleine woonvorm",
    )
    """
    gezinsvervangende tehuizen voor lichamelijk gehandicapten
    """

    seniorenwoning_met_zorg = Referentiedata(
        code="SEN",
        naam="Seniorenwoning met zorg",
    )
    """
    Senioren woningen met zorg (voorheen Wibo-wonen in beschermde omgeving) zijn bij
    elkaar gelegen zelfstandige (aanleun)woningen met een dienstencentrum met allerlei
    voorzieningen dichtbij.
    """

    thomashuis = Referentiedata(
        code="THO",
        naam="Thomashuis",
    )
    """
    Een Thomashuis is een kleinschalige woonvoorziening voor zes à acht mensen met een
    verstandelijke beperking
    """
