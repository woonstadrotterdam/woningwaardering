from typing import Dict, List, Union
from pydantic import BaseModel, ValidationError
import yaml


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
            return stelsel_config
        except ValidationError as e:
            print(e, "Geen valide stelsel configuratie.")
            raise
        except FileNotFoundError as e:
            print(e, f"Config file {path} is niet gevonden.")
            raise


stelsel_config = StelselConfig.load()
# print(stelsel_config)
print(type(stelsel_config))
print(stelsel_config.stelselgroepen)
for stelselgroep, config in stelsel_config.stelselgroepen.items():
    print(config.versies)
