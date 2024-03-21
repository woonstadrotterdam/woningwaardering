import yaml
from typing import Dict, List, Union
from pydantic import BaseModel


class VersieModel(BaseModel):
    begindatum: Union[str, None]
    einddatum: Union[str, None]


class StelselgroepModel(BaseModel):
    class_naam: str
    begindatum: Union[str, None]
    einddatum: Union[str, None]
    versies: List[Dict[str, VersieModel]]


class StelselsModel(BaseModel):
    begindatum: Union[str, None]
    einddatum: Union[str, None]
    stelselgroepen: Dict[str, StelselgroepModel]


class Stelselsconfig(BaseModel):
    stelsels: Dict[str, StelselsModel]

    @classmethod
    def load(
        cls, path: str = "woningwaardering/stelsels/config/stelselsconfig.yml"
    ) -> "Stelselsconfig":
        with open(path, "r") as file:
            config = yaml.safe_load(file)
        return cls(stelsels=config["stelsels"])
