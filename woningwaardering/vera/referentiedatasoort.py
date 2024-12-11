from typing import Any, ClassVar, Dict, Iterator, Type

from woningwaardering.vera.bvg.generated import Referentiedata


class ReferentiedatasoortMeta(type):
    _referentiedata: ClassVar[Dict[str, Referentiedata]]

    def __iter__(cls) -> Iterator[Referentiedata]:
        return iter(cls._referentiedata.values())

    def __new__(
        cls, name: str, bases: tuple[Type[Any], ...], class_dict: Dict[str, object]
    ) -> "ReferentiedatasoortMeta":
        referentiedata_attrs = {
            key: value
            for key, value in class_dict.items()
            if isinstance(value, Referentiedata)
        }

        cls_instance = super().__new__(cls, name, bases, class_dict)
        setattr(cls_instance, "_referentiedata", referentiedata_attrs)

        for attr_name, referentiedata_instance in referentiedata_attrs.items():
            referentiedata_instance._name = attr_name
        return cls_instance


class Referentiedatasoort(metaclass=ReferentiedatasoortMeta):
    pass
