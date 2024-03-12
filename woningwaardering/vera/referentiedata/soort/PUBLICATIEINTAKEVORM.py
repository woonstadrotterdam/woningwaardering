
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PUBLICATIEINTAKEVORM:

    cooptatie = Referentiedata(
        code="COO",
        naam="Coöptatie",
    )
    # cooptatie = ("COO", "Coöptatie")
    """
    Medebewoners bepalen welke woningzoekende de eenheid krijgt.
    """

    intakegesprek = Referentiedata(
        code="INT",
        naam="Intakegesprek",
    )
    # intakegesprek = ("INT", "Intakegesprek")
    """
    Er vindt een intake gesprek plaats met de eigenaar van de woning.
    """

    motivatie = Referentiedata(
        code="MOT",
        naam="Motivatie",
    )
    # motivatie = ("MOT", "Motivatie")
    """
    Toewijzing vindt plaats op basis van de beoordeling van een motivatiebrief of
    -gesprek.
    """

    sociale_spelregels = Referentiedata(
        code="SOC",
        naam="Sociale spelregels",
    )
    # sociale_spelregels = ("SOC", "Sociale spelregels")
    """
    Sociale spelregels bepalen welke woningzoekende de eenheid krijgt.
    """
