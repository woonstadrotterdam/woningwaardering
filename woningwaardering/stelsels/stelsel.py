from datetime import date, datetime
from zoneinfo import ZoneInfo

from woningwaardering.stelsels.config import StelselConfig
from woningwaardering.stelsels.stelselgroep import (
    Stelselgroep,
)
from woningwaardering.stelsels.utils import import_class, is_geldig
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Stelsel:
    """Initialiseert een Stelsel object.

    Parameters:
        stelsel (str): De naam van het stelsel.
        peildatum (date, optional): De peildatum voor de waardering.
            Standaard is de huidige datum.
    """

    def __init__(
        self,
        stelsel: str,
        peildatum: date = datetime.now(ZoneInfo("Europe/Amsterdam")).date(),
    ) -> None:
        self.stelsel = stelsel
        self.peildatum = peildatum
        self.stelsel_config = StelselConfig.load(stelsel=self.stelsel)
        self.geldige_stelselgroepen = self.select_geldige_stelselgroepen(
            self.peildatum,
            self.stelsel,
            self.stelsel_config,
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """Berekent de woningwaardering voor een stelsel.

        Parameters:
            eenheid (EenhedenEenheid): De eenheid waarvoor de woningwaardering wordt berekend.
            resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): Het resultaat van de woningwaardering.

        Returns:
            WoningwaarderingResultatenWoningwaarderingResultaat: Het bijgewerkte resultaat van de woningwaardering.
        """
        resultaat.groepen = []

        for stelselgroep_versie in self.geldige_stelselgroepen:
            resultaat.groepen.append(
                stelselgroep_versie.bereken(
                    eenheid=eenheid,
                    woningwaardering_resultaat=resultaat,
                )
            )

        return resultaat

    @staticmethod
    def select_geldige_stelselgroepen(
        peildatum: date,
        stelsel: str,
        config: StelselConfig | None = None,
    ) -> list[Stelselgroep]:
        """Selecteert de geldige stelselgroepen voor een peildatum en een stelsel.

        Parameters:
            peildatum (date): De peildatum voor de waardering.
            stelsel (str): De naam van het stelsel.
            config (StelselConfig | None, optional): Het configuratiebestand voor het stelsel.
                Standaard is None, wat betekent dat het configuratiebestand wordt geladen.

        Returns:
            list[Stelselgroep]: Een lijst met de geldige stelselgroepen.

        Raises:
            ValueError: Als het stelsel niet geldig is op de peildatum.
            ValueError: Als er geen geldige stelselgroepen zijn gevonden.
        """
        if config is None:
            config = StelselConfig.load(stelsel=stelsel)
        if not is_geldig(
            config.begindatum,
            config.einddatum,
            peildatum,
        ):
            raise ValueError(
                f"Stelsel {stelsel} met begindatum {config.begindatum} en einddatum {config.einddatum} is niet geldig op peildatum {peildatum}."
            )

        geldige_stelselgroepen = []
        for _, stelgroep_config in config.stelselgroepen.items():
            stelselgroep_class = import_class(
                f"woningwaardering.stelsels.{stelsel}",
                stelgroep_config.class_naam,
            )

            geldige_stelselgroepen.append(stelselgroep_class(peildatum=peildatum))
        if geldige_stelselgroepen == []:
            raise ValueError(
                f"{stelsel}: geen geldige stelselgroepen gevonden met peildatum {peildatum}."
            )
        return geldige_stelselgroepen
