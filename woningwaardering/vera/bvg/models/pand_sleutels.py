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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self


class PandSleutels(BaseModel):
    """
    PandSleutels
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
    __properties: ClassVar[List[str]] = [
        "id",
        "idExtern",
        "idGegevensbeheerder",
        "idOrganisatie",
        "idAdministratie",
        "code",
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
        """Create an instance of PandSleutels from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PandSleutels from a dict"""
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
            }
        )
        return _obj
