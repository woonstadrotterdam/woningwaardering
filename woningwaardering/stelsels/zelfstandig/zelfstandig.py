from datetime import date

from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)


class Zelfstandig(Stelsel):
    def __init__(self, peildatum: date = date.today()) -> None:
        super().__init__(
            stelsel="zelfstandig",
            peildatum=peildatum,
        )


if __name__ == "__main__":
    zel = Zelfstandig()
    f = open("./input_modellen/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(f.read())
    print(
        zel.bereken(eenheid).model_dump_json(by_alias=True, indent=2, exclude_none=True)
    )
