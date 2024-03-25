from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class OppervlakteVanOverigeRuimten(Stelselgroep):
    def __init__(self, peildatum: str) -> None:
        super().__init__(
            peildatum,
            stelsel="zelfstandig",
            stelselgroep="oppervlakte_van_overige_ruimten",
        )


if __name__ == "__main__":
    oor = OppervlakteVanOverigeRuimten(peildatum="01-01-2025")
    f = open("./input_models/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(f.read())
    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    print(oor.bereken(eenheid, woningwaardering_resultaat))
