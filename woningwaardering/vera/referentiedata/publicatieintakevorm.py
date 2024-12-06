from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.publicatiemodel import Publicatiemodel
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Publicatieintakevorm(Referentiedatasoort):
    cooptatie = Referentiedata(
        code="COO",
        naam="Coöptatie",
        parent=Publicatiemodel.aanbodmodel,
    )
    """
    Medebewoners bepalen welke woningzoekende de eenheid krijgt.
    """

    intakegesprek = Referentiedata(
        code="INT",
        naam="Intakegesprek",
        parent=Publicatiemodel.aanbodmodel,
    )
    """
    Er vindt een intake gesprek plaats met de eigenaar van de woning.
    """

    motivatie = Referentiedata(
        code="MOT",
        naam="Motivatie",
        parent=Publicatiemodel.aanbodmodel,
    )
    """
    Toewijzing vindt plaats op basis van de beoordeling van een motivatiebrief of
    -gesprek.
    """

    sociale_spelregels = Referentiedata(
        code="SOC",
        naam="Sociale spelregels",
        parent=Publicatiemodel.aanbodmodel,
    )
    """
    Sociale spelregels bepalen welke woningzoekende de eenheid krijgt.
    """
