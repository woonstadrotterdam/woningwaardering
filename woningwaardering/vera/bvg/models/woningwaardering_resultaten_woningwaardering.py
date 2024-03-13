# coding: utf-8

"""
    VERA-Beheer Vastgoedgegevens

    API-specificatie van ketenproces 'Beheer Vastgoedgegevens'. Deze specificatie is gebaseerd op VERA versie 4.1.4+240311.2

    The version of the OpenAPI document: 1.1.4+240311.2
    Contact: VERA@aedesdatastandaarden.nl
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from woningwaardering.vera.bvg.models.referentiedata import Referentiedata
from woningwaardering.vera.bvg.models.woningwaardering_resultaten_woningwaardering_criterium import (
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from typing import Set
from typing_extensions import Self


class WoningwaarderingResultatenWoningwaardering(BaseModel):
    """
    WoningwaarderingResultatenWoningwaardering
    """  # noqa: E501

    id: Optional[StrictStr] = Field(
        default=None,
        description="De primaire sleutel van het gegeven in het bronsysteem. Je verstuurt een entiteit altijd met het eigen id. Id kan leeg zijn.",
    )
    id_extern: Optional[StrictStr] = Field(
        default=None,
        description="De primaire sleutel van het gegeven in het doelsysteem. Deze idExtern wisselt om met id afhankelijk van de richting van de gegevensuitwisseling.",
        alias="idExtern",
    )
    id_gegevensbeheerder: Optional[StrictStr] = Field(
        default=None,
        description="De primaire sleutel van het gegeven van de gegevensbeheerder. Bijv. de overheid of andere standaarden.",
        alias="idGegevensbeheerder",
    )
    id_organisatie: Optional[StrictStr] = Field(
        default=None,
        description="Dit verwijst naar de organisatie die verantwoordelijk is voor het gegeven. Horende bij de idExtern.",
        alias="idOrganisatie",
    )
    id_administratie: Optional[StrictStr] = Field(
        default=None,
        description="Dit verwijst naar de administratie waar het gegeven onderdeel van is. Horende bij de idExtern.",
        alias="idAdministratie",
    )
    code: Optional[StrictStr] = Field(
        default=None,
        description="De unieke code (Bijvoorbeeld om te tonen of te zoeken)",
    )
    soort: Optional[Referentiedata] = Field(
        default=None,
        description="Het soort onderdeel van de woningwaardering. Bijv. Energielabel, Oppervlakte etc. Referentiedatasoort WONINGWAARDERINGSOORT.",
    )
    begindatum: Optional[date] = Field(
        default=None,
        description="De datum waarop het woning waardering  onderdeel in gaat of is ingegaan.",
    )
    einddatum: Optional[date] = Field(
        default=None,
        description="De datum waarop het woningwaardering onderdeel niet meer van toepassing is.",
    )
    aantal: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Het aantal van de opgegeven meeteenheid van de bijbehorende woningwaardering criterium.",
    )
    criterium: Optional[WoningwaarderingResultatenWoningwaarderingCriterium] = Field(
        default=None, description="De omschrijving van het woningwaardering onderdeel."
    )
    punten: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Het aantal punten dat is toegekend op basis van het opgegeven aantal, voor de betreffende woningwaardering. Voor bepaalde woningwaarderingGroepen binnen een woningwaarderingstelsel geldt dat het aantal punten op groepsniveau bepaald wordt. In die gevallen kan het attribuut aantal punten in deze klasse leeg blijven",
    )
    waarde: Optional[StrictStr] = Field(
        default=None,
        description="Bevat een niet numerieke waarde van de woningwaardering.",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "idExtern",
        "idGegevensbeheerder",
        "idOrganisatie",
        "idAdministratie",
        "code",
        "soort",
        "begindatum",
        "einddatum",
        "aantal",
        "criterium",
        "punten",
        "waarde",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WoningwaarderingResultatenWoningwaardering from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of soort
        if self.soort:
            _dict["soort"] = self.soort.to_dict()
        # override the default output from pydantic by calling `to_dict()` of criterium
        if self.criterium:
            _dict["criterium"] = self.criterium.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WoningwaarderingResultatenWoningwaardering from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "idExtern": obj.get("idExtern"),
                "idGegevensbeheerder": obj.get("idGegevensbeheerder"),
                "idOrganisatie": obj.get("idOrganisatie"),
                "idAdministratie": obj.get("idAdministratie"),
                "code": obj.get("code"),
                "soort": Referentiedata.from_dict(obj["soort"])
                if obj.get("soort") is not None
                else None,
                "begindatum": obj.get("begindatum"),
                "einddatum": obj.get("einddatum"),
                "aantal": obj.get("aantal"),
                "criterium": WoningwaarderingResultatenWoningwaarderingCriterium.from_dict(
                    obj["criterium"]
                )
                if obj.get("criterium") is not None
                else None,
                "punten": obj.get("punten"),
                "waarde": obj.get("waarde"),
            }
        )
        return _obj
