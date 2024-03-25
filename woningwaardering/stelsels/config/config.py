import yaml

from datetime import date
from loguru import logger
from typing import Dict, List
from pydantic import BaseModel, ValidationError


class StelselgroepVersieConfig(BaseModel):
    class_naam: str
    begindatum: date
    einddatum: date


class StelselgroepConfig(BaseModel):
    class_naam: str
    begindatum: date
    einddatum: date
    versies: List[StelselgroepVersieConfig]


class StelselConfig(BaseModel):
    stelsel: str
    begindatum: date
    einddatum: date
    stelselgroepen: Dict[str, StelselgroepConfig]

    @classmethod
    def load(cls, stelsel: str = "zelfstandig") -> "StelselConfig":
        try:
            path = f"woningwaardering/stelsels/config/{stelsel}.yml"
            with open(path, "r") as file:
                config = yaml.safe_load(file)

        except FileNotFoundError as e:
            logger.error(e, f"Config file {path} is niet gevonden.")
            raise

        try:
            stelsel_config = cls(**config)

        except ValidationError as e:
            logger.error(e, f"Geen valide stelsel configuratie in {path}.")
            raise

        logger.info(f"Configuratie voor stelsel '{stelsel}' geladen.")
        return stelsel_config
