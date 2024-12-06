from typing import Dict, Iterator

from woningwaardering.vera.bvg.generated import Referentiedata


class ReferentiedatasoortMeta(type):
    def __iter__(cls) -> Iterator[Referentiedata]:
        return iter(cls._items.values())


class Referentiedatasoort(metaclass=ReferentiedatasoortMeta):
    _items: Dict[str, Referentiedata] = {}

    @classmethod
    def __init_subclass__(cls, /, **kwargs):
        super().__init_subclass__(**kwargs)
        for key, value in cls.__dict__.items():
            if isinstance(value, Referentiedata):
                value.name = key
                cls._items[key] = value

    def __iter__(self):
        return iter(self._items.items())
