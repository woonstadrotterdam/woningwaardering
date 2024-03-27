from datetime import date
from typing import Type
from loguru import logger

from woningwaardering.stelsels.config import StelselConfig
from woningwaardering.stelsels.stelselgroepversie import StelselgroepVersie
from woningwaardering.stelsels.utils import (
    import_class,
    is_geldig,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class Stelselgroep:
    """Initialiseert een Stelselgroep.

    Args:
        stelsel (Woningwaarderingstelsel): Het stelsel waartoe de stelselgroep behoort.
        stelselgroep (Woningwaarderingstelselgroep): De naam van de stelselgroep.
        peildatum (date, optional): De peildatum voor de waardering".
        config (StelselConfig | None, optional): Een optionele configuratie. Defaults naar None.
    """

    def __init__(
        self,
        stelsel: Woningwaarderingstelsel,
        stelselgroep: Woningwaarderingstelselgroep,
        peildatum: date = date.today(),
        config: StelselConfig | None = None,
    ) -> None:
        self.peildatum = peildatum
        self.stelsel = stelsel
        self.stelselgroep = stelselgroep
        if config is None:
            config = StelselConfig.load(stelsel=self.stelsel)
        self.geldige_versie = self.select_geldige_stelselgroepversie(
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

    @staticmethod
    def select_geldige_stelselgroepversie(
        stelsel: Woningwaarderingstelsel,
        stelselgroep: Woningwaarderingstelselgroep,
        peildatum: date = date.today(),
        config: StelselConfig | None = None,
    ) -> StelselgroepVersie:
        """Selecteert de geldige stelselgroepversie op basis van de opgegeven peildatum, stelsel en stelselgroep.

        Args:
            stelsel (Woningwaarderingstelsel): Het stelsel waartoe de stelselgroep behoort.
            stelselgroep (Woningwaarderingstelselgroep): De naam van de stelselgroep.
            peildatum (date): De peildatum voor de waardering.
            config (StelselConfig| None, optional): De configuratie. Defaults to None.

        Returns:
            StelselgroepVersie: De geldige stelselgroepversie.

        Raises:
            ValueError: Als er geen geldige stelselgroepen zijn gevonden met de opgegeven peildatum.
            ValueError: Als er meerdere geldige stelselgroepen zijn gevonden met de opgegeven peildatum.
        """
        if not config:
            config = StelselConfig.load(stelsel=stelsel)

        stelselgroep_config = config.stelselgroepen[stelselgroep.name]

        geldige_stelselgroep_versies = [
            versie
            for versie in stelselgroep_config.versies
            if is_geldig(versie.begindatum, versie.einddatum, peildatum)
        ]

        if not geldige_stelselgroep_versies:
            raise ValueError(
                f"{stelsel}: geen geldige stelselgroepen gevonden met peildatum {peildatum}."
            )

        if len(geldige_stelselgroep_versies) > 1:
            raise ValueError(
                f"{stelsel.value.naam}: meerdere geldige stelselgroepen gevonden met peildatum {peildatum}: {geldige_stelselgroep_versies}."
            )

        logger.debug(
            f"{stelsel.value.naam}: stelselgroep '{stelselgroep}' is geldig op peildatum {peildatum}."
        )
        logger.debug(f"{stelsel.value.naam}: versies: {stelselgroep_config.versies}")

        geldige_stelselgroep_versie_class: Type[StelselgroepVersie] = import_class(
            f"woningwaardering.stelsels.{stelsel.name}.{stelselgroep.name}",
            geldige_stelselgroep_versies[0].class_naam,
            StelselgroepVersie,  # type: ignore[type-abstract] # https://github.com/python/mypy/issues/4717
        )

        return geldige_stelselgroep_versie_class()
