from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class KwaliteitsniveauReferentiedata(Referentiedata):
    pass


class Kwaliteitsniveau(Referentiedatasoort):
    eenvoudig = KwaliteitsniveauReferentiedata(
        code="EEN",
        naam="Eenvoudig",
    )
    """
    Woning met een afwerkingsniveau dat lager is dan de vastgestelde basiskwaliteit,
    vaak toegepast in situaties waarin ingrijpende aanpassingen aan het complex
    gepland zijn.
    """

    hoogwaardig = KwaliteitsniveauReferentiedata(
        code="HOO",
        naam="Hoogwaardig",
    )
    """
    Woning waarbij in de afwerking en voorzieningen nadrukkelijk gekozen is voor een
    hoger comfortniveau gericht op specifieke doelgroepen.
    """

    luxe = KwaliteitsniveauReferentiedata(
        code="LUX",
        naam="Luxe",
    )
    """
    Woning met een afwerkings- en voorzieningenniveau dat de basiskwaliteit overstijgt.
    """

    standaard = KwaliteitsniveauReferentiedata(
        code="STA",
        naam="Standaard",
    )
    """
    Woning die bij mutatie wordt hersteld of opgewaardeerd tot de vastgestelde
    basiskwaliteit.
    """
