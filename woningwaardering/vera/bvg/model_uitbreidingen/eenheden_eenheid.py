from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class _EenhedenEenheid(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/69
    datum_afsluiten_huurovereenkomst: Optional[date] = Field(
        default=None, alias="datumAfsluitenHuurovereenkomst"
    )
    """
    De datum waarop de huurovereenkomst is afgesloten.
    """
