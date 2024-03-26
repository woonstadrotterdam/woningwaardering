from datetime import date
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)


class OppervlakteVanVertrekken(Stelselgroep):
    def __init__(self, peildatum: date = date.today()) -> None:
        super().__init__(
            peildatum=peildatum,
            stelsel="zelfstandig",
            stelselgroep="oppervlakte_van_vertrekken",
        )


if __name__ == "__main__":
    ovv = OppervlakteVanVertrekken(peildatum=date(2025, 1, 1))
    f = open("./input_modellen/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(f.read())

    print(
        ovv.bereken(eenheid).model_dump_json(by_alias=True, indent=2, exclude_none=True)
    )
