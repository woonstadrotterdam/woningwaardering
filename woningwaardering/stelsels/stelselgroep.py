from abc import ABC, abstractmethod
from datetime import date

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    WoningwaarderingstelselgroepReferentiedata,
    WoningwaarderingstelselReferentiedata,
)


class Stelselgroep(ABC):
    @property
    def stelsel(self) -> WoningwaarderingstelselReferentiedata:
        return self._stelsel

    @stelsel.setter
    def stelsel(self, value: WoningwaarderingstelselReferentiedata) -> None:
        self._stelsel = value

    @property
    def stelselgroep(self) -> WoningwaarderingstelselgroepReferentiedata:
        return self._stelselgroep

    @stelselgroep.setter
    def stelselgroep(self, value: WoningwaarderingstelselgroepReferentiedata) -> None:
        self._stelselgroep = value

    """Initialiseert een Stelselgroep.

    Args:
        peildatum (date, optional): De peildatum voor de waardering.
    """

    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.peildatum = peildatum

    @abstractmethod
    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        """Bereken de woningwaardering voor een specifieke eenheid op stelselgroep-niveau.

        Args:
            eenheid (EenhedenEenheid): De eenheid waarvoor de woningwaardering wordt berekend.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None, optional): Het resultaat van de woningwaardering.

        Returns:
            WoningwaarderingResultatenWoningwaarderingGroep: Het resultaat van de woningwaardering voor de gehele groep.
        """
        pass  # pragma: no cover
