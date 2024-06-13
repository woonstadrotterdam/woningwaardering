from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class _EenhedenRenovatie(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    omschrijving: Optional[str] = None
    """
    De omschrijving van de renovatie(s) behorend bij de eenheid.
    """
    datum: Optional[date] = None
    """
    De datum dat het object is gerenoveerd.
    """
