
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class DEFECTOORZAAK:

    bewonersopdracht_of_gedrag = Referentiedata(
        code="BEW",
        naam="Bewonersopdracht/gedrag",
    )
    # bewonersopdracht_of_gedrag = ("BEW", "Bewonersopdracht/gedrag")
    """
    Bewoner heeft het defect zelf veroorzaakt (bijv. binnendeur ingetrapt)Relatie met
    Ketenstandaard: oorzaakcode HUU - Huurder
    """

    schade_door_brand = Referentiedata(
        code="BRA",
        naam="Schade door brand",
    )
    # schade_door_brand = ("BRA", "Schade door brand")
    """
    Defect is veroorzaakt door brand. (bijv. keukenbrand).
    """

    ouderdom = Referentiedata(
        code="OUD",
        naam="Ouderdom",
    )
    # ouderdom = ("OUD", "Ouderdom")
    """
    Het element is versleten en defect geraakt. (bijv. kastdeur van 20 jaar oude keuken
    hangt scheef). Relatie met Ketenstandaard: oorzaakcode OUD - Ouderdom
    """

    normale_slijtage = Referentiedata(
        code="SLT",
        naam="Normale slijtage",
    )
    # normale_slijtage = ("SLT", "Normale slijtage")
    """
    Het element is versleten en defect geraakt. (bijv. door veelvuldig gebruik van het
    element). Relatie met Ketenstandaard: oorzaakcode SLT - Slijtage
    """

    slecht_opgeleverd = Referentiedata(
        code="SOP",
        naam="Slecht opgeleverd",
    )
    # slecht_opgeleverd = ("SOP", "Slecht opgeleverd")
    """
    Defect is veroorzaakt door een slechte oplevering van het element bij de installatie
    (bijv. kraan lekt van nieuwe keuken).
    """

    schade_door_storm = Referentiedata(
        code="STO",
        naam="Schade door storm",
    )
    # schade_door_storm = ("STO", "Schade door storm")
    """
    Defect is veroorzaakt door externe invloeden. (bijv. schutting omgewaaid door
    storm).
    """

    schade_door_vandalisme = Referentiedata(
        code="VAN",
        naam="Schade door vandalisme",
    )
    # schade_door_vandalisme = ("VAN", "Schade door vandalisme")
    """
    Defect is veroorzaakt door vandalisme. (bijv. graffiti op gevel).
    """

    verzoek_van_de_vastgoedeigenaar = Referentiedata(
        code="VGE",
        naam="Verzoek van de vastgoedeigenaar",
    )
    # verzoek_van_de_vastgoedeigenaar = ("VGE", "Verzoek van de vastgoedeigenaar")
    """
    Vastgoedeigenaar heeft expliciet verzoek gedaan om het defect op te lossen.
    """

    schade_door_water = Referentiedata(
        code="WAT",
        naam="Schade door water",
    )
    # schade_door_water = ("WAT", "Schade door water")
    """
    Defect is veroorzaakt door lekkage (van binnenuit) of overstroming (van buitenaf).
    (bijv. ondergelopen kelder).
    """
