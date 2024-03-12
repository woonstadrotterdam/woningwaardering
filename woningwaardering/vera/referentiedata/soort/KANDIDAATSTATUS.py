
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class KANDIDAATSTATUS:

    aangeboden = Referentiedata(
        code="AAN",
        naam="Aangeboden",
    )
    # aangeboden = ("AAN", "Aangeboden")
    """
    Kandidaat zit in aanbiedingsproces.
    """

    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    # afgewezen = ("AFG", "Afgewezen")
    """
    Kandidaat is afgewezen door de aanbieder, corporatie, medebewoners etc.
    """

    geweigerd = Referentiedata(
        code="GEW",
        naam="Geweigerd",
    )
    # geweigerd = ("GEW", "Geweigerd")
    """
    Kandidaat heeft de aanbieiding geweigerd.
    """

    potentiele_kandidaat = Referentiedata(
        code="POT",
        naam="Potentiele kandidaat",
    )
    # potentiele_kandidaat = ("POT", "Potentiele kandidaat")
    """
    Kandidaat voldoet aan de spelregels van de publicatie.
    """

    gereageerd = Referentiedata(
        code="REA",
        naam="Gereageerd",
    )
    # gereageerd = ("REA", "Gereageerd")
    """
    Kandidaat heeft gereageerd op de publicatie.
    """

    geselecteerd = Referentiedata(
        code="SEL",
        naam="Geselecteerd",
    )
    # geselecteerd = ("SEL", "Geselecteerd")
    """
    Kandidaat staat op vrijgegeven kandidatenlijst.
    """

    toegewezen = Referentiedata(
        code="TOE",
        naam="Toegewezen",
    )
    # toegewezen = ("TOE", "Toegewezen")
    """
    Kandidaat is de toegewezen gebruiker van de eenheid.
    """
