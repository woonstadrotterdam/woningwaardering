from typing import Optional
from pydantic import BaseModel

from woningwaardering.vera.bvg.generated import Referentiedata


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
