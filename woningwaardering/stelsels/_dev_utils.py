import sys
import warnings
from typing import Any, Optional

from loguru import logger

from woningwaardering._logging import custom_dev_filter, dev_format
from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class DevelopmentContext:
    """
    Een context manager voor het opzetten van een context voor woningwaardering.

    Deze class stelt een context in voor het uitvoeren van woningwaarderingsberekeningen,
    met aanpasbare logging en waarschuwingsinstellingen.

    Parameters:
        instance (Stelselgroep | Stelsel): Het stelsel of de stelselgroep waarvoor de berekeningen worden uitgevoerd.
        strict (bool): Bepaalt of waarschuwingen strikt worden behandeld. Standaard is False.
        log_level (str): Het logniveau voor de uitgevoerde berekeningen. Standaard is "DEBUG".

    Usage:
        with DevelopmentContext(stelsel_instance, strict=True, log_level="INFO") as context:
            resultaat = context.waardeer(eenheid)
    """

    def __init__(
        self,
        instance: Stelselgroep | Stelsel,
        strict: bool = False,
        log_level: str = "DEBUG",
    ):
        self.instance = instance
        self.strict = strict
        self.log_level = log_level

    def __enter__(self) -> "DevelopmentContext":
        self._setup_logging()
        self._setup_warnings()
        return self

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[Any],
    ) -> None:
        pass

    def _setup_logging(self) -> None:
        logger.enable("woningwaardering")
        logger.remove()
        logger.add(
            sys.stderr,
            format=dev_format,
            level=self.log_level,
            filter=custom_dev_filter,
        )

    def _setup_warnings(self) -> None:
        if not self.strict:
            warnings.filterwarnings("default", category=UserWarning)

    def _load_eenheid(self, eenheid_input: EenhedenEenheid | str) -> EenhedenEenheid:
        if isinstance(eenheid_input, str):
            with open(eenheid_input, "r") as file:
                return EenhedenEenheid.model_validate_json(file.read())
        return eenheid_input

    def waardeer(
        self, eenheid_input: EenhedenEenheid | str
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """
        Berekent de punten voor een stelselgroep of stelsel voor een eenheid en print het resultaat

        Args:
            eenheid_input (EenhedenEenheid | str): Het eenheid object of het pad naar het eenheid object in een json bestand.

        Returns:
            WoningwaarderingResultatenWoningwaarderingResultaat: Het resultaat van de berekening.
        """
        eenheid = self._load_eenheid(eenheid_input)
        resultaat = self.instance.waardeer(eenheid)

        if isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep):
            resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
                groepen=[resultaat]
            )

        self._print_resultaat(resultaat)
        return resultaat

    def _print_resultaat(
        self, resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
    ) -> None:
        print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))
        tabel = utils.naar_tabel(resultaat)
        print(tabel)
