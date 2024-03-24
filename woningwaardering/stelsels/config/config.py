import yaml

from loguru import logger
from typing import Dict, List, Union
from pydantic import BaseModel, ValidationError


class StelselgroepVersieConfig(BaseModel):
    versie: str
    begindatum: Union[str, None]
    einddatum: Union[str, None]


class StelselgroepConfig(BaseModel):
    class_naam: str
    begindatum: Union[str, None]
    einddatum: Union[str, None]
    versies: List[StelselgroepVersieConfig]


class StelselConfig(BaseModel):
    stelsel: str
    begindatum: Union[str, None]
    einddatum: Union[str, None]
    stelselgroepen: Dict[str, StelselgroepConfig]

    @classmethod
    def load(cls, stelsel: str = "zelfstandig") -> "StelselConfig":
        try:
            path = f"woningwaardering/stelsels/config/{stelsel}.yml"
            with open(path, "r") as file:
                config = yaml.safe_load(file)
            stelsel_config = cls(**config)
            logger.info(f"Configuratie voor stelsel '{stelsel}' geladen.")
            return stelsel_config

        except ValidationError as e:
            logger.error(e, f"Geen valide stelsel configuratie in {path}.")
            raise

        except FileNotFoundError as e:
            logger.error(e, f"Config file {path} is niet gevonden.")
            raise
