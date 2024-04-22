from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidisolatie(Enum):
    dakisolatie = Referentiedata(
        code="DAK",
        naam="Dakisolatie",
    )

    dubbel_glas = Referentiedata(
        code="DGL",
        naam="Dubbel glas",
    )

    eco_bouw = Referentiedata(
        code="ECO",
        naam="Eco-bouw",
    )
    """
    Ecologische, duurzame bouw
    """

    gedeeltelijk_dubbel_glas = Referentiedata(
        code="GDG",
        naam="Gedeeltelijk dubbel glas",
    )

    muurisolatie = Referentiedata(
        code="MUU",
        naam="Muurisolatie",
    )

    vloerisolatie = Referentiedata(
        code="VLO",
        naam="Vloerisolatie",
    )

    volledig_geisoleerd = Referentiedata(
        code="VOL",
        naam="Volledig geïsoleerd",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
