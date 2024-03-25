from woningwaardering.vera.bvg.generated import Referentiedata


class Publicatieintakevorm:
    cooptatie = Referentiedata(
        code="COO",
        naam="Coöptatie",
    )
    """
    Medebewoners bepalen welke woningzoekende de eenheid krijgt.
    """

    intakegesprek = Referentiedata(
        code="INT",
        naam="Intakegesprek",
    )
    """
    Er vindt een intake gesprek plaats met de eigenaar van de woning.
    """

    motivatie = Referentiedata(
        code="MOT",
        naam="Motivatie",
    )
    """
    Toewijzing vindt plaats op basis van de beoordeling van een motivatiebrief of
    -gesprek.
    """

    sociale_spelregels = Referentiedata(
        code="SOC",
        naam="Sociale spelregels",
    )
    """
    Sociale spelregels bepalen welke woningzoekende de eenheid krijgt.
    """
