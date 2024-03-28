from abc import ABC
from datetime import date
from typing import Type

from loguru import logger

from .config.config import StelselConfig
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

from woningwaardering.stelsels.stelselgroepversie import StelselgroepVersie
from woningwaardering.stelsels.utils import (
    import_class,
    is_geldig,
)


class AbstractStelselgroep(ABC):
    def __init__(
        self,
        stelsel: Woningwaarderingstelsel,
        stelselgroep: Woningwaarderingstelselgroep,
        peildatum: date,
    ) -> None:
        super().__init__()
        self.stelsel = stelsel
        self.stelselgroep = stelselgroep
        self.geldig_versie = self.select_stelselgroepversie(
            stelsel, stelselgroep, peildatum
        )

    stelsel: Woningwaarderingstelsel
    stelselgroep: Woningwaarderingstelselgroep
    geldig_versie: StelselgroepVersie

    @staticmethod
    def select_stelselgroepversie(
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

        geldige_stelselgroep_versie_configs = [
            versie
            for versie in stelselgroep_config.versies
            if is_geldig(versie.begindatum, versie.einddatum, peildatum)
        ]

        if not geldige_stelselgroep_versie_configs:
            raise ValueError(
                f"{stelsel}: geen geldige stelselgroep configuratie gevonden met peildatum {peildatum}."
            )

        if len(geldige_stelselgroep_versie_configs) > 1:
            raise ValueError(
                f"{stelsel.value.naam}: meerdere geldige stelselgroep configuraties gevonden met peildatum {peildatum}: {geldige_stelselgroep_versie_configs}."
            )

        logger.debug(
            f"{stelsel.value.naam}: stelselgroep '{stelselgroep}' is geldig op peildatum {peildatum}."
        )
        logger.debug(f"{stelsel.value.naam}: versies: {stelselgroep_config.versies}")

        geldige_stelselgroep_versie_config = geldige_stelselgroep_versie_configs[0]

        stelselgroep_versie: Type[StelselgroepVersie] = import_class(
            f"woningwaardering.stelsels.{stelsel.name}.{stelselgroep.name}",
            geldige_stelselgroep_versie_config.class_naam,
            StelselgroepVersie,  # type: ignore[type-abstract] # https://github.com/python/mypy/issues/4717
        )

        return stelselgroep_versie()
