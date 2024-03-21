import importlib
from datetime import datetime

import yaml

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Stelselgroep:
    def __init__(
        self,
        peildatum,
        stelsel: str,
        module: str,
    ) -> None:
        self.peildatum = datetime.strptime(peildatum, "%d-%m-%Y").date()
        self.config = self._read_config()
        self.stelsel = stelsel
        self.module = module
        self.geldige_versie_class_naam = self._select_geldige_versie()
        print(f"geldige_versie_class_naam: {self.geldige_versie_class_naam}")
        self.geldige_versie = self._import_versie()

    def _read_config(self) -> dict:
        with open("./woningwaardering/config.yml", "r") as file:
            return yaml.safe_load(file)

    def _select_geldige_versie(self) -> None:
        versies = self.config["stelsels"][self.stelsel]["stelselgroepen"][self.module][
            "versies"
        ]
        print(f"versies: {versies}")
        for versie in versies:
            for versie_class_naam, geldigheid in versie.items():
                begindatum: str = str(geldigheid["begindatum"])
                einddatum: str = str(geldigheid["einddatum"])
                if (
                    datetime.strptime(begindatum, "%d-%m-%Y").date()
                    <= self.peildatum
                    <= datetime.strptime(einddatum, "%d-%m-%Y").date()
                ):
                    return versie_class_naam

    def _import_versie(self):
        module_path = f"woningwaardering.stelsels.{self.stelsel}.{self.module}"
        try:
            module = importlib.import_module(module_path)
            class_: Stelselgroep = getattr(module, self.geldige_versie_class_naam)
            return class_
        except ModuleNotFoundError:
            print(f"Module {module_path} not found.")
            raise
        except AttributeError:
            print(
                f"Class {self.geldige_versie_class_naam} not found in module {module_path}."
            )
            raise

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        return self.geldige_versie.bereken(eenheid, woningwaardering_resultaat)
