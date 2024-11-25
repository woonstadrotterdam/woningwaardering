from datetime import date

from woningwaardering.stelsels._dev_utils import waardeer
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

    def waardeer(
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
        ):
            raise ValueError(
                f"Eenheid ({eenheid.id}): woningwaarderingstelsel-attribuut ontbreekt in het inputmodel."
            )
        elif eenheid.woningwaarderingstelsel.code not in [
            Woningwaarderingstelsel.zelfstandige_woonruimten.code,
            Woningwaarderingstelsel.onzelfstandige_woonruimten.code,
        ]:
            raise ValueError(
                f"Eenheid ({eenheid.id}): ongeldig woningwaarderingsstelsel-attribuut. Code moet één van {Woningwaarderingstelsel.zelfstandige_woonruimten.code} of {Woningwaarderingstelsel.onzelfstandige_woonruimten.code} zijn."
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

        return stelsel.waardeer(eenheid)


if __name__ == "__main__":  # pragma: no cover
    waardeer(
        instance=Woningwaardering(),  # type: ignore
        eenheid_input="tests/data/onzelfstandige_woonruimten/input/15004000185.json",
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    )
