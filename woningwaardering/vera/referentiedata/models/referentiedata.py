from __future__ import annotations
from vera.bvg.generated import Referentiedata as ReferentiedataBase


class Referentiedata(ReferentiedataBase):
    def __eq__(self, other):
        print(self)
        print(other)
        if isinstance(other, ReferentiedataBase):
            return self.code == other.code
        return False
