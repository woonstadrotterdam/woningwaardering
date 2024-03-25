from datetime import date, datetime
from zoneinfo import ZoneInfo
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class OppervlakteVanVertrekken(Stelselgroep):
    def __init__(
        self, peildatum: date = datetime.now(ZoneInfo("Europe/Amsterdam")).date()
    ) -> None:
        super().__init__(
            peildatum=peildatum,
            stelsel="zelfstandig",
            stelselgroep="oppervlakte_van_vertrekken",
        )


if __name__ == "__main__":
    ovv = OppervlakteVanVertrekken(
        peildatum=datetime(2025, 1, 1, tzinfo=ZoneInfo("Europe/Amsterdam")).date()
    )
    f = open("./input_modellen/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(f.read())
    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    print(ovv.bereken(eenheid, woningwaardering_resultaat))
