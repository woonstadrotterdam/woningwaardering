from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Maatschappelijklabel(Enum):
    daeb = Referentiedata(
        code="DAE",
        naam="DAEB",
    )
    """
    Als attribuut van klasse Eenheid: Geeft aan dat de eenheid tot de DAEB-tak behoort.
    Als attribuut van klasse Huurovereenkomst: Geeft aan dat de verhuring als zijnde
    DAEB verantwoord wordt. Dit is gelijk aan een gereguleerd huurovereenkomst. Als
    attribuut van de klasse FinancieelBedrijf: Geeft aan of de bedrijfsactiviteiten
    als DAEB verantwoord worden.
    """

    geconsolideerde_niet_daeb_verbinding = Referentiedata(
        code="GNDV",
        naam="Geconsolideerde NIET-DAEB verbinding",
    )
    """
    Als attribuut van de klasse FinancieelBedrijf: Geeft aan of het bedrijf een
    consolidatiebedrijf is, waarbinnen NIET-DAEB activiteiten worden verricht.
    """

    niet_daeb = Referentiedata(
        code="NDA",
        naam="NIET-DAEB",
    )
    """
    Als attribuut van klasse Eenheid: Geeft aan dat de eenheid tot de niet-DAEB-tak
    behoort. Als attribuut van klasse Huurovereenkomst: Geeft aan dat de verhuring
    als zijnde niet-DAEB verantwoord wordt. Dit is gelijk aan een geliberaliseerde
    huurovereenkomst. Als attribuut van de klasse FinancieelBedrijf: Geeft aan of de
    bedrijfsactiviteiten als NIET-DAEB verantwoord worden.
    """

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
