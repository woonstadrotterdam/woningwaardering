import yaml
from typing import Dict, List, Union
from pydantic import BaseModel


class VersieConfig(BaseModel):
    begindatum: Union[str, None]
    einddatum: Union[str, None]


class StelselgroepConfig(BaseModel):
    class_naam: str
    begindatum: Union[str, None]
    einddatum: Union[str, None]
    versies: List[Dict[str, VersieConfig]]


class StelselConfig(BaseModel):
    begindatum: Union[str, None]
    einddatum: Union[str, None]
    stelselgroepen: Dict[str, StelselgroepConfig]


class Config(BaseModel):
    stelsel: Dict[str, StelselConfig]

    @classmethod
    def load(cls, stelsel: str = "zelfstandig") -> "Config":
        path = f"woningwaardering/stelsels/config/{stelsel}.yml"
        with open(path, "r") as file:
            config = yaml.safe_load(file)
        return cls(stelsel=config)

    # @staticmethod
    # def load_dict(stelsel: str = "zelfstandig") -> dict:
    #     config = Config.load(stelsel=stelsel)
    #     return config.model_dump()
