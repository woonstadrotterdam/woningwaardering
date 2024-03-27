from datetime import date
from woningwaardering.stelsels import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class OppervlakteVanOverigeRuimten(Stelselgroep):
    def __init__(self, peildatum: date = date.today()) -> None:
        super().__init__(
            peildatum=peildatum,
            stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
            stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,
        )


if __name__ == "__main__":
    oor = OppervlakteVanOverigeRuimten(peildatum=date(2025, 1, 1))
    f = open("./input_modellen/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(f.read())
    print(
        oor.bereken(eenheid).model_dump_json(by_alias=True, indent=2, exclude_none=True)
    )
