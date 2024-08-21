import warnings
from datetime import date

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    OppervlakteVanVertrekken,
    OppervlakteVanOverigeRuimten,
    Verwarming,
    Energieprestatie,
    Sanitair,
    Keuken,
    PriveBuitenruimten,
    PuntenVoorDeWozWaarde,
)

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


class ZelfstandigeWoonruimten(Stelsel):
    def __init__(self, peildatum: date = date.today()) -> None:
        raise NotImplementedError(
            "Het stelsel ZelfstandigeWoonruimten is nog niet geïmplementeerd."
        )
        super().__init__(
            stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
            begindatum=date(2024, 7, 1),
            einddatum=date.max,
            peildatum=peildatum,
            stelselgroepen=[
                OppervlakteVanVertrekken,
                OppervlakteVanOverigeRuimten,
                Verwarming,
                Energieprestatie,
                Sanitair,
                Keuken,
                PriveBuitenruimten,
                PuntenVoorDeWozWaarde,
            ],
        )


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")
    warnings.simplefilter("default", UserWarning)

    zelfstandige_woonruimten = ZelfstandigeWoonruimten(peildatum=date(2024, 5, 1))
    with open(
        "tests/data/zelfstandige_woonruimten/input/20004000156.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())
        woningwaardering_resultaat = zelfstandige_woonruimten.bereken(eenheid)
        print(
            woningwaardering_resultaat.model_dump_json(
                by_alias=True, indent=2, exclude_none=True
            )
        )
        tabel = utils.naar_tabel(woningwaardering_resultaat)

        print(tabel)
