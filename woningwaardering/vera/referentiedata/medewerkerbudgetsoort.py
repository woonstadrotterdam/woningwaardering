from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Medewerkerbudgetsoort(Enum):
    individueel_loopbaanontwikkelingsbudget = Referentiedata(
        code="IND",
        naam="Individueel loopbaanontwikkelingsbudget",
    )
    """
    Het individueel loopbaanontwikkelingsbudget (ILOB) is een recht dat werknemers
    hebben op basis van de CAO Woondiensten sinds 1 januari 2010. Werknemers bepalen
    zelf hoe, wanneer en waaraan zij dit budget besteden. Het doel is bijdragen aan
    hun loopbaanontwikkeling.
    """

    functiegebonden_scholing = Referentiedata(
        code="FUN",
        naam="Functiegebonden scholing",
    )
    """
    De werkgever kan een werknemer opdracht geven scholing of training te volgen wanneer
    dat volgens de werkgever nodig is voor het vervullen van zijn huidige functie nu
    en in de toekomst
    """

    informeel_leren = Referentiedata(
        code="INF",
        naam="Informeel leren",
    )

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
