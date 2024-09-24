from typing import Optional

from pydantic import BaseModel, Field

from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
    Referentiedata,
)


class _EenhedenRuimte(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/44
    gedeeld_met_aantal_eenheden: Optional[int] = Field(
        default=None, alias="gedeeldMetAantalEenheden", ge=0
    )
    """
    Het aantal eenheden waarmee deze ruimte wordt gedeeld. Deze waarde wordt gebruikt bij het berekenen van de waardering van een gedeelde ruimte. Wanneer gedeeld_met_aantal_eenheden groter is dan 1, dan wordt de ruimte beschouwd als een gedeelde ruimte.
    """
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/46
    bouwkundige_elementen: Optional[list[BouwkundigElementenBouwkundigElement]] = Field(
        default=None, alias="bouwkundigeElementen"
    )
    """
    De bouwkundige elementen gerelateerd aan deze ruimte. Dit wordt gebruikt bij het berekenen van de waardering voor een zolder op basis van de aanwezigheid van een trap, de lengte van een aanrecht in een keuken en de aanwezigheid van een toilet in een badkamer.
    """
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/47
    verbonden_ruimten: Optional[list[EenhedenRuimte]] = Field(
        default=None, alias="verbondenRuimten"
    )
    """
    De ruimten die in verbinding staan met deze ruimte. Dit wordt gebruikt bij het berekenen van de waardering van kasten en verwarming van ruimten.
    """
    # https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/100
    verwarmd: Optional[bool] = Field(default=None, alias="verwarmd")
    """
    Geeft aan of de ruimte verwarmd wordt door een onroerende zaak. Dit wordt gebruikt bij het berekenen van de waardering van een ruimte.
    """
    # https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/100
    verkoeld: Optional[bool] = Field(default=None, alias="verkoeld")
    """
    Geeft aan of de ruimte verkoeld wordt door een onroerende zaak. Dit wordt gebruikt bij het berekenen van de waardering van een ruimte.
    """
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/70
    installaties: Optional[list[Referentiedata]] = Field(
        default=None, alias="installaties"
    )
    """
    Het soort installaties van de ruimte. Bijvoorbeeld Hangend toilet, Wastafel, Inbouw koelkast, warmkokend water functie etc. Deze installaties zijn van belang voor de woningwaardering. Referentiedatasoort INSTALLATIESOORT.
    """
    aantal: Optional[int] = Field(default=1, alias="aantal", ge=0)
    """
    Geeft aan hoeveel van deze ruimte er zijn. Dit attribuut is aangemaakt om de rubriek 'Gemeenschappelijke Parkeerruimten' van de woningwaardering te kunnen berekenen en te voorkomen dat alle gedeelde parkeervakken van een parkeerruimten apart meegegeven dienen te worden. Dit attribuut wordt uitsluitend gebruikt in het berekenen van de punten voor 'Gemeenschappelijke Parkeerruimten'.
    """
