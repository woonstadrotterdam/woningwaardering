from datetime import date

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.config.config import Stelselconfig
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class PriveBuitenruimten(Stelselgroep):
    def __init__(
        self,
        stelsel: Woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten,
        stelselgroep: Woningwaarderingstelselgroep = Woningwaarderingstelselgroep.prive_buitenruimten,
        peildatum: date = date.today(),
        config: Stelselconfig | None = None,
    ) -> None:
        super().__init__(
            stelsel=stelsel,
            stelselgroep=stelselgroep,
            peildatum=peildatum,
            config=config,
        )


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    prive_buitenruimten = PriveBuitenruimten()
    with open("tests/data/generiek/input/37101000032.json", "r+") as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = prive_buitenruimten.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
