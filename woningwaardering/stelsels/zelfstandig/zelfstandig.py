from datetime import date

from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Zelfstandig(Stelsel):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            stelsel="zelfstandig",
            peildatum=peildatum,
        )


f = open("./woningwaardering/41164000002.json", "r+")
eenheid = EenhedenEenheid.model_validate_json(f.read())
woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()

zelfstandig = Zelfstandig()
print(zelfstandig.bereken(eenheid, woningwaardering_resultaat))
