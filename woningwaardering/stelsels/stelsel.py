from datetime import date

from woningwaardering.stelsels.config import StelselConfig
from woningwaardering.stelsels.stelselgroep import (
    StelselgroepVersie,
    select_geldige_stelselgroepversie,
)
from woningwaardering.utils import is_geldig
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Stelsel:
    def __init__(
        self,
        stelsel: str,
        peildatum: date | str = date.today(),
    ) -> None:
        """
        Initialiseert een Stelsel object.

        Parameters:
            stelsel (str): De naam van het stelsel.
            peildatum (date | str, optional): De peildatum in het formaat "dd-mm-jjjj".
                Standaard is de huidige datum.

        Returns:
            None
        """
        self.stelsel = stelsel
        self.peildatum = (
            peildatum.strftime("%d-%m-%Y") if isinstance(peildatum, date) else peildatum
        )
        self.stelsel_config = StelselConfig.load(stelsel=self.stelsel)
        self.geldige_stelselgroepversies = select_geldige_stelselgroepversies(
            self.peildatum,
            self.stelsel,
            self.stelsel_config,
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """
        Berekent de woningwaardering voor een stelsel.

        Parameters:
            eenheid (EenhedenEenheid): De eenheid waarvoor de woningwaardering wordt berekend.
            resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): Het resultaat van de woningwaardering.

        Returns:
            WoningwaarderingResultatenWoningwaarderingResultaat: Het bijgewerkte resultaat van de woningwaardering.
        """
        resultaat.groepen = []

        for stelselgroep_versie in self.geldige_stelselgroepversies:
            resultaat.groepen.append(
                stelselgroep_versie.bereken(
                    eenheid=eenheid,
                    woningwaardering_resultaat=resultaat,
                )
            )

        return resultaat


def select_geldige_stelselgroepversies(
    peildatum: str,
    stelsel: str,
    config: StelselConfig | None = None,
) -> list[StelselgroepVersie]:
    """
    Selecteert de geldige stelselgroepversies voor een peildatum en een stelsel.

    Parameters:
        peildatum (str): De peildatum in het formaat "dd-mm-jjjj".
        stelsel (str): De naam van het stelsel.
        config (dict[str, Any] | None, optional): Het configuratiebestand voor het stelsel.
            Standaard is None, wat betekent dat het configuratiebestand wordt geladen.

    Returns:
        list[StelselgroepVersie]: Een lijst met de geldige stelselgroepversies.

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

    geldige_stelselgroepversies = []
    for stelselgroep in config.stelselgroepen.keys():
        geldige_stelselgroepversies.append(
            select_geldige_stelselgroepversie(peildatum, stelsel, stelselgroep, config)
        )
    if geldige_stelselgroepversies == []:
        raise ValueError(
            f"{stelsel}: geen geldige stelselgroepen gevonden met peildatum {peildatum}."
        )
    return geldige_stelselgroepversies
