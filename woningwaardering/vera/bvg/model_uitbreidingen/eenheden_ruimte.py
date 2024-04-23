from typing import Optional

from pydantic import BaseModel, Field

from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
)


class _EenhedenRuimte(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/44
    gedeeld_met_aantal_eenheden: Optional[int] = Field(
        default=None, alias="gedeeldMetAantalEenheden"
    )
    """
    Het aantal eenheden waarmee deze ruimte wordt gedeeld. Deze waarde wordt gebruikt bij het berekenen van de waardering van een gedeelde ruimte met ruimtedetailsoort berging.
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
