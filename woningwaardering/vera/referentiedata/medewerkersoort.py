from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Medewerkersoort(Enum):
    in_dienst = Referentiedata(
        code="DIE",
        naam="in dienst",
    )

    meewerkende_partner = Referentiedata(
        code="FAM",
        naam="meewerkende partner",
    )

    inhuur_zzp_en_of_payroll_en_of_detachering = Referentiedata(
        code="INH",
        naam="inhuur: zzp / payroll / detachering",
    )

    oproepkracht = Referentiedata(
        code="OPR",
        naam="oproepkracht",
    )

    stagair = Referentiedata(
        code="STA",
        naam="stagair",
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
