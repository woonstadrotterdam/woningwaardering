from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class MedewerkerbudgetsoortReferentiedata(Referentiedata):
    pass


class Medewerkerbudgetsoort(Referentiedatasoort):
    individueel_loopbaanontwikkelingsbudget = MedewerkerbudgetsoortReferentiedata(
        code="IND",
        naam="Individueel loopbaanontwikkelingsbudget",
    )
    """
    Het individueel loopbaanontwikkelingsbudget (ILOB) is een recht dat werknemers
    hebben op basis van de CAO Woondiensten sinds 1 januari 2010. Werknemers bepalen
    zelf hoe, wanneer en waaraan zij dit budget besteden. Het doel is bijdragen aan
    hun loopbaanontwikkeling.
    """

    functiegebonden_scholing = MedewerkerbudgetsoortReferentiedata(
        code="FUN",
        naam="Functiegebonden scholing",
    )
    """
    De werkgever kan een werknemer opdracht geven scholing of training te volgen wanneer
    dat volgens de werkgever nodig is voor het vervullen van zijn huidige functie nu
    en in de toekomst
    """

    informeel_leren = MedewerkerbudgetsoortReferentiedata(
        code="INF",
        naam="Informeel leren",
    )
