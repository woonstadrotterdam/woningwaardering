from abc import ABC, abstractmethod
from datetime import date


from woningwaardering.stelsels.config import Stelselconfig
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class Stelselgroep(ABC):
    """Initialiseert een Stelselgroep.

    Args:
        peildatum (date, optional): De peildatum voor de waardering".
        config (Stelselconfig | None, optional): Een optionele configuratie. Defaults naar None.
    """

    def __init__(
        self,
        peildatum: date = date.today(),
        config: Stelselconfig | None = None,
    ) -> None:
        self.stelsel: Woningwaarderingstelsel | None = None
        self.stelselgroep: Woningwaarderingstelselgroep | None = None
        self.peildatum = peildatum

        # if config is None and self.stelsel is not None:
        #     config = Stelselconfig.load(stelsel=self.stelsel)
        # self.config = config

    @abstractmethod
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
        return WoningwaarderingResultatenWoningwaarderingGroep()

    # @staticmethod
    # def select_stelselgroep(
    #     stelsel: Woningwaarderingstelsel,
    #     stelselgroep: Woningwaarderingstelselgroep,
    #     peildatum: date = date.today(),
    #     config: Stelselconfig | None = None,
    # ) -> Stelselgroepversie:
    #     """Selecteert de geldige stelselgroepversie op basis van de opgegeven peildatum, stelsel en stelselgroep.

    #     Args:
    #         stelsel (Woningwaarderingstelsel): Het stelsel waartoe de stelselgroep behoort.
    #         stelselgroep (Woningwaarderingstelselgroep): De naam van de stelselgroep.
    #         peildatum (date): De peildatum voor de waardering.
    #         config (Stelselconfig| None, optional): De configuratie. Defaults to None.

    #     Returns:
    #         Stelselgroepversie: De geldige stelselgroepversie.

    #     Raises:
    #         ValueError: Als er geen geldige stelselgroepen zijn gevonden met de opgegeven peildatum.
    #         ValueError: Als er meerdere geldige stelselgroepen zijn gevonden met de opgegeven peildatum.
    #     """
    #     if not config:
    #         config = Stelselconfig.load(stelsel=stelsel)

    #     stelselgroep_config = config.stelselgroepen[stelselgroep.name]

    #     if not stelselgroep_config:
    #         raise NotImplementedError(
    #             f"geen geldige stelselgroep configuratie gevonden voor stelsel {stelsel} en stelselgroep {stelselgroep}."
    #         )

    #     logger.debug(f"{stelsel.value.naam}: {stelselgroep_config.module}")

    #     stelselgroep_object: Type[Stelselgroepversie] = import_class(
    #         f"woningwaardering.stelsels.{stelsel.name}.{stelselgroep.name}",
    #         stelselgroep_config.class_naam,
    #         Stelselgroepversie,  # type: ignore[type-abstract] # https://github.com/python/mypy/issues/4717
    #     )

    #     return stelselgroep_object
