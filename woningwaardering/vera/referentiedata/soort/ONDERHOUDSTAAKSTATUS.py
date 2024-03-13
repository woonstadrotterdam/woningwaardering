from woningwaardering.vera.bvg.models import Referentiedata


class ONDERHOUDSTAAKSTATUS:
    concept_of_aangemaakt = Referentiedata(
        code="CON",
        naam="Concept  / aangemaakt",
    )
    """
    De taak in concept / aangemaakt
    """

    gepland = Referentiedata(
        code="GEP",
        naam="Gepland",
    )
    """
    Voor de taak is een afspraak gepland
    """

    gereed = Referentiedata(
        code="GER",
        naam="Gereed",
    )
    """
    De taak is gereed gemeld door de vakman
    """

    gesloten = Referentiedata(
        code="GES",
        naam="Gesloten",
    )
    """
    De taak is administratief afgesloten
    """

    onderbroken = Referentiedata(
        code="OND",
        naam="Onderbroken",
    )
    """
    De taak is onderbroken door de vakman omdat hij niet verder kan met de uitvoering.
    Een reden kan zijn dat de vakman niet de juiste discipline heeft of dat er materiaal
    besteld moet worden
    """

    gepauzeerd = Referentiedata(
        code="PAU",
        naam="Gepauzeerd",
    )
    """
    De vakman heeft de uitvoering van de taak voor korte tijd gepauzeerd, bijvoorbeeld
    voor een lunchbreak
    """

    onderweg = Referentiedata(
        code="REI",
        naam="Onderweg",
    )
    """
    De vakman is onderweg naar de onderhoudslocatie voor de uitvoering van de taak
    """

    in_uitvoering = Referentiedata(
        code="UIT",
        naam="In uitvoering",
    )
    """
    De vakman is bezig met de uitvoering van de taak.
    """

    uitwerktijd = Referentiedata(
        code="UWT",
        naam="Uitwerktijd",
    )
    """
    De vakman is gereed met de uitvoering van de taak en zit in de uitwerktijd. Wordt
    gebruikt bij bijvoorbeeld het opruimen van het gereedschap in de bus na de
    werkzaamheden.
    """
