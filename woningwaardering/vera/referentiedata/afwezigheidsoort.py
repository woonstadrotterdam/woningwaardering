from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Afwezigheidsoort(Enum):
    adoptieverlof = Referentiedata(
        code="ADO",
        naam="Adoptieverlof",
    )

    bijzonder_verlof = Referentiedata(
        code="BIJ",
        naam="Bijzonder verlof",
    )

    calamiteitenverlof = Referentiedata(
        code="CAL",
        naam="Calamiteitenverlof",
    )

    geschorst = Referentiedata(
        code="GES",
        naam="Geschorst",
    )

    non_actief = Referentiedata(
        code="NON",
        naam="Non-actief",
    )

    onbetaald_verlof = Referentiedata(
        code="ONB",
        naam="Onbetaald verlof",
    )

    ouderschapsverlof = Referentiedata(
        code="OUD",
        naam="Ouderschapsverlof",
    )

    verlof_regulier = Referentiedata(
        code="VER",
        naam="Verlof (regulier)",
    )

    ziek = Referentiedata(
        code="ZIE",
        naam="Ziek",
    )

    zorgverlof = Referentiedata(
        code="ZOR",
        naam="Zorgverlof",
    )

    zwangerschapsverlof = Referentiedata(
        code="ZWA",
        naam="Zwangerschapsverlof",
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
