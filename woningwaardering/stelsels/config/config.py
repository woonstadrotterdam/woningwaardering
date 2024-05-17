import yaml

from importlib.resources import files
from datetime import date
from loguru import logger
from typing import Dict, List
from pydantic import BaseModel, ValidationError

from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


class Stelselgroepversieconfig(BaseModel):
    module: str
    class_naam: str
    begindatum: date = date.min
    einddatum: date = date.max


class Stelselgroepconfig(BaseModel):
    module: str
    class_naam: str
    begindatum: date = date.min
    einddatum: date = date.max
    versies: List[Stelselgroepversieconfig]


class Stelselconfig(BaseModel):
    stelsel: str
    begindatum: date = date.min
    einddatum: date = date.max
    stelselgroepen: Dict[str, Stelselgroepconfig]

    @classmethod
    def load(cls, stelsel: Woningwaarderingstelsel) -> "Stelselconfig":
        try:
            path = files("woningwaardering.stelsels.config").joinpath(
                f"{stelsel.name}.yml"
            )
            config = yaml.safe_load(path.read_text())

        except ModuleNotFoundError:
            logger.error(f"Config file '{path}' is niet gevonden.")
            raise

        except FileNotFoundError:
            logger.error(f"Config file '{path}' is niet gevonden.")
            raise

        try:
            stelsel_config = cls(**config)

        except ValidationError:
            logger.error(f"Configuratie in {path} is niet valide.")
            raise

        logger.info(f"Configuratie voor stelsel '{stelsel.value.naam}' geladen.")
        return stelsel_config

    def save(self) -> None:
        setattr(yaml.SafeDumper, "ignore_aliases", lambda *args: True)
        stream = open(f"woningwaardering/stelsels/config/{self.stelsel}.yml", "w")
        yaml.safe_dump(
            self.model_dump(exclude_defaults=True), stream=stream, sort_keys=False
        )
