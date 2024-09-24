from typing import Optional

from pydantic import BaseModel, Field


class _WoningwaarderingResultatenWoningwaarderingResultaat(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/65
    huurprijsopslag: Optional[float] = None
    """
    De huurprijsopslag in euro's die boven de maximale huurprijs mag worden gerekend.
    """
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/65
    maximale_huur_inclusief_opslag: Optional[float] = Field(
        default=None, alias="maximaleHuurInclusiefOpslag"
    )
    """
    De maximale huurprijs inclusief de huurprijsopslag.
    """
