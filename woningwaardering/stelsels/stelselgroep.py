from abc import ABC, abstractmethod
from typing import Any

from loguru import logger

from woningwaardering.stelsels.config.config import Config
from woningwaardering.utils import (
    import_class,
    is_geldig,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class StelselgroepVersie(ABC):
    @staticmethod
    @abstractmethod
    def bereken(
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        pass


class Stelselgroep:
    def __init__(
        self,
        peildatum: str,
        stelsel: str,
        stelselgroep: str,
        config: dict[str, Any] | None = None,
    ) -> None:
        """
        Initialiseert een Stelselgroep.

        Args:
            peildatum (str): De peildatum in het formaat "dd-mm-jjjj".
            stelsel (str): Het stelsel waartoe de stelselgroep behoort.
            stelselgroep (str): De naam van de stelselgroep.
            config (dict[str, Any] | None, optional): Een optionele configuratie. Defaults naar None.
        """
        self.peildatum = peildatum  # datetime.strptime(peildatum, "%d-%m-%Y").date()
        self.stelsel = stelsel
        self.stelselgroep = stelselgroep
        if config is None:
            config = Config.load(stelsel=self.stelsel).model_dump()
        self.geldige_versie = select_geldige_stelselgroepversie(
            self.peildatum, self.stelsel, self.stelselgroep, config
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        """
        Bereken de woningwaardering voor een specifieke eenheid op stelselgroep-niveau.

        Args:
            eenheid (EenhedenEenheid): De eenheid waarvoor de woningwaardering wordt berekend.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): Het resultaat van de woningwaardering.

        Returns:
            WoningwaarderingResultatenWoningwaarderingGroep: Het resultaat van de woningwaardering voor de gehele groep.
        """
        return self.geldige_versie.bereken(eenheid, woningwaardering_resultaat)


def select_geldige_stelselgroepversie(
    peildatum: str,
    stelsel: str,
    stelselgroep: str,
    config: dict[str, Any] | None = None,
) -> StelselgroepVersie:
    """
    Selecteert de geldige stelselgroepversie op basis van de opgegeven peildatum, stelsel en stelselgroep.

    Args:
        peildatum (str): De peildatum in het formaat "dd-mm-jjjj".
        stelsel (str): De naam van het stelsel.
        stelselgroep (str): De naam van de stelselgroep.
        config (dict[str, Any] | None, optional): De configuratie. Defaults to None.

    Returns:
        StelselgroepVersie: De geldige stelselgroepversie.

    Raises:
        ValueError: Als er geen geldige stelselgroepen zijn gevonden met de opgegeven peildatum.
        ValueError: Als er meerdere geldige stelselgroepen zijn gevonden met de opgegeven peildatum.
    """
    if not config:
        config = Config.load(stelsel=stelsel).model_dump()

    geldige_stelselgroep_versies = []
    stelselgroep_config = config["stelsel"][stelsel]["stelselgroepen"][stelselgroep]
    if is_geldig(
        stelselgroep_config["begindatum"],
        stelselgroep_config["einddatum"],
        peildatum,
    ):
        logger.debug(
            f"{stelsel}: stelselgroep '{stelselgroep}' is geldig op peildatum {peildatum}."
        )
        for versie in stelselgroep_config["versies"]:
            for versie_class_naam, geldigheid in versie.items():
                if is_geldig(
                    geldigheid["begindatum"], geldigheid["einddatum"], peildatum
                ):
                    stelselgroep_versie = import_class(
                        f"woningwaardering.stelsels.{stelsel}.{stelselgroep}",
                        versie_class_naam,
                    )

                    geldige_stelselgroep_versies.append(stelselgroep_versie())
    if len(geldige_stelselgroep_versies) == 0:
        raise ValueError(
            f"{stelsel}: geen geldige stelselgroepen gevonden met peildatum {peildatum}."
        )
    if len(geldige_stelselgroep_versies) > 1:
        raise ValueError(
            f"{stelsel}: meerdere geldige stelselgroepen gevonden met peildatum {peildatum}: {geldige_stelselgroep_versies}."
        )
    return geldige_stelselgroep_versies[0]  # type: ignore[no-any-return]
