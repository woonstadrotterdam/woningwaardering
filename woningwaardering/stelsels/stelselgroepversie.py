from abc import ABC, abstractmethod
from datetime import date

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Stelselgroepversie(ABC):
    def __init__(self, peildatum: date = date.today()):
        self._peildatum = peildatum

    @abstractmethod
    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        pass

    @property
    def peildatum(self) -> date:
        return self._peildatum
