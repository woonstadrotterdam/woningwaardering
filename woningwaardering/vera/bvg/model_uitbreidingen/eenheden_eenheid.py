from typing import Optional
from pydantic import BaseModel, Field

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.bvg.model_uitbreidingen.eenheden_oppervlakte import (
    _EenhedenOppervlakte as EenhedenOppervlakte,
)


class _EenhedenEenheid(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/54
    klimaatbeheersingsoort: Optional[Referentiedata] = None
    """
    Het soort klimaatbeheersing. Bijvoorbeeld: individueel of collectief. Referentiedatasoort EENHEIDKLIMAATBEHEERSINGSOORT.
    """
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/57
    woningtype: Optional[Referentiedata] = None
    """
    Het type woning: eengezinswoning of meergezinswoning. Referentiedatasoort WONINGTYPE.
    """
    oppervlakten: Optional[list[EenhedenOppervlakte]] = Field(
        default=None, alias="verbondenRuimten"
    )
    """
    De verschillende oppervlakten die gedefinieerd zijn (bijv. vanuit de NEN) voor een eenheid. Bijv. het gebruiksoppervlak (GO) of functioneel nuttig oppervlak (FNO).
    """
