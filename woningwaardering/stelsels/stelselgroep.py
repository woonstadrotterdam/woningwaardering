from datetime import date

from woningwaardering.stelsels.abstract_stelselgroep import AbstractStelselgroep
from woningwaardering.stelsels.config import StelselConfig
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Stelselgroep(AbstractStelselgroep):
    """Initialiseert een Stelselgroep.

    Args:
        peildatum (date, optional): De peildatum voor de waardering".
        config (StelselConfig | None, optional): Een optionele configuratie. Defaults naar None.
    """

    def __init__(
        self,
        peildatum: date = date.today(),
        config: StelselConfig | None = None,
    ) -> None:
        self.peildatum = peildatum

        if config is None:
            config = StelselConfig.load(stelsel=self.stelsel)

        self.geldige_versie = self.select_stelselgroepversie(
            self.stelsel, self.stelselgroep, self.peildatum, config
        )

    def bereken(
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
        woningwaardering_resultaat = (
            woningwaardering_resultaat
            or WoningwaarderingResultatenWoningwaarderingResultaat()
        )
        return self.geldige_versie.bereken(eenheid, woningwaardering_resultaat)
