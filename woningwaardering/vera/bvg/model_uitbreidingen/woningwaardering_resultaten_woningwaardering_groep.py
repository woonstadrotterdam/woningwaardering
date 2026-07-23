from pydantic import BaseModel


class _WoningwaarderingResultatenWoningwaarderingGroep(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/65
    opslagpercentage: float | None = None
    """
    Het huurprijsopslagpercentage dat is toegekend.
    """
