from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.publicatiemodel import (
    Publicatiemodel,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PublicatieintakevormReferentiedata(Referentiedata):
    pass


class Publicatieintakevorm(Referentiedatasoort):
    cooptatie = PublicatieintakevormReferentiedata(
        code="COO",
        naam="Coöptatie",
        parent=Publicatiemodel.aanbodmodel,
    )
    """
    Medebewoners bepalen welke woningzoekende de eenheid krijgt.
    """

    intakegesprek = PublicatieintakevormReferentiedata(
        code="INT",
        naam="Intakegesprek",
        parent=Publicatiemodel.aanbodmodel,
    )
    """
    Er vindt een intake gesprek plaats met de eigenaar van de woning.
    """

    motivatie = PublicatieintakevormReferentiedata(
        code="MOT",
        naam="Motivatie",
        parent=Publicatiemodel.aanbodmodel,
    )
    """
    Toewijzing vindt plaats op basis van de beoordeling van een motivatiebrief of
    -gesprek.
    """

    sociale_spelregels = PublicatieintakevormReferentiedata(
        code="SOC",
        naam="Sociale spelregels",
        parent=Publicatiemodel.aanbodmodel,
    )
    """
    Sociale spelregels bepalen welke woningzoekende de eenheid krijgt.
    """
