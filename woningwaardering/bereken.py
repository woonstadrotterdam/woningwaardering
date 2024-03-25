from datetime import date

from loguru import logger

from woningwaardering.stelsels.config import StelselConfig
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.utils import import_class, is_geldig, vind_yaml_bestanden
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Woningwaardering:
    def __init__(self, peildatum: str | date = date.today()) -> None:
        self.peildatum = (
            peildatum if isinstance(peildatum, str) else peildatum.strftime("%d-%m-%Y")
        )
        self.geldige_stelsels = select_geldige_stelsels(self.peildatum)

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        resultaat.groepen = []

        for stelsel in self.geldige_stelsels:
            resultaat.groepen.append(
                stelsel.bereken(eenheid=eenheid, resultaat=resultaat)
            )

        return resultaat


def select_geldige_stelsels(peildatum: str) -> list[Stelsel]:
    stelsels = []
    for stelsel_yaml in vind_yaml_bestanden("./woningwaardering/stelsels/config/"):
        stelsel = stelsel_yaml.split("/")[-1].split(".")[0]
        stelsel_config = StelselConfig.load(stelsel=stelsel)

        if is_geldig(
            stelsel_config.begindatum,
            stelsel_config.einddatum,
            peildatum,
        ):
            logger.debug(f"Stelsel '{stelsel}' is geldig op peildatum {peildatum}.")
            stelsel_object: Stelsel = import_class(
                f"woningwaardering.stelsels.{stelsel}.{stelsel}", stelsel.capitalize()
            )
            stelsels.append(stelsel_object(peildatum=peildatum))
    if len(stelsels) == 0:
        raise ValueError(f"Geen geldige stelsels gevonden voor peildatum {peildatum}.")
    return stelsels


if __name__ == "__main__":
    wws = Woningwaardering()
    f = open("./input_modellen/41164000002.json", "r+")
    eenheid = EenhedenEenheid.model_validate_json(f.read())
    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    print(wws.bereken(eenheid, woningwaardering_resultaat))
