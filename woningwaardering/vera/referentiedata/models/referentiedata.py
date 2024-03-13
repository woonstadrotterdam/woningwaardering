from __future__ import annotations
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ReferentiedataEnum(Referentiedata, Enum):
    def __eq__(self, other):
        print(self)
        print(other)
        if isinstance(other, Referentiedata):
            return self.code == other.code
        return False
