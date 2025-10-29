from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class KandidaatstatusReferentiedata(Referentiedata):
    pass


class Kandidaatstatus(Referentiedatasoort):
    aangeboden = KandidaatstatusReferentiedata(
        code="AAN",
        naam="Aangeboden",
    )
    """
    Kandidaat zit  in aanbiedingsproces.
    """

    afgewezen = KandidaatstatusReferentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Kandidaat is afgewezen door de aanbieder, corporatie, medebewoners etc.
    """

    geweigerd = KandidaatstatusReferentiedata(
        code="GEW",
        naam="Geweigerd",
    )
    """
    Kandidaat heeft de aanbieiding geweigerd.
    """

    potentiele_kandidaat = KandidaatstatusReferentiedata(
        code="POT",
        naam="Potentiele kandidaat",
    )
    """
    Kandidaat voldoet aan de spelregels van de publicatie.
    """

    gereageerd = KandidaatstatusReferentiedata(
        code="REA",
        naam="Gereageerd",
    )
    """
    Kandidaat heeft gereageerd op de publicatie.
    """

    geselecteerd = KandidaatstatusReferentiedata(
        code="SEL",
        naam="Geselecteerd",
    )
    """
    Kandidaat staat op vrijgegeven kandidatenlijst.
    """

    toegewezen = KandidaatstatusReferentiedata(
        code="TOE",
        naam="Toegewezen",
    )
    """
    Kandidaat is de toegewezen gebruiker van de eenheid.
    """
