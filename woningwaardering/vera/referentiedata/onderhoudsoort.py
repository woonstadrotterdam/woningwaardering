from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OnderhoudsoortReferentiedata(Referentiedata):
    pass


class Onderhoudsoort(Referentiedatasoort):
    inspectie = OnderhoudsoortReferentiedata(
        code="INS",
        naam="Inspectie",
    )
    """
    Opdracht tot het uitvoeren van inspectie-/inventarisatie-werkzaamheden om vast te
    stellen óf en zo ja welke onderhoudswerkzaamheden moeten worden uitgevoerd. Dit
    kan een inspectie zijn naar aanleiding van een onduidelijk reparatieverzoek of
    naar aanleiding van een verhuurmutatie.
    """

    mutatie = OnderhoudsoortReferentiedata(
        code="MUT",
        naam="Mutatie",
    )
    """
    Opdracht tot het uitvoeren van onderhoudswerkzaamheden naar aanleiding van een
    verhuurmutatie.
    """

    planmatig = OnderhoudsoortReferentiedata(
        code="PLN",
        naam="Planmatig",
    )
    """
    Opdracht tot het uitvoeren van onderhoudswerkzaamheden naar aanleiding van een
    goedgekeurd MJO-budget
    """

    projectmatig = OnderhoudsoortReferentiedata(
        code="PRJ",
        naam="Projectmatig",
    )
    """
    Opdracht tot het uitvoeren van onderhoudswerkzaamheden naar aanleiding van een
    investeringsproject zoals verduurzaming, renovatie, etc.
    """

    reparatie = OnderhoudsoortReferentiedata(
        code="REP",
        naam="Reparatie",
    )
    """
    Opdracht tot het uitvoeren van reparatiewerkzaamheden naar aanleiding van een
    geconstateerd defect
    """

    wmo_aanpassing = OnderhoudsoortReferentiedata(
        code="WMO",
        naam="WMO Aanpassing",
    )
    """
    Bij benodigde aanpassing van de woning bij de zittende huurder (door ouderdom,
    invaliditeit aanbrengen van WMO-aanpassing)
    """

    woningverbetering = OnderhoudsoortReferentiedata(
        code="WOV",
        naam="Woningverbetering",
    )
    """
    Bij aanpassing op verzoek van de huurder voor verbetering van het woongenot.
    Voorbeeld is het voortijdig vervangen van de wc-pot door een luxe uiitvoering
    """
