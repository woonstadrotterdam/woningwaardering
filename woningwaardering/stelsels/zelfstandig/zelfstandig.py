from datetime import date, datetime
from zoneinfo import ZoneInfo

from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Zelfstandig(Stelsel):
    def __init__(
        self, peildatum: date = datetime.now(ZoneInfo("Europe/Amsterdam")).date()
    ) -> None:
        super().__init__(
            stelsel="zelfstandig",
            peildatum=peildatum,
        )


if __name__ == "__main__":
    zel = Zelfstandig()
    f = open("./input_modellen/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(f.read())
    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    print(zel.bereken(eenheid, woningwaardering_resultaat).model_dump_json(indent=2))
