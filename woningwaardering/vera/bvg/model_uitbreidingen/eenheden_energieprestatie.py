from typing import Optional
from pydantic import BaseModel, Field


class _EenhedenEnergieprestatie(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/58
    gebruiksoppervlakte_thermische_zone: Optional[float] = Field(
        default=None, alias="gebruiksoppervlakteThermischeZone"
    )
    """
    Gebruiksoppervlakte van de thermische zone, afgebakend volgens NTA 8800
    """
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/59
    energieprestatievergoeding: Optional[bool] = Field(default=None)
    """
    Geeft aan of er bij het verhuren een energieprestatievergoeding (EPV) is overeengekomen
    """
