from types import ModuleType
import yaml
import importlib

from datetime import date, datetime
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Stelsel:
    def __init__(
        self,
        code: str,
        config: dict[str, dict[str]],
        eenheid: EenhedenEenheid,
        resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
        peildatum: date = date.today(),
    ) -> None:
        self.code: str = code
        self.config: dict = config
        self.peildatum: date = peildatum
        self.eenheid: EenhedenEenheid = eenheid
        self.resultaat: WoningwaarderingResultatenWoningwaarderingResultaat = resultaat

    def _import_versie(self, module_name: str, class_name: str) -> ModuleType:
        try:
            module = importlib.import_module(module_name)
            class_ = getattr(module, class_name)
            return class_
        except ModuleNotFoundError:
            print(f"Module {module_name} not found.")
        except AttributeError:
            print(f"Class {class_name} not found in module {module_name}.")

    def main(self) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """
        main
        """
        self.resultaat.groepen = []

        stelsel_config = self.config["stelsels"][self.code]

        for stelselgroep, versies in stelsel_config["stelselgroepen"].items():
            for versie, geldigheid in versies.items():
                if (
                    datetime.strptime(geldigheid["begindatum"], "%d-%m-%Y").date()
                    <= self.peildatum
                    <= datetime.strptime(geldigheid["einddatum"], "%d-%m-%Y").date()
                ):
                    stelselgroep_versie = self._import_versie(
                        f"woningwaardering.stelsels.{self.code}.{stelselgroep}",
                        versie,
                    )

                    self.resultaat.groepen.append(
                        stelselgroep_versie.bereken(
                            eenheid=self.eenheid,
                            woningwaardering_resultaat=self.resultaat,
                        )
                    )

        return self.resultaat


# moet de config aan pydantic model worden?
with open("./woningwaardering/config.yml", "r") as file:
    config = yaml.safe_load(file)

f = open("./woningwaardering/41164000002.json", "r+")

eenheid = EenhedenEenheid.model_validate_json(f.read())
woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
# woningwaardering_resultaat.groepen = []

zelfstandig = Stelsel(
    code="zelfstandig",
    config=config,
    eenheid=eenheid,
    resultaat=woningwaardering_resultaat,
)

woningwaardering_resultaat = zelfstandig.main()

woningwaardering_resultaat.punten = sum(
    woningwaardering_groep.punten
    for woningwaardering_groep in woningwaardering_resultaat.groepen or []
    if woningwaardering_groep.punten is not None
)

print(
    woningwaardering_resultaat.model_dump_json(
        by_alias=True, exclude_unset=True, indent=2
    )
)
