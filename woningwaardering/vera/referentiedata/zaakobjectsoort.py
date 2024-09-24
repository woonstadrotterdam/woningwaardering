from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Zaakobjectsoort(Enum):
    cluster = Referentiedata(
        code="CLU",
        naam="Cluster",
    )

    collectief_object = Referentiedata(
        code="COL",
        naam="Collectief object",
    )

    eenheid = Referentiedata(
        code="EEN",
        naam="Eenheid",
    )

    onderhoudsverzoek = Referentiedata(
        code="OND",
        naam="Onderhoudsverzoek",
    )

    overeenkomst = Referentiedata(
        code="OVE",
        naam="Overeenkomst",
    )

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
