from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Onderhoudsoort(Referentiedatasoort):
    inspectie = Referentiedata(
        code="INS",
        naam="Inspectie",
    )
    """
    Opdracht tot het uitvoeren van inspectie-/inventarisatie-werkzaamheden om vast te
    stellen óf en zo ja welke onderhoudswerkzaamheden moeten worden uitgevoerd. Dit
    kan een inspectie zijn naar aanleiding van een onduidelijk reparatieverzoek of
    naar aanleiding van een verhuurmutatie.
    """

    mutatie = Referentiedata(
        code="MUT",
        naam="Mutatie",
    )
    """
    Opdracht tot het uitvoeren van onderhoudswerkzaamheden naar aanleiding van een
    verhuurmutatie.
    """

    planmatig = Referentiedata(
        code="PLN",
        naam="Planmatig",
    )
    """
    Opdracht tot het uitvoeren van onderhoudswerkzaamheden naar aanleiding van een
    goedgekeurd MJO-budget
    """

    projectmatig = Referentiedata(
        code="PRJ",
        naam="Projectmatig",
    )
    """
    Opdracht tot het uitvoeren van onderhoudswerkzaamheden naar aanleiding van een
    investeringsproject zoals verduurzaming, renovatie, etc.
    """

    reparatie = Referentiedata(
        code="REP",
        naam="Reparatie",
    )
    """
    Opdracht tot het uitvoeren van reparatiewerkzaamheden naar aanleiding van een
    geconstateerd defect
    """

    wmo_aanpassing = Referentiedata(
        code="WMO",
        naam="WMO Aanpassing",
    )
    """
    Bij benodigde aanpassing van de woning bij de zittende huurder (door ouderdom,
    invaliditeit aanbrengen van WMO-aanpassing)
    """

    woningverbetering = Referentiedata(
        code="WOV",
        naam="Woningverbetering",
    )
    """
    Bij aanpassing op verzoek van de huurder voor verbetering van het woongenot.
    Voorbeeld is het voortijdig vervangen van de wc-pot door een luxe uiitvoering
    """
