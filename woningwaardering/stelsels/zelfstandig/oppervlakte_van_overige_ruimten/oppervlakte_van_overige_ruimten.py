from datetime import date, datetime
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class OppervlakteVanOverigeRuimten(Stelselgroep):
    def __init__(self, peildatum: date = date.today()) -> None:
        super().__init__(
            peildatum=peildatum,
            stelsel="zelfstandig",
            stelselgroep="oppervlakte_van_overige_ruimten",
        )


if __name__ == "__main__":
    oor = OppervlakteVanOverigeRuimten(peildatum=datetime(2025, 1, 1))
    f = open("./input_modellen/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(f.read())
    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    print(
        oor.bereken(eenheid, woningwaardering_resultaat).model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )
