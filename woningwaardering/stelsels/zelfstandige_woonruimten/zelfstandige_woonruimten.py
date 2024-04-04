from datetime import date

from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


class ZelfstandigeWoonruimten(Stelsel):
    def __init__(self, peildatum: date = date.today()) -> None:
        super().__init__(
            stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
            peildatum=peildatum,
        )


if __name__ == "__main__":
    zel = ZelfstandigeWoonruimten()
    f = open(
        "./data_modellen/input/badkamer_en_of_toilet_boven_en_onder_0.64.json", "r+"
    )
    eenheid = EenhedenEenheid.model_validate_json(f.read())
    print(
        zel.bereken(eenheid).model_dump_json(by_alias=True, indent=2, exclude_none=True)
    )
