from typing import Optional

from pydantic import Field

from woningwaardering.vera.bvg.generated import Referentiedata


class _Referentiedata(Referentiedata):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/53
    parent: Optional[Referentiedata] = Field(None, exclude=True)
    """
    De bovenliggende referentiedata in het geval er sprake is van een hierarchische relatie tussen referentiedata.
    """

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Referentiedata):
            return self.code == other.code
        return False

    def __hash__(self) -> int:
        return hash(self.code)
