import warnings
from datetime import date

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.onzelfstandige_woonruimten.onzelfstandige_woonruimten import (
    OnzelfstandigeWoonruimten,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelsel import (
    Woningwaarderingstelsel,
)


class Woningwaardering:
    """Initialiseert een Woningwaardering object dat automatisch het juiste stelsel detecteert.

    Parameters:
        peildatum (date, optional): De peildatum voor de waardering.
            Standaard is de huidige datum.

    Attributes:
        peildatum (date): De peildatum voor de waardering.
        stelsels (dict): Dictionary met alle beschikbare stelsels.
    """

    def __init__(self, peildatum: date = date.today()) -> None:
        self.peildatum = peildatum

    def bereken(
        self,
        eenheid: EenhedenEenheid,
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """Berekent de woningwaardering voor een eenheid door automatisch het juiste stelsel te detecteren.

        Parameters:
            eenheid (EenhedenEenheid): De eenheid waarvoor de woningwaardering wordt berekend.

        Returns:
            WoningwaarderingResultatenWoningwaarderingResultaat: Het resultaat van de woningwaardering.

        Raises:
            ValueError: Als het type woonruimte niet kan worden bepaald.
        """
        if (
            eenheid.woningwaarderingstelsel is None
            or eenheid.woningwaarderingstelsel.code is None
            or eenheid.woningwaarderingstelsel.code
            not in [
                Woningwaarderingstelsel.zelfstandige_woonruimten.code,
                Woningwaarderingstelsel.onzelfstandige_woonruimten.code,
            ]
        ):
            raise ValueError(
                f"Eenheid {eenheid.id}: kan niet bepalen welk stelsel voor eenheid {eenheid.id} van toepassing is."
            )
        elif (
            eenheid.woningwaarderingstelsel.code
            == Woningwaarderingstelsel.zelfstandige_woonruimten.code
        ):
            stelsel: ZelfstandigeWoonruimten | OnzelfstandigeWoonruimten = (
                ZelfstandigeWoonruimten(peildatum=self.peildatum)
            )
        elif (
            eenheid.woningwaarderingstelsel.code
            == Woningwaarderingstelsel.onzelfstandige_woonruimten.code
        ):
            stelsel = OnzelfstandigeWoonruimten(peildatum=self.peildatum)

        return stelsel.bereken(eenheid)


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")
    warnings.simplefilter("default", UserWarning)

    woningwaardering = Woningwaardering(peildatum=date.today())

    with open(
        "tests/data/generiek/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())
        woningwaardering_resultaat = woningwaardering.bereken(eenheid)
        print(
            woningwaardering_resultaat.model_dump_json(
                by_alias=True, indent=2, exclude_none=True
            )
        )
        tabel = utils.naar_tabel(woningwaardering_resultaat)
        print(tabel)
