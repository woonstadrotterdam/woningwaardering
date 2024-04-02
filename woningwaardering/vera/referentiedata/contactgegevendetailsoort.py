from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Contactgegevendetailsoort(Enum):
    in_case_of_emergency = Referentiedata(
        code="ICE",
        naam="In case of emergency",
    )

    prive = Referentiedata(
        code="PRI",
        naam="Privé",
    )

    zakelijk = Referentiedata(
        code="ZAK",
        naam="Zakelijk",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
