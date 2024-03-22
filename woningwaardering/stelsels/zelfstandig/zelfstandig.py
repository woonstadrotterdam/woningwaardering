from datetime import date

from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Zelfstandig(Stelsel):
    def __init__(
        self,
        peildatum: str | date = date.today(),
    ) -> None:
        super().__init__(
            stelsel="zelfstandig",
            peildatum=peildatum,
        )


if __name__ == "__main__":
    zel = Zelfstandig()
    f = open("./input_models/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(f.read())
    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    print(zel.bereken(eenheid, woningwaardering_resultaat))
