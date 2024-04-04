from typing import Optional

from pydantic import BaseModel, Field

from woningwaardering.vera.bvg.generated import EenhedenRuimte


class _EenhedenRuimte(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/44
    gedeeld_met_aantal_eenheden: Optional[int] = Field(
        default=None, alias="gedeeldMetAantalEenheden"
    )
    """
    Het aantal eenheden waarmee deze ruimte wordt gedeeld. Deze waarde wordt gebruikt bij het berekenen van de waardering van een gedeelde ruimte met ruimtedetailsoort berging.
    """
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/47
    toegangsruimten: Optional[list[EenhedenRuimte]] = Field(
        default=None, alias="toegangsruimten"
    )
    """
    De ruimten die direct toegang geven tot deze ruimte. Dit wordt gebruikt bij het berekenen van de waardering van een ruimte met ruimtedetailsoort kast.
    """
