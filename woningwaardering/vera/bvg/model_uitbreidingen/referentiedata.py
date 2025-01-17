from typing import Optional

from pydantic import Field, field_validator

from woningwaardering.vera.bvg.generated import Referentiedata


class _Referentiedata(Referentiedata):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/53
    parent: Optional[Referentiedata] = Field(None, exclude=True)
    """
    De bovenliggende referentiedata in het geval er sprake is van een hierarchische relatie tussen referentiedata.
    """
    _name: str = ""

    @property
    def name(self) -> str:
        return self._name

    @field_validator("code", mode="after")
    @classmethod
    def niet_optioneel(cls, value: str) -> str:
        if value is None or value.strip() == "":
            raise ValueError("de code van een Referentiedata object mag niet leeg zijn")
        return value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Referentiedata):
            return self.code == other.code
        return False

    def __hash__(self) -> int:
        return hash(self.code)

    def __str__(self) -> str:
        return f"{self.naam} ({self.code})" if self.naam else self.code or ""
