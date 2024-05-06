from typing import Optional
from pydantic import BaseModel, Field


class EenhedenEnergieprestatie(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/58
    gebruiksoppervlakte_thermische_zone: Optional[float] = Field(
        default=None, alias="gebruiksoppervlakteThermischeZone"
    )
    """
    Gebruiksoppervlakte van de thermische zone, afgebakend volgens NTA 8800
    """
