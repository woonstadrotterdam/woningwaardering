import warnings
from datetime import date

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    Buitenruimten,
    Energieprestatie,
    GemeenschappelijkeParkeerruimten,
    Keuken,
    OppervlakteVanOverigeRuimten,
    OppervlakteVanVertrekken,
    PuntenVoorDeWOZWaarde,
    Sanitair,
    VerkoelingEnVerwarming,
)
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


class OnzelfstandigeWoonruimten(Stelsel):
    def __init__(self, peildatum: date = date.today()) -> None:
        super().__init__(
            stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten,
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
            stelselgroepen=[
                OppervlakteVanVertrekken,
                OppervlakteVanOverigeRuimten,
                VerkoelingEnVerwarming,
                Energieprestatie,
                Keuken,
                Sanitair,
                Buitenruimten,
                GemeenschappelijkeParkeerruimten,
                PuntenVoorDeWOZWaarde,
            ],
        )


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")
    warnings.simplefilter("default", UserWarning)

    onzelfstandige_woonruimten = OnzelfstandigeWoonruimten(
        peildatum=date.fromisoformat("2024-07-01")
    )

    with open(
        "tests/data/generiek/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())
        woningwaardering_resultaat = onzelfstandige_woonruimten.bereken(eenheid)
        print(
            woningwaardering_resultaat.model_dump_json(
                by_alias=True, indent=2, exclude_none=True
            )
        )
        tabel = utils.naar_tabel(woningwaardering_resultaat)

        print(tabel)
