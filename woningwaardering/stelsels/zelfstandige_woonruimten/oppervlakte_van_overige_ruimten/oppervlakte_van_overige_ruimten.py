from datetime import date

from loguru import logger

from woningwaardering.stelsels import Stelselgroep, utils
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class OppervlakteVanOverigeRuimten(Stelselgroep):
    def __init__(self, peildatum: date = date.today()) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten
        super().__init__(
            peildatum=peildatum,
        )


if __name__ == "__main__":
    logger.enable("woningwaardering")

    oppervlakte_van_overige_ruimten = OppervlakteVanOverigeRuimten(
        peildatum=date(2025, 1, 1)
    )
    file = open("./tests/data/input/zelfstandige_woonruimten/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = oppervlakte_van_overige_ruimten.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
