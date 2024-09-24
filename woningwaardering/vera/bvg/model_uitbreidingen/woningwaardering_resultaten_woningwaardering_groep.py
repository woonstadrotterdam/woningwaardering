from typing import Optional

from pydantic import BaseModel


class _WoningwaarderingResultatenWoningwaarderingGroep(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/65
    opslagpercentage: Optional[float] = None
    """
    Het huurprijsopslagpercentage dat is toegekend.
    """
