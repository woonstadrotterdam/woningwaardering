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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from woningwaardering.vera.bvg.models.extra_attribuut import ExtraAttribuut
from woningwaardering.vera.bvg.models.informatieobject import Informatieobject
from woningwaardering.vera.bvg.models.sturingslabel import Sturingslabel
from typing import Set
from typing_extensions import Self


class BerichtBasis(BaseModel):
    """
    BerichtBasis
    """  # noqa: E501

    extra_attributen: Optional[List[ExtraAttribuut]] = Field(
        default=None,
        description="Mogelijkheid om het bericht uit te breiden met attributen die nog niet in het logisch datamodel beschikbaar zijn",
        alias="extra-attributen",
    )
    informatieobjecten: Optional[List[Informatieobject]] = Field(
        default=None,
        description="Mogelijkheid om het bericht uit te breiden met documentatie. De beschrijving kan de inhoud van een notitie of memo zijn",
    )
    sturingslabels: Optional[List[Sturingslabel]] = Field(
        default=None,
        description="Mogelijkheid om het bericht uit te breiden met sturingslabels",
    )
    __properties: ClassVar[List[str]] = [
        "extra-attributen",
        "informatieobjecten",
        "sturingslabels",
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
        """Create an instance of BerichtBasis from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in extra_attributen (list)
        _items = []
        if self.extra_attributen:
            for _item in self.extra_attributen:
                if _item:
                    _items.append(_item.to_dict())
            _dict["extra-attributen"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in informatieobjecten (list)
        _items = []
        if self.informatieobjecten:
            for _item in self.informatieobjecten:
                if _item:
                    _items.append(_item.to_dict())
            _dict["informatieobjecten"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sturingslabels (list)
        _items = []
        if self.sturingslabels:
            for _item in self.sturingslabels:
                if _item:
                    _items.append(_item.to_dict())
            _dict["sturingslabels"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BerichtBasis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "extra-attributen": [
                    ExtraAttribuut.from_dict(_item) for _item in obj["extra-attributen"]
                ]
                if obj.get("extra-attributen") is not None
                else None,
                "informatieobjecten": [
                    Informatieobject.from_dict(_item)
                    for _item in obj["informatieobjecten"]
                ]
                if obj.get("informatieobjecten") is not None
                else None,
                "sturingslabels": [
                    Sturingslabel.from_dict(_item) for _item in obj["sturingslabels"]
                ]
                if obj.get("sturingslabels") is not None
                else None,
            }
        )
        return _obj
