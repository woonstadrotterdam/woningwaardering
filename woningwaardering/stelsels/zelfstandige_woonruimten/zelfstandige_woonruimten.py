import warnings
from datetime import date

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    BijzondereVoorzieningen,
    Buitenruimten,
    Energieprestatie,
    GemeenschappelijkeParkeerruimten,
    GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
    Keuken,
    OppervlakteVanOverigeRuimten,
    OppervlakteVanVertrekken,
    PrijsopslagMonumentenEnNieuwbouw,
    PuntenVoorDeWozWaarde,
    Sanitair,
    VerkoelingEnVerwarming,
)
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
            begindatum=date(2024, 7, 1),
            einddatum=date.max,
            peildatum=peildatum,
            stelselgroepen=[
                OppervlakteVanVertrekken,
                OppervlakteVanOverigeRuimten,
                VerkoelingEnVerwarming,
                Buitenruimten,
                Energieprestatie,
                Keuken,
                Sanitair,
                GemeenschappelijkeParkeerruimten,
                GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
                PuntenVoorDeWozWaarde,  # LET OP: deze stelselgroep dient als twee na laatste te worden uitgevoerd
                BijzondereVoorzieningen,  # LET OP: deze stelselgroep dient als een na laatste te worden uitgevoerd
                PrijsopslagMonumentenEnNieuwbouw,  # LET OP: deze stelselgroep dient als laatste te worden uitgevoerd
            ],
        )


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")
    warnings.simplefilter("default", UserWarning)

    zelfstandige_woonruimten = ZelfstandigeWoonruimten(peildatum=date.today())
    with open(
        "tests/data/zelfstandige_woonruimten/input/12006000004.json",
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
