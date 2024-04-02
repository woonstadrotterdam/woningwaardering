import yaml

from datetime import date
from loguru import logger
from typing import Dict, List
from pydantic import BaseModel, ValidationError

from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


class Stelselgroepversieconfig(BaseModel):
    class_naam: str
    begindatum: date
    einddatum: date


class Stelselgroepconfig(BaseModel):
    class_naam: str
    begindatum: date
    einddatum: date
    versies: List[Stelselgroepversieconfig]


class Stelselconfig(BaseModel):
    stelsel: str
    begindatum: date
    einddatum: date
    stelselgroepen: Dict[str, Stelselgroepconfig]

    @classmethod
    def load(cls, stelsel: Woningwaarderingstelsel) -> "Stelselconfig":
        try:
            path = f"woningwaardering/stelsels/config/{stelsel.name}.yml"
            with open(path, "r") as file:
                config = yaml.safe_load(file)

        except FileNotFoundError:
            logger.error(f"Config file '{path}' is niet gevonden.")
            raise

        try:
            stelsel_config = cls(**config)

        except ValidationError as e:
            logger.error(e, f"Geen valide stelsel configuratie in {path}.")
            raise

        logger.info(f"Configuratie voor stelsel '{stelsel.value.naam}' geladen.")
        return stelsel_config
