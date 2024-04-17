from typing import Optional
from pydantic import BaseModel

from woningwaardering.vera.bvg.generated import Referentiedata


class _Referentiedata(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/53
    parent: Optional[Referentiedata] = None
    """
    De bovenliggende referentiedata in het geval er sprake is van een hierarchische relatie tussen referentiedata.
    """
