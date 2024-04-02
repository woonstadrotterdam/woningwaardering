from typing import Optional

from pydantic import BaseModel, Field


class _EenhedenRuimte(BaseModel):
    gedeeld_met_aantal_eenheden: Optional[int] = Field(
        default=None, alias="gedeeldMetAantalEenheden"
    )
    """
    Het aantal eenheden waarmee deze ruimte wordt gedeeld
    """
