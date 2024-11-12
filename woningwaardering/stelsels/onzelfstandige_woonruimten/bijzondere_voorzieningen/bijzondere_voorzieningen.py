import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.bijzondere_voorzieningen.bijzondere_voorzieningen import (
    BijzondereVoorzieningen as BijzondereVoorzieningenZelfstandigeWoonruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class BijzondereVoorzieningen(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.bijzondere_voorzieningen
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel.value,
                stelselgroep=self.stelselgroep.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = list(
            BijzondereVoorzieningenZelfstandigeWoonruimten._genereer_woningwaarderingen(
                peildatum=self.peildatum,
                eenheid=eenheid,
                stelselgroepen_zonder_opslag=[
                    self.stelselgroep,
                    Woningwaarderingstelselgroep.aftrekpunten,
                ],
                stelsel=self.stelsel,
                woningwaardering_resultaat=woningwaardering_resultaat,
            )
        )

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {self.stelselgroep.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")
    warnings.filterwarnings("ignore", category=UserWarning)

    stelselgroep = BijzondereVoorzieningen(peildatum=date.fromisoformat("2024-07-01"))

    with open(
        "tests/data/onzelfstandige_woonruimten/stelselgroepen/bijzondere_voorzieningen/input/zorgwoning.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
